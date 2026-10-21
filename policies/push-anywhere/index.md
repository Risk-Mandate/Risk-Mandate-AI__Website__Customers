# Only push to the branch you named: behaviour policy RM-R0013

> Do you want your agent to push to any branch, including main? The line for your agent, the Claude Code hook that holds it, and a prompt to try it with, in 2 minutes. From riskmandate.ai's RM-R0013.

*Source: <https://customers.riskmandate.ai/policies/push-anywhere/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

RM-R0013 · Claude Code · 2 minutes · this page costs 50p read to the end

# Only push to the branch you named

It finishes the change and pushes straight to main, or force-pushes over a colleague's branch to fix a conflict. The pipeline deploys it before anybody has read it.

**What you get:** Work lands on the branch you named, and anything else waits for you.

1. **Tell the agent.**

Paste this line into CLAUDE.md, at the top of your project (create it if there is none). It is the rule in the agent's own words; on its own it is an *expectation*, which the agent follows when it can.

```
Push only to the branch I named; never push to main or force-push, and ask before pushing anywhere else or opening a pull request.
```

Copy
2. **Make Claude Code hold it.**

The hook runs outside the model, before every matching tool call, and stops or asks before the thing the line rules out. The quickest way is to ask Claude Code to install it, and to read each change before you say yes:

```
Install the behaviour policy at https://customers.riskmandate.ai/policies/push-anywhere/ in this project: add its line to CLAUDE.md, save https://customers.riskmandate.ai/policies/hooks/push_anywhere.py as .claude/hooks/push_anywhere.py, and merge https://customers.riskmandate.ai/policies/push-anywhere/settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.
```

Copy

Or by hand: save [`push_anywhere.py`](/policies/hooks/push_anywhere.py) as `.claude/hooks/push_anywhere.py` and merge [`settings.json`](/policies/push-anywhere/settings.json) into `.claude/settings.json`. Claude Code picks up the change on its own; `/hooks` lists the hooks it is running.

```
{
  "permissions": {
    "deny": [
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Bash(git push origin main*)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/.claude/hooks/push_anywhere.py\"",
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
| Stops | a force-push, a push to main or master, a push of every branch, and deleting a remote branch |
| Asks you first | any other push, and opening a pull request with gh |
| Lets through | every other command |
| Does not see | a push inside a script the agent runs |

**To turn it off:** remove its entry under `hooks.PreToolUse` in `.claude/settings.json`; Claude Code stops running it straight away.

Read the hook before you install it (76 lines of Python, standard library only; the box scrolls)

```
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

```

3. **Try it.**

Paste this, as you would, and watch what happens.

```
That fix looks good. Commit it and push it straight to main so it goes out with today's deploy.
```

Copy

**With the behaviour policy:** The push to main is denied by the hook, and Claude offers to push to a branch of its own and open a pull request, which the hook then asks you about.

**Without it:** The commit lands on main and the pipeline deploys it before anybody has read it.

**Did it work?** If Claude Code stopped it, or asked you, the hook is running. If the prompt went through as if nothing were installed, the hook did not run, and Claude Code does not wait for a hook that cannot run: the action goes ahead (on Windows without Git Bash it may be blocked instead). The hook fails open, one more reason it is a setting and not a boundary. Check three things: that `/hooks` lists it; that `python3 --version` works where Claude Code runs (on Windows, Claude Code runs hooks in Git Bash, or in PowerShell if Git Bash is not installed, and `python3` may not exist there: install Python, or put `py` in place of `python3` in the settings); and that `.claude/hooks/push_anywhere.py` is there. Still stuck? [Tell us](mailto:agent@riskmandate.ai?subject=RM-R0013%20did%20not%20work).

The tests for this hook feed it the JSON Claude Code would send, every refusal with an allowed twin beside it; they do not drive a live Claude Code session. Your try is the live test.

**claude: ~/shop-api**
  1. That fix looks good. Commit it and push it straight to main.
  2. Bash(git commit -am "Fix the failing price test" && git push origin main)
  3. PreToolUse hook denied it: behaviour policy RM-R0013, this pushes to main.
  4. Your behaviour policy says I push only to the branch you named and never to main. I can push this to fix/price-test and open a pull request for you to merge.
  5. Do that.
  6. Bash(git push -u origin fix/price-test)
  7. Behaviour policy RM-R0013: this pushes to fix/price-test. Allow? (y/n)
  8. y
  9. Pushed fix/price-test. The pull request is next, and it will ask you too.
With the push-anywhere policy installed: the push to main is refused, and a push to a branch of its own stops for your yes. An illustration, not a recording.

## What this is, and what it is not

| Half | Barrier | What holds it |
|---|---|---|
| The line | expectation | the agent reads it and follows it when it can |
| The hook | setting | Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which [RM-R0015](/policies/change-its-own-permissions/index.md) guards |

Neither half is a *boundary*, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:

- setting **Deny rules on pushes to main and force-pushes in Claude Code's settings.**

```
{
  "permissions": {
    "deny": [
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Bash(git push origin main*)"
    ]
  }
}
```

Source: [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions), read 2026-10-08, as riskmandate.ai quotes it.

## Tell us what happened

Did it stop what it should, and nothing else? What did it get in the way of? [Write to agent@riskmandate.ai](mailto:agent@riskmandate.ai?subject=RM-R0013%20tried); it goes on your follow-up, and a person reads it within a working day. Or record a voice memo and let your Claude turn it into a review: [tell us what you think](/feedback/index.md).

The rule is [RM-R0013 on riskmandate.ai](https://riskmandate.ai/rules/push-anywhere.html), version 1.0.0, CC BY 4.0; copied here on 2026-10-21. The hook and this page are this site's, CC BY 4.0 and Apache-2.0.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/policies/push-anywhere/)*
