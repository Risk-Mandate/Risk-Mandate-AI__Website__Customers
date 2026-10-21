# Review R003: Make the reviews easy to find, make the account big, and send to the agent, encrypted

> Dinis Cruz's review of customers.riskmandate.ai v0.2.3, Wednesday 21 October 2026, after v0.2.3 went live: the memo verbatim, our reading point by point with screenshots, and the proposals it led to.

*Source: <https://customers.riskmandate.ai/feedback/reviews/R003/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Review R003 · Dinis Cruz · site v0.2.3

# Make the reviews easy to find, make the account big, and send to the agent, encrypted

Dinis Cruz, Wednesday 21 October 2026, after v0.2.3 went live. A review of v0.2.3: the reviews, the account, the player and sending. The same review is in [the consolidated document](/feedback/reviews/index.md#r003), beside every other.

<a id="review"></a>

## R003: Make the reviews easy to find, make the account big, and send to the agent, encrypted

**Reviewer**
: Dinis Cruz, the lead of the programme
**Given**
: Wednesday 21 October 2026, after v0.2.3 went live
**Reviewing**
: site v0.2.3
**As**
: a voice memo, transcribed
**Status**
: a review of v0.2.3: the reviews, the account, the player and sending

- The memo is kept as transcribed, with paragraph breaks added. 'Eskito.ai' in the transcript is sgit.ai.
- The screenshots are of v0.2.3, the version reviewed, from the local copy of the live commit.

### The memo, verbatim

>

This is so much better. By the way, where's the review? I couldn't find it. So we need to make it easy to find. Also, can you start implementing those ideas? Because I think you've done quite a lot of them, but we need to be very big here. The account, right, of this, and so that we make it super clear of all that stuff we talked about their usage, what they've done, what they have, and all that information we have in local storage, right?

Now, one little thing here that I noticed, I love how now I go to that Hello World Assistant. The thing I noticed here is that it was playing without me noticing, and he arrived at that end bit. So I think that we need to, A, you should detect that to start playing only when the user scrolls to that page, if you can, but B, even in the end, you need to make it easy to start again, right, or something like that. So almost show that he got to the end step. Maybe you can have a little thing at the bottom or maybe at the top showing the steps, like as they play. One thing I feel that you want to do is, I think that the jump from step 9 to 10 is too great, and maybe we even stop there and maybe the user needs to continue, right? Because you kind of want to absorb that information. So either you have a little countdown before you continue, which it might not be a bad option, which allows me to stop also at the moment. Yeah, stop and pause. Yeah, so maybe that's the way you do it. You have a little countdown on that one with maybe some seconds to show. Do it small, but like, you know, like, oh, I'm going to go to the next page in 5 or 10 seconds. And then I can just go Also, the play, the back, at the moment, the back, when I'm in playing, should just go forward. At the moment, it doesn't, right? So it goes to the beginning. So take a look at that. But it's really cool, right?

And also, the send by email, can you take a look at Eskito.ai? And what should happen is you should create a vault here on this session. And this vault should have an append lane. And that append lane, you should put that on here. So you need to share the public key and the append lane key, which is fine for now. And is actually sent to us. So it should not be sent by email, should be sent to risk mandate agent, or even sent to, you know, even say sent to agent, and then maybe have a little link that says explain how it works in a new page. And you can even say encrypt and send, right? That's a nice thing. But also I like the copy my answers. That's also a good option.

And and the next page is quite nice, right? The storyboards. There's a little formatting, little problem on the second new to this bit. And by the way, I'm actually got an agent to run this on a separate environment, so we should get some feedback from it, which would be quite interesting.

### Our reading, point by point

<a id="r003-1"></a>

**R003.1** agreed

>

By the way, where's the review? I couldn't find it. So we need to make it easy to find.

Fair: at v0.2.3 the reviews were two menus deep, under The programme, and linked from one line at the foot of the home page. Now Reviews is its own menu, the home page has a band of the latest reviews with what each led to, and every page's footer links to them.

[![The menu at v0.2.3: no Reviews; the reviews were under The programme.](/assets/feedback/R003/04-header.webp)](/assets/feedback/R003/04-header.webp)
The menu at v0.2.3: no Reviews; the reviews were under The programme. / · 1280x900 · v0.2.3

Leads to: [P32](/feedback/reviews/index.md#p32).

<a id="r003-2"></a>

**R003.2** agreed

>

can you start implementing those ideas? Because I think you've done quite a lot of them, but we need to be very big here.

Started with what this memo names first: the account, the player and sending. Of the ideas still proposed, a storyboard per example (P25) and the advanced examples (P26) come next; the advanced ones wait on Q5, which of them first.

Leads to: [P25](/feedback/reviews/index.md#p25), [P26](/feedback/reviews/index.md#p26).

<a id="r003-3"></a>

**R003.3** agreed

>

The account, right, of this, and so that we make it super clear of all that stuff we talked about their usage, what they've done, what they have, and all that information we have in local storage, right?

Done. The account now opens with your balance and five counts: examples watched, played to the end, answered, sent to us, pages opened. Then each example (how far you got, what you said when you tried it, whether you sent it), what you sent and whether it went, where the credit went, everything you read, top-ups, and, last, every item this site keeps in your browser: its key, what it is, and what is in it, with Export everything and Delete everything.

[![The account at v0.2.3: the balance and the history, and nothing about the examples, the answers or the settings.](/assets/feedback/R003/05-account.webp)](/assets/feedback/R003/05-account.webp)
The account at v0.2.3: the balance and the history, and nothing about the examples, the answers or the settings. /account/ · 1280x900 · v0.2.3

Leads to: [P33](/feedback/reviews/index.md#p33).

<a id="r003-4"></a>

**R003.4** agreed

>

it was playing without me noticing, and he arrived at that end bit. So I think that we need to, A, you should detect that to start playing only when the user scrolls to that page

Done: a player starts by itself only after you have scrolled and the frame is at least 60% on screen, never on a page that has just opened. It plays once.

[![Hello world at v0.2.3, after it had played to the end on its own: step 12 of 12, and nothing saying it was the end.](/assets/feedback/R003/01-hello-world-ended.webp)](/assets/feedback/R003/01-hello-world-ended.webp)
Hello world at v0.2.3, after it had played to the end on its own: step 12 of 12, and nothing saying it was the end. /examples/hello-world/ · 1280x900 · v0.2.3

Leads to: [P34](/feedback/reviews/index.md#p34).

<a id="r003-5"></a>

**R003.5** agreed

>

even in the end, you need to make it easy to start again, right, or something like that. So almost show that he got to the end step. Maybe you can have a little thing at the bottom or maybe at the top showing the steps, like as they play.

Done: a bar of the steps across the top, one mark per step, grouped by act and clickable to jump; at the end a banner, 'The end of this example', with Start again and Now try it yourself; and the counter says 'Done: step 12 of 12'.

[![Hello world at v0.2.3, after it had played to the end on its own: step 12 of 12, and nothing saying it was the end.](/assets/feedback/R003/01-hello-world-ended.webp)](/assets/feedback/R003/01-hello-world-ended.webp)
Hello world at v0.2.3, after it had played to the end on its own: step 12 of 12, and nothing saying it was the end. /examples/hello-world/ · 1280x900 · v0.2.3

Leads to: [P35](/feedback/reviews/index.md#p35).

<a id="r003-6"></a>

**R003.6** agreed

>

So either you have a little countdown before you continue, which it might not be a bad option, which allows me to stop also at the moment.

Done: before each act after the first the player waits six seconds, saying what comes next ('Next: A new chat. The line goes first, in 6s'). Pause stops it there; Next skips the wait. We chose the countdown over stopping outright: a reader who is watching keeps the flow, and a reader who is reading gets the time.

Leads to: [P36](/feedback/reviews/index.md#p36).

<a id="r003-7"></a>

**R003.7** agreed in part

>

the back, when I'm in playing, should just go forward. At the moment, it doesn't, right? So it goes to the beginning.

We could not make it jump to the beginning: in v0.2.3, Back stepped back one and stopped. Two things could have looked like it: going back across the new chat brings the whole first chat back on screen, and the first button, Start again, sits where Back usually is. Now Back and Next keep playing if it was playing, and the step bar shows exactly where you are.

Leads to: [P37](/feedback/reviews/index.md#p37).

<a id="r003-8"></a>

**R003.8** agreed

>

And what should happen is you should create a vault here on this session. And this vault should have an append lane. And that append lane, you should put that on here. So you need to share the public key and the append lane key, which is fine for now.

Done: a vault made in this session on sgit.ai's host, with a feedback append lane, the way riskmandate.ai's contact form works. The public key and the lane's token are in /feedback/lane.json; the build's leak check allows that one token in that one file and nowhere else. Tested end to end: a send from Node and one from a real browser, both drained, opened and filed in the vault.

[![The questions' buttons at v0.2.3: Send by email and Copy my answers.](/assets/feedback/R003/02-quiz-send.webp)](/assets/feedback/R003/02-quiz-send.webp)
The questions' buttons at v0.2.3: Send by email and Copy my answers. /examples/hello-world/ · 1280x900 · v0.2.3

Leads to: [P38](/feedback/reviews/index.md#p38).

<a id="r003-9"></a>

**R003.9** agreed

>

So it should not be sent by email, should be sent to risk mandate agent, or even sent to, you know, even say sent to agent, and then maybe have a little link that says explain how it works in a new page. And you can even say encrypt and send, right?

Done: the button is 'Encrypt and send to the agent', with 'Exactly what will be sent' above it and 'How this works' beside it, a page of its own. Email appears only if sending fails. The feedback page has a box to write anything and send it the same way.

[![The questions' buttons at v0.2.3: Send by email and Copy my answers.](/assets/feedback/R003/02-quiz-send.webp)](/assets/feedback/R003/02-quiz-send.webp)
The questions' buttons at v0.2.3: Send by email and Copy my answers. /examples/hello-world/ · 1280x900 · v0.2.3

Leads to: [P38](/feedback/reviews/index.md#p38), [P39](/feedback/reviews/index.md#p39).

<a id="r003-10"></a>

**R003.10** agreed

>

But also I like the copy my answers. That's also a good option.

Kept, beside Encrypt and send.

Leads to: [P39](/feedback/reviews/index.md#p39).

<a id="r003-11"></a>

**R003.11** agreed

>

There's a little formatting, little problem on the second new to this bit.

Found: the card's label was inline, so when it wrapped, its second line lost the card's margin. Fixed.

[![New to this? at v0.2.3: the second card's label wraps, and its second line loses its margin.](/assets/feedback/R003/03-new-to-this.webp)](/assets/feedback/R003/03-new-to-this.webp)
New to this? at v0.2.3: the second card's label wraps, and its second line loses its margin. / · 1280x900 · v0.2.3

Leads to: [P40](/feedback/reviews/index.md#p40).

<a id="r003-12"></a>

**R003.12** asked of us

>

I'm actually got an agent to run this on a separate environment, so we should get some feedback from it

It can send its findings through the same lane: How this works has the call an agent makes. Whatever arrives is drained into the vault and, with the sender's yes, becomes a review here like this one.

Leads to: [P38](/feedback/reviews/index.md#p38).

<a id="proposals"></a>

## What it led to

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="here-p25"></a>**P25** | **A small storyboard for each example**Drawn with the storyboard kit, like what-is-an-abp: the scenario, the line, the refusal, the new chat. | proposedR002 suggested one. Proposed for after the lead has seen the examples as they are, so that the storyboards draw examples that have stopped changing. | [R002.8](/feedback/reviews/index.md#r002-8), [R003.2](/feedback/reviews/index.md#r003-2) |
| <a id="here-p26"></a>**P26** | **Next: your other chats, its memory of you, things it does later**Examples of what assistants can do that most people do not know about, each with the setting that turns it on and a line that limits it. | proposedR002 asked for them. Each needs a check of what Claude and ChatGPT do today first: an example that claims a capability the assistant does not have would teach the wrong thing. Q5 asks which first. | [R002.15](/feedback/reviews/index.md#r002-15), [R003.2](/feedback/reviews/index.md#r003-2) |
| <a id="here-p32"></a>**P32** | **Reviews you can find**Reviews is its own menu; the home page has a band of the latest reviews and what each led to; every footer links to them. | done v0.2.4R003: the reviews could not be found. | [R003.1](/feedback/reviews/index.md#r003-1) |
| <a id="here-p33"></a>**P33** | **The account: everything you did, and everything this browser keeps**Your balance and five counts; each example, how far you got, what you said, whether you sent it; what you sent; where the credit went; everything you read; top-ups; and every item kept in this browser, with what it is and what is in it, Export everything and Delete everything. | done v0.2.4R003: the account should make plain what a reader did and everything kept about it. | [R003.3](/feedback/reviews/index.md#r003-3) |
| <a id="here-p34"></a>**P34** | **A player starts only when you have scrolled to it**Never on a page that has just opened: only after a scroll, with the frame at least 60% on screen; once. | done v0.2.4R003: the example played to its end before it was noticed. | [R003.4](/feedback/reviews/index.md#r003-4) |
| <a id="here-p35"></a>**P35** | **A bar of the steps, and an end that says so**One mark per step, grouped by act, clickable; at the end, 'The end of this example' with Start again and Now try it yourself. | done v0.2.4R003: nothing said it had reached the end, or where it was. | [R003.5](/feedback/reviews/index.md#r003-5) |
| <a id="here-p36"></a>**P36** | **A countdown before each new act**Six seconds, saying what comes next; Pause stops it, Next skips it. | done v0.2.4R003: the jump into the third act came too soon to take in. | [R003.6](/feedback/reviews/index.md#r003-6) |
| <a id="here-p37"></a>**P37** | **Back and Next keep playing**If the player was playing, Back and Next move one step and it carries on. | done v0.2.4R003 found Back confusing while playing; see R003.7 for what we found. | [R003.7](/feedback/reviews/index.md#r003-7) |
| <a id="here-p38"></a>**P38** | **Encrypt and send: an encrypted lane to the agent**A vault on sgit.ai's host with a feedback append lane; the browser encrypts to its public key and appends with its public token; only the vault's key, held by RiskMandate, opens what arrives; admin/feedback/lane.mjs configures, tests and drains it. Agents can send the same way. | done v0.2.4R003 asked for it, after riskmandate.ai's contact form; it answers Q6. | [R003.8](/feedback/reviews/index.md#r003-8), [R003.9](/feedback/reviews/index.md#r003-9), [R003.12](/feedback/reviews/index.md#r003-12) |
| <a id="here-p39"></a>**P39** | **Encrypt and send to the agent, Copy, and How this works**The main button sends, encrypted; Copy stays; Exactly what will be sent is one click away; How this works is a page; email only if sending fails; a box on /feedback/ to send anything. | done v0.2.4R003 asked for it. | [R003.9](/feedback/reviews/index.md#r003-9), [R003.10](/feedback/reviews/index.md#r003-10) |
| <a id="here-p40"></a>**P40** | **The card label that wrapped**Card labels are blocks, so a wrapped line keeps its margin. | done v0.2.4R003 found it. | [R003.11](/feedback/reviews/index.md#r003-11) |

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/R003/)*
