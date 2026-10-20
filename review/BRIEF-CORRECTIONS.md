# Corrections to the review brief, for this repository

*customers.riskmandate.ai · started at v0.1.0 (2026-10-20) · CC BY 4.0*

The review brief is [Code review graphs in the repository](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.html), on sgit.ai. Where this repository does not follow it, the entry is here, dated, with the reason.

## R1. Only the intent half exists at v0.1.0 (2026-10-20)

The brief asks a new repository to build the whole folder before its first source file. This repository built the intent half (stories, rules, examples, anchored to the brief and the memo), a validator and a static rendering, and shipped the site. The derived half, the join, the change files, the web-component navigator and `self/` are proposed, recorded in `data/reality.json` as *site.review-derived*. Reason: the site had to exist on the day the brief was accepted; a review folder for a site that does not exist reviews nothing. The next change starts the derived half, delta first.

## R2. The brief's headings are not numbered (2026-10-20)

The review brief's `sections.json` keys sections by number. The newsroom article that is this site's brief has prose headings with no numbers, so `tools/sections.py` keys them by the heading's slug, which is also the anchor on the rendered page. The memo document is anchored the same way, and both are in one `sections.json` under `docs`.

## R3. The navigator is a page, not components (2026-10-20)

The brief asks for a navigator built as web components in the coding.sgit.ai shape. `review/index.html` is a static page rendered by `tools/render.py`, with the same links a navigator would have (every node to its section of the brief and to the page it lands on), and no script. The components come with the derived half.
