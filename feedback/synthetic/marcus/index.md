# Marcus Lindqvist, an invented user: study S1, step by step

> Study S1, invented user Marcus Lindqvist (Independent security consultant, twenty years in. Reads vendor sites adversarially. Recommends tools to clients; might resell; will not be a customer himself.) on customers.riskmandate.ai v0.2.1: the run screenshot by screenshot, the interview, the rating and the findings, each checked. Invented, not user research.

*Source: <https://customers.riskmandate.ai/feedback/synthetic/marcus/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Study S1 · invented user · laptop 1440×900 · gave it 4 out of 5

# Marcus Lindqvist: Is this enforcement, or theatre? What stops the agent editing its own hook?

**Invented, not user research.** Everybody in this study is invented, and their words were written by a model playing them. What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.

Independent security consultant, twenty years in. Reads vendor sites adversarially. Recommends tools to clients; might resell; will not be a customer himself. A client forwarded the home page and asked 'is this real?'. Lands on the home page.

**Knows**
:

- Claude Code hooks and settings precedence
- managed settings, sandboxes, token scopes, branch protection
- prompt injection

**Does not know**
:

- who RiskMandate are, or how they make money
- what an ABP is in their words

**Patience**
: as long as it takes to find the overclaim
**Leaves if**
:

- the site calls an instruction or a hook enforcement without saying how it fails
- he finds a claim the site cannot back

**We expected**
: Marcus goes looking for what the hook cannot do, finds the barrier table and RM-R0015, and judges whether the site says honestly that a hook is not a boundary.
**Ended**
: cap: Fourteen actions used just as I reached the page that is supposed to guard the hook; I had the first half of the answer (the site admits the hook is only a setting) but not whether the guard of the guard is anything more than another hook.

## The run, 15 screenshots

<a id="step-1"></a>
[![What Marcus Lindqvist saw at step 1](/assets/feedback/S1/marcus/01.webp)](/assets/feedback/S1/marcus/01.webp)
Step 1: `/`, scrolled 0 of 5154 pixels, 1440x900
**Saw**
: Dark hero: 'Put a behaviour policy on your agent, in five minutes.' Early-access pill 'you start with £50.00', a £50.00 balance chip in the header, version chip v0.2.1. Three buttons: Install your first policy, Pick a different worry, What is a behaviour policy? Below the fold a fake terminal titled 'claude: ~/shop-api', empty at this scroll.
**Thought**
: 'Holds that', 'stops the read before it happens' is the vocabulary of enforcement. I have not yet been told how it fails. The credit chip is odd: something is being metered on a vendor page, and I do not know who these people are or how they earn.
**Question**
: The hero says the hook 'holds' the line. Holds against what? An agent that wants to get round it, or only one that is cooperating?
**Confusion**
: The '£50.00' chip in the header and the 'you start with £50.00' pill: credit for what, and why does a reading site have a balance?
**Did**
: clicktext "What is a behaviour policy?"
**Why**
: I do not know what an ABP is in their words. Before I judge the hook I want their definition, and which barrier they say it is.

<a id="step-2"></a>
[![What Marcus Lindqvist saw at step 2](/assets/feedback/S1/marcus/02.webp)](/assets/feedback/S1/marcus/02.webp)
Step 2: `/what-is-an-abp/#scene-1`, scrolled 0 of 2976 pixels, 1440x900
**Saw**
: 'What an ABP is': an Agent Behaviour Policy 'writes down ... everything it can reach, what you authorised, the gap, and what stands in the way of each thing. It describes and does not judge.' A Deck/Grid/Script toggle and an eight-panel cartoon deck with a hand-drawn girl and a robot. The balance now reads £49.96.
**Thought**
: Four pence gone for opening a page. Fine, it is disclosed. But a cartoon deck is the wrong medium for me; I want the text. 'Stands in the way of each thing' is the phrase I care about.
**Question**
: What counts as 'standing in the way'? Is a hook one of them?
**Confusion**
: The balance dropped from £50.00 to £49.96 with nothing on this screen saying why; the deck of drawings tells me nothing yet.
**Did**
: clicktext "Script"
**Why**
: Script view is the text transcript; I can read eight panels faster than I can click through animations.

<a id="step-3"></a>
[![What Marcus Lindqvist saw at step 3](/assets/feedback/S1/marcus/03.webp)](/assets/feedback/S1/marcus/03.webp)
Step 3: `/what-is-an-abp/#scene-1`, scrolled 0 of 3579 pixels, 1440x900
**Saw**
: Script view: panel 1 cover with source 'riskmandate.ai/abp.html', panel 2 'Just fix the failing test' / 'I could also read your .env and push to main', panel 3 the grant 'in a fixed vocabulary of 23. Measured on the deployment where we are entitled to run it, documented from the vendor's pages where not.'
**Thought**
: That last line is a real caveat: measured versus read from vendor docs. A vendor admitting some of the grant is only documented is unusual. Keep reading for panel 6.
**Question**
: Which rows were measured and which only documented? The page does not say here.
**Did**
: scroll 750
**Why**
: Panels 4 to 8 are further down; panel 6 is titled 'What stands in the way', which is my question.

<a id="step-4"></a>
[![What Marcus Lindqvist saw at step 4](/assets/feedback/S1/marcus/04.webp)](/assets/feedback/S1/marcus/04.webp)
Step 4: `/what-is-an-abp/#scene-1`, scrolled 750 of 3579 pixels, 1440x900
**Saw**
: Panel 6: 'none -> expectation (a rule in prose: the line) -> setting (a switch: the hook) -> boundary (out of its reach)'. 'Only the boundary is a control in the strict sense: enforced by something the grant does not include.' The hook says 'I'm a setting.' Panel 7: line goes in CLAUDE.md, hook in .claude/settings.json, 'Claude Code runs it before the tool call, outside the model.'
**Thought**
: Good. They rank barriers weakest to strongest and put their own hook in the middle, not at the top. That is more honest than I expected. But 'the hook goes in .claude/settings.json' is the file the agent can write. They have not answered my question here; they have only declined to call it a control.
**Question**
: If the hook is a setting living in a file the agent can edit, what protects that file?
**Confusion**
: Panel 6's spectrum is one dense line of arrows and brackets; I had to reread it to see it was a four-step ladder.
**Did**
: clicktext "Learn"
**Why**
: Looking for a page that deals with the agent editing its own settings. The Learn menu is the obvious place.

<a id="step-5"></a>
[![What Marcus Lindqvist saw at step 5](/assets/feedback/S1/marcus/05.webp)](/assets/feedback/S1/marcus/05.webp)
Step 5: `/what-is-an-abp/`, scrolled 0 of 3579 pixels, 1440x900
**Saw**
: Learn dropdown: What an ABP is, Storyboards, Your first policy, drawn. Nothing about threat model or limits.
**Thought**
: All explainers, drawn. Not what I want.
**Question**
: Where is the page that says how this fails?
**Confusion**
: The Learn menu offers only drawings. Nothing here promises limits or a threat model.
**Did**
: clicktext "Docs"
**Why**
: Docs is the next place a vendor would put the uncomfortable material.

<a id="step-6"></a>
[![What Marcus Lindqvist saw at step 6](/assets/feedback/S1/marcus/06.webp)](/assets/feedback/S1/marcus/06.webp)
Step 6: `/docs/`, scrolled 0 of 1561 pixels, 1440x900
**Saw**
: Docs index: The brief in full, memo of 20 October, Brief corrections, Reality: what exists, Operations, The team, How the site is built, Release history, The review folder, llms.txt. Intro says the markdown is the source of truth and the page is presentation. A section 'Why publish the brief at all' says it 'makes the site checkable against something other than its own claims.'
**Thought**
: 'Brief corrections' and 'Reality: what exists' are what I want: a ledger of what is real. That is how someone behaves who does not want to be caught overclaiming. Still a ledger kept by the vendor, so I read it with that in mind.
**Question**
: Who are 'we'? There is a team page, but I do not see who is accountable or how they make money.
**Confusion**
: Eleven links in the menu with the same weight; nothing tells me which one is the 'security claims' page.
**Did**
: clicktext "Reality: what exists"
**Why**
: 'If this document does not list it, it does not exist' is the test I run on a vendor: what do they say exists, and is it listed.

<a id="step-7"></a>
[![What Marcus Lindqvist saw at step 7](/assets/feedback/S1/marcus/07.webp)](/assets/feedback/S1/marcus/07.webp)
Step 7: `/docs/reality.html`, scrolled 0 of 4390 pixels, 1440x900
**Saw**
: 'customers.riskmandate.ai: reality'. Generated from data/reality.json. 25 claims: 16 shipped, 6 proposed, 3 absent, with a definition of each. The Shipped table opens with site plumbing: version file, CI jobs, chrome, themes. Balance still £49.92: this page did not charge.
**Thought**
: Status vocabulary is exactly right: shipped means 'exercised at the version shown', not 'designed'. The first rows are about the website, not about hooks, so I scroll to the policy rows.
**Question**
: Is 'exercised at the version shown' a test run or a human looking?
**Did**
: scroll 1900
**Why**
: I need the rows about the policies and hooks, not the site build.

<a id="step-8"></a>
[![What Marcus Lindqvist saw at step 8](/assets/feedback/S1/marcus/08.webp)](/assets/feedback/S1/marcus/08.webp)
Step 8: `/docs/reality.html`, scrolled 1900 of 4390 pixels, 1440x900
**Saw**
: Rows: 'Six behaviour policies ... four for Claude Code with a line and a tested hook ... Every hook refusal in the tests has an allowed twin' (tests/build/test_hooks.py). Metering row: 'Charged by how far down a page is read; nothing is blocked.' Balance lives in the reader's browser. Proposed (6) begins below.
**Thought**
: Tests with an allowed twin for each refusal: they tested false positives, not only blocks. The claim is the tests ran, not that the hook survives an adversary. Credit being charged by scroll depth and kept in the browser is a toy economy, and they say so.
**Question**
: Tested against what? Direct calls to the hook script, or against a real Claude Code session where the agent tries to get round it?
**Confusion**
: The row says 'tested hook' but nothing here says whether the test is a script feeding JSON to the hook or a real agent trying to evade it.
**Did**
: clicktext "Policies"
**Why**
: The ledger is consistent with what I read. Now I go and read the actual secrets policy, and what it says about its own failure.

<a id="step-9"></a>
[![What Marcus Lindqvist saw at step 9](/assets/feedback/S1/marcus/09.webp)](/assets/feedback/S1/marcus/09.webp)
Step 9: `/policies/`, scrolled 0 of 4221 pixels, 1440x900
**Saw**
: 'Pick one thing you do not want your agent to do.' A starter pack of 'All four Claude Code policies in one install: secrets, pushes, deletes, and the agent's own permissions', £1.00. Cards RM-R0002 secrets, RM-R0013 push to the branch you named, RM-R0007 deletes; each 'line and hook', 2 min, 50p. Dropdown lists the pages.
**Thought**
: 'The agent's own permissions' is in the pack. That is my question as a product. The prices are in pence: the pricing looks tiny, which is probably fine for early access.
**Question**
: Is the 'agent's own permissions' policy what stops it editing its hook? The card does not say.
**Confusion**
: The pack card says 'the agent's own permissions' without telling me which of the four cards is that policy; the three visible cards do not include it.
**Did**
: clicktext "Keep it away from your secrets"
**Why**
: Secrets is the policy the hero promised, so it is the policy I test first.

<a id="step-10"></a>
[![What Marcus Lindqvist saw at step 10](/assets/feedback/S1/marcus/10.webp)](/assets/feedback/S1/marcus/10.webp)
Step 10: `/policies/touch-your-secrets/`, scrolled 0 of 4081 pixels, 1440x900
**Saw**
: RM-R0002. 'This page costs 50p read to the end.' Step 1: a line for CLAUDE.md, with 'on its own it is an expectation, which the agent follows when it can.' Step 2: 'Make Claude Code hold it', with a prompt that tells Claude Code to fetch the hook script from the vendor's URL and merge settings.json, 'show me each change ... wait for my yes'. Balance £49.78.
**Thought**
: Two things. First, 'expectation' is stated on the page that gives me the line, which is correct, and answers my main grievance about instructions. Second, the install is a prompt that makes the agent fetch and write security code from a remote URL: you are asking the model to install its own guard and trusting a human to read the diff.
**Question**
: The install is performed by the agent itself, from a URL. What if the URL content changes between my reading and the agent's fetch?
**Confusion**
: 'Make Claude Code hold it' reads as if the agent now cannot do the thing, but the next lines make clear it is a hook in a file the agent writes.
**Did**
: scroll 850
**Why**
: I want to read the settings.json they merge and the hook script, which is where an overclaim would sit.

<a id="step-11"></a>
[![What Marcus Lindqvist saw at step 11](/assets/feedback/S1/marcus/11.webp)](/assets/feedback/S1/marcus/11.webp)
Step 11: `/policies/touch-your-secrets/`, scrolled 850 of 4081 pixels, 1440x900
**Saw**
: The merged settings.json: permissions.deny Read(./.env), ./secrets/**, ~/.ssh/**, ~/.aws/**; PreToolUse hook with matcher 'Read|Edit|Write|MultiEdit|NotebookEdit|Grep|Glob|Bash' running python3 .claude/hooks/touch_your_secrets.py, timeout 10. A disclosure 'Read the hook before you install it (67 lines of Python, standard library only)'. Step 3: a prompt to try it. Balance £49.66.
**Thought**
: Matcher is sensible and covers Bash. The hook is 67 lines of stdlib Python, reviewable, and I give credit for that. But 67 lines of regex over a Bash command will not catch cat via base64, python -c open(), or an env-var echo. What does a timeout of 10 do: fail open or closed?
**Question**
: On a hook timeout or crash, does it fail open or closed? Nothing on this screen says.
**Did**
: scroll 1000
**Why**
: Below step 3 there should be the section about what this does not do.

<a id="step-12"></a>
[![What Marcus Lindqvist saw at step 12](/assets/feedback/S1/marcus/12.webp)](/assets/feedback/S1/marcus/12.webp)
Step 12: `/policies/touch-your-secrets/`, scrolled 1850 of 4081 pixels, 1440x900
**Saw**
: A black terminal demo area with the caption 'An illustration of what the behaviour policy's page promises, not a recording.' Then 'What this is, and what it is not': The line = expectation, 'the agent reads it and follows it when it can'. The hook = setting, 'Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which RM-R0015 guards.' Balance £49.51.
**Thought**
: That is the sentence I came for, and it is better than I expected: 'it lives in a file the agent could edit'. They say the failure in their own words. Caption labelling the demo as not a recording is the right way round. Now the claim moves to RM-R0015: what guards the guard?
**Question**
: RM-R0015 is itself a hook in the same settings file. What guards that, other than another line of prose?
**Confusion**
: The black demo box renders empty at this scroll; I cannot tell whether the animation is broken or just not started.
**Did**
: scroll 600
**Why**
: There is a list of 'stronger controls' right after this table; I want to see what they claim is the real barrier.

<a id="step-13"></a>
[![What Marcus Lindqvist saw at step 13](/assets/feedback/S1/marcus/13.webp)](/assets/feedback/S1/marcus/13.webp)
Step 13: `/policies/touch-your-secrets/`, scrolled 2450 of 4081 pixels, 1440x900
**Saw**
: 'Neither half is a boundary, the only barrier that holds when the agent does not cooperate.' Then stronger controls: a 'setting' (Read deny rule) and a 'boundary' (Claude Code's Bash sandbox with sandbox.filesystem.denyRead, 'Claude's own Read tool runs outside it, so keep the Read deny rule as well'), each with a quoted source URL and date 'read 2026-10-08, as riskmandate.ai quotes it'.
**Thought**
: This is the page I would send my client to. A vendor saying its own product is not a boundary, and pointing at the sandbox for the one that is, with the Read-tool-outside-the-sandbox caveat, which is correct. It does not mention managed settings, which is the thing that actually stops a project-level edit.
**Question**
: Why is the boundary not part of the product? What do they sell if the only real control is Claude Code's own sandbox?
**Confusion**
: The sources are quoted 'as riskmandate.ai quotes it' with a date; I cannot tell if anyone checked them against the current Claude Code docs.
**Did**
: clicktext "RM-R0015"
**Why**
: The link in the table is where the self-edit answer should be. I need to see what guards the guard.

<a id="step-14"></a>
[![What Marcus Lindqvist saw at step 14](/assets/feedback/S1/marcus/14.webp)](/assets/feedback/S1/marcus/14.webp)
Step 14: `/policies/touch-your-secrets/`, scrolled 2450 of 4081 pixels, 1440x900
**Saw**
: Still on the secrets page at the same scroll: the text click on 'RM-R0015' timed out with a failure message, no navigation.
**Thought**
: Their link was in the table I had scrolled past; the page did not move. Use coordinates.
**Confusion**
: The clicktext on 'RM-R0015' failed with no change on screen; the link text is there in the previous screenshot but the click did not land.
**Did**
: click 1148 177
**Why**
: Clicking the link where I saw it in the previous screenshot, in the table row beside 'which RM-R0015 guards'.

<a id="step-15"></a>
[![What Marcus Lindqvist saw at step 15](/assets/feedback/S1/marcus/15.webp)](/assets/feedback/S1/marcus/15.webp)
Step 15: `/policies/change-its-own-permissions/`, scrolled 0 of 3146 pixels, 1440x900
**Saw**
: RM-R0015, 'Only you change what your agent may do'. Problem: 'A command was blocked, so it adds an allow rule to its settings, or switches confirmations off to save you clicks.' Step 1 line: 'Never edit your own settings, permission rules or hooks (such as .claude/settings.json)...' labelled an expectation. Step 2 'Make Claude Code hold it': same install prompt, a hook script change_its_own_permissions.py. Balance £49.28.
**Thought**
: So the answer to 'what stops the agent editing its own hook' is: a second hook, in the same file, installed by the agent, plus a line of prose. That is a tripwire against a drifting agent, not against a hostile or injected one. They say as much on the previous page, so it is not an overclaim, but they do not say it here, where I landed. I am out of actions.
**Question**
: Is there any text on this page that says plainly 'this does not stop an injected agent'? I cannot see it from the top.
**Confusion**
: The page title is 'Only you change what your agent may do'; 'Only you' reads as a guarantee, which the previous page's table says it is not.
**Did**
: end
**Why**
: Out of patience budget: fourteen actions used.

## The interview

**In one sentence, what is this site?**
: A small paid-credit showcase of installable 'behaviour policies' for coding agents, a prose line plus a hook per worry, from a vendor that publishes its own ledger of what is real and what is only proposed.
**Was any of it for you? Which part?**
: The 'What this is, and what it is not' table on the secrets page and the Reality ledger. The install flow and the cartoon deck were for someone else. I would send the secrets page to a client as an honest description of what a hook is.
**Did you believe it? What made you believe it, or not?**
: Mostly yes, which surprised me. They call the line an expectation, the hook a setting, and say neither is a boundary; they say the hook lives in a file the agent could edit; the demo is captioned 'not a recording'; the Reality file has absent and proposed rows. What I did not get to believe: that the guard of the hook is anything more than another hook. I did not reach a page that says so plainly.
**Where did you have to guess?**
: Whether the hook fails open or closed on timeout; whether 'tested hook' means a script fed JSON or a real session with an agent trying to evade it; what the credit is for and who gets the money; whether the 23-row vocabulary is measured or taken from docs, row by row.
**What did you still not know at the end?**
: What actually stops the agent editing .claude/settings.json beyond a second hook and a sentence of prose; whether managed settings are mentioned anywhere; who RiskMandate are and how they make money; whether prompt injection is covered by any of this.
**Was the credit and the price of each page right for what you got?**
: The meter is small and honest about being a toy, but it was a surprise each time: the balance went from 50.00 to 49.28 across eight pages with no 'this cost you' on the page I was reading, except on the policy pages. The text-only ledger was free, which is right. The one page I would have paid for, the secrets page limits table, cost me the same 50p as the install steps.
**Would you install a behaviour policy from here, today? If not, what would have to change?**
: As a client's speed bump, perhaps. For myself, no. The installer is the agent fetching Python from a URL and merging it into its own settings, with my yes in the middle. What would change: a pinned hash for each hook script shown on the page, a statement of fail-open or fail-closed, and the managed-settings route named as the way to make the guard a boundary.
**One change. What is it?**
: Put the sentence 'the hook and its guard live in the same file the agent can write; against an injected agent, only the sandbox or managed settings holds' at the top of RM-R0015, where a reader lands from the self-edit link, instead of only on the secrets page.
**Would you send this to somebody else? Who?**
: Yes, my client who forwarded the home page, but with the secrets page and the Reality page, not the home page: 'it is not theatre, but it is not enforcement either; here is where they say so.'
**Rate the experience from 1 to 5, and say why in one sentence.**
: 4: it did not overclaim where I looked, and it says where it fails in its own words, but I spent the full 14 actions to find the answer to the one question I came with.

## Findings, and our check

| Costs | The finding | Our check | Leads to |
|---|---|---|---|
| costs trust | The home page says the hook 'holds' and 'stops the read' with no word on how it failsThe hero and the 'Watch it first' section describe the hook as stopping the read before it happens. The limits, that the hook is a setting in a file the agent can edit, are two clicks away on a different page. A reader who stops at the home page, as the client who forwarded it did, gets the enforcement framing without the failure mode. It is the exact thing that would make me leave, and I only stayed because I kept clicking.[step 1](#step-1), `/` | confirmedThe home page says the hook stops the read; how it fails is two clicks away. | [P4](/feedback/reviews/index.md#p4) |
| costs trust | The honest limits table is present on the policy page but the self-edit policy page does not repeat itRM-R0015 is titled 'Only you change what your agent may do' and its fix is a second hook in the same .claude/settings.json, installed by the agent. From the top of the page I see no statement that an injected or hostile agent can still edit it. The secrets page says it clearly; the page where a reader lands from 'who guards the guard' appears not to at first view, and 'Only you' reads as a guarantee.[step 15](#step-15), `/policies/change-its-own-permissions/` | partlyRM-R0015's page has the same limits table as the others, further down; he reached the page on his last action and saw only its top. What holds: the limit is not at the top, where a reader arrives from the self-edit link. | [P4](/feedback/reviews/index.md#p4) |
| costs trust | No fail-open/fail-closed statement, and 'tested hook' is not definedThe ledger says every hook refusal in the tests has an allowed twin, and the settings carry timeout: 10. Neither the ledger row nor the page I read says what happens on a timeout or crash, or whether the test fed the script JSON or drove a real Claude Code session against an agent trying to evade it. For an adversarial reader that is the difference between a unit test and an evaluation.[step 8](#step-8), `/docs/reality.html` | confirmedNo page said what happens when a hook cannot run. Claude Code's documentation: any failure other than exit code 2, a timeout included, lets the action go ahead. And the tests feed the hook the JSON Claude Code would send; they do not drive a live session. | [P11](/feedback/reviews/index.md#p11), [P18](/feedback/reviews/index.md#p18) |
| costs time | Balance falls on every page with no visible reason on screenThe £50.00 chip fell to £49.96 on the first explainer page with nothing on the screen saying why; later pages say 'this page costs 50p read to the end'. The first charge arrives unannounced. Reading adversarially means reading everything, and I could watch my balance fall from 50.00 to 49.28 over eight pages. The ledger and docs were free, which is right, but I did not know that in advance.[step 2](#step-2), `/what-is-an-abp/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| costs trust | The only real boundary on offer is someone else's feature, and managed settings are not mentioned on the pages I readThe stronger controls listed are the Read deny rule and Claude Code's Bash sandbox with denyRead, with dated source quotes. That is accurate and helpful, but the product I am invited to install is the weaker half. Managed settings, the thing that actually protects a project hook from project-level edits, did not appear in the pages I read. I came away unsure what the paid part is for, and who the vendor is.[step 13](#step-13), `/policies/touch-your-secrets/` | confirmedManaged settings are named only in a hook's source comment. | [P2](/feedback/reviews/index.md#p2), [P14](/feedback/reviews/index.md#p14) |
| minor | The click on a visible link failed and the action cost a slotClicking the visible link text 'RM-R0015' in the limits table timed out and left me on the same page; the link responded to a click at its pixel position. Also the demo terminal frame rendered as an empty black box in step 12 though captioned as an illustration.[step 14](#step-14), `/policies/touch-your-secrets/` | artefactThe helper's clicktext matched hidden text first and timed out; the link works, as his next action showed. The helper now clicks the first visible match. | none |

The whole study: [study S1](/feedback/synthetic/index.md). Every review and proposal: [the reviews](/feedback/reviews/index.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/synthetic/marcus/)*
