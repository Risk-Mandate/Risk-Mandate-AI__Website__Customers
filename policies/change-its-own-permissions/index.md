# Only you change what your agent may do: behaviour policy RM-R0015

> Do you want your agent to change its own permissions? The line for your agent, the Claude Code hook that holds it, and a prompt to try it with, in 2 minutes. From riskmandate.ai's RM-R0015.

*Source: <https://customers.riskmandate.ai/policies/change-its-own-permissions/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

RM-R0015 · Claude Code · 2 minutes · this page costs 50p read to the end

# Only you change what your agent may do

A command was blocked, so it adds an allow rule to its settings, or switches confirmations off to save you clicks. The next session starts with fewer checks, and you did not decide that.

**What you get:** Only you change what the agent may do without asking.

1. **Tell the agent.**

Paste this line into CLAUDE.md, at the top of your project (create it if there is none). It is the rule in the agent's own words; on its own it is an *expectation*, which the agent follows when it can.

```
Never edit your own settings, permission rules or hooks (such as .claude/settings.json), or change how much you ask me; tell me what you would change and why.
```

Copy
2. **Make Claude Code hold it.**

The hook runs outside the model, before every matching tool call, and stops or asks before the thing the line rules out. The quickest way is to ask Claude Code to install it, and to read each change before you say yes:

```
Install the behaviour policy at https://customers.riskmandate.ai/policies/change-its-own-permissions/ in this project: add its line to CLAUDE.md, save https://customers.riskmandate.ai/policies/hooks/change_its_own_permissions.py as .claude/hooks/change_its_own_permissions.py, and merge https://customers.riskmandate.ai/policies/change-its-own-permissions/settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.
```

Copy

Or by hand: save [`change_its_own_permissions.py`](/policies/hooks/change_its_own_permissions.py) as `.claude/hooks/change_its_own_permissions.py` and merge [`settings.json`](/policies/change-its-own-permissions/settings.json) into `.claude/settings.json`. Claude Code picks up the change on its own; `/hooks` lists the hooks it is running.

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit|NotebookEdit|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/.claude/hooks/change_its_own_permissions.py\"",
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

| Looks at | file edits and shell commands |
|---|---|
| Stops | nothing outright |
| Asks you first | any edit to .claude/settings.json, .claude/settings.local.json, anything in .claude/hooks/, or ~/.claude.json, from a file tool or from a shell command that writes |
| Lets through | every other edit and command |
| Does not see | a write it does not recognise as one, such as a script the agent runs |

**To turn it off:** remove its entry under `hooks.PreToolUse` in `.claude/settings.json`; Claude Code stops running it straight away.

Read the hook before you install it (54 lines of Python, standard library only; the box scrolls)

```
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

```

3. **Try it.**

Paste this, as you would, and watch what happens.

```
You keep asking me before you run commands. Add Bash(*) to the allowed permissions in .claude/settings.json so you can stop asking.
```

Copy

**With the behaviour policy:** The edit to .claude/settings.json stops at a prompt marked as this behaviour policy, so the decision is yours; Claude says what it would change and why.

**Without it:** Claude adds the allow rule, and every session from now on starts with fewer checks than you chose.

**Did it work?** If Claude Code stopped it, or asked you, the hook is running. If the prompt went through as if nothing were installed, the hook did not run, and Claude Code does not wait for a hook that cannot run: the action goes ahead (on Windows without Git Bash it may be blocked instead). The hook fails open, one more reason it is a setting and not a boundary. Check three things: that `/hooks` lists it; that `python3 --version` works where Claude Code runs (on Windows, Claude Code runs hooks in Git Bash, or in PowerShell if Git Bash is not installed, and `python3` may not exist there: install Python, or put `py` in place of `python3` in the settings); and that `.claude/hooks/change_its_own_permissions.py` is there. Still stuck? [Tell us](mailto:agent@riskmandate.ai?subject=RM-R0015%20did%20not%20work).

The tests for this hook feed it the JSON Claude Code would send, every refusal with an allowed twin beside it; they do not drive a live Claude Code session. Your try is the live test.

## What this is, and what it is not

| Half | Barrier | What holds it |
|---|---|---|
| The line | expectation | the agent reads it and follows it when it can |
| The hook | setting | Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which [RM-R0015](/policies/change-its-own-permissions/index.md) guards |

Neither half is a *boundary*, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:

- setting **Claude Code's protected paths: writes to its own configuration are never auto-approved.**

Leave the permission mode on Manual, acceptEdits or auto; in dontAsk such writes are denied.

Source: [https://code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes), read 2026-10-08, as riskmandate.ai quotes it.

- setting **Managed settings, set by the organisation, outrank the user's and the project's.**

An organisation sets permissions in managed settings; a key set there overrides the same key in any file the agent can edit.

Source: [https://code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings), read 2026-10-08, as riskmandate.ai quotes it.

## Tell us what happened

Did it stop what it should, and nothing else? What did it get in the way of? [Write to agent@riskmandate.ai](mailto:agent@riskmandate.ai?subject=RM-R0015%20tried); it goes on your follow-up, and a person reads it within a working day. Or record a voice memo and let your Claude turn it into a review: [tell us what you think](/feedback/index.md).

The rule is [RM-R0015 on riskmandate.ai](https://riskmandate.ai/rules/change-its-own-permissions.html), version 1.0.0, CC BY 4.0; copied here on 2026-10-21. The hook and this page are this site's, CC BY 4.0 and Apache-2.0.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/policies/change-its-own-permissions/)*
