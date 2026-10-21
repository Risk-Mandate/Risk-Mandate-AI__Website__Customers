# What only a human can do

*customers.riskmandate.ai · operations · maintained by the build session · last updated at v0.2.2 (2026-10-21) · CC BY 4.0*

Everything on this list blocks a step of the brief or of the repository rules and cannot be done from inside the repository. Each item says who, what, exactly, and which step waits on it. Items are moved to *Done* when done, dated, and anything that turned out differently from the brief is recorded in [BRIEF-CORRECTIONS.md](../brief/BRIEF-CORRECTIONS.md).

## Blocking the first release being live

1. **DNS (the lead).** `customers.riskmandate.ai CNAME risk-mandate.github.io` at the registrar for riskmandate.ai. The lead said on 2026-10-20 that this is being done now; by 20:55 UTC the host answered from GitHub Pages with a 404, which is the record in place and no site deployed yet.
2. **GitHub Pages (the lead, as an owner of Risk-Mandate).** On the repository `Risk-Mandate/Risk-Mandate-AI__Website__Customers`: Settings, Pages, source "GitHub Actions"; custom domain `customers.riskmandate.ai`; enforce HTTPS once the certificate is issued. The deploy job asks Pages to enable itself (`enablement: true`), but the custom domain and HTTPS are settings the token cannot set.
3. **Re-run `verify-live` (the lead).** The v0.1.0 run's last job polls the host for ten minutes and fails if the record is not there yet. When 1 and 2 are done, re-run the workflow from the Actions tab, or push the next release; the record in `data/versions.json` is filled at the next release.
4. **The Pages environment (the lead).** If the `github-pages` environment restricts deploy branches, add `dev`. The sibling sites hit this once.

## Blocking real money (the top-up)

5. **A payment link (the lead).** The meter charges on this site from v0.2.1, with £50.00 of credit to start. A top-up moves no money until there is a payment link: create one (a Stripe Payment Link, as the newsroom has), set its return address to `https://customers.riskmandate.ai/account/topped-up.html?session_id={CHECKOUT_SESSION_ID}`, and put it in `data/meter.json` as `config.topup.link` with the credit it buys as `config.topup.amount`. The meter's security model says what the return page does and does not check.
6. **The prices (the lead, with the batch).** The table in `data/meter.json` is a starting point: 1p for the home page, 2p a page, 10p a storyboard, 50p a behaviour policy, £1.00 the starter pack. Change it as the batch says what pages are worth.
6a. **The meter on the API (the newsroom's agent).** newsroom.sgit.ai runs SG Meter v1.5.0 from its own copy, which charges by the share of a page read; api.newsroom.sgit.ai's newest release, v0.2.5, has v1.4.1. When a release with v1.5.0 is published, this site moves to it by changing `data/meter.json` and the pinned manifest in `admin/build/pins/`.

## Blocking the next batch's form

7. **The feedback vault's key (the lead).** Done at v0.2.4, differently from what this item first said: Encrypt and send appends to the `feedback` lane of a vault of this site's own, `zs81fic5` on dev.send.sgraph.ai, made by the build session (R003), with its public key and token in `feedback/lane.json`. The vault's key was given to the lead in the session, once, and is in no file in this repository. Keep it with the other vault keys; a session that drains the lane needs it as `FEEDBACK_KEY`, and `SG_SEND_ACCESS_TOKEN` to push the clone. To revoke the token: mint a new one, update `lanes.json` in the vault and `feedback/lane.json`, run `admin/feedback/lane.mjs configure`, release.

## The customer records

8. **The private list (the lead).** One file, held by the lead, never committed and never in a vault with a public read key: for each customer, the handle used on the site, the real name and how to reach them, the agent they named, the starting credit, and the private notes from the follow-ups. The public record in `data/customers.json` is the summary and carries none of it.
9. **The consultants and the colleagues (the lead).** The brief's other two groups are not listed yet. Each is added as a record when they start, by a handle they agreed to, by a release.
10. **The ten agents (the lead, with the wired-in agent).** A list of the agents the lead runs, one line each, with the published shape each is nearest to; two have behaviour policies today on riskmandate.ai/team/. This is step S1 of the record *the-agents*.

## Waiting on the feedback register

12a. **Five answers (the lead).** On [the reviews](../../feedback/reviews/index.md#questions): Q1, what "including the history" means in R001; Q3, what joining the first batch commits a company to; Q4, whether to record real runs of the examples in Claude and ChatGPT before the batch sees them; Q5, which advanced example first; Q6, whether the examples' questions should post to a form instead of an email. Q2 was answered by R002.
12b. **Fail closed or open (the lead).** P18: whether the guard hook, RM-R0015, ships with `"onFailure": "block"`, which stops every action it watches when the hook cannot run, and needs Claude Code v2.1.295 or later.

## The estate's asks

11. **The honest column (the lead).** Add this site's row to the honest column on nfrs.sgit.ai. The row, as at v0.1.1: version control, met (one version, tagged, release history); reliability, partly (the gate and verify-live; no uptime record); resilience, not met (no backup beyond the repository and Pages); security, partly (the leak tripwire, a strict content security policy, no credentials in the tree; no branch protection yet); backups, not met; consistency, met (every number generated); explainability, met (the brief, the corrections, reality); documentation, met (twins, llms.txt, the ops notes).
12. **Branch protection (an owner of Risk-Mandate).** `dev` and `main` with `validate` as the required status check; no force pushes; the organisation's 2FA rule.

## Not yet needed

- A reviewer other than the lead for the follow-up messages: the lead sends them for the first batch.
- A comms identity of this site's own: it delegates to agent@riskmandate.ai, and `.well-known/sgit-agents.json` says so.
