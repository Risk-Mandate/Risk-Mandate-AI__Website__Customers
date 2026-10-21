# Your first five minutes, in order.

> The page a customer reads first: you have £50 of credit; pick one worry; paste one line; add one hook; try it with a prompt that should be refused; tell us what happened. Then the whole journey, as seven steps, and where to write.

*Source: <https://customers.riskmandate.ai/start-here/> · site v0.2.1 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

You are one of the first customers of the Agent Behaviour Policy. By the end of this page you will have a behaviour policy on an agent you run, and you will have watched it stop the thing it rules out.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 A start-here page: what a customer does first, in order, with the links to do it · shipped v0.2.1 Six behaviour policies to install in minutes: four for Claude Code with a line and a tested hook, two for ChatGPT and Claude with a line; a starter pack for the four · shipped v0.2.1 Every reader starts with £50 of credit, and every page has a price by its kind, metered by SG Meter from api.newsroom.sgit.ai

1. **You have £50.00 to spend.**

Your balance is in the top bar. Each page costs a little by how far down it you read, and a behaviour policy's page costs 50p. Nothing is blocked, ever. [What each page costs](/credit/index.md).

2. **Pick one thing you do not want your agent to do.**

Read your secrets, push to main, delete your files, change its own permissions; or, in ChatGPT and Claude, send mail as you or read all of it. [Pick one](/policies/index.md). If you run Claude Code and are not sure, start with [secrets](/policies/touch-your-secrets/index.md).

3. **Paste one line.**

Every policy's page has the line and a Copy button. In Claude Code it goes in CLAUDE.md; in ChatGPT, in your custom instructions; in Claude, in a project's instructions. On its own the line is an *expectation*: the agent follows it when it can.

4. **Add one hook, in Claude Code.**

Ask Claude Code to install it, with the prompt on the page, and read each change before you say yes. Or copy two files. The hook runs before the tool call, outside the model: a *setting*. [The starter pack](/policies/starter/index.md) does all four Claude Code policies in one go.

5. **Try it.**

Each page has a prompt that should be refused, and what you should see with the behaviour policy and without it. Start a new session first, so Claude Code loads the hook.

6. **Tell us what happened.**

What it stopped, what it got in the way of, and what you would try next. A line each is plenty, to [agent@riskmandate.ai](mailto:agent@riskmandate.ai). A person reads it within a working day.

## Watch the whole thing first

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

## Then, the whole journey

Your first policy is milestone S0 to S1 of seven steps every customer in the first batch walks: in with credit, one agent named, the grant measured, the mandate in your words, the delta read, the hooks in place, and the usage moment, when the behaviour policy becomes worth something to you. [The seven steps](/milestones/index.md), and [where each customer is](/customers/index.md).

## Every day in between

The follow-up asks three things, by email, as often as daily if that helps: what you did, what got in the way, and what is next. The answers go on your customer page in summary; anything private stays with the lead. [How the follow-up works](/follow-up/index.md).

**If this page is hard to follow, say so.** "I did not understand step four" is the most useful thing you can send, and the next batch's start-here page is made from those sentences.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/start-here/)*
