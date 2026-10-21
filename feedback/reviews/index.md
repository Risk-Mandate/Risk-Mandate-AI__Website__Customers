# Every review of customers.riskmandate.ai, what we read in it, and what we will do

> The consolidated reviews: each review verbatim, our reading point by point with screenshots, the synthetic study's findings with our checks, and one register of 23 proposals, each with a decision and a reason.

*Source: <https://customers.riskmandate.ai/feedback/reviews/> · site v0.2.2 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Feedback · every review · one document

# Every review, what we read in it, and what we will do.

Each review is kept in the reviewer's own words. Our reading follows point by point, with screenshots of what the reviewer was looking at. Every point leads to a proposal, and every proposal has a decision and a reason: we do not do everything a reviewer asks, but every no is explained here.

- **Reviews by people:** 1.
- **Synthetic users:** [study S1](#s1). 5 invented users took 60 screenshots on site v0.2.1, gave it 3, 3, 4, 2 and 3 out of 5, and reported 29 findings. We checked each one: 24 confirmed, 4 partly, 1 artefact.
- **Proposals:** 23: 8 done, 9 proposed, 1 question, 5 declined. [The register](#register).
- **Questions waiting for an answer:** 3. [The questions](#questions).

Give a review of your own: [tell us what you think](/feedback/index.md).

<a id="by-people"></a>

## Reviews by people

- [R001](#r001), Dinis Cruz, Wednesday 21 October 2026, 1:41, as given in the memo: A first impression: the hook answers a question nobody has asked yet (11 points)

<a id="r001"></a>

## R001: A first impression: the hook answers a question nobody has asked yet

**Reviewer**
: Dinis Cruz, the lead of the programme
**Given**
: Wednesday 21 October 2026, 1:41, as given in the memo
**Reviewing**
: site v0.2.1
**As**
: a voice memo, transcribed
**Status**
: first impression; the reviewer says more memos follow and this one is not complete

- The memo is kept as transcribed, with paragraph breaks added. The transcription spells the name Dennis; the reviewer is Dinis Cruz.
- The time is as given; the memo does not say morning or afternoon, or which time zone.
- The screenshots are of v0.2.1, the version reviewed, taken from a local copy checked byte for byte against the live site.

### The memo, verbatim

>

Very cool. Okay, so let me now do a review of the current website. And this, we need to now capture this as reviews. We also need to encourage the user to record these audio memos and give it to their Claude version, and even get Claude to interview them. And also, I would like us to run this to some synthetic users so that we can also capture them, right, this feedback. So I'm going to now provide, and you can name me, right? So I can say this is my review, you know, Dennis Cruz on Wednesday, 21st of October at 1:41, right? So I'm basically reviewing the website, right?

So first thing is, I like it. Put a behavior policy on your agent in 5 minutes. That is exactly the thing. Pick one thing you don't want your agent to do, paste one line, read, add a hook that holds it, and try with a prompt that should be refused. Great.

Though, a lot of users here won't know what a hook is, right? And I think that's a good example of a solution for a problem that they not have yet. So if you think about it, the hook is a solution for the question, hold on, but the is the agent that is enforcing its own checks, right? But the user will only provide that question once he understands what the policy is doing. But until they understand what the policy is doing, they're not going to ask that question. And it's the same thing, if they then go, but hold on, but the hook is still run by the agent. And then we go, yes, which is why it should be done outside. So I think, which then follows that conversation, right?

And this is where I think it's very important to have a flow where we guide the user through this workflow, and we guide the user through this sort of sequence of events, including the history. So this is not about providing the whole roadmap or a complete solution. This is about getting users to understand the principles of our agent behavior policies and use them straight away.

So actually, what I'm going to do is I'm going to write a whole bunch of these memos, but I'm going to submit it so you can start keeping track of it. But this is not complete. It's just my first impression. And then you can put them all in one document and put them all in one consolidated view. And then what you should do is you should have another part on that where you should comment on everything I said. Even put some screenshots on it, so we documented what I'm seeing, because my text doesn't have screenshots, and then maybe propose a set of changes to be done from it. Because remember that this is the beginning of us also creating a workflow to get feedback from users, right? And we don't have to do everything the user says, right? You know, but we should have a good reason why we don't do that.

### Our reading, point by point

<a id="r001-1"></a>

**R001.1** agreed

>

So first thing is, I like it. Put a behavior policy on your agent in 5 minutes. That is exactly the thing.

The promise stays. The headline, the five minutes and the one-worry framing are what everything else in this review is built on, and nothing proposed here changes them.

[![The home page's first screen at v0.2.1: pick one thing, paste one line, add one hook, try it.](/assets/feedback/R001/01-home-hero.webp)](/assets/feedback/R001/01-home-hero.webp)
The home page's first screen at v0.2.1: pick one thing, paste one line, add one hook, try it. / · 1280x900 · v0.2.1

Leads to: none.

<a id="r001-2"></a>

**R001.2** agreed

>

Pick one thing you don't want your agent to do, paste one line, read, add a hook that holds it, and try with a prompt that should be refused. Great.

These are the hero's four verbs as they stand at v0.2.1: pick, paste, add, try. The next points argue with the third one. What we propose keeps all four and changes their order, so that trying comes before the hook.

[![The home page's first screen at v0.2.1: pick one thing, paste one line, add one hook, try it.](/assets/feedback/R001/01-home-hero.webp)](/assets/feedback/R001/01-home-hero.webp)
The home page's first screen at v0.2.1: pick one thing, paste one line, add one hook, try it. / · 1280x900 · v0.2.1

Leads to: [P1](/feedback/reviews/index.md#p1).

<a id="r001-3"></a>

**R001.3** agreed

>

Though, a lot of users here won't know what a hook is, right?

Agreed, and the screenshots show it is worse than the memo says. On a phone, 'add one hook' is on the first screen, before anything says what a hook is. The first explanation is in the three-step strip, half a page down, and it is in our words rather than the reader's: 'Claude Code runs it before the tool call, outside the model: a setting.' And a ChatGPT user is told to add a hook they cannot have: the hero says it to everybody, and only Claude Code has hooks.

[![On a phone, 'add one hook' is on the first screen, before anything says what a hook is.](/assets/feedback/R001/06-home-phone.webp)](/assets/feedback/R001/06-home-phone.webp)
On a phone, 'add one hook' is on the first screen, before anything says what a hook is. / · 390x844, a phone · v0.2.1
[![The three-step strip under the demo, where the hook is first explained: 'Claude Code runs it before the tool call, outside the model: a setting.'](/assets/feedback/R001/02-home-three-steps.webp)](/assets/feedback/R001/02-home-three-steps.webp)
The three-step strip under the demo, where the hook is first explained: 'Claude Code runs it before the tool call, outside the model: a setting.' / · 1280x900 · v0.2.1

Leads to: [P3](/feedback/reviews/index.md#p3), [P7](/feedback/reviews/index.md#p7).

<a id="r001-4"></a>

**R001.4** agreed

>

the hook is a solution for the question, hold on, but the is the agent that is enforcing its own checks, right? But the user will only provide that question once he understands what the policy is doing.

This is the centre of the memo, and it is right. Every page hands over the line and the hook together, as one package, and puts trying it last: on a behaviour policy's page, step 2, 'Make Claude Code hold it', comes straight after the line; start here goes paste, add the hook, then try. So a customer never sees the line work on its own, never notices that it worked only because the agent chose to follow it, and so never asks the question the hook answers. We answer the question before it has been asked, and an answer to a question you do not have reads as a setup chore.

[![A behaviour policy's step 2, straight after the line and before anything has been tried: install the hook.](/assets/feedback/R001/03-policy-step-2.webp)](/assets/feedback/R001/03-policy-step-2.webp)
A behaviour policy's step 2, straight after the line and before anything has been tried: install the hook. /policies/touch-your-secrets/ · 1280x900 · v0.2.1
[![Start here: paste one line, add one hook, then try it. The try comes after both.](/assets/feedback/R001/04-start-here-steps.webp)](/assets/feedback/R001/04-start-here-steps.webp)
Start here: paste one line, add one hook, then try it. The try comes after both. /start-here/ · 1280x900 · v0.2.1

Leads to: [P1](/feedback/reviews/index.md#p1), [P2](/feedback/reviews/index.md#p2).

<a id="r001-5"></a>

**R001.5** agreed in part

>

if they then go, but hold on, but the hook is still run by the agent. And then we go, yes, which is why it should be done outside.

Right where it matters, with one correction of fact, so that the answer we give is honest. The hook is not run by the model: Claude Code, the program, runs it before the tool call, and the model cannot argue with it. But Claude Code runs it with your full user permissions, on the same machine, from a file in the project's .claude folder. Claude Code does guard that folder: in its default mode an edit there always asks you first, whatever your allow rules say. In bypass-permissions mode it does not ask, and nothing stops you saying yes without reading. So the customer's question is right, and the answer, 'which is why it should be done outside', is the site's own barrier table: a hook is a setting, a switch the agent's own account could flip; only a boundary is out of its reach. Our pages say the hook runs 'outside the model'. That is true, and it answers a narrower question than the one a customer asks next. [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) [Claude Code docs: permission-modes](https://code.claude.com/docs/en/permission-modes)

[![The sequence the memo asks for already exists, as a reference table: none, expectation, setting, boundary.](/assets/feedback/R001/05-abp-barriers.webp)](/assets/feedback/R001/05-abp-barriers.webp)
The sequence the memo asks for already exists, as a reference table: none, expectation, setting, boundary. /what-is-an-abp/ · 1280x900 · v0.2.1
[![A behaviour policy's step 2, straight after the line and before anything has been tried: install the hook.](/assets/feedback/R001/03-policy-step-2.webp)](/assets/feedback/R001/03-policy-step-2.webp)
A behaviour policy's step 2, straight after the line and before anything has been tried: install the hook. /policies/touch-your-secrets/ · 1280x900 · v0.2.1

Leads to: [P4](/feedback/reviews/index.md#p4), [P2](/feedback/reviews/index.md#p2).

<a id="r001-6"></a>

**R001.6** agreed

>

it's very important to have a flow where we guide the user through this workflow, and we guide the user through this sort of sequence of events, including the history.

The sequence already exists, as a table: none, expectation, setting, boundary, weakest first. It sits on the what-is-an-ABP page as reference, not as a path anybody walks. The proposal turns it into the path: four stops, each ending with the question that leads to the next. We read 'including the history' as the story of how each stop came to be needed, the question a customer asks at each one; it could also mean the history of the ABP at riskmandate.ai. That is the first open question below.

[![The sequence the memo asks for already exists, as a reference table: none, expectation, setting, boundary.](/assets/feedback/R001/05-abp-barriers.webp)](/assets/feedback/R001/05-abp-barriers.webp)
The sequence the memo asks for already exists, as a reference table: none, expectation, setting, boundary. /what-is-an-abp/ · 1280x900 · v0.2.1

Leads to: [P2](/feedback/reviews/index.md#p2). Open question: [Q1](/feedback/reviews/index.md#q1).

<a id="r001-7"></a>

**R001.7** agreed

>

So this is not about providing the whole roadmap or a complete solution. This is about getting users to understand the principles of our agent behavior policies and use them straight away.

Agreed. Start here ends in the whole journey: seven milestones, from credit to the usage moment, and the first behaviour policy is introduced as 'milestone S0 to S1 of seven steps'. That is the programme's roadmap: useful to the lead and to us, and a distraction to a customer five minutes in. The proposal moves it to the programme pages and leaves start here with the next stop only.

[![Start here ends in the programme's roadmap: the first behaviour policy is 'milestone S0 to S1 of seven steps'.](/assets/feedback/R001/07-start-here-journey.webp)](/assets/feedback/R001/07-start-here-journey.webp)
Start here ends in the programme's roadmap: the first behaviour policy is 'milestone S0 to S1 of seven steps'. /start-here/ · 1280x900 · v0.2.1

Leads to: [P5](/feedback/reviews/index.md#p5).

<a id="r001-8"></a>

**R001.8** asked of us

>

we need to now capture this as reviews. We also need to encourage the user to record these audio memos and give it to their Claude version, and even get Claude to interview them.

Done in v0.2.2. Tell us what you think, at /feedback/, offers three ways in: one line by email; a voice memo, transcribed, with a prompt that has Claude turn it into a review without softening it; and a prompt that has Claude interview you, one question at a time, criticism first. Every behaviour policy's page and start here link to it, and so does the footer of every page.

Leads to: [P6](/feedback/reviews/index.md#p6).

<a id="r001-9"></a>

**R001.9** asked of us

>

I would like us to run this to some synthetic users so that we can also capture them, right, this feedback.

Done in v0.2.2: study S1, five invented users on the v0.2.1 site, each with a profile and an expected journey written before the run, driving a real browser one screenshot at a time. Their findings are on this page, checked, each with what we will do about it.

Leads to: [P8](/feedback/reviews/index.md#p8).

<a id="r001-10"></a>

**R001.10** asked of us

>

And then you can put them all in one document and put them all in one consolidated view. And then what you should do is you should have another part on that where you should comment on everything I said. Even put some screenshots on it

This page. Every review keeps its words verbatim; our reading follows point by point, with what the reviewer was looking at; and every proposal, from every review, is in one register with a decision.

Leads to: [P6](/feedback/reviews/index.md#p6).

<a id="r001-11"></a>

**R001.11** asked of us

>

And we don't have to do everything the user says, right? You know, but we should have a good reason why we don't do that.

Every proposal in the register carries a decision and a reason, the declined ones included. This review has two declines, D1 and D2. And everything it asks to change on the site is proposed rather than built, because the memo calls itself a first impression: one redesign made with all of the lead's memos is better than two.

Leads to: [D1](/feedback/reviews/index.md#d1), [D2](/feedback/reviews/index.md#d2).

<a id="s1"></a>

## Synthetic users: study S1

**Invented, not user research.** Everybody in this study is invented, and their words were written by a model playing them. What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.

5 invented users took 60 screenshots on site v0.2.1, gave it 3, 3, 4, 2 and 3 out of 5, and reported 29 findings. We checked each one: 24 confirmed, 4 partly, 1 artefact. The study, with each run step by step: [study S1](/feedback/synthetic/index.md).

| Invented user | On | Ended | Rating | Their one change |
|---|---|---|---|---|
| [Sam Okoye](/feedback/synthetic/sam/index.md)Backend developer at a 12-person payments start-up. Uses Claude Code every day in a monorepo with .env files for four services. | laptop, 1440×900 | left, after 12 screenshots | **3** of 5 | Show the whole hook, uncut, with a short plain-words list: 'blocks these filenames, leaves these alone, to turn it off delete this block'. |
| [Nadia Farouk](/feedback/synthetic/nadia/index.md)Product manager at a 200-person retailer. Uses ChatGPT with the Gmail connector, and Claude in the browser. Not a developer. | phone, 390×844 | got-it, after 8 screenshots | **3** of 5 | Put my question first on the home page: 'Stop ChatGPT sending email as you', in plain words, instead of a headline about hooks and Claude Code. |
| [Marcus Lindqvist](/feedback/synthetic/marcus/index.md)Independent security consultant, twenty years in. Reads vendor sites adversarially. Recommends tools to clients; might resell; will not be a customer himself. | laptop, 1440×900 | cap, after 15 screenshots | **4** of 5 | Put the sentence 'the hook and its guard live in the same file the agent can write; against an injected agent, only the sandbox or managed settings holds' at the top of RM-R0015, where a reader lands from the self-edit link, instead of only on the secrets page. |
| [Joan Mbeki](/feedback/synthetic/joan/index.md)CTO of a 30-person software company. Fifteen engineers use Claude Code. Holds the budget. | tablet, 1180×820 | left, after 14 screenshots | **2** of 5 | A page for a team lead: how fifteen engineers get the same baseline from one place, who can change it, what stops one person turning it off, and what joining commits us to. |
| [Tomás Reyes](/feedback/synthetic/tomas/index.md)Junior developer, a year into his first job. Uses Claude Code through the VS Code extension on a Windows laptop. Follows instructions literally. | laptop, 1366×768 | patience, after 11 screenshots | **3** of 5 | Add one short 'did it work?' box under Try it: what you see if it worked, and what to do if python3 is missing or nothing happens. |

### Every finding, by what it costs, with our check

| Costs | The finding, in their words | Our check | Leads to |
|---|---|---|---|
| <a id="s1-tomas-1"></a>blocks the first install | No fallback when python3 is missing or the hook does not runTomás Reyes, [step 3](/feedback/synthetic/tomas/index.md#step-3), `/policies/touch-your-secrets/` | confirmedThe settings run python3 and no page says so. On Windows, Claude Code runs hooks in Git Bash, or PowerShell if Git Bash is not installed; a hook that cannot start lets the action through. | [P11](/feedback/reviews/index.md#p11) |
| <a id="s1-sam-1"></a>blocks the first install | The hook source is cut off before the rules that say which files it blocksSam Okoye, [step 7](/feedback/synthetic/sam/index.md#step-7), `/policies/touch-your-secrets/` | partlyThe source is all there, in a box that scrolls: 418 of its 1,246 pixels show, and nothing says it scrolls. What he needed, which files it stops, is not in plain words anywhere on the page. | [P12](/feedback/reviews/index.md#p12), [D3](/feedback/reviews/index.md#d3) |
| <a id="s1-joan-3"></a>costs trust | Policy 4 hands the decision to the individual, not the companyJoan Mbeki, [step 9](/feedback/synthetic/joan/index.md#step-9), `/policies/starter/` | confirmedRM-R0015 asks the person at the keyboard. For a company, the answer is managed settings, which no page names. | [P14](/feedback/reviews/index.md#p14) |
| <a id="s1-joan-4"></a>costs trust | Pages cost real-looking money and the price rule is unexplainedJoan Mbeki, [step 7](/feedback/synthetic/joan/index.md#step-7), `/policies/starter/` | confirmedConfirmed that nothing explains it; we are keeping the prices. | [P9](/feedback/reviews/index.md#p9), [D5](/feedback/reviews/index.md#d5) |
| <a id="s1-marcus-1"></a>costs trust | The home page says the hook 'holds' and 'stops the read' with no word on how it failsMarcus Lindqvist, [step 1](/feedback/synthetic/marcus/index.md#step-1), `/` | confirmedThe home page says the hook stops the read; how it fails is two clicks away. | [P4](/feedback/reviews/index.md#p4) |
| <a id="s1-marcus-3"></a>costs trust | No fail-open/fail-closed statement, and 'tested hook' is not definedMarcus Lindqvist, [step 8](/feedback/synthetic/marcus/index.md#step-8), `/docs/reality.html` | confirmedNo page said what happens when a hook cannot run. Claude Code's documentation: any failure other than exit code 2, a timeout included, lets the action go ahead. And the tests feed the hook the JSON Claude Code would send; they do not drive a live session. | [P11](/feedback/reviews/index.md#p11), [P18](/feedback/reviews/index.md#p18) |
| <a id="s1-marcus-5"></a>costs trust | The only real boundary on offer is someone else's feature, and managed settings are not mentioned on the pages I readMarcus Lindqvist, [step 13](/feedback/synthetic/marcus/index.md#step-13), `/policies/touch-your-secrets/` | confirmedManaged settings are named only in a hook's source comment. | [P2](/feedback/reviews/index.md#p2), [P14](/feedback/reviews/index.md#p14) |
| <a id="s1-nadia-3"></a>costs trust | The balance drops while scrolling and the home page does not explain whyNadia Farouk, [step 3](/feedback/synthetic/nadia/index.md#step-3), `/policies/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| <a id="s1-nadia-4"></a>costs trust | The key limit of the line is stated, but the stronger lock is for claude.ai admins onlyNadia Farouk, [step 7](/feedback/synthetic/nadia/index.md#step-7), `/policies/send-as-you/` | confirmedThe only stronger control listed for send-as-you is an organisation administrator's setting in Claude, from riskmandate.ai's rule. We do not yet know what a ChatGPT user can set for themselves. | [P7](/feedback/reviews/index.md#p7) |
| <a id="s1-sam-3"></a>costs trust | No word on how to turn the hook off or undo the installSam Okoye, [step 9](/feedback/synthetic/sam/index.md#step-9), `/policies/touch-your-secrets/` | confirmedNo page says how to remove a hook. | [P12](/feedback/reviews/index.md#p12) |
| <a id="s1-sam-4"></a>costs trust | The £50 and the falling balance are unexplained until the third page I openSam Okoye, [step 1](/feedback/synthetic/sam/index.md#step-1), `/` | confirmedFive of five asked what the £50 was. | [P9](/feedback/reviews/index.md#p9) |
| <a id="s1-tomas-3"></a>costs trust | Try it lists two outcomes only; there is no 'it did not work' branchTomás Reyes, [step 4](/feedback/synthetic/tomas/index.md#step-4), `/policies/touch-your-secrets/` | confirmedTry it gave only the two outcomes. | [P11](/feedback/reviews/index.md#p11), [D4](/feedback/reviews/index.md#d4) |
| <a id="s1-tomas-4"></a>costs trust | Balance falls as you scroll, with the price disclosed only in small printTomás Reyes, [step 2](/feedback/synthetic/tomas/index.md#step-2), `/policies/touch-your-secrets/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| <a id="s1-marcus-2"></a>costs trust | The honest limits table is present on the policy page but the self-edit policy page does not repeat itMarcus Lindqvist, [step 15](/feedback/synthetic/marcus/index.md#step-15), `/policies/change-its-own-permissions/` | partlyRM-R0015's page has the same limits table as the others, further down; he reached the page on his last action and saw only its top. What holds: the limit is not at the top, where a reader arrives from the self-edit link. | [P4](/feedback/reviews/index.md#p4) |
| <a id="s1-joan-1"></a>loses a customer | Nothing for a team: every page is one person, one projectJoan Mbeki, [step 7](/feedback/synthetic/joan/index.md#step-7), `/policies/starter/` | confirmedNothing says that committing .claude/settings.json gives everybody who pulls the same hooks, which Claude Code's documentation says it does. | [P14](/feedback/reviews/index.md#p14) |
| <a id="s1-joan-2"></a>loses a customer | No page says what joining the first batch commits a company toJoan Mbeki, [step 14](/feedback/synthetic/joan/index.md#step-14), `/programme/` | confirmedNo page says what joining commits a company to. | [P15](/feedback/reviews/index.md#p15) |
| <a id="s1-nadia-1"></a>loses a customer | The first screen speaks to developers, not to a ChatGPT userNadia Farouk, [step 1](/feedback/synthetic/nadia/index.md#step-1), `/` | confirmedThe first paragraph names a hook and Claude Code; ChatGPT first appears half a page down. | [P1](/feedback/reviews/index.md#p1), [P7](/feedback/reviews/index.md#p7) |
| <a id="s1-sam-2"></a>loses a customer | The matcher includes Bash, Edit and Write with no plain-words reasonSam Okoye, [step 5](/feedback/synthetic/sam/index.md#step-5), `/policies/touch-your-secrets/` | confirmedThe matcher names every file tool and Bash, and nothing beside it says the hook answers only when a credential file is named. | [P12](/feedback/reviews/index.md#p12) |
| <a id="s1-joan-5"></a>costs time | Page is the lead's own tracking, not a customer-facing explanationJoan Mbeki, [step 3](/feedback/synthetic/joan/index.md#step-3), `/customers/` | confirmedThe first batch page is the lead's tracking. She went there looking for terms, which are nowhere. | [P15](/feedback/reviews/index.md#p15) |
| <a id="s1-marcus-4"></a>costs time | Balance falls on every page with no visible reason on screenMarcus Lindqvist, [step 2](/feedback/synthetic/marcus/index.md#step-2), `/what-is-an-abp/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| <a id="s1-nadia-2"></a>costs time | The policy list leads with a Claude Code pack and a hook section before the ChatGPT onesNadia Farouk, [step 2](/feedback/synthetic/nadia/index.md#step-2), `/policies/` | confirmedOn /policies/ the Claude Code pack and section come first; the ChatGPT section is about 1,500 pixels down on a phone. | [P7](/feedback/reviews/index.md#p7) |
| <a id="s1-nadia-5"></a>costs time | Unexplained terms and a one-row table on the key pageNadia Farouk, [step 7](/feedback/synthetic/nadia/index.md#step-7), `/policies/send-as-you/` | confirmedOur generator wrote 'Neither half is a boundary' on pages with only one half. | [P13](/feedback/reviews/index.md#p13) |
| <a id="s1-tomas-2"></a>costs time | 'Start a new session' is not explained for the VS Code extensionTomás Reyes, [step 3](/feedback/synthetic/tomas/index.md#step-3), `/policies/touch-your-secrets/` | confirmedWorse than the finding: the instruction is out of date. Claude Code applies changes to hooks in the running session. | [P10](/feedback/reviews/index.md#p10) |
| <a id="s1-tomas-5"></a>costs time | 'What this is, and what it is not' reads as a to-do and uses unexplained termsTomás Reyes, [step 6](/feedback/synthetic/tomas/index.md#step-6), `/policies/touch-your-secrets/` | confirmedThe stronger controls read as a second required step; nothing says they are optional. | [P4](/feedback/reviews/index.md#p4) |
| <a id="s1-sam-5"></a>costs time | The typing terminal demo shows nothing useful and looks stuckSam Okoye, [step 2](/feedback/synthetic/sam/index.md#step-2), `/` | partlyA still screenshot cannot watch an animation: the demo is typing, not stuck. What holds: measured in the same browser, the refusal appears about eleven seconds after the demo comes into view. | [P17](/feedback/reviews/index.md#p17) |
| <a id="s1-joan-6"></a>minor | Unexplained balance in the header and an unexplained 'reading account'Joan Mbeki, [step 1](/feedback/synthetic/joan/index.md#step-1), `/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| <a id="s1-sam-6"></a>minor | Docs menu and status line are the company's internal papers, not user helpSam Okoye, [step 12](/feedback/synthetic/sam/index.md#step-12), `/docs/` | confirmedThe Docs menu is the brief, the memo and how the site is built. | [P16](/feedback/reviews/index.md#p16) |
| <a id="s1-tomas-6"></a>minor | Start-here page opens with internal status text and a dropdown that covers contentTomás Reyes, [step 11](/feedback/synthetic/tomas/index.md#step-11), `/start-here/` | partlyThe status line at the top of start here holds. The dropdown over step 4 was our helper: the mouse stayed where it clicked the menu, and the menu opens on hover. | [P16](/feedback/reviews/index.md#p16) |
| <a id="s1-marcus-6"></a>minor | The click on a visible link failed and the action cost a slotMarcus Lindqvist, [step 14](/feedback/synthetic/marcus/index.md#step-14), `/policies/touch-your-secrets/` | artefactThe helper's clicktext matched hidden text first and timed out; the link works, as his next action showed. The helper now clicks the first visible match. | none |

<a id="register"></a>

## The proposals, with a decision each

From every review and every finding above. proposed we think yes; not built yet, and the reason says why; accepted will be built; not yet; done built, in the version named; declined not doing it, and why; question we need an answer first; the question is named.

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="p1"></a>**P1** | **The line first, the hook second, in answer to a question**The home page, the three steps, start here and every Claude Code behaviour policy go: pick one worry, paste one line, try it. It refuses. Then: it refused because it chose to; what if it decides your task needs the file? The hook is the answer to that question, and arrives with it. The demo plays in the same order. | proposedWe agree with the memo. Not built yet because it changes the first screen and every policy page, and the lead says more memos are coming: one redesign made with all of them is better than two. | [R001.2](/feedback/reviews/index.md#r001-2), [R001.4](/feedback/reviews/index.md#r001-4), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1) |
| <a id="p2"></a>**P2** | **A guided path: four stops, each ending in the question that leads to the next**1. Say it: the line, an expectation. Try it; it refuses. 'It chose to.' 2. Hold it: the hook, a setting. Try it again; Claude Code stops the read before the model sees the file. 'But the hook is a file in my project.' 3. Guard the guard: RM-R0015, and Claude Code's own prompt before any edit to .claude/. 'But it is still my machine and my user.' 4. Put it outside: a boundary, out of the agent's reach: the secret not on the machine, branch protection on the server, the sandbox, managed settings an administrator owns. 'Which of my worries need a boundary?' That question is the start of your mandate. Drawn as a storyboard first, then a page; every behaviour policy shows where it sits on the path. | proposedThis is the sequence the memo describes, and the site already has its words: the barrier table runs none, expectation, setting, boundary. Not built yet for the same reason as P1, and because Q1 (what 'the history' means) changes what each stop says. | [R001.4](/feedback/reviews/index.md#r001-4), [R001.5](/feedback/reviews/index.md#r001-5), [R001.6](/feedback/reviews/index.md#r001-6), [S1 Marcus 5](/feedback/reviews/index.md#s1-marcus-5) |
| <a id="p3"></a>**P3** | **Say what a hook is, in plain words, where the word first appears**A hook: a small script Claude Code itself runs before the agent acts, which can stop the action. Said once, at the first mention, on every page that mentions one. | proposedCheap and right, but the first mention is exactly the text P1 rewrites. It ships with P1, so the first screen changes once. | [R001.3](/feedback/reviews/index.md#r001-3) |
| <a id="p4"></a>**P4** | **Say what the hook is outside of, and how it fails, where it is offered**Replace 'outside the model' with what is true and what the customer will ask next: Claude Code runs it, not the model, so the model cannot argue with it; it runs as you, from a file in your project, so it is a setting, not a boundary; if it cannot run, the action goes ahead. Each policy page's limits move up, beside the install, and RM-R0015's page says its own limit at the top. The stronger controls are labelled as optional, for later, not a second required step. | proposedThe memo's correction and two invented users (Marcus, Tomás) point the same way. It ships with P1 and P2, because the limits are the questions those two make into steps; how the hook fails ships now, as P11. | [R001.5](/feedback/reviews/index.md#r001-5), [S1 Marcus 1](/feedback/reviews/index.md#s1-marcus-1), [S1 Marcus 2](/feedback/reviews/index.md#s1-marcus-2), [S1 Tomás 5](/feedback/reviews/index.md#s1-tomas-5) |
| <a id="p5"></a>**P5** | **Start here shows the next stop, not the whole journey**The seven milestones move off start here to the programme's pages; start here ends with the next stop of the path in P2. | proposedAgreed; the milestones are the programme's roadmap, not a customer's next step. Not built yet because the next stop is P2's, which is not built. | [R001.7](/feedback/reviews/index.md#r001-7) |
| <a id="p6"></a>**P6** | **A way for every customer to give feedback, and one place it all goes**/feedback/: one line by email; a voice memo with a prompt that has Claude turn the transcript into a review; a prompt that has Claude interview you. /feedback/reviews/: every review verbatim, our reading point by point with screenshots, and this register. | done v0.2.2The memo asked for it, and the programme exists to learn from its customers. | [R001.8](/feedback/reviews/index.md#r001-8), [R001.10](/feedback/reviews/index.md#r001-10) |
| <a id="p7"></a>**P7** | **ChatGPT and Claude users never meet the word hook, and find their worry first**A path for people who use ChatGPT or Claude in the browser: their worries first (mail sent as you, all of your mail read), a line, a try, and the honest answer on what holds it. We do not yet know which boundary a ChatGPT user who is not an administrator can set for a connector; until we do, the page says so rather than offering only an administrator's setting. | proposedThe memo's point about hooks applies twice over to people who cannot have one, and Nadia, an invented ChatGPT user on a phone, met 'hook' and 'Claude Code' in the first paragraph. Ships with P1; the facts about ChatGPT's connector settings have to be checked first. | [R001.3](/feedback/reviews/index.md#r001-3), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1), [S1 Nadia 2](/feedback/reviews/index.md#s1-nadia-2), [S1 Nadia 4](/feedback/reviews/index.md#s1-nadia-4) |
| <a id="p8"></a>**P8** | **Synthetic users, run again after every change that matters**Study S1: five invented users on v0.2.1, with profiles and expected journeys written first, the browser helper and the protocol in the repository. The same five run again after P1 and P2 ship, and the two studies are compared. | done v0.2.2The memo asked for it. They are invented, not user research: they find what a page fails to say, not what a customer wants. | [R001.9](/feedback/reviews/index.md#r001-9) |
| <a id="p9"></a>**P9** | **Say what the £50 is where the balance first appears**All five invented users asked whether the £50 was real money, and four watched the balance fall with nothing on the screen saying why. The home page's badge and the account link now say it: credit for reading, not money; nothing is billed and nothing is blocked; each page's price is on the page. | done v0.2.2Five of five, and a line of text. It does not touch the sequence P1 changes. | [S1 Sam 4](/feedback/reviews/index.md#s1-sam-4), [S1 Nadia 3](/feedback/reviews/index.md#s1-nadia-3), [S1 Marcus 4](/feedback/reviews/index.md#s1-marcus-4), [S1 Joan 4](/feedback/reviews/index.md#s1-joan-4), [S1 Joan 6](/feedback/reviews/index.md#s1-joan-6), [S1 Tomás 4](/feedback/reviews/index.md#s1-tomas-4) |
| <a id="p10"></a>**P10** | **Stop telling people to start a new session**Our pages said to start a new session, or open /hooks, so Claude Code loads the hook. Claude Code's documentation says it watches its settings files and applies changes to hooks in the running session, and that /hooks is a read-only list. The pages now say that, and that /hooks is where to check the hook is there. | done v0.2.2A correction of fact, found because Tomás, an invented junior developer, could not tell what a new session meant in the VS Code extension. [Claude Code docs: settings](https://code.claude.com/docs/en/settings) [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Tomás 2](/feedback/reviews/index.md#s1-tomas-2) |
| <a id="p11"></a>**P11** | **Did it work? And what happens when the hook cannot run**Under every Try it: what you see if it worked; what it means if the prompt was not refused (the hook did not run); how to check (is it listed in /hooks? does python3 run where Claude Code runs it? on Windows, Claude Code runs hooks in Git Bash, or PowerShell if Git Bash is not installed); and the fact that matters most: if the hook cannot run, Claude Code lets the action through. The hook fails open (on Windows without Git Bash, Claude Code may block instead), which is one more reason it is a setting and not a boundary. The tests are named for what they are: they feed the hook the JSON Claude Code would send, and do not drive a live session. | done v0.2.2Missing safety information, found by two invented users (Tomás on Windows, Marcus asking fail open or closed). It is about trying, which P1 keeps, so it does not wait for P1. [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Marcus 3](/feedback/reviews/index.md#s1-marcus-3), [S1 Tomás 1](/feedback/reviews/index.md#s1-tomas-1), [S1 Tomás 3](/feedback/reviews/index.md#s1-tomas-3) |
| <a id="p12"></a>**P12** | **Each hook, in plain words, beside the install: what it looks at, stops, asks, lets through, and misses; and how to turn it off**A short table beside each hook's settings, and one line on turning it off: remove its entry from .claude/settings.json, and Claude Code stops running it. The box with the hook's source says that it scrolls. | done v0.2.2Sam, an invented developer, left without installing because he could not predict what the hook would block or how to remove it. The table is written from the hooks' own rules. | [S1 Sam 1](/feedback/reviews/index.md#s1-sam-1), [S1 Sam 2](/feedback/reviews/index.md#s1-sam-2), [S1 Sam 3](/feedback/reviews/index.md#s1-sam-3) |
| <a id="p13"></a>**P13** | **Line-only pages stop talking about two halves**On a behaviour policy with only a line, the limits table had one row headed 'Half' and the text said 'Neither half is a boundary'. It now says the line is an expectation and is not a boundary. | done v0.2.2A plain mistake in our generator, found by Nadia. | [S1 Nadia 5](/feedback/reviews/index.md#s1-nadia-5) |
| <a id="p14"></a>**P14** | **A page for a team: one baseline for everybody, and who can turn it off**For a team lead: commit .claude/settings.json and the hooks to the repository, so everybody who pulls gets them; and for 'does it hold if one of them turns it off', managed settings, which an administrator deploys and no user or project file can override, with the setting that runs only the organisation's hooks. Then branch protection and token scopes, which no setting on a laptop can undo. | proposedJoan, an invented CTO, left over this, and Marcus asked for managed settings by name. It is stop 4 of P2 for a company; it waits for P2 and for Q3. [Claude Code docs: settings](https://code.claude.com/docs/en/settings) [Claude Code docs: managed-settings](https://code.claude.com/docs/en/managed-settings) | [S1 Marcus 5](/feedback/reviews/index.md#s1-marcus-5), [S1 Joan 1](/feedback/reviews/index.md#s1-joan-1), [S1 Joan 3](/feedback/reviews/index.md#s1-joan-3) |
| <a id="p15"></a>**P15** | **What joining the first batch commits a company to**One page a company reads before saying yes: what we ask of you, what you get, what it costs now and later, and how you leave. | questionJoan could not find it and left. Only the lead can say what joining commits a company to: Q3. | [S1 Joan 2](/feedback/reviews/index.md#s1-joan-2), [S1 Joan 5](/feedback/reviews/index.md#s1-joan-5) |
| <a id="p16"></a>**P16** | **Customer pages lead with the customer's business**Start here opened with a status line read from docs/reality.md; it now closes the page. The Docs menu, which holds the brief, the memo and how the site is built, is the lead's and ours, not a customer's: proposed to move it under the programme. | done v0.2.2Three invented users stopped on internal papers. The status line moved now; the menu waits for P1, which changes what a customer looks for in it. | [S1 Sam 6](/feedback/reviews/index.md#s1-sam-6), [S1 Tomás 6](/feedback/reviews/index.md#s1-tomas-6) |
| <a id="p17"></a>**P17** | **The demo shows its point first**The refusal arrives about eleven seconds after the demo comes into view; a reader who scrolls past sooner sees a terminal typing. Proposed: the demo opens on its last frame, the refusal, with a Play button for the whole session. | proposedTwo invented users saw the demo as stuck or empty. Partly a limit of the method (a screenshot cannot watch an animation), and partly real. P1 changes what the demo plays, so it changes with P1. | [S1 Sam 5](/feedback/reviews/index.md#s1-sam-5) |
| <a id="p18"></a>**P18** | **Make the guard fail closed**Claude Code can be told to block the action when a hook fails, with "onFailure": "block" on the hook (Claude Code v2.1.295 or later). Proposed for RM-R0015's hook, the guard of the other three, first; for the others, a choice on each policy's page. | proposedFailing closed is safer and louder, but on a hook that looks at every read, a missing python3 would then stop every read until it is fixed, and older versions of Claude Code do not know the setting. The trade-off belongs on the page, and the default is the lead's call. [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Marcus 3](/feedback/reviews/index.md#s1-marcus-3) |
| <a id="d1"></a>**D1** | **Take the hook out of the first five minutes**One reading of 'a solution for a problem they don't have yet' is to leave the hook for later. | declinedThe hook stays in the first five minutes, second rather than first (P1). A customer who stops after the line leaves believing their agent is held when it has only been asked, and that difference is the point of the ABP. The memo's own sequence keeps it: the question that the hook answers comes up in the first try, if we let it. | [R001.11](/feedback/reviews/index.md#r001-11) |
| <a id="d2"></a>**D2** | **A glossary page for hook, expectation, setting and boundary**A page that defines the words. | declinedA glossary is a page a customer does not open at the moment they need it. Each word is said in plain words where it first appears (P3), and the path (P2) teaches the barrier words by using them. | [R001.11](/feedback/reviews/index.md#r001-11) |
| <a id="d3"></a>**D3** | **Show the whole hook, uncut, on the page**Sam's one change, read literally: every line of the hook on the page. | declinedSixty-seven lines of Python on the page push Try it down by a screen for everybody, to help the few who read code, and they can open the box or the file. What Sam needed was to predict what it blocks and how to remove it: P12 gives him that in five lines. | [S1 Sam 1](/feedback/reviews/index.md#s1-sam-1) |
| <a id="d4"></a>**D4** | **A help or FAQ page for installers**Tomás looked for one. | declinedHis two questions were asked on the page where he got stuck, and P10 and P11 answer them there. A help page would be one more place to look. | [S1 Tomás 3](/feedback/reviews/index.md#s1-tomas-3) |
| <a id="d5"></a>**D5** | **Stop charging for pages, or hide the balance**Joan found pages that cost real-looking money alarming. | declinedEvery page has a price because the lead asked for it, and the programme exists to find fair prices with its customers. What was wrong was that nothing said what the money is: P9 fixes that. | [S1 Joan 4](/feedback/reviews/index.md#s1-joan-4) |

<a id="questions"></a>

## Questions we need answered

- <a id="q1"></a>**Q1, to Dinis Cruz.** 'Including the history': do you mean the history of each question, the conversation a customer has with us as they go from stop to stop, which is how we read it, or the history of the ABP at riskmandate.ai, how the rules came to be?
- <a id="q2"></a>**Q2, to Dinis Cruz.** Should the first try show the line failing? An honest demonstration of a line being ignored is hard to stage without making the agent look worse than it is. We propose showing instead that it refused because it chose to: the same refusal, read differently. Is that enough?
- <a id="q3"></a>**Q3, to Dinis Cruz.** What does joining the first batch commit a company to: what we ask of them, what it costs now and later, and how they leave? And should the first batch include companies that want a team-wide baseline, or individuals first?

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/)*
