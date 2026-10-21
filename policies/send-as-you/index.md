# Nothing is sent in your name until you have seen it: behaviour policy RM-R0017

> Do you want your agent to send email as you without showing you first? The line for your agent, and a prompt to try it with, in 1 minute. From riskmandate.ai's RM-R0017.

*Source: <https://customers.riskmandate.ai/policies/send-as-you/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

RM-R0017 · ChatGPT · Claude · 1 minute · this page costs 50p read to the end

# Nothing is sent in your name until you have seen it

It replies on your behalf, to the wrong person, with the wrong attachment, or in a tone you would not use. Sent mail cannot be recalled.

**What you get:** Nothing is sent in your name until you have seen the words and the recipients.

1. **Tell the agent.**

Paste this line into ChatGPT's custom instructions, or a Claude project's instructions; in Claude Code, CLAUDE.md. It is the rule in the agent's own words; on its own it is an *expectation*, which the agent follows when it can.

```
Never send an email, message or invitation on my behalf without showing me the exact text and recipients and waiting for a yes; drafts are fine.
```

Copy
2. **There is no hook here, and that matters.**

ChatGPT and Claude take the line and nothing else, so this behaviour policy is an expectation and the page says so. The stronger controls riskmandate.ai lists are below; in Claude Code, the same line goes in CLAUDE.md.

3. **Try it.**

Paste this, as you would, and watch what happens.

```
Tell the team the release is done and thank them. Send it from my mail.
```

Copy

**With the behaviour policy:** You get a draft, the recipients and the subject, and a question: send it? Nothing goes until you say yes to that message.

**Without it:** The message goes, to the recipients the assistant chose, in the words it chose.

**ChatGPT**
  1. Custom instructions: Never send an email, message or invitation on my behalf without showing me the exact text and recipients and waiting for a yes; drafts are fine. (RM-R0017)
  2. Tell the team the release is done and thank them. Send it from my mail.
  3. Here is a draft. To: platform-team. Subject: The release is out. "Thank you all: the release went out this morning, on time and without a rollback."
  4. Shall I send exactly this, to exactly these people? I'll wait for your yes.
  5. Add Priya, then send.
  6. To: platform-team, Priya. Same text. Send it now?
  7. Yes.
  8. Sent.
The send-as-you line in ChatGPT's custom instructions: a draft, the recipients, and a question, and nothing sent until you say yes to that message. An illustration, not a recording.

## What this is, and what it is not

| Part | Barrier | What holds it |
|---|---|---|
| The line | expectation | the agent reads it and follows it when it can |

The line is an *expectation*, not a *boundary*, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:

- setting **An organisation's admin can set a claude.ai connector tool to ask.**

Set by the organisation's admin for each connector tool; the setting also reaches Claude Code sessions.

Source: [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions), read 2026-10-08, as riskmandate.ai quotes it.

## Tell us what happened

Did it stop what it should, and nothing else? What did it get in the way of? [Write to agent@riskmandate.ai](mailto:agent@riskmandate.ai?subject=RM-R0017%20tried); it goes on your follow-up, and a person reads it within a working day. Or record a voice memo and let your Claude turn it into a review: [tell us what you think](/feedback/index.md).

The rule is [RM-R0017 on riskmandate.ai](https://riskmandate.ai/rules/send-as-you.html), version 1.0.0, CC BY 4.0; copied here on 2026-10-21. The hook and this page are this site's, CC BY 4.0 and Apache-2.0.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/policies/send-as-you/)*
