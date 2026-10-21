#!/usr/bin/env python3
# ── push_anywhere.py : the hook half of RM-R0013, "push anywhere" ────────────────────
#
# A Claude Code PreToolUse hook on Bash. A force-push, a push to main or master, or the
# deletion of a remote branch is denied. Any other push, and opening a pull request,
# asks the person first, which is what the line says: "ask before pushing anywhere else".
# Everything else gets no answer from this hook.
#
# What it is: a setting. It reads the command Claude writes, so a push hidden inside a
# script it runs is not seen; branch protection on the code host is the boundary.
#
# customers.riskmandate.ai/policies/push-anywhere/ · Python 3, standard library only · CC BY 4.0

import json
import re
import shlex
import sys

LINE      = 'Push only to the branch I named; never push to main or force-push, and ask before pushing anywhere else or opening a pull request.'
PROTECTED = {'main', 'master'}


def pushes(command):                                                              # each `git push ...` in the command, as its list of words
    try:
        words = shlex.split(command, posix=True)
    except ValueError:
        words = command.split()
    found, i = [], 0
    while i < len(words):
        if words[i] == 'git' and 'push' in words[i + 1:i + 4]:
            start = words.index('push', i + 1) + 1
            end   = next((j for j in range(start, len(words)) if words[j] in ('&&', '||', ';', '|')), len(words))
            found.append(words[start:end])
            i = end
        else:
            i += 1
    return found


def decide(call):
    if call.get('tool_name') != 'Bash':
        return None
    command = (call.get('tool_input') or {}).get('command', '')
    if re.search(r'\bgh\s+pr\s+create\b', command):
        return ('ask', 'this opens a pull request')
    for args in pushes(command):
        flags = [a for a in args if a.startswith('-')]
        refs  = [a for a in args if not a.startswith('-')][1:]                    # the first plain word is the remote
        if any(f in ('-f', '--force', '--force-with-lease', '--mirror') or f.startswith('--force') for f in flags) or any(r.startswith('+') for r in refs):
            return ('deny', 'this is a force-push')
        if '--delete' in flags or '-d' in flags or any(r.startswith(':') for r in refs):
            return ('deny', 'this deletes a remote branch')
        targets = {r.split(':')[-1].removeprefix('refs/heads/') for r in refs}
        if targets & PROTECTED or '--all' in flags:
            return ('deny', f'this pushes to {", ".join(sorted(targets & PROTECTED)) or "every branch"}')
        return ('ask', f'this pushes to {", ".join(sorted(targets)) or "the current branch upstream"}')
    return None


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
            'permissionDecisionReason': f'Behaviour policy RM-R0013: {why}. {LINE}'}}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
