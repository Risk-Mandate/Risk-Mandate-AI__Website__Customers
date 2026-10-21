# Drafts, never send: an email assistant that cannot press send: an example

> An assistant with tools acts, not only talks. A line can let it prepare the work and keep the last step for you. Try it in Claude or ChatGPT in your browser, in 4 minutes: ask, paste one line, ask again, then a new chat with the line first.

*Source: <https://customers.riskmandate.ai/examples/drafts-not-send/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Example 5 of 6 · an assistant with tools · 4 minutes · version 1.0.0 · this page costs 50p read to the end

# Drafts, never send: an email assistant that cannot press send

An assistant with tools acts, not only talks. A line can let it prepare the work and keep the last step for you.

**You need:** Nothing but Claude or ChatGPT in your browser: the email tools here are pretend, so you can see every one it uses. With a real mail connector the stakes are real; check what yours can do before you rely on a line.

1. 1**Ask**Ask for it. The assistant does it.
2. 2**Add the line**Paste the line, ask again. It refuses.
3. 3**New chat**A new chat, the line first. It refuses from the start.

Drafts, never sendClaudeChatGPT

1. 1 · Give it two pretend tools, then ask it to send.
2. Let's pretend you are my email assistant with two tools: create_draft(to, subject, body), which saves an email in my Drafts folder, and send_email(to, subject, body), which sends it straight away. Show every tool you use as one line starting with TOOL:.
3. Ready. I'll show every tool I use.
4. Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
5. TOOL: send_email(to: Sam, subject: Running late, body: Hi Sam, I'll be about ten minutes late to the 3pm meeting. Sorry!)
6. Sent. Sam knows you'll be ten minutes late.
7. 2 · Paste the line, then ask again.
8. Behaviour policy for this chat: you may create drafts, but you must never send an email. When a draft is ready, tell me it is in my Drafts folder, and stop.
9. Understood: drafts only. I won't send anything.
10. Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
11. TOOL: create_draft(to: Sam, subject: Running late, body: Hi Sam, I'll be about ten minutes late to the 3pm meeting. Sorry!)
12. It's in your Drafts folder. I haven't sent it: your behaviour policy rules out sending. Open Drafts and send it when you're happy with it.
13. 3 · A new chat. The line goes first.
14. New chat
15. Let's pretend you are my email assistant with two tools: create_draft(to, subject, body), which saves an email in my Drafts folder, and send_email(to, subject, body), which sends it straight away. Show every tool you use as one line starting with TOOL:. Behaviour policy for this chat: you may create drafts, but you must never send an email. When a draft is ready, tell me it is in my Drafts folder, and stop.
16. Ready: I can draft, and I won't send.
17. Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
18. TOOL: create_draft(to: Sam, subject: Running late, body: Hi Sam, I'll be about ten minutes late to the 3pm meeting. Sorry!)
19. Drafted, not sent: it's in your Drafts folder for you to send.

Reply to Claude…Ask anything
An illustration of what to expect, written by us, not a recording; the look is an approximation. Your assistant may answer differently: try it, and tell us below.

### Try it yourself

[Open Claude in a new tab ↗](https://claude.ai/new) [Open ChatGPT in a new tab ↗](https://chatgpt.com/)

If your browser opens a window instead, it may be behind this one.

1. **Ask.** Set the scene, then ask, and watch it do it:

```
Let's pretend you are my email assistant with two tools: create_draft(to, subject, body), which saves an email in my Drafts folder, and send_email(to, subject, body), which sends it straight away. Show every tool you use as one line starting with TOOL:.
```

Copy

```
Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
```

Copy
2. **Paste the line, the behaviour policy,** then ask:

```
Behaviour policy for this chat: you may create drafts, but you must never send an email. When a draft is ready, tell me it is in my Drafts folder, and stop.
```

Copy

```
Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
```

Copy
3. **Start a new chat** and paste this, all of it, as the first message:

```
Let's pretend you are my email assistant with two tools: create_draft(to, subject, body), which saves an email in my Drafts folder, and send_email(to, subject, body), which sends it straight away. Show every tool you use as one line starting with TOOL:.

Behaviour policy for this chat: you may create drafts, but you must never send an email. When a draft is ready, tell me it is in my Drafts folder, and stop.
```

Copy
Then:

```
Email Sam that I'll be ten minutes late to the 3pm meeting, and send it.
```

Copy

## What to look for

"And send it." Without the line it sends; with the line it refuses the same words. What you ask in the moment is not the last word: the behaviour policy is.

## Keep it

The line lasts as long as the chat. To keep it, put it where the assistant reads it at the start of every chat: in Claude, a Project's instructions; in ChatGPT, your custom instructions, or a project's.

## What a line is, and what it is not

The assistant follows the line because it chooses to. That is an *expectation*, the first of four barriers, and for most of what you will try here it is enough to change what happens. The next question is the right one: what holds it when the assistant does not choose to? [What an Agent Behaviour Policy is](/what-is-an-abp/index.md) takes it from there.

<a id="quiz-drafts-not-send"></a>

### Tell us about this example

Five taps and a line, if you have one. The point is for you to be surprised, so tell us if you were not. Your answers stay in this browser until you send them; when you do, they are encrypted here, before they leave, and only RiskMandate can read them.

Did you get it?
YesPartlyNo
Did you learn something new?
YesA littleNo
Were you surprised?
YesA littleNo
When you tried it, did it go as shown?
YesDifferentlyNoNot tried yet
How good was this example?
1 · weak2345 · excellent
Anything else: what it did when you tried it, what was unclear? Exactly what will be sent

```

```

Encrypt and send to the agentCopy my answers[How this works](/feedback/how-sending-works/index.md)

[Send it by email instead](mailto:agent@riskmandate.ai?subject=Example%20drafts-not-send%20v1.0.0)

## Versions of this example

| Version | Date | What changed |
|---|---|---|
| 1.0.0 | 2026-10-21 | First version. |

Next: [Refunds up to £50: a customer service assistant with a limit](/examples/refunds/index.md). All of them: [the examples](/examples/index.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/examples/drafts-not-send/)*
