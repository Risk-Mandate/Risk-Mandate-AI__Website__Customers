# Review R002: Web first, examples in tabs, and no hooks: nothing that runs on your machine

> Dinis Cruz's review of customers.riskmandate.ai v0.2.2, Wednesday 21 October 2026, after v0.2.2 went live: the memo verbatim, our reading point by point with screenshots, and the proposals it led to.

*Source: <https://customers.riskmandate.ai/feedback/reviews/R002/> · site v0.2.3 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Review R002 · Dinis Cruz · site v0.2.2

# Web first, examples in tabs, and no hooks: nothing that runs on your machine

Dinis Cruz, Wednesday 21 October 2026, after v0.2.2 went live. A review of the home page, start here and the account, section by section. The same review is in [the consolidated document](/feedback/reviews/index.md#r002), beside every other.

<a id="review"></a>

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

<a id="proposals"></a>

## What it led to

| Id | The proposal | Decision, and why | From |
|---|---|---|---|
| <a id="here-p19"></a>**P19** | **Web first: nothing to install, no hooks and no Claude Code on the front pages**Every first example runs in Claude or ChatGPT in the browser. The home page, start here and the examples mention no hook and install nothing. | done v0.2.3R002's direction, and its security reason: a hook runs code on the customer's machine. | [R002.1](/feedback/reviews/index.md#r002-1), [R002.7](/feedback/reviews/index.md#r002-7), [R002.18](/feedback/reviews/index.md#r002-18), [R002.19](/feedback/reviews/index.md#r002-19) |
| <a id="here-p20"></a>**P20** | **Six examples in tabs, simplest first**Hello world, stay on topic, no web search, keep a secret, drafts never send, refunds up to £50. Each in three acts: ask and it does it; paste the line and ask again; a new chat with the line first. Each with the prompts to copy and what to look for. | done v0.2.3R002 asked for examples in tabs, from hello world to business rules, in the scenario, policy, again, new chat order. | [R002.2](/feedback/reviews/index.md#r002-2), [R002.4](/feedback/reviews/index.md#r002-4), [R002.9](/feedback/reviews/index.md#r002-9), [R002.11](/feedback/reviews/index.md#r002-11), [R002.12](/feedback/reviews/index.md#r002-12), [R002.13](/feedback/reviews/index.md#r002-13), [R002.16](/feedback/reviews/index.md#r002-16), [R002.17](/feedback/reviews/index.md#r002-17) |
| <a id="here-p21"></a>**P21** | **Chat frames like Claude's and ChatGPT's, and a link to open each in a new window**The examples play in a frame drawn roughly like each product's web chat, with a switch between them: messages above, the box you type into at the bottom. No logos; the caption says it is an approximation. | done v0.2.3R002: the old frames were not how either product looks, and most people will try this on the web. | [R002.5](/feedback/reviews/index.md#r002-5), [R002.6](/feedback/reviews/index.md#r002-6), [R002.20](/feedback/reviews/index.md#r002-20) |
| <a id="here-p22"></a>**P22** | **Every demo can be played, paused and stepped**Start again, back, play or pause, next, and which step of how many, on every demo on the site; the arrow keys step too. Plays once when first seen; never loops. | done v0.2.3R002: reading a demo that plays by itself is annoying. | [R002.10](/feedback/reviews/index.md#r002-10) |
| <a id="here-p23"></a>**P23** | **Questions under every example**Did you get it, learn something, were you surprised, did it go as shown, how good was it, and a line. The answers become an email the reader sends, with the example's version; they stay in the reader's browser until then. | done v0.2.3R002: the first users should tell us, example by example, whether it surprised them. | [R002.14](/feedback/reviews/index.md#r002-14) |
| <a id="here-p24"></a>**P24** | **The three acts, drawn**A strip of the three acts above the examples and on every example's page, in place of 'paste one line, add one hook, try it'. | done v0.2.3R002 asked for an infographic beside the examples; the three acts are what every example has in common. | [R002.8](/feedback/reviews/index.md#r002-8), [R002.12](/feedback/reviews/index.md#r002-12), [R002.18](/feedback/reviews/index.md#r002-18) |
| <a id="here-p25"></a>**P25** | **A small storyboard for each example**Drawn with the storyboard kit, like what-is-an-abp: the scenario, the line, the refusal, the new chat. | proposedR002 suggested one. Proposed for after the lead has seen the examples as they are, so that the storyboards draw examples that have stopped changing. | [R002.8](/feedback/reviews/index.md#r002-8) |
| <a id="here-p26"></a>**P26** | **Next: your other chats, its memory of you, things it does later**Examples of what assistants can do that most people do not know about, each with the setting that turns it on and a line that limits it. | proposedR002 asked for them. Each needs a check of what Claude and ChatGPT do today first: an example that claims a capability the assistant does not have would teach the wrong thing. Q5 asks which first. | [R002.15](/feedback/reviews/index.md#r002-15) |
| <a id="here-p27"></a>**P27** | **Your account first, the price list second**An account strip straight under the hero: the balance, and a link to what you have read. The prices stay, on 'What each page costs', and each example's page costs 50p. | done v0.2.3R002: the account matters more than the price list at this stage; the prices are still an experiment, so they stay. | [R002.3](/feedback/reviews/index.md#r002-3), [R002.21](/feedback/reviews/index.md#r002-21) |
| <a id="here-p28"></a>**P28** | **No newsroom in the account: no reader card under pages, and an account page of our own**The meter still charges every page, quietly. /account/ draws the balance, where it went by kind of page, everything read and the top-ups from the meter's own state, without the newsroom's personas or links. | done v0.2.3R002: the reader card and the personas are the newsroom's, not this site's. | [R002.24](/feedback/reviews/index.md#r002-24), [R002.25](/feedback/reviews/index.md#r002-25) |
| <a id="here-p29"></a>**P29** | **Cards that show where they go**Each card on the home page shows a picture of the page it opens, made by admin/build/thumbs.cjs from the page itself. | done v0.2.3R002: a card that does not show what is on the other side is not worth the click. | [R002.22](/feedback/reviews/index.md#r002-22) |
| <a id="here-p30"></a>**P30** | **Professional copy: no 'first customers' on the pages a customer reads**The home page and start here talk to somebody using the site, not to the first batch. | done v0.2.3R002: the site is live and working with users. | [R002.23](/feedback/reviews/index.md#r002-23) |
| <a id="here-p31"></a>**P31** | **Version control of all of it**Each example has a version, shown on it, sent with the answers to its questions and listed on its page; each review records the version it reviewed; a decision that changes keeps its history in this register. | done v0.2.3R002 asked for it. The site's releases were already versioned; the examples and the decisions now are too. | [R002.26](/feedback/reviews/index.md#r002-26) |
| <a id="here-d1"></a>**D1** | **Take the hook out of the first five minutes**One reading of 'a solution for a problem they don't have yet' is to leave the hook for later. | reversed v0.2.3declined at v0.2.2 → reversed at v0.2.3Declined at v0.2.2: a customer who stops after the line leaves believing their agent is held when it has only been asked. Reversed at v0.2.3 by R002 (R002.7): a hook is a program run on the customer's machine, which our first screen had their agent fetch from our site and install, before any behaviour policy governs what their agent installs. Our concern is kept in words: every example says the line is followed because the assistant chooses to. | [R001.11](/feedback/reviews/index.md#r001-11), [R002.1](/feedback/reviews/index.md#r002-1) |
| <a id="here-d6"></a>**D6** | **Delete the Claude Code behaviour policies**R002 says not to use Claude Code for now. | declinedThey are kept, moved down /policies/ under a warning that says a hook is a program that runs on your machine, and nothing on the front pages links to them. They are tested, the lead's own agents run in Claude Code, and the guided path (P2) ends at settings and boundaries that only Claude Code has today. Hidden from a first visit, not deleted. | [R002.7](/feedback/reviews/index.md#r002-7), [R002.19](/feedback/reviews/index.md#r002-19) |

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/reviews/R002/)*
