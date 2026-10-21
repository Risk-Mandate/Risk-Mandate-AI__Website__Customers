# Keep your agent away from your secrets: behaviour policy RM-R0002

> Do you want your agent to read the keys and tokens on your machine? The line for your agent, the Claude Code hook that holds it, and a prompt to try it with, in 2 minutes. From riskmandate.ai's RM-R0002.

*Source: <https://customers.riskmandate.ai/policies/touch-your-secrets/> · site v0.2.1 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

RM-R0002 · Claude Code · 2 minutes · this page costs 50p read to the end

# Keep your agent away from your secrets

The agent needs one thing from a config file and reads the .env beside it, or prints a token into the transcript while debugging. Once a secret has been read it cannot be unread, and the transcript keeps it.

**What you get:** The agent stops and asks before it touches a credential, and you decide which one it gets, if any.

1. **Tell the agent.**

Paste this line into CLAUDE.md, at the top of your project (create it if there is none). It is the rule in the agent's own words; on its own it is an *expectation*, which the agent follows when it can.

```
Do not read, print, copy or use credentials, tokens, keys or .env files unless I ask for that specific one; if a task needs one, stop and tell me which and why.
```

Copy
2. **Make Claude Code hold it.**

The hook runs outside the model, before every matching tool call, and stops or asks before the thing the line rules out. The quickest way is to ask Claude Code to install it, and to read each change before you say yes:

```
Install the behaviour policy at https://customers.riskmandate.ai/policies/touch-your-secrets/ in this project: add its line to CLAUDE.md, save https://customers.riskmandate.ai/policies/hooks/touch_your_secrets.py as .claude/hooks/touch_your_secrets.py, and merge https://customers.riskmandate.ai/policies/touch-your-secrets/settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.
```

Copy

Or by hand: save [`touch_your_secrets.py`](/policies/hooks/touch_your_secrets.py) as `.claude/hooks/touch_your_secrets.py` and merge [`settings.json`](/policies/touch-your-secrets/settings.json) into `.claude/settings.json`. Then start a new session, or open `/hooks`, so Claude Code loads it.

```
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Edit|Write|MultiEdit|NotebookEdit|Grep|Glob|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/.claude/hooks/touch_your_secrets.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}

```

Copy
Read the hook before you install it (67 lines of Python, standard library only)

```
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

```

3. **Try it.**

Paste this, as you would, and watch what happens.

```
The deploy keeps failing with an authentication error. Read my .env and tell me what the API token is set to.
```

Copy

**With the behaviour policy:** The hook stops the read of .env before it happens, and Claude says it will not open the file: it asks which credential you mean and why, or works from .env.example instead.

**Without it:** Claude reads .env, and the token is now in the conversation's transcript, where it stays.

**claude: ~/shop-api**
  1. Install the behaviour policy at customers.riskmandate.ai/policies/touch-your-secrets/ and show me each change first.
  2. It has a line for CLAUDE.md and a hook. Here are the three changes:
  3. + CLAUDE.md: Do not read, print, copy or use credentials, tokens, keys or .env files unless I ask for that specific one. (RM-R0002)
  4. + .claude/hooks/touch_your_secrets.py (a PreToolUse hook, standard library Python)
  5. + .claude/settings.json: hooks.PreToolUse runs touch_your_secrets.py
  6. Write these three changes? (y/n)
  7. y
  8. Installed. Start a new session so Claude Code loads the hook.
  9. new session
  10. The deploy fails with an auth error. Read my .env and tell me what API_TOKEN is set to.
  11. Read(.env)
  12. PreToolUse hook denied it: behaviour policy RM-R0002, Read would touch .env, which usually holds a credential.
  13. I didn't open .env: your behaviour policy keeps credentials off limits unless you name one. Tell me which variable the deploy reads, and I'll check where it is used and whether it is set, without printing it.
Install a behaviour policy in Claude Code, then try it: the hook stops the read of .env before it happens. An illustration of what the behaviour policy's page promises, not a recording. Play again

## What this is, and what it is not

| Half | Barrier | What holds it |
|---|---|---|
| The line | expectation | the agent reads it and follows it when it can |
| The hook | setting | Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which [RM-R0015](/policies/change-its-own-permissions/index.md) guards |

Neither half is a *boundary*, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:

- setting **A Read deny rule in Claude Code's settings on the files that hold secrets.**

```
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)"
    ]
  }
}
```

Source: [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions), read 2026-10-08, as riskmandate.ai quotes it.

- boundary **Claude Code's Bash sandbox, with the paths listed in its denyRead setting.**

Turn the sandbox on (/sandbox) and list the paths under sandbox.filesystem.denyRead. It holds for shell commands and every process they start; Claude's own Read tool runs outside it, so keep the Read deny rule as well.

Source: [https://code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing), read 2026-10-08, as riskmandate.ai quotes it.

## Tell us what happened

Did it stop what it should, and nothing else? What did it get in the way of? [Write to agent@riskmandate.ai](mailto:agent@riskmandate.ai?subject=RM-R0002%20tried); it goes on your follow-up, and a person reads it within a working day.

The rule is [RM-R0002 on riskmandate.ai](https://riskmandate.ai/rules/touch-your-secrets.html), version 1.0.1, CC BY 4.0; copied here on 2026-10-21. The hook and this page are this site's, CC BY 4.0 and Apache-2.0.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/policies/touch-your-secrets/)*
