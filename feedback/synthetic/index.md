# Synthetic users, study S1: five invented people on customers.riskmandate.ai

> Study S1: five invented users, with profiles and expected journeys written first, drove a browser through customers.riskmandate.ai v0.2.1 one screenshot at a time. Their runs, interviews, ratings and findings, each checked. Invented, not user research.

*Source: <https://customers.riskmandate.ai/feedback/synthetic/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Feedback · synthetic users · study S1 · site v0.2.1

# Five people who do not exist, on the site as it was.

**Invented, not user research.** Everybody in this study is invented, and their words were written by a model playing them. What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.

5 invented users took 60 screenshots on site v0.2.1, gave it 3, 3, 4, 2 and 3 out of 5, and reported 29 findings. We checked each one: 24 confirmed, 4 partly, 1 artefact.

Why these five: The first batch is people the lead knows who run Claude Code or ChatGPT, and the site has to win three kinds of them: the developer who installs a behaviour policy in five minutes, the non-developer whose agent sends mail as them, and the person who decides for a team. Two more are there to break it: a security consultant who reads the claims adversarially and will never be a customer, and a junior developer on Windows who follows instructions literally. Two are on something other than a laptop: one on a phone, one on an iPad.

## Who, what we expected, and what happened

Each expected journey was written before the run, so a run is compared with a hypothesis instead of being explained afterwards.

| Invented user | Arrived asking | We expected | What happened, in their words |
|---|---|---|---|
| [Sam Okoye](/feedback/synthetic/sam/index.md)Backend developer at a 12-person payments start-up. Uses Claude Code every day in a monorepo with .env files for four services. | Can I stop Claude Code reading my .env without breaking my workflow? | Sam reaches the secrets policy in one click and has the install prompt within two minutes. | I could see the hook only partly (the pasted source was cut off before the part that says which files it refuses), it watches Bash, Grep and Glob, and the deny list names only ./.env at the root; the Docs menu led to the site's own internal papers, so I went back to work rather than install something I could not predict in a four-service monorepo. |
| [Nadia Farouk](/feedback/synthetic/nadia/index.md)Product manager at a 200-person retailer. Uses ChatGPT with the Gmail connector, and Claude in the browser. Not a developer. | Can I stop ChatGPT sending an email in my name before I have seen it? | Nadia is put off by 'hook' and 'Claude Code' in the hero, scrolls, and may find the ChatGPT section or the send-as-you policy. | She found the page that gives her a line to paste into ChatGPT's custom instructions so nothing is sent in her name without a yes, though the page itself says the line is only an expectation, not a guarantee. |
| [Marcus Lindqvist](/feedback/synthetic/marcus/index.md)Independent security consultant, twenty years in. Reads vendor sites adversarially. Recommends tools to clients; might resell; will not be a customer himself. | Is this enforcement, or theatre? What stops the agent editing its own hook? | Marcus goes looking for what the hook cannot do, finds the barrier table and RM-R0015, and judges whether the site says honestly that a hook is not a boundary. | Fourteen actions used just as I reached the page that is supposed to guard the hook; I had the first half of the answer (the site admits the hook is only a setting) but not whether the guard of the guard is anything more than another hook. |
| [Joan Mbeki](/feedback/synthetic/joan/index.md)CTO of a 30-person software company. Fifteen engineers use Claude Code. Holds the budget. | Can I give my whole team a baseline in one go, and does it hold if one of them turns it off? | Joan looks for a team rollout and the commitment of joining, finds the starter pack and the programme pages, and does not find a team-wide or managed install. | After thirteen actions every page was per person or per project, and I found nothing on what joining commits my company to or what it costs. |
| [Tomás Reyes](/feedback/synthetic/tomas/index.md)Junior developer, a year into his first job. Uses Claude Code through the VS Code extension on a Windows laptop. Follows instructions literally. | How do I install the secrets one, and how do I know it worked? | Tomás follows 'Install your first policy', copies the install prompt, and is unsure about python3 on Windows and what a new session is in VS Code. | He found a paste-into-Claude-Code route but hit two gaps the page never answered (what a 'new session' means in the extension, and what happens if python3 is not on his Windows laptop), so he stopped to ask his team lead rather than guess. |

## Ratings, and the one change each asked for

| Invented user | On | Ended | Rating | Their one change |
|---|---|---|---|---|
| [Sam Okoye](/feedback/synthetic/sam/index.md)Backend developer at a 12-person payments start-up. Uses Claude Code every day in a monorepo with .env files for four services. | laptop, 1440×900 | left, after 12 screenshots | **3** of 5 | Show the whole hook, uncut, with a short plain-words list: 'blocks these filenames, leaves these alone, to turn it off delete this block'. |
| [Nadia Farouk](/feedback/synthetic/nadia/index.md)Product manager at a 200-person retailer. Uses ChatGPT with the Gmail connector, and Claude in the browser. Not a developer. | phone, 390×844 | got-it, after 8 screenshots | **3** of 5 | Put my question first on the home page: 'Stop ChatGPT sending email as you', in plain words, instead of a headline about hooks and Claude Code. |
| [Marcus Lindqvist](/feedback/synthetic/marcus/index.md)Independent security consultant, twenty years in. Reads vendor sites adversarially. Recommends tools to clients; might resell; will not be a customer himself. | laptop, 1440×900 | cap, after 15 screenshots | **4** of 5 | Put the sentence 'the hook and its guard live in the same file the agent can write; against an injected agent, only the sandbox or managed settings holds' at the top of RM-R0015, where a reader lands from the self-edit link, instead of only on the secrets page. |
| [Joan Mbeki](/feedback/synthetic/joan/index.md)CTO of a 30-person software company. Fifteen engineers use Claude Code. Holds the budget. | tablet, 1180×820 | left, after 14 screenshots | **2** of 5 | A page for a team lead: how fifteen engineers get the same baseline from one place, who can change it, what stops one person turning it off, and what joining commits us to. |
| [Tomás Reyes](/feedback/synthetic/tomas/index.md)Junior developer, a year into his first job. Uses Claude Code through the VS Code extension on a Windows laptop. Follows instructions literally. | laptop, 1366×768 | patience, after 11 screenshots | **3** of 5 | Add one short 'did it work?' box under Try it: what you see if it worked, and what to do if python3 is missing or nothing happens. |

## Every finding, by what it costs

Checked against the browser's own record, the screenshots, the site's files and, where a finding is about Claude Code, its documentation. Each finding is kept whatever the verdict, so the next study can be compared with this one.

| Costs | The finding, in their words | Our check | Leads to |
|---|---|---|---|
| blocks the first install | No fallback when python3 is missing or the hook does not runTomás Reyes, [step 3](/feedback/synthetic/tomas/index.md#step-3), `/policies/touch-your-secrets/` | confirmedThe settings run python3 and no page says so. On Windows, Claude Code runs hooks in Git Bash, or PowerShell if Git Bash is not installed; a hook that cannot start lets the action through. | [P11](/feedback/reviews/index.md#p11) |
| blocks the first install | The hook source is cut off before the rules that say which files it blocksSam Okoye, [step 7](/feedback/synthetic/sam/index.md#step-7), `/policies/touch-your-secrets/` | partlyThe source is all there, in a box that scrolls: 418 of its 1,246 pixels show, and nothing says it scrolls. What he needed, which files it stops, is not in plain words anywhere on the page. | [P12](/feedback/reviews/index.md#p12), [D3](/feedback/reviews/index.md#d3) |
| costs trust | Policy 4 hands the decision to the individual, not the companyJoan Mbeki, [step 9](/feedback/synthetic/joan/index.md#step-9), `/policies/starter/` | confirmedRM-R0015 asks the person at the keyboard. For a company, the answer is managed settings, which no page names. | [P14](/feedback/reviews/index.md#p14) |
| costs trust | Pages cost real-looking money and the price rule is unexplainedJoan Mbeki, [step 7](/feedback/synthetic/joan/index.md#step-7), `/policies/starter/` | confirmedConfirmed that nothing explains it; we are keeping the prices. | [P9](/feedback/reviews/index.md#p9), [D5](/feedback/reviews/index.md#d5) |
| costs trust | The home page says the hook 'holds' and 'stops the read' with no word on how it failsMarcus Lindqvist, [step 1](/feedback/synthetic/marcus/index.md#step-1), `/` | confirmedThe home page says the hook stops the read; how it fails is two clicks away. | [P4](/feedback/reviews/index.md#p4) |
| costs trust | No fail-open/fail-closed statement, and 'tested hook' is not definedMarcus Lindqvist, [step 8](/feedback/synthetic/marcus/index.md#step-8), `/docs/reality.html` | confirmedNo page said what happens when a hook cannot run. Claude Code's documentation: any failure other than exit code 2, a timeout included, lets the action go ahead. And the tests feed the hook the JSON Claude Code would send; they do not drive a live session. | [P11](/feedback/reviews/index.md#p11), [P18](/feedback/reviews/index.md#p18) |
| costs trust | The only real boundary on offer is someone else's feature, and managed settings are not mentioned on the pages I readMarcus Lindqvist, [step 13](/feedback/synthetic/marcus/index.md#step-13), `/policies/touch-your-secrets/` | confirmedManaged settings are named only in a hook's source comment. | [P2](/feedback/reviews/index.md#p2), [P14](/feedback/reviews/index.md#p14) |
| costs trust | The balance drops while scrolling and the home page does not explain whyNadia Farouk, [step 3](/feedback/synthetic/nadia/index.md#step-3), `/policies/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| costs trust | The key limit of the line is stated, but the stronger lock is for claude.ai admins onlyNadia Farouk, [step 7](/feedback/synthetic/nadia/index.md#step-7), `/policies/send-as-you/` | confirmedThe only stronger control listed for send-as-you is an organisation administrator's setting in Claude, from riskmandate.ai's rule. We do not yet know what a ChatGPT user can set for themselves. | [P7](/feedback/reviews/index.md#p7) |
| costs trust | No word on how to turn the hook off or undo the installSam Okoye, [step 9](/feedback/synthetic/sam/index.md#step-9), `/policies/touch-your-secrets/` | confirmedNo page says how to remove a hook. | [P12](/feedback/reviews/index.md#p12) |
| costs trust | The £50 and the falling balance are unexplained until the third page I openSam Okoye, [step 1](/feedback/synthetic/sam/index.md#step-1), `/` | confirmedFive of five asked what the £50 was. | [P9](/feedback/reviews/index.md#p9) |
| costs trust | Try it lists two outcomes only; there is no 'it did not work' branchTomás Reyes, [step 4](/feedback/synthetic/tomas/index.md#step-4), `/policies/touch-your-secrets/` | confirmedTry it gave only the two outcomes. | [P11](/feedback/reviews/index.md#p11), [D4](/feedback/reviews/index.md#d4) |
| costs trust | Balance falls as you scroll, with the price disclosed only in small printTomás Reyes, [step 2](/feedback/synthetic/tomas/index.md#step-2), `/policies/touch-your-secrets/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| costs trust | The honest limits table is present on the policy page but the self-edit policy page does not repeat itMarcus Lindqvist, [step 15](/feedback/synthetic/marcus/index.md#step-15), `/policies/change-its-own-permissions/` | partlyRM-R0015's page has the same limits table as the others, further down; he reached the page on his last action and saw only its top. What holds: the limit is not at the top, where a reader arrives from the self-edit link. | [P4](/feedback/reviews/index.md#p4) |
| loses a customer | Nothing for a team: every page is one person, one projectJoan Mbeki, [step 7](/feedback/synthetic/joan/index.md#step-7), `/policies/starter/` | confirmedNothing says that committing .claude/settings.json gives everybody who pulls the same hooks, which Claude Code's documentation says it does. | [P14](/feedback/reviews/index.md#p14) |
| loses a customer | No page says what joining the first batch commits a company toJoan Mbeki, [step 14](/feedback/synthetic/joan/index.md#step-14), `/programme/` | confirmedNo page says what joining commits a company to. | [P15](/feedback/reviews/index.md#p15) |
| loses a customer | The first screen speaks to developers, not to a ChatGPT userNadia Farouk, [step 1](/feedback/synthetic/nadia/index.md#step-1), `/` | confirmedThe first paragraph names a hook and Claude Code; ChatGPT first appears half a page down. | [P1](/feedback/reviews/index.md#p1), [P7](/feedback/reviews/index.md#p7) |
| loses a customer | The matcher includes Bash, Edit and Write with no plain-words reasonSam Okoye, [step 5](/feedback/synthetic/sam/index.md#step-5), `/policies/touch-your-secrets/` | confirmedThe matcher names every file tool and Bash, and nothing beside it says the hook answers only when a credential file is named. | [P12](/feedback/reviews/index.md#p12) |
| costs time | Page is the lead's own tracking, not a customer-facing explanationJoan Mbeki, [step 3](/feedback/synthetic/joan/index.md#step-3), `/customers/` | confirmedThe first batch page is the lead's tracking. She went there looking for terms, which are nowhere. | [P15](/feedback/reviews/index.md#p15) |
| costs time | Balance falls on every page with no visible reason on screenMarcus Lindqvist, [step 2](/feedback/synthetic/marcus/index.md#step-2), `/what-is-an-abp/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| costs time | The policy list leads with a Claude Code pack and a hook section before the ChatGPT onesNadia Farouk, [step 2](/feedback/synthetic/nadia/index.md#step-2), `/policies/` | confirmedOn /policies/ the Claude Code pack and section come first; the ChatGPT section is about 1,500 pixels down on a phone. | [P7](/feedback/reviews/index.md#p7) |
| costs time | Unexplained terms and a one-row table on the key pageNadia Farouk, [step 7](/feedback/synthetic/nadia/index.md#step-7), `/policies/send-as-you/` | confirmedOur generator wrote 'Neither half is a boundary' on pages with only one half. | [P13](/feedback/reviews/index.md#p13) |
| costs time | 'Start a new session' is not explained for the VS Code extensionTomás Reyes, [step 3](/feedback/synthetic/tomas/index.md#step-3), `/policies/touch-your-secrets/` | confirmedWorse than the finding: the instruction is out of date. Claude Code applies changes to hooks in the running session. | [P10](/feedback/reviews/index.md#p10) |
| costs time | 'What this is, and what it is not' reads as a to-do and uses unexplained termsTomás Reyes, [step 6](/feedback/synthetic/tomas/index.md#step-6), `/policies/touch-your-secrets/` | confirmedThe stronger controls read as a second required step; nothing says they are optional. | [P4](/feedback/reviews/index.md#p4) |
| costs time | The typing terminal demo shows nothing useful and looks stuckSam Okoye, [step 2](/feedback/synthetic/sam/index.md#step-2), `/` | partlyA still screenshot cannot watch an animation: the demo is typing, not stuck. What holds: measured in the same browser, the refusal appears about eleven seconds after the demo comes into view. | [P17](/feedback/reviews/index.md#p17) |
| minor | Unexplained balance in the header and an unexplained 'reading account'Joan Mbeki, [step 1](/feedback/synthetic/joan/index.md#step-1), `/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| minor | Docs menu and status line are the company's internal papers, not user helpSam Okoye, [step 12](/feedback/synthetic/sam/index.md#step-12), `/docs/` | confirmedThe Docs menu is the brief, the memo and how the site is built. | [P16](/feedback/reviews/index.md#p16) |
| minor | Start-here page opens with internal status text and a dropdown that covers contentTomás Reyes, [step 11](/feedback/synthetic/tomas/index.md#step-11), `/start-here/` | partlyThe status line at the top of start here holds. The dropdown over step 4 was our helper: the mouse stayed where it clicked the menu, and the menu opens on hover. | [P16](/feedback/reviews/index.md#p16) |
| minor | The click on a visible link failed and the action cost a slotMarcus Lindqvist, [step 14](/feedback/synthetic/marcus/index.md#step-14), `/policies/touch-your-secrets/` | artefactThe helper's clicktext matched hidden text first and timed out; the link works, as his next action showed. The helper now clicks the first visible match. | none |

## How it was run

The method is newsroom.sgit.ai's, [How to run synthetic users](https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html), adapted for this site. Each user was played by Claude Sonnet, driving a real browser one screenshot at a time. feedback/synthetic/tools/step.mjs and driver.mjs: one browser per run that stays open, so the meter's session and the scroll position are those of a real tab. It reaches only a local copy of the site, by GET, and the two pinned APIs the site loads code from; every other request is refused and written in _capture.json.

### The loop

1. observe: a screenshot at the persona's own window size
2. say what you see, at the detail this persona takes in
3. think: what they weigh, what they suspect
4. question: one the page raised and did not answer
5. confusion: if any, pointing at something on the screenshot
6. act: one action, with the reason in the persona's terms
7. loop, until they get what they came for, leave, or run out of patience

### The rules

- stay in the persona; never claim to be a real person
- never use knowledge the persona would not have; a page not opened is a page not known
- leaving is a valid ending, and often the most useful one
- do not fix the site in the narration; that belongs in the interview
- every confusion points at something on the screenshot
- at most 14 actions
- decide each action from the screenshot alone: never the HTML, the DOM or the markdown twin

### The interview

1. In one sentence, what is this site?
2. Was any of it for you? Which part?
3. Did you believe it? What made you believe it, or not?
4. Where did you have to guess?
5. What did you still not know at the end?
6. Was the credit and the price of each page right for what you got?
7. Would you install a behaviour policy from here, today? If not, what would have to change?
8. One change. What is it?
9. Would you send this to somebody else? Who?
10. Rate the experience from 1 to 5, and say why in one sentence.

### What we changed from the newsroom's method

- question 6 asks about the credit and page prices, not a purchase
- question 7 asks about installing, the site's one action
- the costs name this site's outcomes: the first install, trust, a customer
- the browser stays open for the whole run, the first change the newsroom study asked for
- clicktext now clicks the first visible match; in S1 it could pick a hidden one (Marcus, step 14)

### The files

```
data/feedback/synthetic/personas.json     the users, and why these ones
data/feedback/synthetic/journeys.json     what each was expected to do, written before any run
data/feedback/synthetic/protocol.json     the loop, the rules, the interview, the record format
data/feedback/synthetic/checks.json       what we checked, finding by finding
data/feedback/synthetic/runs/<who>/run.json        the run as the invented user wrote it
data/feedback/synthetic/runs/<who>/_capture.json   the browser's own record of every step
assets/feedback/S1/<who>/NN.webp                    what they were looking at, step by step
feedback/synthetic/tools/step.mjs, driver.mjs      the browser helper
```

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/synthetic/)*
