# Brief corrections: where the brief and the memo were wrong, open, or decided differently

*customers.riskmandate.ai · maintained by the build session · started at v0.1.0 (2026-10-20) · CC BY 4.0*

The brief ([our-first-customers.md](our-first-customers.md)) and the memo ([memo-2026-10-20-user-onboarding-plan.md](memo-2026-10-20-user-onboarding-plan.md)) are never edited. When building finds them wrong, open, or decides something they left to the builder, the finding goes here, dated, with what was done instead. Entries are numbered C1, C2, … and never removed; a later entry may say an earlier one was itself wrong.

## C1. The site is customers.riskmandate.ai, not customers.sgit.ai (2026-10-20, v0.1.0)

The repository was made as `SGit-AI__Website__Customers`, "repo for customers.sgit.ai", and the first instruction to the build session named that host. During the first session the lead corrected it: the programme is RiskMandate's, so the site is a sub-site of riskmandate.ai at `customers.riskmandate.ai`, and the lead changes the DNS record and the GitHub mapping. Done: the CNAME, every canonical URL, the chrome and the licence line say riskmandate.ai. The repository kept its name and its organisation (SGit-AI) for the first release; see C9. The pipeline and the repository rules are still the sgit.ai estate's, because that is where the tooling comes from; the look and the house words are riskmandate.ai's.

## C2. The brief says no customer is named; the memo names the first users (2026-10-20, v0.1.0)

The brief's last section says "No customer is named. The first group is people we already work with." The memo of the same day names the first users: the lead, the co-founder and the lead's agents. Decided: the two founders are listed as customers by their public names, because they are the company's own founders and are already named on riskmandate.ai; the agents are one record, "the lead's agents"; nobody else is listed until they start and agree to a handle; contact details are never in the repository and the gate fails on anything contact-shaped. One worked example with invented numbers, marked as such, shows the shape of a customer page.

## C3. The credit is not metered on this site yet (2026-10-20, v0.1.0)

The brief says "the site already meters and bills, the way this newsroom does today" and, in its own disclaimer, "the metering is real. It is this newsroom's meter today, not yet the programme's site." Both are true and the second is the one this site states: *programme.credit* is proposed in the reality file, the credit on a customer page is a number kept by hand, and wiring SG Meter to this host is the lead's step in [needs.md](../ops/needs.md). The credit page says so in its own status line.

## C4. The mailing list has no form on this site (2026-10-20, v0.1.0)

The brief proposes a mailing list. Decided: the list is held by the lead, never committed; the way to ask is an email to agent@riskmandate.ai or the riskmandate.ai contact form, which already encrypts to the agent's lane; a form on this site is proposed and not built, and the content security policy forbids forms until it is. The only thing published about the list is its count, as a row the lead updates by a release.

## C5. The milestones are shared steps; the objectives are each customer's own (2026-10-20, v0.1.0)

The brief asks for "objectives and milestones written with them". Decided: a shared ladder of seven steps for the whole batch (S0 to S6, in `data/milestones.json`), so the batch reads in one table and the next batch can be compared with this one, and free-text objectives per customer on their page. Step S5, the hooks half, is from the memo, not the brief. The word is steps: riskmandate.ai's rule.

## C6. The review folder has its top-down half only (2026-10-20, v0.1.0)

Every sgit repository is asked to carry a review folder from its first commit: the brief as intent, the code derived by parsers, the join, every commit read upwards, a navigator as web components, and review/self/. Done at v0.1.0: the brief as stories, rules and examples, each anchored to a section of the brief; a validator; a rendered review page. Not done: everything derived, the join, the navigator as web components, review/self/. Recorded as *site.review-derived*, proposed, and in [review/BRIEF-CORRECTIONS.md](../../review/BRIEF-CORRECTIONS.md).

## C7. The honest column row on nfrs.sgit.ai is an ask, not a change (2026-10-20, v0.1.0)

The repository rules ask each repository to add a row to the honest column on nfrs.sgit.ai saying what it meets and what it does not. That is another repository, which this session cannot write to. The row's content is in [needs.md](../ops/needs.md) for the lead to carry across.

## C8. "Policy" alone is never written here (2026-10-20, v0.1.0)

The brief and the memo say "policy" and "policies" alone throughout, as the newsroom does. riskmandate.ai's rule is that on its sites *policy* is also the insurance instrument, so the ABP is always *the ABP* or *the behaviour policy*. Decided: the rule applies to every word this site writes, and the gate enforces it; the brief and the memo are verbatim and exempt. The same for "beta users" (the brief's own heading is the one allowed use), "rung", "ADP", a score, and American spellings.

## C9. The repository moved to the Risk-Mandate organisation (2026-10-20, v0.1.1)

Between the first push and the first CI run the lead moved the repository from `SGit-AI/SGit-AI__Website__Customers` to `Risk-Mandate/Risk-Mandate-AI__Website__Customers`, so the site is served from the Risk-Mandate organisation's Pages, and the DNS record points at `risk-mandate.github.io`. GitHub redirects the old name. Done at v0.1.1: the source link in the chrome and the footer, the release script's Actions lookup, the participant disclosure and needs.md say the new name. The v0.1.0 release note and its commit keep the old name, because they are a record.
