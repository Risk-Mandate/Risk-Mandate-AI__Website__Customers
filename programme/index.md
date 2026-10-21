# Customers, not beta users.

> What the early access programme is, from the brief: why the people in it are customers, not beta users, why each starts with credit on a site that meters, why there is a dedicated site, why the hand-holding does not scale and is not meant to yet, and what exists today against each of those.

*Source: <https://customers.riskmandate.ai/programme/> · site v0.2.2 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

The brief thought about what to call the people in the first batch: "early access users", "beta users", "the first batch". Beta describes the state of the product. What we want to name is the relationship. So they are customers, and the programme is built around that word.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 The brief and the memo published in full, never edited, with the corrections file beside them · shipped v0.1.0 A page per customer with the fields the brief asks to track, generated from data/customers.json, with no contact details · shipped v0.1.0 The daily follow-up: three questions, recorded on the customer page as a log · shipped v0.2.1 Every reader starts with £50 of credit, and every page has a price by its kind, metered by SG Meter from api.newsroom.sgit.ai

## Where the batch is, counted from the data.

Every number below is read from `data/customers.json` on every release; nothing is typed. The one worked example is not counted. [The batch, one row per customer →](/customers/index.md)

**3**customers in the first batch
**2**started
**0**first behaviour policies written
**3 of 21**milestone steps done
**£0 of £10**credit used
**0**topped up
**2**follow-ups recorded

## Why now

We have a workflow that works: grant, mandate, delta and barrier, with a holder for every row. We have a mapping to what regulators are now asking for, worked through against the FCA's four elements in [the Pellbridge agents](https://newsroom.sgit.ai/articles/inside-the-pellbridge-agents.html). And we have a good understanding of how it should all fit together, from [a behaviour policy beside the prompt](https://newsroom.sgit.ai/articles/a-policy-beside-the-prompt.html) to [one for every skill](https://newsroom.sgit.ai/articles/a-policy-for-every-skill.html). What is left is execution, and we have the people to execute it with: friendlies who are engaged and motivated. Some are consultants who are going to be selling this and already use some of it. Some are people the lead works with. Some of it is us.

## Each customer starts with credit

Each of them starts with credit, £5 or £50 or whatever the number turns out to be, to spend on a site we run. From the first day, what they use is metered, and the question of what they would pay is a real one. That is the same idea as [paying after the value](https://newsroom.sgit.ai/articles/paying-after-the-value.html): the newsroom gives every reader £5 of credit, each page uses a few pence, and the reader decides when to top up with the value already in front of them. Give it for free until there is enough value that they want to pay for it. The other reason is the one in [can you sell it?](https://newsroom.sgit.ai/articles/can-you-sell-it.html): a customer who pays is the best signal you will get, and making it easy to pay goes in early, not at the end. [Credit, and the meter: what is wired and what is not →](/credit/index.md)

## A site of their own

One place where we can follow how everyone is getting on, and where the lead can keep things up to date. It starts with [a start-here page](/start-here/index.md): what to do first, in order, with clear instructions. Then [a page for each customer](/customers/index.md), with the objectives and milestones agreed with them, and where they are. The billing is already there on the newsroom; the same works for any site we run: even if all a customer does is use the website, we can measure it, and we can bill for it. The price per use is something to discover.

## Hand-holding, on purpose

For this first batch we invest in following up: an email every day if that is what helps, very specific hand-holding, and objectives and milestones mapped out for each customer. That will not scale, and it is not meant to yet. Paul Graham made the case in [Do Things that Don't Scale](https://paulgraham.com/ds.html) (July 2013): the most common unscalable thing founders have to do at the start is to recruit users manually, and you can give users an insanely great experience with an early, incomplete, buggy product if you make up the difference with attentiveness. Each follow-up asks three things: what they did, what got in the way, and what is next. [The follow-up →](/follow-up/index.md)

## The first batch, after the memo

The voice memo of the same day made the first batch concrete. The first users are the lead, the co-founder, and the agents the lead already runs, about ten of them, which are the ones that need behaviour policies. The programme is one people can propose to join, because capacity is limited. The behaviour policies are explicit ones that work with Claude and with ChatGPT, and they cover two of the three places a behaviour policy can run: the rows for the agent, and the rows for the hooks. The agent that is already wired in gets the responsibility and the requirement to produce the end behaviour policy. The milestone is to find behaviour policies that add value to these users, with the onboarding as smooth and effective as it can be made, to the point where it adds a lot of value and they understand what the behaviour policy is doing. [The memo, verbatim →](/docs/brief/memo-2026-10-20-user-onboarding-plan.md)

## Batches, not a launch

This is a first batch, small enough to follow closely. Alongside it we keep a list: everyone who asks to join is kept for the next batch, with what they want to use it for. The next batch gets a start-here page made from what the first one taught us, and needs less hand-holding per customer. [The next batch →](/next-batch/index.md)

## What exists today, in this area

From [docs/reality.md](/docs/reality.md), generated on every release. A row that says proposed is described on this site in the future tense only.

| Area | Feature | Status | Where | Notes |
|---|---|---|---|---|
| programme | The brief and the memo published in full, never edited, with the corrections file beside them | shipped v0.1.0 | docs/brief/ | The newsroom article of 20 October 2026 and the voice memo of the same day, byte for byte, with its digest. |
| programme | A start-here page: what a customer does first, in order, with the links to do it | shipped v0.1.0 | start-here/index.html | The brief's first fix for pages that were hard to understand; each customer will show where it still is. |
| programme | A page per customer with the fields the brief asks to track, generated from data/customers.json, with no contact details | shipped v0.1.0 | data/customers.json, admin/build/gen_customers.py, customers/ | Start date, first behaviour policy with rows and gaps, steps done, credit used, topped up, and the follow-up log. One worked example, marked as such. |
| programme | Seven milestone steps shared across the batch, from in-with-credit to the usage moment | shipped v0.1.0 | data/milestones.json, milestones/index.html | The objectives per customer are theirs; the steps are the shared shape so the batch reads in one table. |
| programme | The daily follow-up: three questions, recorded on the customer page as a log | shipped v0.1.0 | follow-up/index.html, data/customers.json | What they did, what got in the way, what is next. Daily if that is what helps; the record is the summary. |
| programme | The three questions the programme exists to answer, with a findings table that starts empty | shipped v0.1.0 | learning/index.html | The simplest useful behaviour policy, the entry point with least friction, the price that feels fair. |
| programme | Every reader starts with £50 of credit, and every page has a price by its kind, metered by SG Meter from api.newsroom.sgit.ai | shipped v0.2.1 | data/meter.json, assets/site-config.js, admin/build/chrome.py, account/ | Meter v1.4.1 from the API release v0.2.5, pinned and checked against its hash. Charged by how far down a page is read; nothing is blocked. The balance lives in the reader's browser. |
| programme | A payment link, so a top-up moves money | proposed | data/meter.json config.topup.link, docs/ops/needs.md | Until the lead adds one, the top-up page is the meter's simulated cart, which says so. |
| programme | Six behaviour policies to install in minutes: four for Claude Code with a line and a tested hook, two for ChatGPT and Claude with a line; a starter pack for the four | shipped v0.2.1 | data/policies.json, data/rules/, policies/, tests/build/test_hooks.py | Built from riskmandate.ai's rules, copied byte for byte. Every hook refusal in the tests has an allowed twin. |
| programme | Three storyboards drawn in the reader's browser by the kit from api.storyboards.sgit.ai: what an ABP is, your first policy, the first batch | shipped v0.2.1 | storyboards/, data/storyboards.json, assets/storyboards.js | The kit is pinned and loaded with its integrity strings; its delay attributes are allowed by hash and no other inline style. |
| programme | Animated demos of a session: installing and trying a policy in Claude Code, and the send-as-you line in ChatGPT | shipped v0.2.1 | data/demos.json, assets/demo.js | Illustrations of what each policy's page promises, labelled as such; not recordings. Still and complete with reduced motion or no JavaScript. |
| programme | A form on this site for the next batch, encrypted in the browser to the riskmandate.ai agent's lane | proposed | next-batch/index.html | Today the route is the riskmandate.ai contact form or an email to agent@riskmandate.ai; the page says so. |
| programme | The private record per customer (contact details, the agreed objectives in full, the private notes) in a vault the lead holds | proposed | docs/ops/needs.md | Never in this repository. The public page carries the summary. |
| programme | A behaviour policy for each of the agents the lead runs, produced by the agent that is wired in | proposed | customers/the-agents/ | The memo of 20 October: about ten agents; two have one today, on riskmandate.ai/team/. |
| programme | This site's row on the honest column at nfrs.sgit.ai | proposed | docs/ops/needs.md | Another repository; the ask is recorded. |
| programme | A page for giving feedback: one line by email, a voice memo your Claude turns into a review, or an interview by Claude | shipped v0.2.2 | /feedback/ | The two prompts are files too, in feedback/prompts/. Nothing is published without the reviewer's yes. |
| programme | Every review in one document: verbatim, our reading point by point with screenshots, and one register of proposals, each with a decision and a reason | shipped v0.2.2 | /feedback/reviews/ | Generated from data/feedback/ by admin/build/gen_feedback.py, which fails the build if a quote is not word for word in its memo or a proposal has no reason. |
| programme | Synthetic users: invented people driving the site one screenshot at a time, with their findings checked | shipped v0.2.2 | /feedback/synthetic/ | Study S1: five invented users on v0.2.1. Invented, not user research. The browser helper is in feedback/synthetic/tools/. |
| programme | A guided path through the barriers: the line, then the hook, then its guard, then a boundary, each stop ending in the question that leads to the next | proposed | /feedback/reviews/#p2 | P1 and P2 of the feedback register, from the lead's review R001; held for his further memos. |
| programme | A page for a team: one baseline for everybody through the repository, and managed settings so nobody turns it off | proposed | /feedback/reviews/#p14 | P14, from study S1; waits for the guided path and for question Q3. |
| programme | Accounts, sign-in or a customer login on this site | absent | nowhere | The site is static. The meter, when wired, carries its own reading account, as on the newsroom. |
| programme | Customer contact details, company names that are not already public, or private notes in this repository | absent | nowhere | The gate fails on anything contact-shaped in data/customers.json. |
| programme | A score, rating or level on any behaviour policy | absent | nowhere | An Agent Behaviour Policy describes and does not judge. The gate fails on the words. |

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/programme/)*
