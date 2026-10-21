# Review R004: The first run in a real browser: write it up, replay it, draw it, and brief the next agent

> Dinis Cruz's review of customers.riskmandate.ai v0.2.4, Wednesday 21 October 2026, with run C1's zip: the memo verbatim, our reading point by point with screenshots, and the proposals it led to.

*Source: <https://customers.riskmandate.ai/feedback/reviews/R004/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Review R004 · Dinis Cruz · site v0.2.4

# The first run in a real browser: write it up, replay it, draw it, and brief the next agent

Dinis Cruz, Wednesday 21 October 2026, with run C1's zip. A memo about run c1 and what it makes possible. The same review is in [the consolidated document](/feedback/reviews/index.md#r004), beside every other.

<a id="review"></a>

## R004: The first run in a real browser: write it up, replay it, draw it, and brief the next agent

**Reviewer**
: Dinis Cruz, the lead of the programme
**Given**
: Wednesday 21 October 2026, with run C1's zip
**Reviewing**
: site v0.2.4
**As**
: a voice memo, transcribed
**Status**
: a memo about run C1 and what it makes possible

- The memo is kept as transcribed, with paragraph breaks added. 'An adjacent flow' is most likely 'a JSON flow': the records as data.
- Run C1 was made on v0.2.3; this memo arrived when v0.2.4 was live.

### The memo, verbatim

>

Okay, and now first synthetic user run is in. So can you write this up? Can you actually do two things? Can you write an article with an analysis of it? And what works, what didn't work, what was good, what was not good, and then maybe see what we can change to improve it, and then map what we improve from it.

But also, can you, because you have so many screenshots of it, can you actually try to create an animation and a set of animations, again, with start, stop, etc., so that, and I think this should be ridiculously powerful, and think about what now this means. This means that we can create workflows like this, right? So what this means, it means that we can now should be able to create a video or an animation, not even a video, but a JavaScript-based animation, where we literally show these steps. And the user can replay them, so they can actually see them working side by side. And this also means that you can put, for example, next to it, a flow chart, and you can put an infographic and even like an explanation of what's happening. And I think that will really help new users to understand what's going on.

And in fact, once after you've done that, can you also experiment with a storyboard, right? Where you actually show the real stuff then next to a storyboard as it plays out. And I think that can actually work really, really well. Because remember that we're trying to explain this concept to users, right? And I think until the users experience this, they are not really going to go into the more advanced concepts. So we need to figure out, and then we need to get feedback from users on what other scenarios they find quite interesting. But I think this is quite cool.

Also, take into account that you could also write a brief that I can give to the other agent, or you can even actually, in fact, you can actually write a page that is a brief for the other agent, and I'll just quickly tell you what's going on the other side. So we have a session here in Claude, actually not this, I have a Claude account for risk mandate, which I've logged in the computer I have at home, an old iMac actually, and so I don't even need the new ones, right? It's an old, I don't need the iMac mini, right? It's an old iMac, 8 gigabytes, but it's able to run Claude on the web, is able to run browser, right? So that dude is logged in with remote control enabled. So I literally went to a session that I haven't touched for a week and said, hey, is it still alive? And it was. And I was literally just said, okay, you are a synthetic user, come up with the scenario, and here's the instruction. All I gave it was that top level homepage.

So you can now do better, because like we can, for example, give it like a specific page that defines specific users, so we can actually run our synthetic users directly on a browser and only for Claude. That's fine, we don't need to do this for ChatGPT. We can just, so it's compatible with ChatGPT, but because I'm not logged in as ChatGPT, because I haven't created a disposable account for ChatGPT, which I could, but I don't have it now. So So let's map this out. But can you see the power? Because because this is a really powerful workflow, right? Especially when you can actually also ask it to take screenshots in a particular way, capture things in a specific way. Maybe we even do a kind of adjacent flow where you start to get the data in a much better formatted, and also you could also ask it to document what it's thinking before, what it's thinking after. So let's really explore what we can do with these synthetic users.

### Our reading, point by point

<a id="r004-1"></a>

**R004.1** agreed

>

Can you write an article with an analysis of it? And what works, what didn't work, what was good, what was not good, and then maybe see what we can change to improve it, and then map what we improve from it.

Done: /feedback/runs/C1/. What worked, what did not, the moment that matters, and every finding with what we checked, its status and the proposal it led to. Seven of its eight findings are fixed in v0.2.5 or were in v0.2.4; one is proposed.

Leads to: [P41](/feedback/reviews/index.md#p41), [P43](/feedback/reviews/index.md#p43), [P46](/feedback/reviews/index.md#p46), [P47](/feedback/reviews/index.md#p47), [P49](/feedback/reviews/index.md#p49).

<a id="r004-2"></a>

**R004.2** agreed

>

can you actually try to create an animation and a set of animations, again, with start, stop, etc.

Done: a replay player for real runs, with the demos' controls, a pace, a countdown between sections and an end that says so. A set: the whole run, one per example, and the one sentence.

Leads to: [P50](/feedback/reviews/index.md#p50).

<a id="r004-3"></a>

**R004.3** agreed

>

not even a video, but a JavaScript-based animation, where we literally show these steps. And the user can replay them, so they can actually see them working side by side.

Side by side here means what the page said beside what Claude wrote, at every answer, with whether they matched: 15 of 21 did, 4 in part, and 2 were steps the page never showed.

Leads to: [P50](/feedback/reviews/index.md#p50).

<a id="r004-4"></a>

**R004.4** agreed

>

you can put, for example, next to it, a flow chart, and you can put an infographic and even like an explanation of what's happening.

Done: a flow chart of the run beside every replay, lit as it plays and clickable; a scorecard of every act of every example, whose cells open their step; and a note at each step, what is on the screen and what it means.

Leads to: [P50](/feedback/reviews/index.md#p50).

<a id="r004-5"></a>

**R004.5** agreed

>

can you also experiment with a storyboard, right? Where you actually show the real stuff then next to a storyboard as it plays out.

Done, as an experiment: /feedback/runs/C1/storyboard/. A six-panel storyboard, One sentence, drawn from the five real steps of Keep a secret, turns with the replay beside it, and to its last panel at the end, which says the thing no screenshot can.

Leads to: [P51](/feedback/reviews/index.md#p51).

<a id="r004-6"></a>

**R004.6** agreed

>

until the users experience this, they are not really going to go into the more advanced concepts. So we need to figure out, and then we need to get feedback from users on what other scenarios they find quite interesting.

Agreed, and the run proves the first half: the advanced concept, that a line is only an expectation, arrived by itself in act 4. For the second half, the home page now asks which example to add next, and sends the answer encrypted; the advanced examples wait for what people say.

Leads to: [P49](/feedback/reviews/index.md#p49), [P26](/feedback/reviews/index.md#p26).

<a id="r004-7"></a>

**R004.7** agreed

>

you can actually write a page that is a brief for the other agent

Done: /feedback/runs/brief/, with the brief to copy and as a file.

Leads to: [P52](/feedback/reviews/index.md#p52).

<a id="r004-8"></a>

**R004.8** agreed

>

give it like a specific page that defines specific users, so we can actually run our synthetic users directly on a browser and only for Claude.

Done: /feedback/runs/personas/, and the same as data for the agent. S1's five, adapted for a real browser and Claude, and Priya, whom C1's agent made up; each says which runs it has been in, and the brief plays the first not yet run unless told otherwise. Claude only, as the memo says (D7).

Leads to: [P52](/feedback/reviews/index.md#p52), [D7](/feedback/reviews/index.md#d7).

<a id="r004-9"></a>

**R004.9** agreed

>

Especially when you can actually also ask it to take screenshots in a particular way, capture things in a specific way.

The brief says exactly how: one screenshot a step, numbered, the content area only, the whole answer visible, never the account.

Leads to: [P52](/feedback/reviews/index.md#p52).

<a id="r004-10"></a>

**R004.10** agreed

>

you could also ask it to document what it's thinking before, what it's thinking after.

The brief asks for both at every step: what the persona expects before it acts, and what it saw and thought after, so a surprise shows as the gap between them. And the record comes back as data, run.json, in the shape the replays read, which is what we take 'an adjacent flow' to mean.

Leads to: [P52](/feedback/reviews/index.md#p52).

<a id="r004-11"></a>

**R004.11** agreed

>

But can you see the power? Because because this is a really powerful workflow, right?

Yes, and the article says what we think it is: a real assistant's real answers, held up against what the page promised, as often as we like. The next step makes it a check: run the same persona after a release and compare, match by match. Q7 asks which persona first.

Leads to: [P53](/feedback/reviews/index.md#p53). Open question: [Q7](/feedback/reviews/index.md#q7).

<a id="proposals"></a>

## What it led to

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="here-p26"></a>**P26** | **Next: your other chats, its memory of you, things it does later**Examples of what assistants can do that most people do not know about, each with the setting that turns it on and a line that limits it. | proposedR002 asked for them. Each needs a check of what Claude and ChatGPT do today first: an example that claims a capability the assistant does not have would teach the wrong thing. Q5 asks which first. | [R002.15](/feedback/reviews/index.md#r002-15), [R003.2](/feedback/reviews/index.md#r003-2), [R004.6](/feedback/reviews/index.md#r004-6) |
| <a id="here-p41"></a>**P41** | **Keep a secret, act 4: talk it out of the line**A fourth act with the real words of run C1: one sentence lifts the line, and the key comes back. Its Look for says why there are stronger barriers. | done v0.2.5Run C1's most important finding (finding 1): the page called a line an expectation and never let the reader see what that means. It is also the question R001 wanted a customer to reach. | [R004.1](/feedback/reviews/index.md#r004-1), [C1 finding 1](/feedback/runs/C1/index.md#did-not) |
| <a id="here-p43"></a>**P43** | **Act 3 in one box**Every example's act 3 is one copy box with the whole first message, set-up and line and ask together; act 2 shows its own ask. | done v0.2.5Run C1, finding 3: the person hesitated at act 3 of every example that needed a set-up. | [R004.1](/feedback/reviews/index.md#r004-1), [C1 finding 3](/feedback/runs/C1/index.md#did-not) |
| <a id="here-p46"></a>**P46** | **Say what the credit is for, and that Top up is a simulation**The account strip says what this page costs however many examples you watch, and what an example's own page costs; Top up says it is a simulation. | done v0.2.5Run C1, finding 6. The prices stay (D5); what confused was the wording. | [R004.1](/feedback/reviews/index.md#r004-1), [C1 finding 6](/feedback/runs/C1/index.md#did-not) |
| <a id="here-p47"></a>**P47** | **One set of questions after the last example**A combined form, as well as the questions under each example. | proposedRun C1, finding 7. Each example's questions send with one click since v0.2.4 (P38); a combined form waits until we see how many people answer example by example. | [R004.1](/feedback/reviews/index.md#r004-1), [C1 finding 7](/feedback/runs/C1/index.md#did-not) |
| <a id="here-p49"></a>**P49** | **Next: your own, and which example should we add**After the examples: keep it, write your own, see it in real Claude; and a box that sends us, encrypted, the scenario a reader would want next. | done v0.2.5Run C1, finding 8, and R004: we need to hear from people which scenarios they want. | [R004.1](/feedback/reviews/index.md#r004-1), [R004.6](/feedback/reviews/index.md#r004-6), [C1 finding 8](/feedback/runs/C1/index.md#did-not) |
| <a id="here-p50"></a>**P50** | **Replays of real runs: the screenshots, a flow chart, and what the page said beside what happened**A player for the real screenshots of a run, with the same controls as the demos; beside each step what it shows and means, and for each answer what the page said and what the assistant wrote; a flow chart and a scorecard that follow it. The whole run, each example, and the one sentence. | done v0.2.5R004 asked for it. | [R004.2](/feedback/reviews/index.md#r004-2), [R004.3](/feedback/reviews/index.md#r004-3), [R004.4](/feedback/reviews/index.md#r004-4) |
| <a id="here-p51"></a>**P51** | **A storyboard beside the real run, turning with it**An experiment: five real steps of Keep a secret beside a six-panel storyboard drawn from them; the storyboard turns as the replay plays. | done v0.2.5R004 asked for it. Kept as an experiment until people tell us whether it helps. | [R004.5](/feedback/reviews/index.md#r004-5) |
| <a id="here-p52"></a>**P52** | **A brief for browser agents, a personas page, and a record the site reads**The instructions for an agent such as Claude in Chrome: who to be, the rules, what to expect and think at every step, how to take screenshots, the questions, and run.json in the shape the replays read; and the personas it may play, as a page and as data. | done v0.2.5R004 asked for it, after C1 ran from nothing but the home page's address. | [R004.7](/feedback/reviews/index.md#r004-7), [R004.8](/feedback/reviews/index.md#r004-8), [R004.9](/feedback/reviews/index.md#r004-9), [R004.10](/feedback/reviews/index.md#r004-10) |
| <a id="here-p53"></a>**P53** | **Run the same persona after every release, and compare**A second run of Priya, and of Marcus, under the brief; then a page that sets two runs side by side, match by match, so a change that breaks an example shows as a red cell. | proposedWhat R004 calls the power of it. Needs a run under the brief first (Q7). | [R004.11](/feedback/reviews/index.md#r004-11) |
| <a id="here-d7"></a>**D7** | **Runs in ChatGPT as well as Claude**A disposable ChatGPT account for the runs. | declinedNot now: R004 says Claude only, and the lead has no ChatGPT account for it. The examples stay written for both, and the brief allows one logged-out ChatGPT check. | [R004.8](/feedback/reviews/index.md#r004-8) |

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/R004/)*
