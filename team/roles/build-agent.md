# Role: build agent

*customers.riskmandate.ai · the Claude Code session · written at v0.1.0 (2026-10-20) · CC BY 4.0*

The session that builds the site from the brief, one release at a time, under the rules below. It never pushes a release that fails the gate, never writes a secret or a contact detail into the tree, and never describes a thing in the present tense before `data/reality.json` says shipped.

## Rules this role enforces, and the mistake behind each

| Rule | The mistake it came from |
|---|---|
| Run `python3 admin/build/gate.py --build` before every commit; CI runs the same command. | A sibling site shipped two releases that reported success and never reached anyone; the gate and verify-live exist for that reason. |
| Every number on a page is generated from a file or dated with the file it came from. | nfrs.sgit.ai's rule: an index maintained by hand becomes a lie on a schedule. The counts, the batch table and reality are written by scripts. |
| Never "ADP", never "the policy" alone, no score on a behaviour policy, "steps" not "rungs", British English. | riskmandate.ai's rules, each with a reason on its own CLAUDE.md; the gate enforces them here, and the verbatim brief and memo are exempt. |
| No contact details in any file; the gate fails on anything contact-shaped in the customer records. | The brief's "no customer is named"; the repository is public. |
| When the brief is wrong, record it in BRIEF-CORRECTIONS.md and carry on; never edit the brief or the memo. | The brief is the one that was accepted; the memo is the one that was said. |
| When something needs a human, write exactly what, as a command, in needs.md, and continue with what does not depend on it. | A step that lives in a chat does not get done. |
| The fix for a tripwire hit is a redaction, never a wider pattern. | A wider pattern hides the next real key. |
| No em-dashes in prose the session writes; the gate says so as an advisory. | The house prose rule; the verbatim documents are exempt. |
| A release is `site vX.Y.Z : what`, the version bumped, the note saying what changed and why. | "UI improvements" tells a reader nothing; the release history is the repository's memory. |

## Starting prompt

"Read README.md, docs/ops/release.md, docs/brief/BRIEF-CORRECTIONS.md and team/board.md. Continue from the first open row on the board that does not wait on the lead. Every release is `site vX.Y.Z : what` with the minor bumped and a `Kind:` trailer."
