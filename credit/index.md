# Credit, and the meter.

> How the credit works: every reader starts with £50, each page costs a little by how far down it is read, a behaviour policy costs the most, and nothing is ever blocked. The meter is the newsroom's SG Meter, from api.newsroom.sgit.ai; there is no payment link yet.

*Source: <https://customers.riskmandate.ai/credit/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Everyone who opens this site starts with **£50.00** of credit. What you read is metered from the first page, so the question of what you would pay is a real one, asked with the value already in front of you.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.2.1 Every reader starts with £50 of credit, and every page has a price by its kind, metered by SG Meter from api.newsroom.sgit.ai · absent Accounts, sign-in or a customer login on this site

## What each page costs

By kind, in pence, for a page read to the end. A page you open and leave costs a tenth of its price; read half, pay half. Each page is charged once per browser session; coming back does not charge it again. The table is generated from `data/meter.json`.

| Kind | Which pages | Read to the end | Read to the end, on £50.00 |
|---|---|---|---|
| `free` | your account, the top-up pages, the page where you tell us what you think, the not-found page | nothing |  |
| `home` | the home page | 1p | 5,000 |
| `page` | an ordinary page: start here, the programme, the lists | 2p | 2,500 |
| `doc` | a document: the brief, the memo, operations, the team, admin | 2p | 2,500 |
| `storyboard` | a storyboard, or a page built around one | 10p | 500 |
| `example` | an example: a behaviour policy you try in Claude or ChatGPT, act by act | 50p | 100 |
| `policy` | a behaviour policy: its line, its hook, and how to try it | 50p | 100 |
| `pack` | the starter pack: four behaviour policies and their hooks, ready to install | £1.00 | 50 |

At the foot of every page is what that page has cost you so far, and three ratings: how useful it was sets the price, from free to double. If something was wrong with a page, you can say why and not be charged for it.

## How it works

- **The meter is the newsroom's.** [SG Meter](https://newsroom.sgit.ai/meter/) v1.4.1, loaded from [api.newsroom.sgit.ai](https://api.newsroom.sgit.ai/) at release v0.2.5, pinned, with the browser checking the file against the release's hash. newsroom.sgit.ai runs a newer meter, v1.5.0, from its own copy; it is not on the API yet.
- **It lives in your browser.** The balance and the history are this browser's, under one storage key, and are sent nowhere. Another browser starts again at £50.00. [Your account](/account/index.md) shows all of it, and can export it.
- **It never blocks.** Below zero is allowed. It is an honesty box, not a paywall, and [its security model](https://newsroom.sgit.ai/meter/security.html) says what a reader can do to it and why that is accepted.
- **Two numbers per customer.** Credit used, and whether they topped up. Both are on the customer's page, and both are what the price question is answered from.

## What is not wired yet

**No money moves yet.** The meter charges on this site from v0.2.1. There is no payment link of this site's own, so [the top-up page](/account/top-up.md) is the meter's simulated cart, which says it is simulated. The credit on a customer's page is still written by hand from what they tell us, because the meter's history never leaves their browser. What is waiting on the lead is in [what needs a human](/docs/ops/needs.md).

## Why credit rather than a price

Most purchases are bets on future value; a balance that can go negative asks for payment when the value is already in view. That is the experiment the newsroom runs, in [paying after the value](https://newsroom.sgit.ai/articles/paying-after-the-value.html). And a customer who pays is the best signal you will get, which is why making it easy to pay goes in early, in [can you sell it?](https://newsroom.sgit.ai/articles/can-you-sell-it.html). The point of the programme is not the sale. It is what we learn trying.

## What the store already sells

The Agent Behaviour Policy is for sale on riskmandate.ai at [four levels, £10 to £1,500](https://riskmandate.ai/pricing.html): a pack, a working vault, one corrected for your situation, and one a professional signs. The programme's credit is a different question: not which level, but what a use of the site is worth, a few pence at a time, to a particular person.

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/credit/)*
