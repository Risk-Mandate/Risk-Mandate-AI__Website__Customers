# How the site is built

> How customers.riskmandate.ai is built and released: one version in one file, seven generators that keep the parts that must agree in agreement, an eight-check gate that fails the build, and a pipeline that validates, tags, deploys and then checks the live host. Copied from the newest gate in the sgit.ai estate.

*Source: <https://customers.riskmandate.ai/admin/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

A static site, served byte for byte from this repository by GitHub Pages. There is no build step at deploy time: seven small generators run before a commit and keep the parts that must agree in agreement, and a gate refuses the push when they do not.

Status, from [docs/reality.md](/docs/reality.md): shipped v0.1.0 One version in admin/build/version.txt, a release history, and four CI jobs: validate, tag, deploy, verify live · shipped v0.1.0 The RiskMandate chrome (head, header, breadcrumbs, footer, CSP) generated into every page from one definition · shipped v0.1.0 A markdown twin for every page, llms.txt, llms-full.txt and sitemap.xml, generated from the pages · shipped v0.1.0 The eight-check gate: version agreement, links and orphans, canonical host, the leak tripwire, no foreign runtime origin, the data holding together, reality regenerating identically, the house words · shipped v0.1.0 The review folder: the brief read as intent, each node anchored to a section of the brief, validated and rendered · proposed The derived half of the review folder: the code graph from parsers, the join with a coverage figure, every commit read upwards, the navigator as web components

## The one-screen version

```
pip install pytest                        # the gate's only Python dependency; Node 22 and Python 3.11+ otherwise
python3 admin/build/gate.py --build       # regenerate everything, then run the whole gate
python3 admin/build/gate.py               # what CI runs: check mode only
python3 -m http.server 8000               # serve the tree locally; there is no build step
python3 admin/build/release.py --version 0.2.2 --kind feature --title "what" --notes "why"   # the next patch: bump, build, gate, commit, push, verify live
```

## The generators, in order

| Generator | Reads | Writes |
|---|---|---|
| `gen_customers.py` | `data/customers.json`, `data/milestones.json` | a page per customer, the batch table, the steps, the counts on the home page |
| `gen_meter.py` | `data/meter.json`, `data/storyboards.json` | `assets/site-config.js` (the meter's config, £50 to start), the prices table |
| `gen_policies.py` | `data/policies.json`, `data/rules/`, `policies/hooks/` | every page and file under `policies/`: the behaviour policies, their settings, the starter pack and its `INSTALL.md` |
| `gen_storyboards.py` | `storyboards/`, `data/demos.json` | each bundle, the storyboard viewers and pages, and the demos |
| `gen_reality.py` | `data/reality.json` | `docs/reality.md`, the status lines and tables on the pages |
| `gen_docs.py` | `docs/**/*.md`, `team/**/*.md`, `review/*.md` | an HTML page beside each, and an index page per folder |
| `review/tools/` | the brief, `review/intent/stories.json` | `review/intent/sections.json`, the review page; validates the intent files |
| `gen_chrome.py` | `chrome.py`, `version.txt`, `CNAME` | the head, header, breadcrumbs and footer of every page |
| `gen_versions.py` | `data/versions.json` | the release table on [the release history](/admin/versions.md) |
| `gen_twins.py` | every page's `<main>` | the markdown twin beside it |
| `gen_llms.py` | every page and document | `llms.txt`, `llms-full.txt`, `sitemap.xml` |

## The eight checks of the gate

In `admin/build/validate.js`, with no dependency beyond Node. Every problem of every check is printed before the run fails, so one run shows everything.

1. **Version agreement.** `version.txt`, every badge, the release table, the indexes and the home twin say the same version.
2. **Internal links, fragments and no orphans.** Every link resolves against the real tree; every fragment exists; a page nothing links to fails, because an orphan is unpublished.
3. **Canonical host.** Every page's canonical URL and og:url are on the CNAME host and agree.
4. **The leak tripwire.** sgit key shapes, write tokens, cloud key prefixes, private key blocks, append tokens, bare account numbers, against every text file. The fix for a trip is a redaction, never a wider pattern.
5. **Code from another origin only from the two pinned releases.** The meter from api.newsroom.sgit.ai v0.2.5 and the storyboard kit from api.storyboards.sgit.ai v0.1.0, each URL a file of that release's manifest (copied in `admin/build/pins/`), loaded with the manifest's integrity and `crossorigin`; anything else fails. Every script parses; no inline script or style.
6. **The data holds together.** Every customer record has a page and every page a record; the milestones name the ladder; no contact details; the versions file is valid.
7. **Reality regenerates identically.** `docs/reality.md` and the status tables are what `data/reality.json` says.
8. **The house words.** riskmandate.ai's rules: never "ADP", never "the policy" alone, no score on a behaviour policy, "steps" not "rungs", British spelling, customers not "beta users". The verbatim brief and memo are exempt.

Plus an advisory that never fails the build: em-dashes in prose we write. Then `pytest tests/build/` (the chrome on every page, the twins, the customer data, the converters, and the themes: every token in every theme, no colour outside `assets/themes.css`, and contrast in all six) and `node --test tests/unit/` (the gate's own helpers). How the themes work, and how to add one, is in [the themes note](/docs/ops/themes.md).

## The four CI jobs

| Job | When | Does | On failure |
|---|---|---|---|
| `validate` | every push to `dev` or `main`, every pull request, manual dispatch | `python3 admin/build/gate.py` | nothing is tagged or deployed |
| `tag-release` | push to `dev` only | asserts `version.txt` equals the newest `site vX.Y.Z : …` commit subject and that the bump is the next minor, a patch or a major; tags; backfills; pushes the tags | no deploy |
| `deploy` | any push or dispatch, never a pull request | copies the tree minus `.git`, `.github`, `tests/unit` into the Pages artifact and deploys it | the previous version stays live |
| `verify-live` | after deploy | polls `https://customers.riskmandate.ai/admin/build/version.txt` and the home page badge, with a cache-buster, until both equal the version, for up to ten minutes | the run is red: green does not mean live |

The whole of it is in [how a release works](/docs/ops/release.md). What only a human can do, starting with the DNS record for this host, is in [what needs a human](/docs/ops/needs.md).

## Where this came from

The pipeline is copied from [secrets.sgit.ai](https://secrets.sgit.ai/admin/), the newest gate in the sgit.ai estate, as [every sgit repository](https://sgit.ai/docs/guidance/repositories.html) says a new repository should do first; the look and the house words are [riskmandate.ai](https://riskmandate.ai)'s, because this is a sub-site of it. What was changed and why is in [the corrections file](/docs/brief/BRIEF-CORRECTIONS.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/admin/)*
