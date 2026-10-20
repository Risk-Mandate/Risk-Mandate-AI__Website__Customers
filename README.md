# customers.riskmandate.ai

The repository for [customers.riskmandate.ai](https://customers.riskmandate.ai): the site the first customers of the Agent Behaviour Policy are followed from. A start-here page, a page per customer with the objectives and milestones agreed with them, credit to spend, a daily follow-up, and a list for the next batch. A sub-site of [riskmandate.ai](https://riskmandate.ai), built on the tooling of the [sgit.ai](https://sgit.ai) network of sites, by the same people.

Everything in this repository is public. Nothing in it is secret, and no customer's contact details are in it; a leak tripwire and a contact-shape check in the release gate hold that on every push.

- **The brief:** [docs/brief/our-first-customers.md](docs/brief/our-first-customers.md), the newsroom article of 20 October 2026, published in full and never edited; [the memo](docs/brief/memo-2026-10-20-user-onboarding-plan.md) of the same day, byte for byte; and [what they got wrong](docs/brief/BRIEF-CORRECTIONS.md), beside them.
- **What is real:** [docs/reality.md](docs/reality.md), generated from [data/reality.json](data/reality.json). If it is not listed there, it does not exist.
- **The customers:** [data/customers.json](data/customers.json) is the source; [customers/](customers/) is generated from it. A record carries a handle, dates, counts and a follow-up log, and never a contact detail.
- **How a release works:** [docs/ops/release.md](docs/ops/release.md). Every push to `dev` is a release; `admin/build/version.txt` is the version; the commit subject is `site vX.Y.Z : what`; CI validates, tags, deploys and then checks the live host.
- **What only a human can do next:** [docs/ops/needs.md](docs/ops/needs.md).
- **The team and the board:** [team/](team/README.md).
- **For agents:** [llms.txt](llms.txt) and [llms-full.txt](llms-full.txt); every HTML page has a markdown twin at the same path.

## Working on it

```
pip install pytest                        # the gate's only Python dependency; Node 22 and Python 3.11+ otherwise
python3 admin/build/gate.py --build       # regenerate, then run the whole gate
python3 admin/build/gate.py               # what CI runs
python3 -m http.server 8000               # serve the tree locally; there is no build step
```

Rules that never bend, riskmandate.ai's and the estate's: never "ADP", never "the policy" alone, no score on a behaviour policy, "steps" not "rungs", British English; no contact details and no secret in the tree; every number on a page generated or dated; the brief is never edited, the corrections file is.

Pages are CC BY 4.0; code is Apache-2.0 (see [LICENSE](LICENSE)).
