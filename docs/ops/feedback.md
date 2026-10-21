# Feedback: from a memo to a decision, and invented users in between

*customers.riskmandate.ai · operations · written at v0.2.2 (2026-10-21) · CC BY 4.0*

The site learns from its customers in one loop: somebody tells us what they saw, we keep their words, read them point by point against what they were looking at, and every point leads to a proposal with a decision and a reason. We do not do everything a reviewer asks; every no has its reason in the register. Between reviews by people, invented users run the same pages and find what a page fails to say.

| What | Where it lives | What makes the page |
|---|---|---|
| A memo, word for word | `data/feedback/memos/<id>.txt` | nothing: it is never edited |
| Our reading of it | `data/feedback/reviews/<id>.json` | `admin/build/gen_feedback.py` |
| The screenshots it cites | `assets/feedback/<id>/*.webp` | `feedback/tools/shoot.cjs`, from a spec like `feedback/tools/R001-shots.json` |
| Every proposal, with a decision | `data/feedback/proposals.json` | the same generator |
| A synthetic study | `data/feedback/synthetic/` and `assets/feedback/S1/` | the same generator |
| The two prompts customers use | `feedback/prompts/*.txt` | served as they are, and shown on `/feedback/` |

## A review by a person

1. **Keep the words.** Save the memo or the transcript as `data/feedback/memos/R00N.txt`, as given. Paragraph breaks may be added; nothing else changes. The house-word check does not read this folder.
2. **Take the screenshots first,** of the version the reviewer saw. Serve that version locally (`git archive <commit> | tar -x -C <dir>`, then `python3 -m http.server`), check a page or two against the live site by sha256, and shoot the elements the memo is about with `feedback/tools/shoot.cjs`. Convert to WebP into `assets/feedback/R00N/`.
3. **Read it point by point** in `data/feedback/reviews/R00N.json`. Each point quotes the memo word for word (the build fails otherwise), takes a stance (agree, agree in part, disagree, a question, asked of us), says what we read in it, cites its screenshots, and names the proposals it leads to. Check facts about other people's products against their documentation, and name the page in `sources`.
4. **Decide.** Add or update proposals in `data/feedback/proposals.json`. Each has a decision (done, reversed, accepted, proposed, question, declined) and a reason; a done or reversed one names its version, and a decision that changes keeps its history (`history`), so the register shows what we decided at each version. Which points led to it is worked out, not written.
5. **Ask.** Anything only the reviewer can answer goes in `questions`.
6. `python3 admin/build/gate.py --build`, then release as usual.

Nothing a customer sends is published without their yes, and no contact details ever are: a test fails on an email address in `data/feedback/` other than ours.

## A synthetic study

Follow newsroom.sgit.ai's method, [How to run synthetic users](https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html), as adapted in `data/feedback/synthetic/protocol.json`:

1. **Before any run:** the invented users in `personas.json` (a situation and a question, never a real person) and what each is expected to do in `journeys.json`.
2. **Freeze the site:** a local copy of the version under study, checked against the live site.
3. **Run:** one agent per invented user, each driving the browser only through `feedback/synthetic/tools/step.mjs`, which keeps one browser open for the run, reaches only the local copy and the two pinned APIs, and writes `_capture.json`. At most 14 actions, then the ten interview questions, a rating and three to six findings, in `run.json`.
4. **Check every finding** in `checks.json` against the capture, the screenshots, the site's files and outside documentation: confirmed, partly, artefact, or not confirmed. Keep every finding whatever its verdict.
5. **Decide,** as for a review: each finding leads to proposals in the register.
6. **Run the same users again** after the changes they led to, and compare.

The study pages say on every page that the users are invented and that this is not user research.

## Encrypt and send: the feedback lane

From v0.2.4 a reader's answers, and anything written on `/feedback/`, are encrypted in their browser and appended to the `feedback` lane of a private vault, `zs81fic5` on dev.send.sgraph.ai (R003). The pieces:

| Piece | Where | Secret? |
|---|---|---|
| The lane's address, token and public key | `feedback/lane.json` | no: the token can only append, the key can only encrypt |
| The envelope and the send | `assets/envelope.js` (sgit's hybrid envelope v2) | no |
| The private key | the vault, `feedback-lane/keys/feedback.encrypt.pem`, encrypted with a passphrase derived from the vault's write key | it is in the vault, which needs the vault key |
| The vault key | with the lead | yes; never in a file in this repository |

```bash
sgit clone "$FEEDBACK_KEY" customers-feedback                                   # or sgit pull in an existing clone
FEEDBACK_KEY="$FEEDBACK_KEY" node admin/feedback/lane.mjs drain --vault customers-feedback --dry-run   # look first
FEEDBACK_KEY="$FEEDBACK_KEY" node admin/feedback/lane.mjs drain --vault customers-feedback             # then file
cd customers-feedback && sgit commit "drain: <n>" && sgit push --token "$SG_SEND_ACCESS_TOKEN"
node admin/feedback/lane.mjs send "a test"                                       # a test send, as a browser makes it
```

Each message is filed as `feedback-lane/inbox/<file>.eml` beside its `.enc`, with a line in `feedback-lane/log.jsonl`. A message becomes a review on this site only with the sender's yes, as the feedback page promises.
