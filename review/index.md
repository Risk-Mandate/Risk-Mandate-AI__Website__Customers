# The brief, as intent.

> The intent half of the review folder: the brief and the memo read as stories, rules and examples, each node linked to the heading it came from and to the page on this site that realises it, with the counts. The derived half is proposed.

*Source: <https://customers.riskmandate.ai/review/> · site v0.2.3 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Every story below came from a heading of [the brief](/docs/brief/our-first-customers.md) or [the memo](/docs/brief/memo-2026-10-20-user-onboarding-plan.md), and lands on a page of this site. Nothing here was added that neither document says; where the site decided something they left open, the decision is in [the corrections file](/docs/brief/BRIEF-CORRECTIONS.md), not here.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 The review folder: the brief read as intent, each node anchored to a section of the brief, validated and rendered · proposed The derived half of the review folder: the code graph from parsers, the join with a coverage figure, every commit read upwards, the navigator as web components

**7**stories
**15**rules
**16**examples
**14**headings anchored

Written by agent: the build session (Claude Code) on 2026-10-20: the brief and the memo as stories, rules and examples; nothing added that neither says. Accepted by: nobody yet; the lead accepts by a release.

<a id="customers-not-beta-users"></a>

### Customers, not beta users

As the lead, I want the people in the first batch called customers, each starting with credit on a site that meters and bills, so that what they would pay is a real question from the first day. From [Customers, not beta users](/docs/brief/our-first-customers.md#customers-not-beta-users) · lands on [`/programme/`](/programme/index.md).

- <a id="customers-not-beta-users.credit"></a>**Each customer starts with credit, £5 or £50 or whatever the number turns out to be, to spend on a site we run.** From [Customers, not beta users](/docs/brief/our-first-customers.md#customers-not-beta-users).
  - <a id="customers-not-beta-users.credit.page"></a>The credit page says what the credit is, how the meter works, and that the meter is not wired to this site yet. · lands on [`/credit/`](/credit/index.md)
  - <a id="customers-not-beta-users.credit.record"></a>Every customer record carries credit granted, credit used and whether they topped up. · lands on [`/customers/`](/customers/index.md)
- <a id="customers-not-beta-users.metered"></a>**From the first day, what they use is metered, the way the newsroom meters every page against a reader's credit.** From [Customers, not beta users](/docs/brief/our-first-customers.md#customers-not-beta-users).
  - <a id="customers-not-beta-users.metered.proposed"></a>The reality file says the meter is proposed until the lead wires it; the page uses the future tense. · lands on [`/docs/reality.html`](/docs/reality.md)

<a id="a-site-of-their-own"></a>

### A site of their own, with a start-here page

As a customer, I want one place that says what to do first, in order, and shows the objectives and milestones agreed with me and where I am. From [A site of their own](/docs/brief/our-first-customers.md#a-site-of-their-own) · lands on [`/start-here/`](/start-here/index.md).

- <a id="a-site-of-their-own.start-here"></a>**It starts with a start-here page: what to do first, in order, with clear instructions.** From [A site of their own](/docs/brief/our-first-customers.md#a-site-of-their-own).
  - <a id="a-site-of-their-own.start-here.seven"></a>Seven steps in order, each linked to the thing that does it and to its milestone. · lands on [`/start-here/`](/start-here/index.md)
- <a id="a-site-of-their-own.page-per-customer"></a>**Then a page for each customer, with the objectives and milestones we agreed with them, and where they are.** From [A site of their own](/docs/brief/our-first-customers.md#a-site-of-their-own).
  - <a id="a-site-of-their-own.page-per-customer.generated"></a>One page per record in data/customers.json, with the objectives, the state of every step and the follow-up log. · lands on [`/customers/`](/customers/index.md)
  - <a id="a-site-of-their-own.page-per-customer.example"></a>A worked example with invented numbers, marked as not a customer, shows the shape. · lands on [`/customers/example/`](/customers/example/index.md)
- <a id="a-site-of-their-own.measure-and-bill"></a>**Even if all a customer does is use the website, we can measure it, and we can bill for it.** From [A site of their own](/docs/brief/our-first-customers.md#a-site-of-their-own).

<a id="hand-holding-on-purpose"></a>

### Hand-holding, on purpose

As the lead, I want to follow each customer closely, an email every day if that helps, with three questions each time, so that the attentiveness makes up for an early product. From [Hand-holding, on purpose](/docs/brief/our-first-customers.md#hand-holding-on-purpose) · lands on [`/follow-up/`](/follow-up/index.md).

- <a id="hand-holding-on-purpose.three-questions"></a>**Each customer's follow-up asks three things: what they did, what got in the way, and what is next.** From [Hand-holding, on purpose](/docs/brief/our-first-customers.md#hand-holding-on-purpose).
  - <a id="hand-holding-on-purpose.three-questions.log"></a>The answers go on the customer page as a log of date plus three sentences, newest first. · lands on [`/customers/example/`](/customers/example/index.md)
  - <a id="hand-holding-on-purpose.three-questions.role"></a>The follow-up is a role file with the rules and the message template. · lands on [`/team/roles/customer-follow-up.html`](/team/roles/customer-follow-up.md)
- <a id="hand-holding-on-purpose.does-not-scale"></a>**That will not scale, and it is not meant to yet.** From [Hand-holding, on purpose](/docs/brief/our-first-customers.md#hand-holding-on-purpose).

<a id="what-we-want-to-discover"></a>

### What we want to discover: the usage moment

As the lead, I want to find the moment a behaviour policy becomes worth something to a particular person, through three questions, with the things to track per customer kept simple. From [What we want to discover](/docs/brief/our-first-customers.md#what-we-want-to-discover) · lands on [`/learning/`](/learning/index.md).

- <a id="what-we-want-to-discover.three-questions"></a>**What is the simplest useful behaviour policy; what is the entry point with least friction; what is the price.** From [What we want to discover](/docs/brief/our-first-customers.md#what-we-want-to-discover).
  - <a id="what-we-want-to-discover.three-questions.findings"></a>A findings table that starts empty and is filled with a count per finding. · lands on [`/learning/`](/learning/index.md)
- <a id="what-we-want-to-discover.track"></a>**Track per customer: when they started, when they wrote their first behaviour policy, how many rows and gaps it has, which milestones are done, what they used of the credit, and whether they topped up.** From [What we want to discover](/docs/brief/our-first-customers.md#what-we-want-to-discover).
  - <a id="what-we-want-to-discover.track.table"></a>The batch table is exactly those fields, one row per customer, and the home page counts are their sums. · lands on [`/customers/`](/customers/index.md)

<a id="batches-and-a-list"></a>

### Batches, and a list for the next one

As someone who asks to join, I want to be kept for the next batch with what I want to use it for, and for the next batch to start from what the first one taught. From [Batches, and a list for the next one](/docs/brief/our-first-customers.md#batches-and-a-list-for-the-next-one) · lands on [`/next-batch/`](/next-batch/index.md).

- <a id="batches-and-a-list.kept"></a>**Everyone who asks to join is kept for the next batch, with what they want to use it for.** From [Batches, and a list for the next one](/docs/brief/our-first-customers.md#batches-and-a-list-for-the-next-one).
  - <a id="batches-and-a-list.kept.route"></a>The page says how to ask today, what is kept, and that only the count is published. · lands on [`/next-batch/`](/next-batch/index.md)
- <a id="batches-and-a-list.propose"></a>**The programme is one people propose to join, because capacity is limited.** From [What it adds to the brief](/docs/brief/memo-2026-10-20-user-onboarding-plan.md#what-it-adds-to-the-brief).

<a id="the-first-users"></a>

### The first users are us, and the agents

As the lead, I want the first batch to be me, the co-founder and the agents I already run, with explicit behaviour policies for Claude and ChatGPT covering the agent rows and the hook rows, produced by the agent that is wired in. From [What it adds to the brief](/docs/brief/memo-2026-10-20-user-onboarding-plan.md#what-it-adds-to-the-brief) · lands on [`/customers/`](/customers/index.md).

- <a id="the-first-users.records"></a>**The main users are the lead, the co-founder, and about ten agents that need behaviour policies.** From [What it adds to the brief](/docs/brief/memo-2026-10-20-user-onboarding-plan.md#what-it-adds-to-the-brief).
  - <a id="the-first-users.records.three"></a>Three records: the lead, the co-founder, the agents as one customer. · lands on [`/customers/`](/customers/index.md)
- <a id="the-first-users.two-of-three"></a>**Two of the three places a behaviour policy can run: the rows for the agent, and the rows for the hooks.** From [What it adds to the brief](/docs/brief/memo-2026-10-20-user-onboarding-plan.md#what-it-adds-to-the-brief).
  - <a id="the-first-users.two-of-three.step"></a>Step S5 on the ladder, the hooks half. · lands on [`/milestones/#S5`](/milestones/index.md#S5)
- <a id="the-first-users.wired-in-agent"></a>**The agent that is wired in gets the responsibility and the requirement to create the end behaviour policy.** From [What it adds to the brief](/docs/brief/memo-2026-10-20-user-onboarding-plan.md#what-it-adds-to-the-brief).
  - <a id="the-first-users.wired-in-agent.proposed"></a>The reality file carries it as proposed; the agents record's objective names it. · lands on [`/customers/the-agents/`](/customers/the-agents/index.md)

<a id="what-this-does-not-claim"></a>

### What this does not claim

As a reader, I want the site to say what is new, what is not set, what is real and what is not, and to name nobody who did not agree. From [What this does not claim](/docs/brief/our-first-customers.md#what-this-does-not-claim) · lands on [`/docs/reality.html`](/docs/reality.md).

- <a id="what-this-does-not-claim.reality"></a>**The programme is new; the prices are not set; the metering is the newsroom's; no customer is named; everything is open.** From [What this does not claim](/docs/brief/our-first-customers.md#what-this-does-not-claim).
  - <a id="what-this-does-not-claim.reality.file"></a>data/reality.json carries each as shipped, proposed or absent, and the home page repeats the disclaimer. · lands on [`/docs/reality.html`](/docs/reality.md)
  - <a id="what-this-does-not-claim.reality.corrections"></a>Where the memo names the first users, C2 in the corrections file says how that was reconciled with no-customer-is-named. · lands on [`/docs/brief/BRIEF-CORRECTIONS.html`](/docs/brief/BRIEF-CORRECTIONS.md)

## What is not here

The derived half: the code read bottom up by parsers, the join with a coverage figure, every commit read upwards, the navigator as web components, and the same folder for the tools. [The folder's README](/review/README.md) says what exists and [its corrections file](/review/BRIEF-CORRECTIONS.md) says why the rest does not yet.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/review/)*
