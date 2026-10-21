#!/usr/bin/env python3
# ── delete_files.py : the hook half of RM-R0007, "delete files" ──────────────────────
#
# A Claude Code PreToolUse hook on Bash. rm -rf, and any delete outside the project
# folder, is denied; any other delete (rm, rmdir, unlink, git clean, find -delete, git rm)
# asks the person first, so they see the paths before anything goes. Everything else gets
# no answer from this hook.
#
# What it is: a setting. It reads the command Claude writes; a delete inside a script it
# runs is not seen. Claude Code's sandbox, which limits where commands can write, is the
# boundary.
#
# customers.riskmandate.ai/policies/delete-files/ · Python 3, standard library only · CC BY 4.0

import json
import os
import re
import shlex
import sys

LINE   = 'Ask before deleting any file or folder you did not create in this session, and never run rm -rf or delete anything outside this project.'
DELETE = re.compile(r'(^|[;&|(]\s*|\bsudo\s+|\bxargs\s+)(rm|rmdir|unlink|shred)\b|\bgit\s+(clean|rm)\b|\bfind\b.*\s-delete\b')


def words_after_rm(command):
    try:
        words = shlex.split(command, posix=True)
    except ValueError:
        words = command.split()
    out, on = [], False
    for w in words:
        if w in ('rm', 'rmdir', 'unlink', 'shred'):
            on = True
            continue
        if w in ('&&', '||', ';', '|'):
            on = False
        elif on:
            out.append(w)
    return out


def outside(path, cwd):
    path = os.path.expanduser(path)
    full = os.path.normpath(path if os.path.isabs(path) else os.path.join(cwd, path))
    return not (full == cwd or full.startswith(cwd.rstrip('/') + '/'))


def decide(call):
    if call.get('tool_name') != 'Bash':
        return None
    command = (call.get('tool_input') or {}).get('command', '')
    if not DELETE.search(command):
        return None
    cwd   = os.path.normpath(call.get('cwd') or os.getcwd())
    args  = words_after_rm(command)
    flags = ''.join(a.lstrip('-') for a in args if a.startswith('-') and not a.startswith('--')) + ' '.join(a for a in args if a.startswith('--'))
    paths = [a for a in args if not a.startswith('-')]
    if ('r' in flags or 'R' in flags or 'recursive' in flags) and ('f' in flags or 'force' in flags):
        return ('deny', 'this is rm -rf')
    far = [p for p in paths if outside(p, cwd)]
    if far:
        return ('deny', f'this deletes outside the project: {", ".join(far)}')
    return ('ask', f'this deletes {", ".join(paths) or "files"}; say yes only if the agent made them in this session or you want them gone')


def main():
    try:
        call = json.load(sys.stdin)
    except ValueError:
        return 0
    answer = decide(call)
    if answer:
        decision, why = answer
        print(json.dumps({'hookSpecificOutput': {
            'hookEventName'           : 'PreToolUse',
            'permissionDecision'      : decision,
            'permissionDecisionReason': f'Behaviour policy RM-R0007: {why}. {LINE}'}}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
