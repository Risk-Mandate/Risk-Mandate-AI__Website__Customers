# customers.riskmandate.ai: reality

*Generated from `data/reality.json` by `admin/build/gen_reality.py` at site v0.2.2 (2026-10-21). If this document does not list it, it does not exist. The brief is an aspiration; this file is the fact.*

30 claims: 19 shipped, 8 proposed, 3 absent.

| Status | Meaning |
|---|---|
| shipped | exists in the repository, runs, and was exercised at the version shown |
| proposed | the brief or the memo says how; not built; described only in the future tense |
| absent | deliberately not on this site; comes as a later version, lives elsewhere, or never |

## Shipped (19)

| Area | Feature | Status | Where | Notes |
|---|---|---|---|---|
| site | One version in admin/build/version.txt, a release history, and four CI jobs: validate, tag, deploy, verify live | shipped v0.1.0 | admin/build/version.txt, data/versions.json, .github/workflows/deploy-pages.yml | Copied from secrets.sgit.ai, the newest gate in the estate. A clean push is not a release: verify-live polls the host. |
| site | The RiskMandate chrome (head, header, breadcrumbs, footer, CSP) generated into every page from one definition | shipped v0.1.0 | admin/build/chrome.py, admin/build/gen_chrome.py, assets/site.css | The look of riskmandate.ai; every colour is a token in one file. |
| site | Six themes picked from the header and kept in the reader's browser: RiskMandate (the default), Canvas, Night, Ember, Paper, Blueprint | shipped v0.2.0 | data/themes.json, assets/themes.css, assets/theme.js, tests/build/test_themes.py | The newsroom's five themes mapped onto this site's tokens, plus riskmandate.ai's own dark. Every colour is a token in one file; the gate checks every theme for every token and for contrast. |
| site | A markdown twin for every page, llms.txt, llms-full.txt and sitemap.xml, generated from the pages | shipped v0.1.0 | admin/build/gen_twins.py, admin/build/gen_llms.py | Links inside the markdown point at markdown. |
| site | The eight-check gate: version agreement, links and orphans, canonical host, the leak tripwire, no foreign runtime origin, the data holding together, reality regenerating identically, the house words | shipped v0.1.0 | admin/build/validate.js, admin/build/gate.py, tests/ | The house words are riskmandate.ai's rules, listed on the admin page and in WORD_RULES in admin/build/validate.js. The verbatim brief and memo are exempt. |
| site | The review folder: the brief read as intent, each node anchored to a section of the brief, validated and rendered | shipped v0.1.0 | review/intent/, review/tools/, review/index.html | The top-down half only; see site.review-derived. |
| programme | The brief and the memo published in full, never edited, with the corrections file beside them | shipped v0.1.0 | docs/brief/ | The newsroom article of 20 October 2026 and the voice memo of the same day, byte for byte, with its digest. |
| programme | A start-here page: what a customer does first, in order, with the links to do it | shipped v0.1.0 | start-here/index.html | The brief's first fix for pages that were hard to understand; each customer will show where it still is. |
| programme | A page per customer with the fields the brief asks to track, generated from data/customers.json, with no contact details | shipped v0.1.0 | data/customers.json, admin/build/gen_customers.py, customers/ | Start date, first behaviour policy with rows and gaps, steps done, credit used, topped up, and the follow-up log. One worked example, marked as such. |
| programme | Seven milestone steps shared across the batch, from in-with-credit to the usage moment | shipped v0.1.0 | data/milestones.json, milestones/index.html | The objectives per customer are theirs; the steps are the shared shape so the batch reads in one table. |
| programme | The daily follow-up: three questions, recorded on the customer page as a log | shipped v0.1.0 | follow-up/index.html, data/customers.json | What they did, what got in the way, what is next. Daily if that is what helps; the record is the summary. |
| programme | The three questions the programme exists to answer, with a findings table that starts empty | shipped v0.1.0 | learning/index.html | The simplest useful behaviour policy, the entry point with least friction, the price that feels fair. |
| programme | Every reader starts with £50 of credit, and every page has a price by its kind, metered by SG Meter from api.newsroom.sgit.ai | shipped v0.2.1 | data/meter.json, assets/site-config.js, admin/build/chrome.py, account/ | Meter v1.4.1 from the API release v0.2.5, pinned and checked against its hash. Charged by how far down a page is read; nothing is blocked. The balance lives in the reader's browser. |
| programme | Six behaviour policies to install in minutes: four for Claude Code with a line and a tested hook, two for ChatGPT and Claude with a line; a starter pack for the four | shipped v0.2.1 | data/policies.json, data/rules/, policies/, tests/build/test_hooks.py | Built from riskmandate.ai's rules, copied byte for byte. Every hook refusal in the tests has an allowed twin. |
| programme | Three storyboards drawn in the reader's browser by the kit from api.storyboards.sgit.ai: what an ABP is, your first policy, the first batch | shipped v0.2.1 | storyboards/, data/storyboards.json, assets/storyboards.js | The kit is pinned and loaded with its integrity strings; its delay attributes are allowed by hash and no other inline style. |
| programme | Animated demos of a session: installing and trying a policy in Claude Code, and the send-as-you line in ChatGPT | shipped v0.2.1 | data/demos.json, assets/demo.js | Illustrations of what each policy's page promises, labelled as such; not recordings. Still and complete with reduced motion or no JavaScript. |
| programme | A page for giving feedback: one line by email, a voice memo your Claude turns into a review, or an interview by Claude | shipped v0.2.2 | /feedback/ | The two prompts are files too, in feedback/prompts/. Nothing is published without the reviewer's yes. |
| programme | Every review in one document: verbatim, our reading point by point with screenshots, and one register of proposals, each with a decision and a reason | shipped v0.2.2 | /feedback/reviews/ | Generated from data/feedback/ by admin/build/gen_feedback.py, which fails the build if a quote is not word for word in its memo or a proposal has no reason. |
| programme | Synthetic users: invented people driving the site one screenshot at a time, with their findings checked | shipped v0.2.2 | /feedback/synthetic/ | Study S1: five invented users on v0.2.1. Invented, not user research. The browser helper is in feedback/synthetic/tools/. |

## Proposed (8)

| Area | Feature | Status | Where | Notes |
|---|---|---|---|---|
| site | The derived half of the review folder: the code graph from parsers, the join with a coverage figure, every commit read upwards, the navigator as web components | proposed | review/ | The review brief asks for it from the first commit; this site has the intent half and says so in review/BRIEF-CORRECTIONS.md. |
| programme | A payment link, so a top-up moves money | proposed | data/meter.json config.topup.link, docs/ops/needs.md | Until the lead adds one, the top-up page is the meter's simulated cart, which says so. |
| programme | A form on this site for the next batch, encrypted in the browser to the riskmandate.ai agent's lane | proposed | next-batch/index.html | Today the route is the riskmandate.ai contact form or an email to agent@riskmandate.ai; the page says so. |
| programme | The private record per customer (contact details, the agreed objectives in full, the private notes) in a vault the lead holds | proposed | docs/ops/needs.md | Never in this repository. The public page carries the summary. |
| programme | A behaviour policy for each of the agents the lead runs, produced by the agent that is wired in | proposed | customers/the-agents/ | The memo of 20 October: about ten agents; two have one today, on riskmandate.ai/team/. |
| programme | This site's row on the honest column at nfrs.sgit.ai | proposed | docs/ops/needs.md | Another repository; the ask is recorded. |
| programme | A guided path through the barriers: the line, then the hook, then its guard, then a boundary, each stop ending in the question that leads to the next | proposed | /feedback/reviews/#p2 | P1 and P2 of the feedback register, from the lead's review R001; held for his further memos. |
| programme | A page for a team: one baseline for everybody through the repository, and managed settings so nobody turns it off | proposed | /feedback/reviews/#p14 | P14, from study S1; waits for the guided path and for question Q3. |

## Absent (3)

| Area | Feature | Status | Where | Notes |
|---|---|---|---|---|
| programme | Accounts, sign-in or a customer login on this site | absent | nowhere | The site is static. The meter, when wired, carries its own reading account, as on the newsroom. |
| programme | Customer contact details, company names that are not already public, or private notes in this repository | absent | nowhere | The gate fails on anything contact-shaped in data/customers.json. |
| programme | A score, rating or level on any behaviour policy | absent | nowhere | An Agent Behaviour Policy describes and does not judge. The gate fails on the words. |

*Source: [https://github.com/Risk-Mandate/Risk-Mandate-AI__Website__Customers](https://github.com/Risk-Mandate/Risk-Mandate-AI__Website__Customers) · CC BY 4.0*
