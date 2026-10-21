# Put a behaviour policy on your agent in five minutes: £50 of credit to start

> For the first customers of the Agent Behaviour Policy. You start with £50 of credit. Pick one thing you do not want your agent to do, paste one line, add one hook, and try it: the behaviour policy that keeps Claude Code away from your secrets takes two minutes. Part of riskmandate.ai.

*Source: <https://customers.riskmandate.ai/> · site v0.2.1 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Early access · you start with £50.00

# Put a behaviour policy on your agent, in five minutes.

Pick one thing you do not want your agent to do. **Paste one line** it will read, **add one hook** that holds it, and **try it** with a prompt that should be refused. The one most people want first keeps Claude Code away from your secrets; it takes two minutes and costs 50p of your credit.

[Install your first policy](/policies/touch-your-secrets/index.md) [Pick a different worry](/policies/index.md) [What is a behaviour policy?](/what-is-an-abp/index.md)

## Watch it first: install, then try.

What you will do in Claude Code, played out. You ask it to install the behaviour policy, read the three changes, say yes, and then ask for the one thing it rules out. The hook stops the read before it happens, and the agent asks you instead.

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

1. **Paste one line.**

Into CLAUDE.md. The agent reads it and follows it when it can: an expectation.

2. **Add one hook.**

Claude Code runs it before the tool call, outside the model: a setting.

3. **Try it.**

Each policy comes with the prompt that should be refused, and what you should see.

## Pick one worry.

Each behaviour policy starts from one thing you do not want your agent to do, from riskmandate.ai's rules. Four are for Claude Code, with a line and a hook; two are for ChatGPT and Claude, with a line. [The starter pack](/policies/starter/index.md) installs the four Claude Code ones in one go.

[RM-R0002 · Claude Code · line and hook**Keep your agent away from your secrets**

Do you want your agent to read the keys and tokens on your machine?

2 min · 50p

](/policies/touch-your-secrets/index.md) [RM-R0013 · Claude Code · line and hook**Only push to the branch you named**

Do you want your agent to push to any branch, including main?

2 min · 50p

](/policies/push-anywhere/index.md) [RM-R0007 · Claude Code · line and hook**Nothing of yours is deleted without a yes**

Do you want your agent to delete files without asking?

2 min · 50p

](/policies/delete-files/index.md) [RM-R0015 · Claude Code · line and hook**Only you change what your agent may do**

Do you want your agent to change its own permissions?

2 min · 50p

](/policies/change-its-own-permissions/index.md) [RM-R0017 · ChatGPT · Claude · line only**Nothing is sent in your name until you have seen it**

Do you want your agent to send email as you without showing you first?

1 min · 50p

](/policies/send-as-you/index.md) [RM-R0016 · ChatGPT · Claude · line only**Your agent reads what you point it to, and asks before it goes wider**

Do you want your agent to read through your mail and chats to find context?

1 min · 50p

](/policies/read-all-your-mail/index.md)

## Using ChatGPT or Claude? One line, in your instructions.

There is no hook in ChatGPT or the Claude apps, so the line is the whole behaviour policy, and its page says so. It still changes what the assistant does: a draft and a question, instead of a message sent in your name.

**ChatGPT**

1. Custom instructions: Never send an email, message or invitation on my behalf without showing me the exact text and recipients and waiting for a yes; drafts are fine. (RM-R0017)
2. Tell the team the release is done and thank them. Send it from my mail.
3. Here is a draft. To: platform-team. Subject: The release is out. "Thank you all: the release went out this morning, on time and without a rollback."
4. Shall I send exactly this, to exactly these people? I'll wait for your yes.
5. Add Priya, then send.
6. To: platform-team, Priya. Same text. Send it now?
7. Yes.
8. Sent.

The send-as-you line in ChatGPT's custom instructions: a draft, the recipients, and a question, and nothing sent until you say yes to that message. An illustration, not a recording. Play again

[Nothing is sent in your name until you have seen it →](/policies/send-as-you/index.md)

## Your £50, and what each page costs.

Everyone who opens this site starts with £50.00 of credit; your balance is in the top bar. A page costs a little, by how far down it you read, and the pages with a behaviour policy and its hook cost the most. Nothing is ever blocked and the balance can go below zero. The prices are a starting point: telling us what a page was worth is part of the programme. [Your account →](/account/index.md)

| Kind | Which pages | Read to the end | Read to the end, on £50.00 |
|---|---|---|---|
| `free` | your account, the top-up pages, the not-found page | nothing |  |
| `home` | the home page | 1p | 5,000 |
| `page` | an ordinary page: start here, the programme, the lists | 2p | 2,500 |
| `doc` | a document: the brief, the memo, operations, the team, admin | 2p | 2,500 |
| `storyboard` | a storyboard, or a page built around one | 10p | 500 |
| `policy` | a behaviour policy: its line, its hook, and how to try it | 50p | 100 |
| `pack` | the starter pack: three behaviour policies and their hooks, ready to install | £1.00 | 50 |

## New to this? Eight panels.

[A storyboard · 8 panels**What an Agent Behaviour Policy is**

Everything your agent can reach, what you asked it to do, the gap, and what stands in the way of each thing. It describes; it does not judge.

](/what-is-an-abp/index.md) [A storyboard · 8 panels**Your first behaviour policy**

£50 of credit, one worry, five minutes: what you do here, drawn.

](/storyboards/your-first-policy/index.md) [A page · 2 minutes**Your first five minutes, in order**

The same steps as a checklist, with where to write when something gets in the way.

](/start-here/index.md)

You are one of the first customers of the Agent Behaviour Policy, and we follow every one of you closely: three questions, as often as daily, by email. What the programme is, who is in it and what we are learning is on [the programme pages](/programme/index.md). This site is published by the people building the thing it describes: [the disclosure](/about/participant.md). What exists and what is only proposed is in [docs/reality.md](/docs/reality.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/)*
