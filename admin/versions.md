# Release history

> Every release of customers.riskmandate.ai, newest first, from data/versions.json: the version, the date, the title that was the commit subject, and a note that says what changed and why in words a reader can act on. The tag for each is on the repository.

*Source: <https://customers.riskmandate.ai/admin/versions.html> · site v0.2.0 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

One row per release, newest first. The version lives in `admin/build/version.txt`, goes up on every push to `dev`, and is the commit subject, `site vX.Y.Z : what`. CI tags the commit and deploys it, and then checks the live host serves it. The note says what changed and why, not "UI improvements".

| Version | Date | Release | What changed, and why |
|---|---|---|---|
| `v0.2.0` | 2026-10-21 | six themes, the newsroom's five mapped onto RiskMandate's look plus its own dark; the header fits an iPad | A theme pill in the header picks one of six, kept in this browser: RiskMandate (the default, riskmandate.ai's paper and green), Canvas (its dark, from the dark hero band), and newsroom.sgit.ai's Night, Ember, Paper and Blueprint, mapped onto this site's tokens. Every colour now lives in assets/themes.css and nowhere else; site.css reads tokens only. A new test fails the build on a theme missing a token, a colour written outside that file, or a pair under its contrast in any theme; it found riskmandate.ai's green at 4.24:1 on its own alternate band, so the link accent is one shade darker. The header lost the first-batch stage pill, gained the picker beside the version, and now folds its links behind the menu button below 1100px: between 1040 and 1200 the version chip used to run past the right edge and the page scrolled sideways, which is an iPad in landscape. Wide tables scroll inside themselves on a phone instead of widening the customers page. docs/ops/themes.md says how it works and how to add a seventh. |
| `v0.1.1` | 2026-10-20 | the repository moved to Risk-Mandate; the source links and the DNS target follow it | The lead moved the repository from the SGit-AI organisation to Risk-Mandate/Risk-Mandate-AI__Website__Customers between the first push and the first CI run, and pointed customers.riskmandate.ai at risk-mandate.github.io. Every source link on the site, the release script's Actions lookup, the participant disclosure and the DNS line in needs.md now name the new home; the corrections file records the move as C9. Nothing else changed. |
| `v0.1.0` | 2026-10-20 | the first customers site: the brief, the start-here page, the batch, the steps and the gate | The site exists, as customers.riskmandate.ai, a sub-site of riskmandate.ai, built from the newsroom brief of 20 October 2026 and the voice memo that followed it the same day. What is here: the brief published in full with its corrections file beside it; a start-here page in order; the programme pages (customers not beta users, credit and the meter, the seven milestone steps, the daily follow-up, what we want to discover, the next batch); a page per customer generated from data/customers.json with no contact details in it; the reality file; the team as files; the review folder with the brief as intent; and the eight-check gate with a leak tripwire and the house words. What is not here: the meter (the newsroom's, not yet wired to this site), a form, any customer's private details, and the derived half of the review folder. Every number on a page is counted from a file. |

The release records in `data/versions.json` also carry, once CI has run, the commit, the Actions run and whether verify-live passed; the release script fills them in at the next release. [How a release works →](/docs/ops/release.md)

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/admin/versions.html)*
