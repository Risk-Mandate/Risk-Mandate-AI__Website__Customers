# Install the starter pack (v1) from customers.riskmandate.ai

For the agent the person is talking to. Four Agent Behaviour Policies, each a line for CLAUDE.md and a Claude Code hook. Follow these steps in order. Show the person every file before you write it, and wait for a yes for each one. Do not change anything this file does not name, and do not remove anything already in their settings.

1. Tell the person what is about to be installed: the four lines in https://customers.riskmandate.ai/policies/starter/CLAUDE.md, and that each comes with a hook that stops or asks before the thing the line rules out.
2. Fetch and show each hook, then save it, keeping its name:
   - https://customers.riskmandate.ai/policies/hooks/touch_your_secrets.py to `.claude/hooks/touch_your_secrets.py`
   - https://customers.riskmandate.ai/policies/hooks/push_anywhere.py to `.claude/hooks/push_anywhere.py`
   - https://customers.riskmandate.ai/policies/hooks/delete_files.py to `.claude/hooks/delete_files.py`
3. Merge https://customers.riskmandate.ai/policies/starter/settings.json into the project's `.claude/settings.json`: add its `permissions` entries and its `hooks.PreToolUse` entries to any already there, keep everything else, and show the person the result before saving it. Create the file if there is none.
4. Add the block in https://customers.riskmandate.ai/policies/starter/CLAUDE.md to the end of the project's CLAUDE.md, creating it if there is none.
5. Last, because from then on any change to your own settings asks the person: save https://customers.riskmandate.ai/policies/hooks/change_its_own_permissions.py to `.claude/hooks/change_its_own_permissions.py`.
6. Tell the person to start a new session, or open /hooks, so Claude Code loads the hooks, and give them the four prompts on https://customers.riskmandate.ai/policies/starter/ to try.

The hooks need Python 3 and nothing else. Each is under eighty lines; the person may want to read them, and should.
