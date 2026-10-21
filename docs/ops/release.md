# How a release works

*customers.riskmandate.ai · operations · written at v0.1.0 (2026-10-20), the numbering changed at v0.2.1 (2026-10-21) · CC BY 4.0*

Every push to `dev` is a release. There is no build step at deploy time: the committed tree is the deployed tree, and seven small generators keep the parts that must agree in agreement. One pipeline validates, tags, deploys and then checks that the live site is serving what was pushed.

## The version

- The version lives in one file, `admin/build/version.txt`, as `X.Y.Z` with no `v`.
- Every push to `dev` moves the third number: `0.2.0`, `0.2.1`, `0.2.2`, `0.2.3`. The lead decided this on 21 October 2026, the way riskmandate.ai numbers its releases. The second number moves only when the lead says the site has become a different thing; the first is the lead's. `tag_release.py` accepts a patch, a minor or a major `.0.0`, so the gate does not change with the convention.
- The release commit's subject is `site vX.Y.Z : <what>`, with the same version. CI anchors on the newest commit whose subject has that shape, not on HEAD, because a merge commit may sit on top.
- `data/versions.json` gets a new first row: version, date, title, notes. The title is the `<what>` of the subject. The note says what changed and why, in words a reader can act on.
- The version is repeated by the generators into every page badge, every markdown twin, `llms.txt`, `llms-full.txt`, `sitemap.xml` and the release table. Check 1 of the gate fails on any disagreement.

## The steps, locally

```
# 1. edit content; edit data/customers.json, data/reality.json as the facts change
python3 admin/build/release.py --version X.Y.Z --kind feature --title "<what>" --notes "<why>"
#    which does: bump version.txt and versions.json; gate.py --build; commit "site vX.Y.Z : <what>"; push dev; verify live
# or by hand:
python3 admin/build/gate.py --build      # regenerate everything, then run the whole gate
git add -A
git commit -m "site vX.Y.Z : <what>"
git push -u origin dev                   # or open a pull request to dev from claude/<description>-<session-id>
```

`gate.py --build` runs the generators in order (customers, reality, docs, the review tools, chrome, versions, twins, llms), then runs them again with `--check`, then `node admin/build/validate.js`, then `python3 -m pytest tests/build/ -q`, then `node --test tests/unit/**/*.test.js`. `gate.py` without `--build` runs the same list in check mode only, which is exactly what CI does.

## The steps, in CI (`.github/workflows/deploy-pages.yml`)

| Job | When | Does | On failure |
|---|---|---|---|
| `validate` | every push to `dev` or `main`, every pull request to either, manual dispatch | `python3 admin/build/gate.py` | nothing is tagged or deployed |
| `tag-release` | push to `dev` only | `admin/build/tag_release.py`: version.txt equals the newest `site vX.Y.Z` subject; the version is the next minor, a patch or a major `.0.0` after the newest tag; backfills missing historical tags; pushes `refs/tags/vX.Y.Z` | no deploy |
| `deploy` | any push or dispatch, never a pull request | `admin/build/assemble_site.py` copies the tree minus `.git`, `.github`, `tests/unit`, `node_modules` into `_site/`; upload and deploy to GitHub Pages | the previous version stays live |
| `verify-live` | after deploy | `admin/build/verify_live.py` polls `https://customers.riskmandate.ai/admin/build/version.txt` and the home page badge with a cache-buster until both equal the version, for up to ten minutes | the run is red; the site may be stale |

A push to `main` deploys without tagging: `main` is promoted from `dev` and is the fallback. Both branches deploy to the one Pages site of this repository, so whichever pushed last is what the host serves; `main` is promoted only to a version `dev` already released.

## Green does not mean live

A sibling site once pushed two releases that reported success and never reached anyone, because the Pages deploy job died downloading its own action. The `verify-live` job exists for that reason: the release is not done until the origin answers with the new version. When `verify-live` is red and `deploy` is green, the usual causes are the domain not yet pointing at Pages (see [needs.md](needs.md)), Pages not yet enabled for the repository with the custom domain, or a transient `429` on an action download, which a re-run fixes. The first release of this site, v0.1.0, was pushed before the DNS record existed, so its `verify-live` is expected red until the lead's step is done; the re-run is the lead's.

## The eight checks of the gate

See `/admin/` on the site or the header of `admin/build/validate.js`. The rule for the leak tripwire is worth repeating: the fix for a trip is always a redaction, never a wider pattern. The rule for the house words is riskmandate.ai's: the verbatim documents are exempt and nothing else is.

## Backfilling tags

`tag_release.py` tags every historical release commit that has no tag, oldest first, then pushes all the new tags. A tag that already points at its release commit is left alone. A tag that points elsewhere fails the job: tags are never moved.
