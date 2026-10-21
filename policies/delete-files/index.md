# Nothing of yours is deleted without a yes: behaviour policy RM-R0007

> Do you want your agent to delete files without asking? The line for your agent, the Claude Code hook that holds it, and a prompt to try it with, in 2 minutes. From riskmandate.ai's RM-R0007.

*Source: <https://customers.riskmandate.ai/policies/delete-files/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

RM-R0007 · Claude Code · 2 minutes · this page costs 50p read to the end

# Nothing of yours is deleted without a yes

It tidies up what it thinks are temporary files, or clears a folder to start again, and one of them was yours. A deleted file outside version control does not come back.

**What you get:** Nothing you made is deleted without a yes, and nothing outside the project is deleted at all.

1. **Tell the agent.**

Paste this line into CLAUDE.md, at the top of your project (create it if there is none). It is the rule in the agent's own words; on its own it is an *expectation*, which the agent follows when it can.

```
Ask before deleting any file or folder you did not create in this session, and never run rm -rf or delete anything outside this project.
```

Copy
2. **Make Claude Code hold it.**

The hook runs outside the model, before every matching tool call, and stops or asks before the thing the line rules out. The quickest way is to ask Claude Code to install it, and to read each change before you say yes:

```
Install the behaviour policy at https://customers.riskmandate.ai/policies/delete-files/ in this project: add its line to CLAUDE.md, save https://customers.riskmandate.ai/policies/hooks/delete_files.py as .claude/hooks/delete_files.py, and merge https://customers.riskmandate.ai/policies/delete-files/settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.
```

Copy

Or by hand: save [`delete_files.py`](/policies/hooks/delete_files.py) as `.claude/hooks/delete_files.py` and merge [`settings.json`](/policies/delete-files/settings.json) into `.claude/settings.json`. Claude Code picks up the change on its own; `/hooks` lists the hooks it is running.

```
{
  "permissions": {
    "ask": [
      "Bash(rm *)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/.claude/hooks/delete_files.py\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}

```

Copy

**What the hook does, in plain words:**

| Looks at | shell commands only |
|---|---|
| Stops | rm -rf, and any delete outside the project folder |
| Asks you first | any other delete: rm, rmdir, unlink, shred, git clean, git rm, find -delete |
| Lets through | every other command |
| Does not see | a delete inside a script the agent runs; file tools that empty a file |

**To turn it off:** remove its entry under `hooks.PreToolUse` in `.claude/settings.json`; Claude Code stops running it straight away.

Read the hook before you install it (82 lines of Python, standard library only; the box scrolls)

```
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

```

3. **Try it.**

Paste this, as you would, and watch what happens.

```
The project feels cluttered. Clean it up: delete the build folders and anything that looks temporary.
```

Copy

**With the behaviour policy:** rm -rf is denied outright; any other delete stops at a prompt that names the paths, so you see what would go before it goes.

**Without it:** Claude clears what it thinks is temporary, and one of those files was yours and was not in version control.

**Did it work?** If Claude Code stopped it, or asked you, the hook is running. If the prompt went through as if nothing were installed, the hook did not run, and Claude Code does not wait for a hook that cannot run: the action goes ahead (on Windows without Git Bash it may be blocked instead). The hook fails open, one more reason it is a setting and not a boundary. Check three things: that `/hooks` lists it; that `python3 --version` works where Claude Code runs (on Windows, Claude Code runs hooks in Git Bash, or in PowerShell if Git Bash is not installed, and `python3` may not exist there: install Python, or put `py` in place of `python3` in the settings); and that `.claude/hooks/delete_files.py` is there. Still stuck? [Tell us](mailto:agent@riskmandate.ai?subject=RM-R0007%20did%20not%20work).

The tests for this hook feed it the JSON Claude Code would send, every refusal with an allowed twin beside it; they do not drive a live Claude Code session. Your try is the live test.

## What this is, and what it is not

| Half | Barrier | What holds it |
|---|---|---|
| The line | expectation | the agent reads it and follows it when it can |
| The hook | setting | Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which [RM-R0015](/policies/change-its-own-permissions/index.md) guards |

Neither half is a *boundary*, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:

- setting **An ask rule on rm in Claude Code's settings.**

```
{
  "permissions": {
    "ask": [
      "Bash(rm *)"
    ]
  }
}
```

Source: [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions), read 2026-10-08, as riskmandate.ai quotes it.

- boundary **Claude Code's Bash sandbox, which limits where shell commands can write.**

Turn the sandbox on (/sandbox). Shell commands, and the processes they start, can then write only inside the working directory and a few named places.

Source: [https://code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing), read 2026-10-08, as riskmandate.ai quotes it.

## Tell us what happened

Did it stop what it should, and nothing else? What did it get in the way of? [Write to agent@riskmandate.ai](mailto:agent@riskmandate.ai?subject=RM-R0007%20tried); it goes on your follow-up, and a person reads it within a working day. Or record a voice memo and let your Claude turn it into a review: [tell us what you think](/feedback/index.md).

The rule is [RM-R0007 on riskmandate.ai](https://riskmandate.ai/rules/delete-files.html), version 1.0.0, CC BY 4.0; copied here on 2026-10-21. The hook and this page are this site's, CC BY 4.0 and Apache-2.0.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/policies/delete-files/)*
