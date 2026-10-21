#!/usr/bin/env python3
# ── touch_your_secrets.py : the hook half of RM-R0002, "touch your secrets" ─────────
#
# A Claude Code PreToolUse hook. It reads the tool call Claude Code sends on stdin and
# denies any read, write, search or shell command that names a file that usually holds
# a credential: .env files, private keys, SSH, cloud and package-manager credentials.
# Everything else gets no answer from this hook, so the normal permission flow applies.
#
# What it is: a setting, in the vocabulary of the Agent Behaviour Policy. It runs outside
# the model and the model cannot talk its way past it, but it lives in a file the agent
# could edit, which is why RM-R0015 (change its own permissions) is installed with it.
# What it is not: a sandbox. A command that reaches a secret without naming the file
# (a script that opens it) gets past this hook; Claude Code's sandbox is the boundary.
#
# customers.riskmandate.ai/policies/touch-your-secrets/ · Python 3, standard library only · CC BY 4.0

import json
import re
import sys

LINE    = ('Do not read, print, copy or use credentials, tokens, keys or .env files unless I ask for that specific one; '
           'if a task needs one, stop and tell me which and why.')
SECRET  = re.compile(r'''(?ix)
    (^|[\s/'"=:])(
        \.env(\.(?!example\b|sample\b|template\b|dist\b)[\w.-]+)?   # .env and .env.local, not .env.example
      | [\w.-]*\.(pem|key|p12|pfx|keystore|jks)                     # key files
      | id_(rsa|dsa|ecdsa|ed25519)\b                                # SSH private keys
      | \.ssh/ | \.aws/ | \.config/gcloud/ | \.azure/ | \.kube/config | \.docker/config\.json
      | \.netrc | \.npmrc | \.pypirc | \.git-credentials | \.pgpass
      | secrets?/ | credentials?(\.json|\.ya?ml)?\b
    )(?=$|[\s'"/;|&)>]|(?<=/))''')                                        # a folder name already ends at its slash
ENV_DUMP = re.compile(r'(^|[;&|]\s*)(printenv|env|set|export\s+-p)\s*($|[;&|])')
PATH_KEYS = ('file_path', 'path', 'notebook_path', 'pattern', 'glob')


def decide(call):
    tool, args = call.get('tool_name', ''), call.get('tool_input') or {}
    if tool == 'Bash':
        command = args.get('command', '')
        if SECRET.search(command):
            return f'this command names a file that holds a credential ({SECRET.search(command).group(2)})'
        if ENV_DUMP.search(command):
            return 'this command prints every environment variable, which usually include tokens'
        return None
    for key in PATH_KEYS:
        value = str(args.get(key) or '')
        if value and SECRET.search(value):
            return f'{tool} would touch {value}, which usually holds a credential'
    return None


def main():
    try:
        call = json.load(sys.stdin)
    except ValueError:
        return 0                                                                  # not a tool call: no answer, the normal flow applies
    why = decide(call)
    if why:
        print(json.dumps({'hookSpecificOutput': {
            'hookEventName'           : 'PreToolUse',
            'permissionDecision'      : 'deny',
            'permissionDecisionReason': f'Behaviour policy RM-R0002: {why}. {LINE} Ask the person which credential, and why.'}}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
