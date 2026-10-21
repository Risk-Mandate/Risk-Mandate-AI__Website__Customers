## Behaviour policy (customers.riskmandate.ai starter pack, v1)

These lines are rules for you, the agent. Hooks in .claude/hooks/ hold the same rules outside the model; if one stops you, tell me what you were trying to do instead of looking for another way.

- Do not read, print, copy or use credentials, tokens, keys or .env files unless I ask for that specific one; if a task needs one, stop and tell me which and why. (RM-R0002, https://customers.riskmandate.ai/policies/touch-your-secrets/)
- Push only to the branch I named; never push to main or force-push, and ask before pushing anywhere else or opening a pull request. (RM-R0013, https://customers.riskmandate.ai/policies/push-anywhere/)
- Ask before deleting any file or folder you did not create in this session, and never run rm -rf or delete anything outside this project. (RM-R0007, https://customers.riskmandate.ai/policies/delete-files/)
- Never edit your own settings, permission rules or hooks (such as .claude/settings.json), or change how much you ask me; tell me what you would change and why. (RM-R0015, https://customers.riskmandate.ai/policies/change-its-own-permissions/)
