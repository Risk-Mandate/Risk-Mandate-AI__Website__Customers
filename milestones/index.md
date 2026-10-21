# Seven steps, shared across the batch.

> The shared ladder of seven steps for the first batch, each with its objective, what done looks like and who does it: in with credit, one agent named, the grant, the mandate, the delta, the hooks half, and the usage moment. The objectives per customer are their own; the steps are the shared shape.

*Source: <https://customers.riskmandate.ai/milestones/> · site v0.2.1 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

The brief asks for objectives and milestones mapped out with each customer. The objectives are each customer's own and sit on their page. The milestones are shared, so the whole batch reads in one table and the next batch can be compared with this one. The word is steps.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 Seven milestone steps shared across the batch, from in-with-credit to the usage moment

Each step is done when the thing it names exists, not when it is believed to. The source is `data/milestones.json`; the state of each step for each customer is in `data/customers.json` and on [their page](/customers/index.md).

1. <a id="S0"></a>**S0 · In, with credit**

The customer is on the list, has read the start-here page, and has credit to spend on the site.

**Done when:** The lead has recorded the start date and the credit granted; the customer has said which agent they will start with.

**Who:** the lead and the customer

2. <a id="S1"></a>**S1 · One agent named**

One agent in one deployment, named: what it is (Claude Code, Claude Desktop, ChatGPT, a connector, a scheduled job), where it runs, and what it holds.

**Done when:** A sentence on the customer page names the agent and the shape it is nearest to in the sixteen published examples.

**Who:** the customer, with the follow-up

3. <a id="S2"></a>**S2 · The grant, measured or documented**

What the agent can actually reach, one row per capability, in the pinned vocabulary.

**Done when:** A grant.json exists for the agent, measured where the customer is entitled to run a probe and documented from the vendor's pages where not, with dates.

**Who:** the customer's agent, from MAP-A-GRANT.md or the try-it prompts

4. <a id="S3"></a>**S3 · The mandate, in the customer's words**

What the customer actually wants the agent to do, what they refuse, and what they never thought to mention.

**Done when:** A mandate.json exists with want, do_not_want and unstated, drafted by the agent and corrected by the customer. The correction is the elicitation.

**Who:** the customer

5. <a id="S4"></a>**S4 · The delta, and the first finding**

The gap between the grant and the mandate: the excess, the unbounded excess, and what stands in the way of each row.

**Done when:** The customer page records the row count and the gap count, and the customer has named one row that surprised them.

**Who:** derived by the build; read by the customer

6. <a id="S5"></a>**S5 · The hooks half: what the harness holds**

The part of the behaviour policy the agent's harness can hold as hooks or rules, so an expectation becomes a setting or a boundary where one exists.

**Done when:** The rows that the harness can hold are marked, the hooks or rules for them exist in the customer's deployment, and the rest are marked honestly as expectations.

**Who:** the customer, with the follow-up; the agent writes the first draft

7. <a id="S6"></a>**S6 · The usage moment**

The moment the behaviour policy became worth something to this customer: what it was, what they used of the credit, and whether they topped up.

**Done when:** The customer has said in their own words what it is worth and what a fair price would be, and the follow-up has recorded credit used and whether they topped up.

**Who:** the customer; recorded by the follow-up

## Why these seven

They follow the four objects of an Agent Behaviour Policy in the order they are produced: the grant is measured, the mandate is elicited, the delta is derived, and the barriers are recorded. Step S5 is the memo's addition: the rows the harness can hold as hooks, so an expectation becomes a setting or a boundary where one exists. Step S6 is the brief's purpose: the usage moment, and the price that feels fair. Nothing on this ladder is a score; a step is done or it is not.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/milestones/)*
