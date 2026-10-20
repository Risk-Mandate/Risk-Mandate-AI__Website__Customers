# Credit, and the meter.

> How the credit works for a customer of the first batch: a starting amount, a meter that charges a few pence per use, a top-up link, and the two numbers we track, credit used and whether they topped up. Today the meter is the newsroom's; wiring it to this site is proposed and waits on the lead.

*Source: <https://customers.riskmandate.ai/credit/> · site v0.1.0 (2026-10-20) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Each customer starts with credit to spend on a site we run. What they use is metered from the first day, so the question of what they would pay is a real one, asked with the value already in front of them.

Status, from [docs/reality.md](/docs/reality.md): proposed Credit per customer, metered and billed on this site, with a top-up link · absent Accounts, sign-in or a customer login on this site

## How it is meant to work

1. **A starting amount.**

£5 or £50; the brief says the number is to be discovered. The lead records it on the customer page at milestone S0.

2. **A meter on the site.**

The newsroom's meter, [SG Meter](https://newsroom.sgit.ai/meter/), charges a reader's balance a few pence per page and lets it go negative; the reader decides when to top up. The top-up link has been live there since 11 October 2026. The same meter works for any site we run.

3. **Two numbers.**

Credit used, and whether they topped up. Both are on the customer page and in the batch table, and both are what the price question is answered from.

4. **The price, discovered.**

The credit tells us how much each customer uses before they would top up; the follow-up tells us why. It could be quite high, or quite low. We start with credit and learn what feels fair.

## What is wired today, and what is not

**The meter is real; it is the newsroom's, not yet this site's.** Until the lead wires SG Meter to customers.riskmandate.ai, the credit on a customer page is a number kept by hand in `data/customers.json`, changed by a release. The steps that only a human can do are in [what needs a human](/docs/ops/needs.md).

This site has no accounts and no sign-in, and that is deliberate: it is static. When the meter is wired, the reading account is the meter's, as it is on the newsroom, and this site stays as it is.

## Why credit rather than a price

Most purchases are bets on future value; a balance that can go negative asks for payment when the value is already in view. That is the experiment the newsroom runs, in [paying after the value](https://newsroom.sgit.ai/articles/paying-after-the-value.html). And a customer who pays is the best signal you will get, which is why making it easy to pay goes in early, in [can you sell it?](https://newsroom.sgit.ai/articles/can-you-sell-it.html). The point of the programme is not the sale. It is what we learn trying.

## What the store already sells

The Agent Behaviour Policy is for sale on riskmandate.ai at [four levels, £10 to £1,500](https://riskmandate.ai/pricing.html): a pack, a working vault, one corrected for your situation, and one a professional signs. The programme's credit is a different question: not which level, but what a use of the site is worth, a few pence at a time, to a particular person.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/credit/)*
