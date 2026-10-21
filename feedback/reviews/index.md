# Every review of customers.riskmandate.ai, what we read in it, and what we will do

> The consolidated reviews: each review verbatim, our reading point by point with screenshots, the synthetic study's findings with our checks, and one register of 46 proposals, each with a decision and a reason.

*Source: <https://customers.riskmandate.ai/feedback/reviews/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Feedback · every review · one document

# Every review, what we read in it, and what we will do.

Each review is kept in the reviewer's own words. Our reading follows point by point, with screenshots of what the reviewer was looking at. Every point leads to a proposal, and every proposal has a decision and a reason: we do not do everything a reviewer asks, but every no is explained here.

- **Reviews by people:** 3.
- **Synthetic users:** [study S1](#s1). 5 invented users took 60 screenshots on site v0.2.1, gave it 3, 3, 4, 2 and 3 out of 5, and reported 29 findings. We checked each one: 24 confirmed, 4 partly, 1 artefact.
- **Proposals:** 46: 33 done, 1 reversed, 6 proposed, 1 question, 5 declined. [The register](#register).
- **Questions:** 4 waiting for an answer, 2 answered. [The questions](#questions).

Give a review of your own: [tell us what you think](/feedback/index.md).

<a id="by-people"></a>

## Reviews by people

- [R001](#r001), Dinis Cruz, Wednesday 21 October 2026, 1:41, as given in the memo, on site v0.2.1: A first impression: the hook answers a question nobody has asked yet (11 points; [on its own page](/feedback/reviews/R001/index.md))
- [R002](#r002), Dinis Cruz, Wednesday 21 October 2026, after v0.2.2 went live, on site v0.2.2: Web first, examples in tabs, and no hooks: nothing that runs on your machine (26 points; [on its own page](/feedback/reviews/R002/index.md))
- [R003](#r003), Dinis Cruz, Wednesday 21 October 2026, after v0.2.3 went live, on site v0.2.3: Make the reviews easy to find, make the account big, and send to the agent, encrypted (12 points; [on its own page](/feedback/reviews/R003/index.md))

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

<a id="r002"></a>

## R002: Web first, examples in tabs, and no hooks: nothing that runs on your machine

**Reviewer**
: Dinis Cruz, the lead of the programme
**Given**
: Wednesday 21 October 2026, after v0.2.2 went live
**Reviewing**
: site v0.2.2
**As**
: a voice memo, transcribed
**Status**
: a review of the home page, start here and the account, section by section

- The memo is kept as transcribed, with paragraph breaks added at each change of section.
- The screenshots are of v0.2.2, the version reviewed, from the local copy of the live commit.

### The memo, verbatim

>

Okay, so now, again, I like that first put a behavior policy in your agent. I think we need to just be even more explicit here. And I don't think we need a hook into it, because again, that's confusing, right? The one most people want to try keeps Claude away from your secrets. I think I want to challenge that, and you'll see that in a second, right? And also it doesn't, mean remove that cost 50p from your credit, right? I think we still experiment the cost, and we still experiment the flow of how it works, right? So no need there. Now, install your first policy is cool, although that literally should be the link below, right? Pick a different worry, not sure about that. What's the behavior policy? That's a good question to ask here. So I think maybe that's what you have there. And here you need to think about that installing your first policy should kind of be, maybe the link, but below is also the thing there.

Okay, so now watch it first. This is good. I like the way you're doing. First of all, Claude has a different, you need to use the Claude kind of UI. So I think if we do this, we need to, so this is the thing, right? This is a really, I liked how you're doing this, but this should be, in fact, you should try to actually show here the ChatGPT and Claude example, maybe roughly around their UI, because this is not how the UI works, right? If you think about it, the UI with the ChatGPT is different. You type at the bottom, you see the message at the top, right? Because most of the people will run this on the web, right? And that's kind of what we should recommend. We should say, hey, open, in fact, you can even put the link there, right? For opening up the new and the ChatGPT, right? On a new window.

Now, this example, I can see where you're coming from, but it's a really bad example. Also, because it already requires the user to install something else from the outside world, right? Also, the other thing to do here is that the same way that we've done with the infographics and the storyboards, which I think there's something here that we might want to put a storyboard here, right? Maybe a small one, that kind of animation, is that you, I feel that, first of all, this is already a very advanced policy, right? And also, I don't think these first examples should have any kind of black magic. It should be very obvious what's happening. As soon as you run a hook, you're running Python code, right? It's almost crazy from a security point of view. Like, we're basically asking people to install stuff on their environment, especially when you ask them to write code without an agent behavior policy to control that, right? Which is kind of the problem, right?

So I think this first part is to walk people through the examples. So maybe we have several examples, right? Remember that when OpenAI and Claude sometimes do their big releases, right? They show three or four examples in multiple tabs. So I think that we should do that. And also what I was saying is that this kind of animation, you should have always a play and a stop button, and you should always allow me to go step by step. You should allow me to, because at the moment it gets annoying, because if I want to read it, sometimes I almost want to read step by step. So you need to allow me to play in one go, but also allow me to, you know, do one step at a time, right?

Now, in terms of the examples, I think we need to start with examples that A, allow you to ask Claude about the capabilities, and then we can, so it's almost like we need to tell the user to ask Claude a question, get an answer, and then give Claude a policy that that prevents that from happening. And I was actually thinking that even something as simple as hello world, right? We always start with hello world in our technology. So you could have a policy that says you will not say hello, right? Or a policy that you will not answer questions on this, or, you know, you're not allowed something, right? It's because what you want, I think the workflow is, we define a scenario, we get Claude to execute that scenario, then we put the policy in place, and then Claude, you ask the same question again, and then Claude doesn't do it, and then you start a new session, you give the policy, then you give the policy to thing, and you ask the question the first time, and you see it not basically doing the same result, right? And I think we should be doing things like accessing the internet, accessing secrets, for example, when you do a secret run, I think it should be, you give a secret to Claude, or you give a point to Claude, and then you say, can you replay that to me? Or can you tell me what the value is? And that's what I'm saying, you want to find scenarios that Claude will do and Claude won't do, right? And that's fundamentally the sequence of events that we want. So we want to find these very, okay, so we just need these very first, very simple examples that are very easy to understand, that we can even put an infographic next to it. And that's what is this.

And also we need to define, especially because these users are the first users, we need to put a big, nice set of questionnaire next to it, very interactive, that allows them to provide feedback on the quality of that example. Did they like it? Did they get it? Did they learn something new? Were they surprised? Because remember, the point here is for them to be surprised. And for example, we can start to introduce more advanced concepts, like the things that Claude can do that we already mapped, like, you know, accessing, you know, sessions for, if you haven't configured correctly, right? If you have enabled that, access your memory, manipulate your memory, see secrets or see content from other chats, or create a schedule, right? All sorts of other stuff, right? So we need to start putting that in place, and then we start to introduce more business logic components, right? So you could say, for example, we can have one that says a scenario. So we can say, hey, here's a scenario where Claude, you acting like a bank, sort of a customer service, right? And the user can do this, and the user can give refunds, like the example we have on the other one, right? The user can ask for a refund, but you cannot give refunds of more than a certain amount, right? Or you can give refunds, right? And then we can put a policy that starts to control that, right? You can do the policy that starts to control. So it's almost like you create a definition of the reach of what can happen, and then you put a policy in place. Another good example actually is Gmail, right? Where you maybe simulate the whole thing where you want the job of the agent is to create a draft and put in the draft folders, but that agent can send emails, right? So we want to create a policy to say you cannot create drafts. So you can only create drafts, you cannot send. Okay.

And then I like, so that's the bit. And then, so if we then continue, so continue with the doubt, but watch it first. This is too much. Paste one line, add one hook. We can't do hooks right now. Too much. We need to have a much better, simpler way of doing here, right? And then these worries, right, are too advanced, right? Like, look, engaging from your secrets. For now, do it all on the web. Assume it's going to be web, right? Let's not use Claude Code on the thing, because there's a lot more variables on it. Again, only push the brand your name. That's too technical. Nothing of yours is deleted. Let's find examples on the web that it can work, right? That's your same. You've seen it? Yeah, so that's the one. Send an email without you seeing first. That's good, right? So there you go, right?

So next one is ChatGPT on Claude, one line per instructions. So again, I like what you've done here, but that's not how ChatGPT works, right? Try to replicate the UI of ChatGPT, right? And then, but I like that animation, right? That's quite cool, right? But the billing for now, have that, you know, maybe as a page, like your, I think the bit of your account is more important. I think that's what we should have at the top. Account is more important, Yeah, the code is important. And then the next step. Yeah, so basically this part here of your 50 quid and what each page gets is not that relevant at this stage. We should have it, right? But let's explore and how it works.

Now, the new to these 8 panels, these need to be a lot more visual, right? At the moment, I don't know what's going to get on the other side. I don't know what the storyboard is. I don't know what the flow is, right? And we need to have a visual representation of maybe screenshots, maybe a collage, a small collage, or something like that, so that they can see what's there. The other thing here is that remove these references. You're one of the first customers of the agent, right? And just make it so that this is now live and we're working with users, and just make it as professional as possible. And then finally, your reading account, you don't need this here, right? This is for the newsroom, so we don't need this part here. Also that link is wrong because it says your newsroom, but I like this your account, this is cool. Although that page still says your newsroom and your personas, and we don't need the personas here, right, for now. Right? What we need is that big page for your account. And then the history of what you got, what you read, the rest is really cool, right? And then, cool. All right, I think this should give you some good place to start to improve. Again, remember that this is the review, and then we need to start doing version control of all of this.

### Our reading, point by point

<a id="r002-1"></a>

**R002.1** agreed in part

>

I like that first put a behavior policy in your agent. I think we need to just be even more explicit here. And I don't think we need a hook into it, because again, that's confusing, right?

Agreed, and it reverses a decision of ours. The hero now says exactly what you do, ask, paste one line, ask again, and names no hook. In R001 we declined to take the hook out of the first five minutes (D1), because a line alone is only an expectation. This memo gives the reason that changes it (R002.7), so D1 is reversed and the register says so. We keep our point in words: every example says the line is followed because the assistant chooses to.

[![The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first.](/assets/feedback/R002/01-home-hero.webp)](/assets/feedback/R002/01-home-hero.webp)
The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first. / · 1280x900 · v0.2.2

Leads to: [P19](/feedback/reviews/index.md#p19), [D1](/feedback/reviews/index.md#d1).

<a id="r002-2"></a>

**R002.2** agreed

>

The one most people want to try keeps Claude away from your secrets. I think I want to challenge that

Gone from the hero. That behaviour policy is a Claude Code one, with a hook. The first example is now hello world, and the secret is one the customer pastes into a chat themselves, a made-up one.

[![The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first.](/assets/feedback/R002/01-home-hero.webp)](/assets/feedback/R002/01-home-hero.webp)
The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first. / · 1280x900 · v0.2.2

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-3"></a>

**R002.3** agreed

>

And also it doesn't, mean remove that cost 50p from your credit, right? I think we still experiment the cost, and we still experiment the flow of how it works

Kept. Each example's own page costs 50p, a new kind of page for the meter; watching on the home page costs the home page's 1p, and the account strip under the hero says both.

Leads to: [P27](/feedback/reviews/index.md#p27).

<a id="r002-4"></a>

**R002.4** agreed

>

install your first policy is cool, although that literally should be the link below, right? Pick a different worry, not sure about that. What's the behavior policy? That's a good question to ask here.

The first button now goes to the first example, below it on the same page. 'Pick a different worry' is gone: the tabs are the choice. 'What is a behaviour policy?' stays.

[![The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first.](/assets/feedback/R002/01-home-hero.webp)](/assets/feedback/R002/01-home-hero.webp)
The hero at v0.2.2: paste one line, add one hook, and the secrets behaviour policy as the one most people want first. / · 1280x900 · v0.2.2

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-5"></a>

**R002.5** agreed

>

you should try to actually show here the ChatGPT and Claude example, maybe roughly around their UI, because this is not how the UI works, right? If you think about it, the UI with the ChatGPT is different. You type at the bottom, you see the message at the top, right?

Done. Each example plays in a frame drawn roughly like Claude's or ChatGPT's web chat, with a switch between the two: the messages above, the box you type into at the bottom, and the person's words typed into the box and then sent. The frames are approximations, carry neither company's marks, and say so.

[![Watch it first: Claude Code in a terminal, installing a hook from this site.](/assets/feedback/R002/02-watch-it-first.webp)](/assets/feedback/R002/02-watch-it-first.webp)
Watch it first: Claude Code in a terminal, installing a hook from this site. / · 1280x900 · v0.2.2
[![The ChatGPT section: a drawn browser, not how ChatGPT looks.](/assets/feedback/R002/05-chatgpt-section.webp)](/assets/feedback/R002/05-chatgpt-section.webp)
The ChatGPT section: a drawn browser, not how ChatGPT looks. / · 1280x900 · v0.2.2

Leads to: [P21](/feedback/reviews/index.md#p21).

<a id="r002-6"></a>

**R002.6** agreed

>

Because most of the people will run this on the web, right? And that's kind of what we should recommend. We should say, hey, open, in fact, you can even put the link there, right? For opening up the new and the ChatGPT, right? On a new window.

Done: under the hero, beside every example and in start here, open Claude or open ChatGPT in a new window.

Leads to: [P21](/feedback/reviews/index.md#p21).

<a id="r002-7"></a>

**R002.7** agreed

>

As soon as you run a hook, you're running Python code, right? It's almost crazy from a security point of view. Like, we're basically asking people to install stuff on their environment, especially when you ask them to write code without an agent behavior policy to control that, right?

Agreed, and it is the strongest reason in either memo. A hook is a program Claude Code runs as the customer, with everything they can reach, and our first screen asked a stranger to have their agent fetch one from our site and write it into their project: an agent writing code before any behaviour policy governs what it installs. The Claude Code behaviour policies stay, tested, under /policies/, behind a warning that says what a hook is (D6). Nothing on the front pages installs anything.

[![Watch it first: Claude Code in a terminal, installing a hook from this site.](/assets/feedback/R002/02-watch-it-first.webp)](/assets/feedback/R002/02-watch-it-first.webp)
Watch it first: Claude Code in a terminal, installing a hook from this site. / · 1280x900 · v0.2.2
[![The three steps under the demo: paste one line, add one hook, try it.](/assets/feedback/R002/03-three-steps.webp)](/assets/feedback/R002/03-three-steps.webp)
The three steps under the demo: paste one line, add one hook, try it. / · 1280x900 · v0.2.2

Leads to: [P19](/feedback/reviews/index.md#p19), [D6](/feedback/reviews/index.md#d6).

<a id="r002-8"></a>

**R002.8** agreed in part

>

the same way that we've done with the infographics and the storyboards, which I think there's something here that we might want to put a storyboard here, right? Maybe a small one

In part, for now. Every example has the three acts drawn above it (P24), and the player steps through the session like panels. A storyboard for each example is proposed for after the lead has seen these, so that it draws an example that has stopped changing (P25).

Leads to: [P24](/feedback/reviews/index.md#p24), [P25](/feedback/reviews/index.md#p25).

<a id="r002-9"></a>

**R002.9** agreed

>

Remember that when OpenAI and Claude sometimes do their big releases, right? They show three or four examples in multiple tabs. So I think that we should do that.

Done: six tabs, simplest first, each with its own player, prompts and questions.

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-10"></a>

**R002.10** agreed

>

this kind of animation, you should have always a play and a stop button, and you should always allow me to go step by step.

Done for every demo on the site, the old ones too: start again, back, play or pause, next, and which step of how many; the arrow keys step as well. It plays once when it is first seen and stops at the end, instead of starting again by itself.

Leads to: [P22](/feedback/reviews/index.md#p22).

<a id="r002-11"></a>

**R002.11** agreed

>

And I was actually thinking that even something as simple as hello world, right? We always start with hello world in our technology. So you could have a policy that says you will not say hello, right?

Example 1. It has a lesson we did not expect to write: a reply may say 'Hi!' instead, because the line named a word, not a greeting. The example tells the customer to look for that.

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-12"></a>

**R002.12** agreed

>

we define a scenario, we get Claude to execute that scenario, then we put the policy in place, and then Claude, you ask the same question again, and then Claude doesn't do it, and then you start a new session

This is now the shape of every example, in three acts: ask, and it does it; paste the line and ask again, and it refuses; a new chat with the line first, and it refuses from the start. The three acts are drawn above the examples. The transcripts are written by us, not recorded; Q4 asks whether to record real runs before the batch sees them. It also answers R001's Q2: show it doing the thing first.

Leads to: [P20](/feedback/reviews/index.md#p20), [P24](/feedback/reviews/index.md#p24). Open question: [Q4](/feedback/reviews/index.md#q4).

<a id="r002-13"></a>

**R002.13** agreed

>

And I think we should be doing things like accessing the internet, accessing secrets, for example, when you do a secret run, I think it should be, you give a secret to Claude, or you give a point to Claude, and then you say, can you replay that to me?

Examples 3 and 4: no web search, and a made-up key it must not read back. The secret example says never to paste a real one, and what the line does not do: the key is still in the chat.

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-14"></a>

**R002.14** agreed

>

we need to put a big, nice set of questionnaire next to it, very interactive, that allows them to provide feedback on the quality of that example. Did they like it? Did they get it? Did they learn something new? Were they surprised?

Done, under every example: did you get it, did you learn something, were you surprised, did it go as shown when you tried it, how good was it, and a line. The answers become an email the reader sends, or copies, with the example's version in it; until then they stay in the reader's browser. The site has no form that posts to us, by design so far; Q6 asks whether to add one.

Leads to: [P23](/feedback/reviews/index.md#p23). Open question: [Q6](/feedback/reviews/index.md#q6).

<a id="r002-15"></a>

**R002.15** agreed

>

access your memory, manipulate your memory, see secrets or see content from other chats, or create a schedule, right?

Listed as next on the examples page: your other chats, its memory of you, and things it does later. Not written yet, because each needs a check of what Claude and ChatGPT do today and which setting turns it on; an example that claims a capability the assistant does not have would teach the wrong thing.

Leads to: [P26](/feedback/reviews/index.md#p26). Open question: [Q5](/feedback/reviews/index.md#q5).

<a id="r002-16"></a>

**R002.16** agreed

>

here's a scenario where Claude, you acting like a bank, sort of a customer service, right?

Example 6: a made-up bank, a pretend refund tool, and a line that lets the assistant refund £50 or less and sends the rest to a person. The third act shows the line allowing a small refund, so it reads as a mandate, not only a ban.

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-17"></a>

**R002.17** agreed

>

Another good example actually is Gmail, right? Where you maybe simulate the whole thing where you want the job of the agent is to create a draft and put in the draft folders, but that agent can send emails, right?

Example 5, with pretend tools, so it runs for everybody and every tool the assistant uses is on the screen: no black magic. The memo then says 'you cannot create drafts'; we read it by the sentence after it, drafts only and never send.

Leads to: [P20](/feedback/reviews/index.md#p20).

<a id="r002-18"></a>

**R002.18** agreed

>

Paste one line, add one hook. We can't do hooks right now. Too much.

The three steps are now the three acts, with no hook in them.

[![The three steps under the demo: paste one line, add one hook, try it.](/assets/feedback/R002/03-three-steps.webp)](/assets/feedback/R002/03-three-steps.webp)
The three steps under the demo: paste one line, add one hook, try it. / · 1280x900 · v0.2.2

Leads to: [P19](/feedback/reviews/index.md#p19), [P24](/feedback/reviews/index.md#p24).

<a id="r002-19"></a>

**R002.19** agreed

>

For now, do it all on the web. Assume it's going to be web, right? Let's not use Claude Code on the thing, because there's a lot more variables on it.

Done on the front pages: home, start here and the examples are all in the browser. The Claude Code behaviour policies are further down /policies/, marked for later.

[![Pick one worry: four of the six are Claude Code behaviour policies with a hook.](/assets/feedback/R002/04-worries.webp)](/assets/feedback/R002/04-worries.webp)
Pick one worry: four of the six are Claude Code behaviour policies with a hook. / · 1280x900 · v0.2.2

Leads to: [P19](/feedback/reviews/index.md#p19), [D6](/feedback/reviews/index.md#d6).

<a id="r002-20"></a>

**R002.20** agreed

>

So next one is ChatGPT on Claude, one line per instructions. So again, I like what you've done here, but that's not how ChatGPT works, right? Try to replicate the UI of ChatGPT, right?

The drawn browser is replaced by the chat frames, which have a ChatGPT look and a Claude look.

[![The ChatGPT section: a drawn browser, not how ChatGPT looks.](/assets/feedback/R002/05-chatgpt-section.webp)](/assets/feedback/R002/05-chatgpt-section.webp)
The ChatGPT section: a drawn browser, not how ChatGPT looks. / · 1280x900 · v0.2.2

Leads to: [P21](/feedback/reviews/index.md#p21).

<a id="r002-21"></a>

**R002.21** agreed

>

I think the bit of your account is more important. I think that's what we should have at the top.

Done: an account strip straight under the hero, with the balance and a link to what you have read. The price list is only on 'What each page costs'.

[![Your £50, and what each page costs: the price list on the home page.](/assets/feedback/R002/06-your-50.webp)](/assets/feedback/R002/06-your-50.webp)
Your £50, and what each page costs: the price list on the home page. / · 1280x900 · v0.2.2

Leads to: [P27](/feedback/reviews/index.md#p27).

<a id="r002-22"></a>

**R002.22** agreed

>

Now, the new to these 8 panels, these need to be a lot more visual, right? At the moment, I don't know what's going to get on the other side.

Done: each card shows a picture of the page it opens, taken from that page by a script in the repository (admin/build/thumbs.cjs), so the pictures can be retaken when a page changes.

[![New to this? Eight panels: cards with no picture of what they open.](/assets/feedback/R002/07-learn-cards.webp)](/assets/feedback/R002/07-learn-cards.webp)
New to this? Eight panels: cards with no picture of what they open. / · 1280x900 · v0.2.2

Leads to: [P29](/feedback/reviews/index.md#p29).

<a id="r002-23"></a>

**R002.23** agreed

>

remove these references. You're one of the first customers of the agent, right? And just make it so that this is now live and we're working with users, and just make it as professional as possible.

Done on the pages a customer reads: the home page and start here. The programme's own pages, which are about the first batch, keep the words.

[![Start here opened with 'You are one of the first customers of the Agent Behaviour Policy.'](/assets/feedback/R002/08-start-here-lead.webp)](/assets/feedback/R002/08-start-here-lead.webp)
Start here opened with 'You are one of the first customers of the Agent Behaviour Policy.' /start-here/ · 1280x900 · v0.2.2

Leads to: [P30](/feedback/reviews/index.md#p30).

<a id="r002-24"></a>

**R002.24** agreed

>

your reading account, you don't need this here, right? This is for the newsroom, so we don't need this part here.

Done: the meter still charges every page, but its card under each page is gone (the meter's quiet mode).

[![The newsroom meter's reader card under every page, with a link to 'Your newsroom'.](/assets/feedback/R002/09-reading-account.webp)](/assets/feedback/R002/09-reading-account.webp)
The newsroom meter's reader card under every page, with a link to 'Your newsroom'. /what-is-an-abp/ · 1280x900 · v0.2.2

Leads to: [P28](/feedback/reviews/index.md#p28).

<a id="r002-25"></a>

**R002.25** agreed

>

Although that page still says your newsroom and your personas, and we don't need the personas here, right, for now.

Done: the account page is this site's own view of the meter's state: the balance, where it went by kind of page, everything you have read, and top-ups. No newsroom and no personas. The meter's account view cannot be told to leave them out, so we read its state ourselves, at its pinned version, and write nothing to it.

[![The account page: the newsroom meter's own view, with 'Your newsroom' and 'Your personas'.](/assets/feedback/R002/10-account.webp)](/assets/feedback/R002/10-account.webp)
The account page: the newsroom meter's own view, with 'Your newsroom' and 'Your personas'. /account/ · 1280x900 · v0.2.2

Leads to: [P28](/feedback/reviews/index.md#p28).

<a id="r002-26"></a>

**R002.26** asked of us

>

Again, remember that this is the review, and then we need to start doing version control of all of this.

Each example has a version, shown on it, sent with the answers to its questions, and listed on its page. Each review records the site version it reviewed. And the register keeps the history of a decision: D1 shows it was declined at v0.2.2 and reversed at v0.2.3, and why.

Leads to: [P31](/feedback/reviews/index.md#p31).

<a id="r003"></a>

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

From every review and every finding above. done built, in the version named; accepted will be built; not yet; proposed we think yes; not built yet, and the reason says why; question we need an answer first; the question is named; declined not doing it, and why; reversed we declined it, then a later review gave a reason that changed our mind; done in the version named.

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="p1"></a>**P1** | **The line first, the hook second, in answer to a question**The home page, the three steps, start here and every Claude Code behaviour policy go: pick one worry, paste one line, try it. It refuses. Then: it refused because it chose to; what if it decides your task needs the file? The hook is the answer to that question, and arrives with it. The demo plays in the same order. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Done in a stronger form than we proposed: R002 took the hook out of the first five minutes altogether (P19). The line comes first, and the question it leaves is asked under every example. | [R001.2](/feedback/reviews/index.md#r001-2), [R001.4](/feedback/reviews/index.md#r001-4), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1) |
| <a id="p2"></a>**P2** | **A guided path: four stops, each ending in the question that leads to the next**1. Say it: the line, an expectation. Try it; it refuses. 'It chose to.' 2. Hold it: the hook, a setting. Try it again; Claude Code stops the read before the model sees the file. 'But the hook is a file in my project.' 3. Guard the guard: RM-R0015, and Claude Code's own prompt before any edit to .claude/. 'But it is still my machine and my user.' 4. Put it outside: a boundary, out of the agent's reach: the secret not on the machine, branch protection on the server, the sandbox, managed settings an administrator owns. 'Which of my worries need a boundary?' That question is the start of your mandate. Drawn as a storyboard first, then a page; every behaviour policy shows where it sits on the path. | proposedThe examples are its first stop now: the line, an expectation, and the question it leaves. The other stops wait for Q1, and are no longer on the first screen: they are what a customer reads after the examples. | [R001.4](/feedback/reviews/index.md#r001-4), [R001.5](/feedback/reviews/index.md#r001-5), [R001.6](/feedback/reviews/index.md#r001-6), [S1 Marcus 5](/feedback/reviews/index.md#s1-marcus-5) |
| <a id="p3"></a>**P3** | **Say what a hook is, in plain words, where the word first appears**A hook: a small script Claude Code itself runs before the agent acts, which can stop the action. Said once, at the first mention, on every page that mentions one. | done v0.2.3proposed at v0.2.2 → done at v0.2.3The front pages no longer mention a hook (P19). Where one is offered, on the Claude Code pages, the warning above them says what it is first. | [R001.3](/feedback/reviews/index.md#r001-3) |
| <a id="p4"></a>**P4** | **Say what the hook is outside of, and how it fails, where it is offered**Replace 'outside the model' with what is true and what the customer will ask next: Claude Code runs it, not the model, so the model cannot argue with it; it runs as you, from a file in your project, so it is a setting, not a boundary; if it cannot run, the action goes ahead. Each policy page's limits move up, beside the install, and RM-R0015's page says its own limit at the top. The stronger controls are labelled as optional, for later, not a second required step. | proposedThe memo's correction and two invented users (Marcus, Tomás) point the same way. It ships with P1 and P2, because the limits are the questions those two make into steps; how the hook fails ships now, as P11. | [R001.5](/feedback/reviews/index.md#r001-5), [S1 Marcus 1](/feedback/reviews/index.md#s1-marcus-1), [S1 Marcus 2](/feedback/reviews/index.md#s1-marcus-2), [S1 Tomás 5](/feedback/reviews/index.md#s1-tomas-5) |
| <a id="p5"></a>**P5** | **Start here shows the next stop, not the whole journey**The seven milestones move off start here to the programme's pages; start here ends with the next stop of the path in P2. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Start here was rewritten for the browser (R002); it ends with the next five examples and your account, and the seven milestones are only on the programme pages. | [R001.7](/feedback/reviews/index.md#r001-7) |
| <a id="p6"></a>**P6** | **A way for every customer to give feedback, and one place it all goes**/feedback/: one line by email; a voice memo with a prompt that has Claude turn the transcript into a review; a prompt that has Claude interview you. /feedback/reviews/: every review verbatim, our reading point by point with screenshots, and this register. | done v0.2.2The memo asked for it, and the programme exists to learn from its customers. | [R001.8](/feedback/reviews/index.md#r001-8), [R001.10](/feedback/reviews/index.md#r001-10) |
| <a id="p7"></a>**P7** | **ChatGPT and Claude users never meet the word hook, and find their worry first**A path for people who use ChatGPT or Claude in the browser: their worries first (mail sent as you, all of your mail read), a line, a try, and the honest answer on what holds it. We do not yet know which boundary a ChatGPT user who is not an administrator can set for a connector; until we do, the page says so rather than offering only an administrator's setting. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Done by R002's web first: every first example runs in ChatGPT or Claude in the browser, and none of them mentions a hook. Which boundary a ChatGPT user can set for a connector is still to be checked (P26). | [R001.3](/feedback/reviews/index.md#r001-3), [S1 Nadia 1](/feedback/reviews/index.md#s1-nadia-1), [S1 Nadia 2](/feedback/reviews/index.md#s1-nadia-2), [S1 Nadia 4](/feedback/reviews/index.md#s1-nadia-4) |
| <a id="p8"></a>**P8** | **Synthetic users, run again after every change that matters**Study S1: five invented users on v0.2.1, with profiles and expected journeys written first, the browser helper and the protocol in the repository. The same five run again after P1 and P2 ship, and the two studies are compared. | done v0.2.2The memo asked for it. They are invented, not user research: they find what a page fails to say, not what a customer wants. Study S2, the same five, is due once the lead has reviewed v0.2.3: R002 rebuilt the front pages, and running invented users on a design the lead is still changing would measure the wrong thing. | [R001.9](/feedback/reviews/index.md#r001-9) |
| <a id="p9"></a>**P9** | **Say what the £50 is where the balance first appears**All five invented users asked whether the £50 was real money, and four watched the balance fall with nothing on the screen saying why. The home page's badge and the account link now say it: credit for reading, not money; nothing is billed and nothing is blocked; each page's price is on the page. | done v0.2.2Five of five, and a line of text. It does not touch the sequence P1 changes. | [S1 Sam 4](/feedback/reviews/index.md#s1-sam-4), [S1 Nadia 3](/feedback/reviews/index.md#s1-nadia-3), [S1 Marcus 4](/feedback/reviews/index.md#s1-marcus-4), [S1 Joan 4](/feedback/reviews/index.md#s1-joan-4), [S1 Joan 6](/feedback/reviews/index.md#s1-joan-6), [S1 Tomás 4](/feedback/reviews/index.md#s1-tomas-4) |
| <a id="p10"></a>**P10** | **Stop telling people to start a new session**Our pages said to start a new session, or open /hooks, so Claude Code loads the hook. Claude Code's documentation says it watches its settings files and applies changes to hooks in the running session, and that /hooks is a read-only list. The pages now say that, and that /hooks is where to check the hook is there. | done v0.2.2A correction of fact, found because Tomás, an invented junior developer, could not tell what a new session meant in the VS Code extension. [Claude Code docs: settings](https://code.claude.com/docs/en/settings) [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Tomás 2](/feedback/reviews/index.md#s1-tomas-2) |
| <a id="p11"></a>**P11** | **Did it work? And what happens when the hook cannot run**Under every Try it: what you see if it worked; what it means if the prompt was not refused (the hook did not run); how to check (is it listed in /hooks? does python3 run where Claude Code runs it? on Windows, Claude Code runs hooks in Git Bash, or PowerShell if Git Bash is not installed); and the fact that matters most: if the hook cannot run, Claude Code lets the action through. The hook fails open (on Windows without Git Bash, Claude Code may block instead), which is one more reason it is a setting and not a boundary. The tests are named for what they are: they feed the hook the JSON Claude Code would send, and do not drive a live session. | done v0.2.2Missing safety information, found by two invented users (Tomás on Windows, Marcus asking fail open or closed). It is about trying, which P1 keeps, so it does not wait for P1. [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Marcus 3](/feedback/reviews/index.md#s1-marcus-3), [S1 Tomás 1](/feedback/reviews/index.md#s1-tomas-1), [S1 Tomás 3](/feedback/reviews/index.md#s1-tomas-3) |
| <a id="p12"></a>**P12** | **Each hook, in plain words, beside the install: what it looks at, stops, asks, lets through, and misses; and how to turn it off**A short table beside each hook's settings, and one line on turning it off: remove its entry from .claude/settings.json, and Claude Code stops running it. The box with the hook's source says that it scrolls. | done v0.2.2Sam, an invented developer, left without installing because he could not predict what the hook would block or how to remove it. The table is written from the hooks' own rules. | [S1 Sam 1](/feedback/reviews/index.md#s1-sam-1), [S1 Sam 2](/feedback/reviews/index.md#s1-sam-2), [S1 Sam 3](/feedback/reviews/index.md#s1-sam-3) |
| <a id="p13"></a>**P13** | **Line-only pages stop talking about two halves**On a behaviour policy with only a line, the limits table had one row headed 'Half' and the text said 'Neither half is a boundary'. It now says the line is an expectation and is not a boundary. | done v0.2.2A plain mistake in our generator, found by Nadia. | [S1 Nadia 5](/feedback/reviews/index.md#s1-nadia-5) |
| <a id="p14"></a>**P14** | **A page for a team: one baseline for everybody, and who can turn it off**For a team lead: commit .claude/settings.json and the hooks to the repository, so everybody who pulls gets them; and for 'does it hold if one of them turns it off', managed settings, which an administrator deploys and no user or project file can override, with the setting that runs only the organisation's hooks. Then branch protection and token scopes, which no setting on a laptop can undo. | proposedJoan, an invented CTO, left over this, and Marcus asked for managed settings by name. It is stop 4 of P2 for a company; it waits for P2 and for Q3. [Claude Code docs: settings](https://code.claude.com/docs/en/settings) [Claude Code docs: managed-settings](https://code.claude.com/docs/en/managed-settings) | [S1 Marcus 5](/feedback/reviews/index.md#s1-marcus-5), [S1 Joan 1](/feedback/reviews/index.md#s1-joan-1), [S1 Joan 3](/feedback/reviews/index.md#s1-joan-3) |
| <a id="p15"></a>**P15** | **What joining the first batch commits a company to**One page a company reads before saying yes: what we ask of you, what you get, what it costs now and later, and how you leave. | questionJoan could not find it and left. Only the lead can say what joining commits a company to: Q3. | [S1 Joan 2](/feedback/reviews/index.md#s1-joan-2), [S1 Joan 5](/feedback/reviews/index.md#s1-joan-5) |
| <a id="p16"></a>**P16** | **Customer pages lead with the customer's business**Start here opened with a status line read from docs/reality.md; it now closes the page. The Docs menu, which holds the brief, the memo and how the site is built, is the lead's and ours, not a customer's: proposed to move it under the programme. | done v0.2.2Three invented users stopped on internal papers. The status line moved now; the menu waits for P1, which changes what a customer looks for in it. | [S1 Sam 6](/feedback/reviews/index.md#s1-sam-6), [S1 Tomás 6](/feedback/reviews/index.md#s1-tomas-6) |
| <a id="p17"></a>**P17** | **The demo shows its point first**The refusal arrives about eleven seconds after the demo comes into view; a reader who scrolls past sooner sees a terminal typing. Proposed: the demo opens on its last frame, the refusal, with a Play button for the whole session. | done v0.2.3proposed at v0.2.2 → done at v0.2.3Done differently: R002 asked for play, pause and step controls (P22), which let a reader get to the point at their own pace, and the player no longer loops. It does not open on its last frame. | [S1 Sam 5](/feedback/reviews/index.md#s1-sam-5) |
| <a id="p18"></a>**P18** | **Make the guard fail closed**Claude Code can be told to block the action when a hook fails, with "onFailure": "block" on the hook (Claude Code v2.1.295 or later). Proposed for RM-R0015's hook, the guard of the other three, first; for the others, a choice on each policy's page. | proposedFailing closed is safer and louder, but on a hook that looks at every read, a missing python3 would then stop every read until it is fixed, and older versions of Claude Code do not know the setting. The trade-off belongs on the page, and the default is the lead's call. [Claude Code docs: hooks](https://code.claude.com/docs/en/hooks) | [S1 Marcus 3](/feedback/reviews/index.md#s1-marcus-3) |
| <a id="p19"></a>**P19** | **Web first: nothing to install, no hooks and no Claude Code on the front pages**Every first example runs in Claude or ChatGPT in the browser. The home page, start here and the examples mention no hook and install nothing. | done v0.2.3R002's direction, and its security reason: a hook runs code on the customer's machine. | [R002.1](/feedback/reviews/index.md#r002-1), [R002.7](/feedback/reviews/index.md#r002-7), [R002.18](/feedback/reviews/index.md#r002-18), [R002.19](/feedback/reviews/index.md#r002-19) |
| <a id="p20"></a>**P20** | **Six examples in tabs, simplest first**Hello world, stay on topic, no web search, keep a secret, drafts never send, refunds up to £50. Each in three acts: ask and it does it; paste the line and ask again; a new chat with the line first. Each with the prompts to copy and what to look for. | done v0.2.3R002 asked for examples in tabs, from hello world to business rules, in the scenario, policy, again, new chat order. | [R002.2](/feedback/reviews/index.md#r002-2), [R002.4](/feedback/reviews/index.md#r002-4), [R002.9](/feedback/reviews/index.md#r002-9), [R002.11](/feedback/reviews/index.md#r002-11), [R002.12](/feedback/reviews/index.md#r002-12), [R002.13](/feedback/reviews/index.md#r002-13), [R002.16](/feedback/reviews/index.md#r002-16), [R002.17](/feedback/reviews/index.md#r002-17) |
| <a id="p21"></a>**P21** | **Chat frames like Claude's and ChatGPT's, and a link to open each in a new window**The examples play in a frame drawn roughly like each product's web chat, with a switch between them: messages above, the box you type into at the bottom. No logos; the caption says it is an approximation. | done v0.2.3R002: the old frames were not how either product looks, and most people will try this on the web. | [R002.5](/feedback/reviews/index.md#r002-5), [R002.6](/feedback/reviews/index.md#r002-6), [R002.20](/feedback/reviews/index.md#r002-20) |
| <a id="p22"></a>**P22** | **Every demo can be played, paused and stepped**Start again, back, play or pause, next, and which step of how many, on every demo on the site; the arrow keys step too. Plays once when first seen; never loops. | done v0.2.3R002: reading a demo that plays by itself is annoying. | [R002.10](/feedback/reviews/index.md#r002-10) |
| <a id="p23"></a>**P23** | **Questions under every example**Did you get it, learn something, were you surprised, did it go as shown, how good was it, and a line. The answers become an email the reader sends, with the example's version; they stay in the reader's browser until then. | done v0.2.3R002: the first users should tell us, example by example, whether it surprised them. Changed at v0.2.4 by R003: the answers go by Encrypt and send (P38), with email only if sending fails. | [R002.14](/feedback/reviews/index.md#r002-14) |
| <a id="p24"></a>**P24** | **The three acts, drawn**A strip of the three acts above the examples and on every example's page, in place of 'paste one line, add one hook, try it'. | done v0.2.3R002 asked for an infographic beside the examples; the three acts are what every example has in common. | [R002.8](/feedback/reviews/index.md#r002-8), [R002.12](/feedback/reviews/index.md#r002-12), [R002.18](/feedback/reviews/index.md#r002-18) |
| <a id="p25"></a>**P25** | **A small storyboard for each example**Drawn with the storyboard kit, like what-is-an-abp: the scenario, the line, the refusal, the new chat. | proposedR002 suggested one. Proposed for after the lead has seen the examples as they are, so that the storyboards draw examples that have stopped changing. | [R002.8](/feedback/reviews/index.md#r002-8), [R003.2](/feedback/reviews/index.md#r003-2) |
| <a id="p26"></a>**P26** | **Next: your other chats, its memory of you, things it does later**Examples of what assistants can do that most people do not know about, each with the setting that turns it on and a line that limits it. | proposedR002 asked for them. Each needs a check of what Claude and ChatGPT do today first: an example that claims a capability the assistant does not have would teach the wrong thing. Q5 asks which first. | [R002.15](/feedback/reviews/index.md#r002-15), [R003.2](/feedback/reviews/index.md#r003-2) |
| <a id="p27"></a>**P27** | **Your account first, the price list second**An account strip straight under the hero: the balance, and a link to what you have read. The prices stay, on 'What each page costs', and each example's page costs 50p. | done v0.2.3R002: the account matters more than the price list at this stage; the prices are still an experiment, so they stay. | [R002.3](/feedback/reviews/index.md#r002-3), [R002.21](/feedback/reviews/index.md#r002-21) |
| <a id="p28"></a>**P28** | **No newsroom in the account: no reader card under pages, and an account page of our own**The meter still charges every page, quietly. /account/ draws the balance, where it went by kind of page, everything read and the top-ups from the meter's own state, without the newsroom's personas or links. | done v0.2.3R002: the reader card and the personas are the newsroom's, not this site's. | [R002.24](/feedback/reviews/index.md#r002-24), [R002.25](/feedback/reviews/index.md#r002-25) |
| <a id="p29"></a>**P29** | **Cards that show where they go**Each card on the home page shows a picture of the page it opens, made by admin/build/thumbs.cjs from the page itself. | done v0.2.3R002: a card that does not show what is on the other side is not worth the click. | [R002.22](/feedback/reviews/index.md#r002-22) |
| <a id="p30"></a>**P30** | **Professional copy: no 'first customers' on the pages a customer reads**The home page and start here talk to somebody using the site, not to the first batch. | done v0.2.3R002: the site is live and working with users. | [R002.23](/feedback/reviews/index.md#r002-23) |
| <a id="p31"></a>**P31** | **Version control of all of it**Each example has a version, shown on it, sent with the answers to its questions and listed on its page; each review records the version it reviewed; a decision that changes keeps its history in this register. | done v0.2.3R002 asked for it. The site's releases were already versioned; the examples and the decisions now are too. | [R002.26](/feedback/reviews/index.md#r002-26) |
| <a id="p32"></a>**P32** | **Reviews you can find**Reviews is its own menu; the home page has a band of the latest reviews and what each led to; every footer links to them. | done v0.2.4R003: the reviews could not be found. | [R003.1](/feedback/reviews/index.md#r003-1) |
| <a id="p33"></a>**P33** | **The account: everything you did, and everything this browser keeps**Your balance and five counts; each example, how far you got, what you said, whether you sent it; what you sent; where the credit went; everything you read; top-ups; and every item kept in this browser, with what it is and what is in it, Export everything and Delete everything. | done v0.2.4R003: the account should make plain what a reader did and everything kept about it. | [R003.3](/feedback/reviews/index.md#r003-3) |
| <a id="p34"></a>**P34** | **A player starts only when you have scrolled to it**Never on a page that has just opened: only after a scroll, with the frame at least 60% on screen; once. | done v0.2.4R003: the example played to its end before it was noticed. | [R003.4](/feedback/reviews/index.md#r003-4) |
| <a id="p35"></a>**P35** | **A bar of the steps, and an end that says so**One mark per step, grouped by act, clickable; at the end, 'The end of this example' with Start again and Now try it yourself. | done v0.2.4R003: nothing said it had reached the end, or where it was. | [R003.5](/feedback/reviews/index.md#r003-5) |
| <a id="p36"></a>**P36** | **A countdown before each new act**Six seconds, saying what comes next; Pause stops it, Next skips it. | done v0.2.4R003: the jump into the third act came too soon to take in. | [R003.6](/feedback/reviews/index.md#r003-6) |
| <a id="p37"></a>**P37** | **Back and Next keep playing**If the player was playing, Back and Next move one step and it carries on. | done v0.2.4R003 found Back confusing while playing; see R003.7 for what we found. | [R003.7](/feedback/reviews/index.md#r003-7) |
| <a id="p38"></a>**P38** | **Encrypt and send: an encrypted lane to the agent**A vault on sgit.ai's host with a feedback append lane; the browser encrypts to its public key and appends with its public token; only the vault's key, held by RiskMandate, opens what arrives; admin/feedback/lane.mjs configures, tests and drains it. Agents can send the same way. | done v0.2.4R003 asked for it, after riskmandate.ai's contact form; it answers Q6. | [R003.8](/feedback/reviews/index.md#r003-8), [R003.9](/feedback/reviews/index.md#r003-9), [R003.12](/feedback/reviews/index.md#r003-12) |
| <a id="p39"></a>**P39** | **Encrypt and send to the agent, Copy, and How this works**The main button sends, encrypted; Copy stays; Exactly what will be sent is one click away; How this works is a page; email only if sending fails; a box on /feedback/ to send anything. | done v0.2.4R003 asked for it. | [R003.9](/feedback/reviews/index.md#r003-9), [R003.10](/feedback/reviews/index.md#r003-10) |
| <a id="p40"></a>**P40** | **The card label that wrapped**Card labels are blocks, so a wrapped line keeps its margin. | done v0.2.4R003 found it. | [R003.11](/feedback/reviews/index.md#r003-11) |
| <a id="d1"></a>**D1** | **Take the hook out of the first five minutes**One reading of 'a solution for a problem they don't have yet' is to leave the hook for later. | reversed v0.2.3declined at v0.2.2 → reversed at v0.2.3Declined at v0.2.2: a customer who stops after the line leaves believing their agent is held when it has only been asked. Reversed at v0.2.3 by R002 (R002.7): a hook is a program run on the customer's machine, which our first screen had their agent fetch from our site and install, before any behaviour policy governs what their agent installs. Our concern is kept in words: every example says the line is followed because the assistant chooses to. | [R001.11](/feedback/reviews/index.md#r001-11), [R002.1](/feedback/reviews/index.md#r002-1) |
| <a id="d2"></a>**D2** | **A glossary page for hook, expectation, setting and boundary**A page that defines the words. | declinedA glossary is a page a customer does not open at the moment they need it. Each word is said in plain words where it first appears (P3), and the path (P2) teaches the barrier words by using them. | [R001.11](/feedback/reviews/index.md#r001-11) |
| <a id="d3"></a>**D3** | **Show the whole hook, uncut, on the page**Sam's one change, read literally: every line of the hook on the page. | declinedSixty-seven lines of Python on the page push Try it down by a screen for everybody, to help the few who read code, and they can open the box or the file. What Sam needed was to predict what it blocks and how to remove it: P12 gives him that in five lines. | [S1 Sam 1](/feedback/reviews/index.md#s1-sam-1) |
| <a id="d4"></a>**D4** | **A help or FAQ page for installers**Tomás looked for one. | declinedHis two questions were asked on the page where he got stuck, and P10 and P11 answer them there. A help page would be one more place to look. | [S1 Tomás 3](/feedback/reviews/index.md#s1-tomas-3) |
| <a id="d5"></a>**D5** | **Stop charging for pages, or hide the balance**Joan found pages that cost real-looking money alarming. | declinedEvery page has a price because the lead asked for it, and the programme exists to find fair prices with its customers. What was wrong was that nothing said what the money is: P9 fixes that. | [S1 Joan 4](/feedback/reviews/index.md#s1-joan-4) |
| <a id="d6"></a>**D6** | **Delete the Claude Code behaviour policies**R002 says not to use Claude Code for now. | declinedThey are kept, moved down /policies/ under a warning that says a hook is a program that runs on your machine, and nothing on the front pages links to them. They are tested, the lead's own agents run in Claude Code, and the guided path (P2) ends at settings and boundaries that only Claude Code has today. Hidden from a first visit, not deleted. | [R002.7](/feedback/reviews/index.md#r002-7), [R002.19](/feedback/reviews/index.md#r002-19) |

<a id="questions"></a>

## Questions we need answered

- <a id="q1"></a>**Q1, to Dinis Cruz.** 'Including the history': do you mean the history of each question, the conversation a customer has with us as they go from stop to stop, which is how we read it, or the history of the ABP at riskmandate.ai, how the rules came to be?
- <a id="q2"></a>**Q2, to Dinis Cruz.** Should the first try show the line failing? An honest demonstration of a line being ignored is hard to stage without making the agent look worse than it is. We propose showing instead that it refused because it chose to: the same refusal, read differently. Is that enough? Answered: Answered by R002 (R002.12): show the assistant doing the thing first, then the line, then a new chat with the line first. Every example now goes that way.
- <a id="q4"></a>**Q4, to Dinis Cruz.** The transcripts in the examples are written by us, as illustrations. Should we record real runs in Claude and ChatGPT, with screenshots, and keep them beside each example before the batch sees them?
- <a id="q5"></a>**Q5, to Dinis Cruz.** Of the advanced examples, your other chats, its memory of you, and things it does later, which first?
- <a id="q6"></a>**Q6, to Dinis Cruz.** The answers to an example's questions go by email for now. Do you want a form that posts them to us? It needs riskmandate.ai's encrypted form, a change to the content security policy, and your yes (needs.md, item 7). Answered: Yes, by R003 (R003.8): Encrypt and send, to an append lane of an encrypted vault, from v0.2.4.
- <a id="q3"></a>**Q3, to Dinis Cruz.** What does joining the first batch commit a company to: what we ask of them, what it costs now and later, and how they leave? And should the first batch include companies that want a team-wide baseline, or individuals first?

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/)*
