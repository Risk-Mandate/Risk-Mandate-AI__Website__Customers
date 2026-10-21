#!/usr/bin/env python3
# ── change_its_own_permissions.py : the hook half of RM-R0015 ────────────────────────
#
# A Claude Code PreToolUse hook. Any edit to Claude Code's own settings, permission rules
# or hooks (.claude/settings.json, .claude/settings.local.json, anything in .claude/hooks/,
# and the same in the home directory) asks the person first, whether it comes from a file
# tool or a shell command. It is the hook that keeps the other three hooks in place.
#
# What it is: a setting, and the one that makes the others hold, since every hook lives in
# a file the agent could otherwise rewrite. Managed settings, which an organisation sets
# and no project file can override, are the stronger control.
#
# customers.riskmandate.ai/policies/change-its-own-permissions/ · Python 3, standard library only · CC BY 4.0

import json
import re
import sys

LINE  = ('Never edit your own settings, permission rules or hooks (such as .claude/settings.json), '
         'or change how much you ask me; tell me what you would change and why.')
OWN   = re.compile(r'\.claude/(settings(\.local)?\.json|hooks/)|\.claude\.json\b')
WRITE = re.compile(r'(>|>>|\btee\b|\bsed\s+-i|\bperl\s+-pi|\bmv\b|\bcp\b|\brm\b|\bchmod\b|\bln\b|\btruncate\b|\bpython3?\s+-c|\bnode\s+-e|\bjq\b.*>)')
FILE_TOOLS = ('Edit', 'Write', 'MultiEdit', 'NotebookEdit')


def decide(call):
    tool, args = call.get('tool_name', ''), call.get('tool_input') or {}
    if tool in FILE_TOOLS:
        path = str(args.get('file_path') or args.get('notebook_path') or '')
        if OWN.search(path):
            return f'{tool} would change {path}, part of the agent\'s own permissions'
    if tool == 'Bash':
        command = args.get('command', '')
        if OWN.search(command) and WRITE.search(command):
            return 'this command writes to the agent\'s own settings or hooks'
    return None


def main():
    try:
        call = json.load(sys.stdin)
    except ValueError:
        return 0
    why = decide(call)
    if why:
        print(json.dumps({'hookSpecificOutput': {
            'hookEventName'           : 'PreToolUse',
            'permissionDecision'      : 'ask',
            'permissionDecisionReason': f'Behaviour policy RM-R0015: {why}. {LINE}'}}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
