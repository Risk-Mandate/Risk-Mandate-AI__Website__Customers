# The first batch, and where each customer is.

> The customers of the first batch and where each is: started, first behaviour policy with its rows and gaps, milestone steps done, credit used and topped up, and follow-ups recorded. Generated from data/customers.json on every release. One worked example, marked as such, shows the shape.

*Source: <https://customers.riskmandate.ai/customers/> · site v0.1.1 (2026-10-20) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

One row per customer, with the fields the brief asks us to track, and a page for each with the objectives agreed with them, the state of every milestone step and the follow-up log. The table and the pages are generated from `data/customers.json`; a change to the data is a release.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 A page per customer with the fields the brief asks to track, generated from data/customers.json, with no contact details · absent Customer contact details, company names that are not already public, or private notes in this repository

| Customer | Kind | Status | Started | First behaviour policy | Steps done | Credit | Follow-ups |
|---|---|---|---|---|---|---|---|
| [The lead (Dinis Cruz, co-founder)](/customers/lead/index.md) | us | starting | 2026-10-20 | not yet | 2 of 7 | £0 used of £5 granted; not topped up (credit is a starting point; the meter is the newsroom's, not yet this site's) | 1 |
| [The co-founder (Nimay Parekh, chief executive)](/customers/co-founder/index.md) | us | invited | not yet | not yet | 0 of 7 | £0 used of £5 granted; not topped up (credit is a starting point; the meter is the newsroom's, not yet this site's) | 0 |
| [The lead's agents (about ten, as one customer)](/customers/the-agents/index.md) | agents | starting | 2026-10-20 | not yet | 1 of 7 | none (the agents spend nothing; the measure for them is a behaviour policy each) | 1 |
| [Example Co (a worked example, not a customer)](/customers/example/index.md) | example | example | 2026-10-01 | 2026-10-04: 9 rows, 4 gaps | 5 of 7 | £12 used of £50 granted; not topped up (invented numbers, to show the page) | 2 |

## Who is in the first batch

The memo of 20 October named the first users: the lead, the co-founder, and the agents the lead already runs, about ten, counted here as one customer because the measure for them is a behaviour policy each. The brief named two more groups, not yet listed: consultants who will sell this and already use some of it, and people the lead works with. They are added as records when they start, by their own handle, and nothing about them is published without their yes.

## What a record carries, and what it never does

- **Carries:** a handle, a kind, a status, the start date, the agent in a sentence, the credit granted and used, the first behaviour policy's date with its row and gap counts, the state of each of the seven steps, the objectives, and the follow-ups as date plus three sentences.
- **Never:** an email address, a phone number, a profile link, a company name that is not already public, the contents of a grant or a mandate, or a private note. The gate fails the build on anything contact-shaped in the file.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/customers/)*
