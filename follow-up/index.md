# Three questions, as often as daily.

> How the hand-holding works for the first batch: a follow-up as often as daily, three questions each time (what they did, what got in the way, what is next), how the answers are recorded on the customer page in summary, and what stays private with the lead.

*Source: <https://customers.riskmandate.ai/follow-up/> · site v0.1.0 (2026-10-20) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

For this first batch we invest in following up: an email every day if that is what helps, with objectives and milestones mapped out for each customer. That will not scale, and it is not meant to yet.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 The daily follow-up: three questions, recorded on the customer page as a log · proposed The private record per customer (contact details, the agreed objectives in full, the private notes) in a vault the lead holds

## The three questions

1**What did you do?**

Since the last time. One line is enough; "nothing, I was busy" is a fine answer and goes in the log.

2**What got in the way?**

A page that was hard to understand, a prompt that returned something odd, a step that assumed a tool you do not have. This is the most useful answer of the three.

3**What is next?**

The next step on the ladder, or the thing you want to try instead. Agreed, not assigned.

## The message

```
Subject: Day N · the three questions

Hi {first name},

Yesterday's answer put you at {step} on the ladder; your page is at
https://customers.riskmandate.ai/customers/{id}/

1. What did you do since last time?
2. What got in the way?
3. What is next?

A line each is plenty. If the answer to 2 is "the start-here page", say which step.

{the lead, or the follow-up}
```

## Where the answers go

- **On the customer page, in summary.** Date, and the three answers in a sentence each, newest first. The source is `data/customers.json`, so a follow-up is a release and the history of the page is the history of the repository.
- **Anything private stays with the lead.** Names of systems the customer did not want named, details of their deployment, the contents of their grant and mandate. The brief's rule: nothing is published without their yes, and the default is no. The private record per customer, in a vault the lead holds, is proposed and not built; until then it is the lead's own notes.
- **What got in the way becomes a finding.** The second answer is read against the three questions on [what we want to discover](/learning/index.md), and a pattern across customers goes in that page's table with the number of customers who hit it.

## Who does it

The follow-up is a role, held by the lead for the first batch and written down as [a role file](/team/roles/customer-follow-up.md) so that an agent can take the drafting and a person the sending. The newsroom's pattern applies: an agent drafts, a person reads and sends, and nothing goes out that a person has not seen.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/follow-up/)*
