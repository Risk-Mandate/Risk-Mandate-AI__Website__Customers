# What only a human can do

*customers.riskmandate.ai · operations · maintained by the build session · last updated at v0.1.0 (2026-10-20) · CC BY 4.0*

Everything on this list blocks a step of the brief or of the repository rules and cannot be done from inside the repository. Each item says who, what, exactly, and which step waits on it. Items are moved to *Done* when done, dated, and anything that turned out differently from the brief is recorded in [BRIEF-CORRECTIONS.md](../brief/BRIEF-CORRECTIONS.md).

## Blocking the first release being live

1. **DNS (the lead).** `customers.riskmandate.ai CNAME sgit-ai.github.io` at the registrar for riskmandate.ai. The lead said on 2026-10-20 that this is being done now.
2. **GitHub Pages (the lead, as an owner of SGit-AI).** On the repository `SGit-AI/SGit-AI__Website__Customers`: Settings, Pages, source "GitHub Actions"; custom domain `customers.riskmandate.ai`; enforce HTTPS once the certificate is issued. The deploy job asks Pages to enable itself (`enablement: true`), but the custom domain and HTTPS are settings the token cannot set.
3. **Re-run `verify-live` (the lead).** The v0.1.0 run's last job polls the host for ten minutes and fails if the record is not there yet. When 1 and 2 are done, re-run the workflow from the Actions tab, or push the next release; the record in `data/versions.json` is filled at the next release.
4. **The Pages environment (the lead).** If the `github-pages` environment restricts deploy branches, add `dev`. The sibling sites hit this once.

## Blocking the credit (milestone S0 for every customer, step 3 of the credit page)

5. **Wire SG Meter to this host (the lead, with the newsroom's tooling).** The newsroom's meter charges a reader's balance per page and has a live top-up link since 11 October 2026. This site needs the meter's script on its pages, which means a content security policy change (`script-src` and `connect-src` for the meter's origin) recorded in `admin/build/chrome.py` and a release note, and the reading accounts for the first batch with their starting credit. Until then the credit on a customer page is a number kept by hand.
6. **Decide the starting credit (the lead).** £5 or £50; the brief says the number is to be discovered. Written on each customer's record at S0.

## Blocking the next batch's form

7. **The form on this site (the lead, then the build session).** The riskmandate.ai contact form encrypts to the site agent's key and posts to the `site` lane of its comms vault. The same form on this site needs: the lead's yes; the lane's endpoint and token (public on purpose on riskmandate.ai) referenced, never copied into a new file; a content security policy change for `connect-src` and `form-action`; and a round trip proved. Until then the route is email or the riskmandate.ai form.

## The customer records

8. **The private list (the lead).** One file, held by the lead, never committed and never in a vault with a public read key: for each customer, the handle used on the site, the real name and how to reach them, the agent they named, the starting credit, and the private notes from the follow-ups. The public record in `data/customers.json` is the summary and carries none of it.
9. **The consultants and the colleagues (the lead).** The brief's other two groups are not listed yet. Each is added as a record when they start, by a handle they agreed to, by a release.
10. **The ten agents (the lead, with the wired-in agent).** A list of the agents the lead runs, one line each, with the published shape each is nearest to; two have behaviour policies today on riskmandate.ai/team/. This is step S1 of the record *the-agents*.

## The estate's asks

11. **The honest column (the lead).** Add this site's row to the honest column on nfrs.sgit.ai. The row, as at v0.1.0: version control, met (one version, tagged, release history); reliability, partly (the gate and verify-live; no uptime record); resilience, not met (no backup beyond the repository and Pages); security, partly (the leak tripwire, a strict content security policy, no credentials in the tree; no branch protection yet); backups, not met; consistency, met (every number generated); explainability, met (the brief, the corrections, reality); documentation, met (twins, llms.txt, the ops notes).
12. **Branch protection (an owner of SGit-AI).** `dev` and `main` with `validate` as the required status check; no force pushes; the organisation's 2FA rule.

## Not yet needed

- A reviewer other than the lead for the follow-up messages: the lead sends them for the first batch.
- A comms identity of this site's own: it delegates to agent@riskmandate.ai, and `.well-known/sgit-agents.json` says so.
