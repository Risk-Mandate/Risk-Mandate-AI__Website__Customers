# Review R001: A first impression: the hook answers a question nobody has asked yet

> Dinis Cruz's review of customers.riskmandate.ai v0.2.1, Wednesday 21 October 2026, 1:41, as given in the memo: the memo verbatim, our reading point by point with screenshots, and the proposals it led to.

*Source: <https://customers.riskmandate.ai/feedback/reviews/R001/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Review R001 · Dinis Cruz · site v0.2.1

# A first impression: the hook answers a question nobody has asked yet

Dinis Cruz, Wednesday 21 October 2026, 1:41, as given in the memo. First impression; the reviewer says more memos follow and this one is not complete. The same review is in [the consolidated document](/feedback/reviews/index.md#r001), beside every other.

<a id="review"></a>

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

<a id="proposals"></a>

## What it led to

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="here-p1"></a>**P1** | **The line first, the hook second, in answer to a question**The home page, the three steps, start here and every Claude Code behaviour policy go: pick one worry, paste one line, try it. It refuses. Then: it refused because it chose to; what if it decides your task needs the file? The hook is the answer to that question, and arrives with it. The demo plays in the same order. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Done in a stronger form than we proposed: R002 took the hook out of the first five minutes altogether (P19). The line comes first, and the question it leaves is asked under every example. | [R001.2](/feedback/reviews/index.md#r001-2), [R001.4](/feedback/reviews/index.md#r001-4), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1) |
| <a id="here-p2"></a>**P2** | **A guided path: four stops, each ending in the question that leads to the next**1. Say it: the line, an expectation. Try it; it refuses. 'It chose to.' 2. Hold it: the hook, a setting. Try it again; Claude Code stops the read before the model sees the file. 'But the hook is a file in my project.' 3. Guard the guard: RM-R0015, and Claude Code's own prompt before any edit to .claude/. 'But it is still my machine and my user.' 4. Put it outside: a boundary, out of the agent's reach: the secret not on the machine, branch protection on the server, the sandbox, managed settings an administrator owns. 'Which of my worries need a boundary?' That question is the start of your mandate. Drawn as a storyboard first, then a page; every behaviour policy shows where it sits on the path. | proposedThe examples are its first stop now: the line, an expectation, and the question it leaves. The other stops wait for Q1, and are no longer on the first screen: they are what a customer reads after the examples. | [R001.4](/feedback/reviews/index.md#r001-4), [R001.5](/feedback/reviews/index.md#r001-5), [R001.6](/feedback/reviews/index.md#r001-6), [S1 Marcus 5](/feedback/reviews/index.md#s1-marcus-5) |
| <a id="here-p3"></a>**P3** | **Say what a hook is, in plain words, where the word first appears**A hook: a small script Claude Code itself runs before the agent acts, which can stop the action. Said once, at the first mention, on every page that mentions one. | done v0.2.3proposed at v0.2.2 → done at v0.2.3The front pages no longer mention a hook (P19). Where one is offered, on the Claude Code pages, the warning above them says what it is first. | [R001.3](/feedback/reviews/index.md#r001-3) |
| <a id="here-p4"></a>**P4** | **Say what the hook is outside of, and how it fails, where it is offered**Replace 'outside the model' with what is true and what the customer will ask next: Claude Code runs it, not the model, so the model cannot argue with it; it runs as you, from a file in your project, so it is a setting, not a boundary; if it cannot run, the action goes ahead. Each policy page's limits move up, beside the install, and RM-R0015's page says its own limit at the top. The stronger controls are labelled as optional, for later, not a second required step. | proposedThe memo's correction and two invented users (Marcus, Tomás) point the same way. It ships with P1 and P2, because the limits are the questions those two make into steps; how the hook fails ships now, as P11. | [R001.5](/feedback/reviews/index.md#r001-5), [S1 Marcus 1](/feedback/reviews/index.md#s1-marcus-1), [S1 Marcus 2](/feedback/reviews/index.md#s1-marcus-2), [S1 Tomás 5](/feedback/reviews/index.md#s1-tomas-5) |
| <a id="here-p5"></a>**P5** | **Start here shows the next stop, not the whole journey**The seven milestones move off start here to the programme's pages; start here ends with the next stop of the path in P2. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Start here was rewritten for the browser (R002); it ends with the next five examples and your account, and the seven milestones are only on the programme pages. | [R001.7](/feedback/reviews/index.md#r001-7) |
| <a id="here-p6"></a>**P6** | **A way for every customer to give feedback, and one place it all goes**/feedback/: one line by email; a voice memo with a prompt that has Claude turn the transcript into a review; a prompt that has Claude interview you. /feedback/reviews/: every review verbatim, our reading point by point with screenshots, and this register. | done v0.2.2The memo asked for it, and the programme exists to learn from its customers. | [R001.8](/feedback/reviews/index.md#r001-8), [R001.10](/feedback/reviews/index.md#r001-10) |
| <a id="here-p7"></a>**P7** | **ChatGPT and Claude users never meet the word hook, and find their worry first**A path for people who use ChatGPT or Claude in the browser: their worries first (mail sent as you, all of your mail read), a line, a try, and the honest answer on what holds it. We do not yet know which boundary a ChatGPT user who is not an administrator can set for a connector; until we do, the page says so rather than offering only an administrator's setting. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Done by R002's web first: every first example runs in ChatGPT or Claude in the browser, and none of them mentions a hook. Which boundary a ChatGPT user can set for a connector is still to be checked (P26). | [R001.3](/feedback/reviews/index.md#r001-3), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1), [S1 Nadia 2](/feedback/reviews/index.md#s1-nadia-2), [S1 Nadia 4](/feedback/reviews/index.md#s1-nadia-4) |
| <a id="here-p8"></a>**P8** | **Synthetic users, run again after every change that matters**Study S1: five invented users on v0.2.1, with profiles and expected journeys written first, the browser helper and the protocol in the repository. The same five run again after P1 and P2 ship, and the two studies are compared. | done v0.2.2The memo asked for it. They are invented, not user research: they find what a page fails to say, not what a customer wants. Study S2, the same five, is due once the lead has reviewed v0.2.3: R002 rebuilt the front pages, and running invented users on a design the lead is still changing would measure the wrong thing. | [R001.9](/feedback/reviews/index.md#r001-9) |
| <a id="here-d1"></a>**D1** | **Take the hook out of the first five minutes**One reading of 'a solution for a problem they don't have yet' is to leave the hook for later. | reversed v0.2.3declined at v0.2.2 → reversed at v0.2.3Declined at v0.2.2: a customer who stops after the line leaves believing their agent is held when it has only been asked. Reversed at v0.2.3 by R002 (R002.7): a hook is a program run on the customer's machine, which our first screen had their agent fetch from our site and install, before any behaviour policy governs what their agent installs. Our concern is kept in words: every example says the line is followed because the assistant chooses to. | [R001.11](/feedback/reviews/index.md#r001-11), [R002.1](/feedback/reviews/index.md#r002-1) |
| <a id="here-d2"></a>**D2** | **A glossary page for hook, expectation, setting and boundary**A page that defines the words. | declinedA glossary is a page a customer does not open at the moment they need it. Each word is said in plain words where it first appears (P3), and the path (P2) teaches the barrier words by using them. | [R001.11](/feedback/reviews/index.md#r001-11) |

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/R001/)*
