# Sam Okoye, an invented user: study S1, step by step

> Study S1, invented user Sam Okoye (Backend developer at a 12-person payments start-up. Uses Claude Code every day in a monorepo with .env files for four services.) on customers.riskmandate.ai v0.2.1: the run screenshot by screenshot, the interview, the rating and the findings, each checked. Invented, not user research.

*Source: <https://customers.riskmandate.ai/feedback/synthetic/sam/> · site v0.2.4 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Study S1 · invented user · laptop 1440×900 · gave it 3 out of 5

# Sam Okoye: Can I stop Claude Code reading my .env without breaking my workflow?

**Invented, not user research.** Everybody in this study is invented, and their words were written by a model playing them. What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.

Backend developer at a 12-person payments start-up. Uses Claude Code every day in a monorepo with .env files for four services. From a Slack message from the lead: 'try this, five minutes, tell me if it gets in the way'. Lands on the home page.

**Knows**
:

- Claude Code, CLAUDE.md, the terminal, git
- that Claude Code has hooks, from the changelog; has never written one

**Does not know**
:

- what an ABP is, or riskmandate.ai
- what the £50 is for, or whether it is real money
- what PreToolUse means

**Patience**
: ten minutes, then back to work
**Leaves if**
:

- installing needs an account, a card or a call
- the hook looks like it could block things he needs every day
- he cannot tell what the hook will do before he installs it

**We expected**
: Sam reaches the secrets policy in one click and has the install prompt within two minutes.
**Ended**
: left: I could see the hook only partly (the pasted source was cut off before the part that says which files it refuses), it watches Bash, Grep and Glob, and the deny list names only ./.env at the root; the Docs menu led to the site's own internal papers, so I went back to work rather than install something I could not predict in a four-service monorepo.

## The run, 12 screenshots

<a id="step-1"></a>
[![What Sam Okoye saw at step 1](/assets/feedback/S1/sam/01.webp)](/assets/feedback/S1/sam/01.webp)
Step 1: `/`, scrolled 0 of 5154 pixels, 1440x900
**Saw**
: Dark hero: 'Put a behaviour policy on your agent, in five minutes.' Green pill 'Early access, you start with £50.00'. Text says paste one line, add one hook, try it; the first one keeps Claude Code away from secrets, two minutes, 50p of your credit. Three buttons. Top bar has a £50.00 pill, a 'RiskMandate' dropdown, v0.2.1.
**Thought**
: Secrets is exactly my question. But 50p of whose credit, and is that money? Not going to click Install yet; I want to see what it does first. The page says there is a played-out demo below, so I scroll.
**Question**
: What is the £50.00 in the top bar, and is it real money or my card?
**Confusion**
: The '£50.00' pill and 'you start with £50.00' in the green pill and 'costs 50p of your credit' in the paragraph: nothing there says whether it is money, a trial balance, or what I am paying for.
**Did**
: scroll 650
**Why**
: I want to see the walkthrough before I install anything; I am not clicking a green Install button for something I cannot picture.

<a id="step-2"></a>
[![What Sam Okoye saw at step 2](/assets/feedback/S1/sam/02.webp)](/assets/feedback/S1/sam/02.webp)
Step 2: `/`, scrolled 650 of 5154 pixels, 1440x900
**Saw**
: A laptop-shaped terminal 'claude: ~/shop-api' typing 'Install the b' with a blinking cursor, and a caption saying it is an illustration, not a recording, plus a 'Play again' link. Under it three cards: Paste one line (into CLAUDE.md), Add one hook (a setting), Try it.
**Thought**
: Slow typing animation, nothing to read yet; I am not waiting on a typewriter. The three steps are clear enough, but 'a hook, outside the model: a setting' is vague. Good that it says the animation is not a recording, so it is not pretending.
**Question**
: What does 'outside the model' mean for my daily use: will it fire on every tool call?
**Confusion**
: The terminal box in the middle of the screen is mostly empty black with 'Install the b' typed; I cannot tell if it is stuck or just slow.
**Did**
: scroll 700
**Why**
: The animation is going nowhere for me; I will go to the list of policies and the one I came for.

<a id="step-3"></a>
[![What Sam Okoye saw at step 3](/assets/feedback/S1/sam/03.webp)](/assets/feedback/S1/sam/03.webp)
Step 3: `/`, scrolled 1350 of 5154 pixels, 1440x900
**Saw**
: The balance in the top bar now reads £49.99. 'Pick one worry.' Six cards with codes like RM-R0002, 'Claude Code', 'Line and hook', '2 min, 50p'. First card: 'Keep your agent away from your secrets'. Others: only push to the branch you named, nothing deleted without a yes.
**Thought**
: The balance went down while I scrolled; so something is metering me. 'Nothing deleted without a yes' sounds like it would nag me all day. Secrets is mine.
**Question**
: Why did the balance drop from £50.00 to £49.99 just from my scrolling?
**Confusion**
: The top-bar balance changed from £50.00 to £49.99 with no message about why.
**Did**
: clicktext "Keep your agent away from your secrets"
**Why**
: That is the card that answers my question about .env.

<a id="step-4"></a>
[![What Sam Okoye saw at step 4](/assets/feedback/S1/sam/04.webp)](/assets/feedback/S1/sam/04.webp)
Step 4: `/policies/touch-your-secrets/`, scrolled 0 of 4081 pixels, 1440x900
**Saw**
: Page 'Keep your agent away from your secrets', tag line 'THIS PAGE COSTS 50P READ TO THE END'. Balance £49.87. 'What you get: the agent stops and asks before it touches a credential, and you decide which one it gets, if any.' Step 1: a line to paste into CLAUDE.md with a Copy button. Step 2: 'Make Claude Code hold it', with a long prompt to ask Claude Code to install it, 'show me each change before you make it, and wait for my yes'.
**Thought**
: OK, a line in CLAUDE.md is harmless. The install is a prompt I give Claude Code, and it asks me yes before each change. That I like. But it fetches a Python file and merges settings.json; I want to see that file first. 'Read to the end' costs 50p of what, though?
**Question**
: Is the 50p charged only if I read to the bottom, and what happens at zero?
**Confusion**
: The label 'THIS PAGE COSTS 50P READ TO THE END' next to the balance falling as I scroll: I cannot tell if I am being charged per scroll or once.
**Did**
: scroll 750
**Why**
: I need to see the settings change and the hook before I say yes to anything.

<a id="step-5"></a>
[![What Sam Okoye saw at step 5](/assets/feedback/S1/sam/05.webp)](/assets/feedback/S1/sam/05.webp)
Step 5: `/policies/touch-your-secrets/`, scrolled 750 of 4081 pixels, 1440x900
**Saw**
: The settings.json to be merged: permissions deny for Read(./.env), ./secrets/**, ~/.ssh, ~/.aws; then hooks, 'PreToolUse', a matcher 'Read|Edit|Write|MultiEdit|NotebookEdit|Grep|Glob|Bash' running python3 touch_your_secrets.py, timeout 10. Below it a collapsed 'Read the hook before you install it (67 lines of Python, standard library only)'.
**Thought**
: PreToolUse I have never written. But I can read this: it runs a script before Read, Edit, Write, Grep, Glob and Bash. Bash and Edit and Write is basically everything I do all day. If that script is too eager it will stop me running tests. Deny only covers ./.env at the root, and I have four services each with its own .env. I want the script.
**Question**
: With Bash and Edit in the matcher, what exactly will it stop, and what will it leave alone?
**Confusion**
: The matcher string 'Read|Edit|Write|MultiEdit|NotebookEdit|Grep|Glob|Bash' in the JSON block: the page never says in plain words why a secrets hook needs to fire on Edit and Bash, or whether it will slow every command.
**Did**
: clicktext "Read the hook before you install it"
**Why**
: The page itself tells me to read the hook before installing; that is the exact thing I need to judge if it gets in the way.

<a id="step-6"></a>
[![What Sam Okoye saw at step 6](/assets/feedback/S1/sam/06.webp)](/assets/feedback/S1/sam/06.webp)
Step 6: `/policies/touch-your-secrets/`, scrolled 750 of 4523 pixels, 1440x900
**Saw**
: The disclosure arrow turned and a code box opened at the bottom edge, only its top lines visible at this scroll.
**Thought**
: Fine, it opened. I need to scroll to read it.
**Did**
: scroll 700
**Why**
: Read the code.

<a id="step-7"></a>
[![What Sam Okoye saw at step 7](/assets/feedback/S1/sam/07.webp)](/assets/feedback/S1/sam/07.webp)
Step 7: `/policies/touch-your-secrets/`, scrolled 1450 of 4523 pixels, 1440x900
**Saw**
: A Python file with a long header comment: it reads the tool call on stdin and denies any read, write, search or shell command that names a file that usually holds a credential: .env files, private keys, SSH, cloud and package-manager credentials; everything else gets no answer from the hook so normal permissions apply. It says a script that opens the file gets past it, and the sandbox is the boundary. Then imports and a LINE variable. The box ends there, cut off at the bottom edge of the code box. Below, step 3 'Try it': a prompt to paste, with 'With the behaviour policy' and 'Without it' outcomes.
**Thought**
: The comment is honest and I like it: it says it will not catch a script that opens the file. And 'everything else gets no answer' tells me it will not block my normal commands. But the box is cut off right where the actual patterns would start; I cannot see which filenames match. Does .env.example match? .env.test? Does `docker compose up`, which reads .env, get stopped? It says 67 lines and I have seen about 25.
**Question**
: Which exact filenames match, and does .env.example or my docker-compose use of .env get blocked?
**Confusion**
: The hook code box stops after the 'LINE = (...)' statement, with a hard edge at the bottom of the box; I cannot tell if the rest is hidden or I have to scroll inside it.
**Did**
: scroll 800
**Why**
: Maybe the rest of the page tells me what it matches, or the box continues; I will read on.

<a id="step-8"></a>
[![What Sam Okoye saw at step 8](/assets/feedback/S1/sam/08.webp)](/assets/feedback/S1/sam/08.webp)
Step 8: `/policies/touch-your-secrets/`, scrolled 2250 of 4523 pixels, 1440x900
**Saw**
: Another copy of the terminal animation, stuck at 'Install the'. Below it a heading 'What this is, and what it is not' with a table: the line is an expectation, the hook is a setting, and RM-R0015 guards the file the agent could edit.
**Thought**
: Same typed animation again, frozen mid-word. 'Expectation', 'setting', 'boundary' are the site's words, I get them roughly. Still nothing about false positives.
**Question**
: What is RM-R0015 and do I need it installed with this?
**Confusion**
: The table row 'The hook | setting | ... which RM-R0015 guards': it names another policy that I apparently need, with no word on whether it is installed alongside.
**Did**
: scroll 800
**Why**
: Keep going for a section on what it blocks or what to do if it blocks too much.

<a id="step-9"></a>
[![What Sam Okoye saw at step 9](/assets/feedback/S1/sam/09.webp)](/assets/feedback/S1/sam/09.webp)
Step 9: `/policies/touch-your-secrets/`, scrolled 3050 of 4523 pixels, 1440x900
**Saw**
: The deny rule alone as a 'setting', then the sandbox as a 'boundary' with links to Claude Code docs. Then 'Tell us what happened': write to agent@riskmandate.ai, a person reads within a working day. Balance £49.49.
**Thought**
: Good: the deny rule on its own is something I could paste in a minute and trust, and it is Claude Code's own docs. But still nothing on how to turn the hook off if it gets in the way, and no list of what it matches. Email to a person is not an undo.
**Question**
: How do I switch it off in two seconds if it blocks a deploy?
**Did**
: click 632 28 (Start here menu)
**Why**
: Before I give up, I will check the start-here page, maybe it covers the £50 and removal.

<a id="step-10"></a>
[![What Sam Okoye saw at step 10](/assets/feedback/S1/sam/10.webp)](/assets/feedback/S1/sam/10.webp)
Step 10: `/start-here/`, scrolled 0 of 2850 pixels, 1440x900
**Saw**
: 'Your first five minutes, in order.' A dropdown open over the heading. Status line with green 'shipped' tags. Step 1: 'You have £50.00 to spend ... Nothing is blocked, ever.' Step 2: pick one thing. Step 3: paste one line. Step 4: add one hook.
**Thought**
: OK, the £50 is a reading allowance, not my card, and nothing is blocked when it runs out. No account, no card. Good. The dropdown covering the heading is annoying. The 'Status, from docs/reality.md' line with 'shipped v0.1.0' tags is their internal noise, not for me.
**Question**
: Who is SG Meter and api.newsroom.sgit.ai, and does reading here send anything of mine anywhere?
**Confusion**
: The grey status paragraph full of 'shipped v0.2.1' tags and 'metered by SG Meter from api.newsroom.sgit.ai': jargon I cannot parse, sitting above the actual steps.
**Did**
: scroll 750
**Why**
: See steps 4 to 6, whether anything covers undo or removal.

<a id="step-11"></a>
[![What Sam Okoye saw at step 11](/assets/feedback/S1/sam/11.webp)](/assets/feedback/S1/sam/11.webp)
Step 11: `/start-here/`, scrolled 750 of 2850 pixels, 1440x900
**Saw**
: Steps 4 to 6: add one hook, try it, tell us what happened. Then 'Watch the whole thing first' with the same terminal animation stuck at 'Install the'. The open Start here dropdown still covers part of step 4's text. Balance £49.48.
**Thought**
: Nothing about undoing it or what the hook matches. Third time seeing a frozen terminal. Same story as the policy page.
**Question**
: Is there anything about removing the hook?
**Confusion**
: The dropdown menu hangs over the text of step 4 ('Ask Claude Code to install it, wi...'), so I cannot read that sentence.
**Did**
: click 985 28 (Docs menu)
**Why**
: Last try: the Docs menu might have a page on what the hooks match.

<a id="step-12"></a>
[![What Sam Okoye saw at step 12](/assets/feedback/S1/sam/12.webp)](/assets/feedback/S1/sam/12.webp)
Step 12: `/docs/`, scrolled 0 of 1561 pixels, 1440x900
**Saw**
: 'Documents: the documents this site was built from and the notes it is run by.' Menu items: the brief in full, the memo of 20 October, brief corrections, reality, operations, the team, how the site is built, release history, llms.txt for agents. Text about publishing the brief so a reader can check the site is faithful.
**Thought**
: This is the company's own paperwork, not a how-it-works for my hook. I have used about eleven minutes of looking; the lead said five. I will tell him: promising, but I could not see everything the hook matches, and I am not putting a script that watches Bash and Edit into a payments repo on that.
**Question**
: Where is the list of what the hook refuses and the way to turn it off?
**Confusion**
: 'Documents: the documents this site was built from...' under the Docs menu: it is the site's internal papers, not documentation for me as a user.
**Did**
: end (leave the site)
**Why**
: Over my ten minutes and the thing I needed (what it blocks, how to undo) was not where I looked.

## The interview

**In one sentence, what is this site?**
: A site that gives you a one-line rule for CLAUDE.md plus a small hook script so Claude Code stops and asks before it reads your secrets, push to main, deletes and so on, with a pretend £50 reading balance ticking down.
**Was any of it for you? Which part?**
: Yes, the secrets page. The install-by-asking-Claude-Code prompt with 'show me each change and wait for my yes' is how I would want to do it, and the header comment in the hook is honest about what it does not catch.
**Did you believe it? What made you believe it, or not?**
: Mostly. It says plainly that the line is only an expectation, that the hook cannot stop a script that opens the file, and the sandbox is the real boundary, and it links Claude Code's own docs. What I did not believe yet is that it would not get in my way, because I never saw the matching rules.
**Where did you have to guess?**
: What the £50 and 50p are (I only found out on the Start here page that it is not money), why the balance drops as I scroll, whether .env.example or a .env in a service folder is matched, and whether Bash in the matcher means every shell command goes through a Python script.
**What did you still not know at the end?**
: Which filenames the hook matches, what it does to docker compose or my test runner reading .env, how to remove it, and who riskmandate.ai is. I also never worked out what 'ABP' or RM-R0015 means for me.
**Was the credit and the price of each page right for what you got?**
: 50p for the secrets page is fine as a number but I could not tell what it bought me. The page says 'read to the end' but the hook box cut off before the part I needed, so I paid for the part I did not need. The start page was the one that actually explained the credit, and it came last.
**Would you install a behaviour policy from here, today? If not, what would have to change?**
: Not into the payments repo today. I might paste the CLAUDE.md line and the plain permissions deny rule, which are Claude Code's own settings. For the hook I need the full file and a plain list of what it matches (including .env.example and nested .env), plus one line on how to turn it off.
**One change. What is it?**
: Show the whole hook, uncut, with a short plain-words list: 'blocks these filenames, leaves these alone, to turn it off delete this block'.
**Would you send this to somebody else? Who?**
: My lead, with a note that the secrets idea is right but the hook needs to be readable first. Not to the juniors yet.
**Rate the experience from 1 to 5, and say why in one sentence.**
: 3: it answered my question about secrets and told me the truth about its limits, but I could not see what the hook would stop in my daily work and the credit numbers moving as I scrolled were unexplained.

## Findings, and our check

| Costs | The finding | Our check | Leads to |
|---|---|---|---|
| blocks the first install | The hook source is cut off before the rules that say which files it blocksThe opened 'Read the hook' box ends at the LINE variable with a hard edge, about 25 of the 67 lines. The patterns that decide what is refused (.env.example? nested .env?) are not visible. For someone who will not install what he cannot predict, this is the exact blocker.[step 7](#step-7), `/policies/touch-your-secrets/` | partlyThe source is all there, in a box that scrolls: 418 of its 1,246 pixels show, and nothing says it scrolls. What he needed, which files it stops, is not in plain words anywhere on the page. | [P12](/feedback/reviews/index.md#p12), [D3](/feedback/reviews/index.md#d3) |
| loses a customer | The matcher includes Bash, Edit and Write with no plain-words reasonThe settings.json block shows matcher 'Read\|Edit\|Write\|MultiEdit\|NotebookEdit\|Grep\|Glob\|Bash'. A daily user reads that as 'this script sits in front of everything I do', and nothing beside it says it only refuses on credential filenames and stays silent otherwise (that sentence is only in the code comment further down).[step 5](#step-5), `/policies/touch-your-secrets/` | confirmedThe matcher names every file tool and Bash, and nothing beside it says the hook answers only when a credential file is named. | [P12](/feedback/reviews/index.md#p12) |
| costs trust | No word on how to turn the hook off or undo the installThe page after the deny-rule section goes straight to 'Tell us what happened' by email. Nothing says how to remove the hook in seconds if it blocks a deploy, which is the first thing a cautious developer asks before installing.[step 9](#step-9), `/policies/touch-your-secrets/` | confirmedNo page says how to remove a hook. | [P12](/feedback/reviews/index.md#p12) |
| costs trust | The £50 and the falling balance are unexplained until the third page I openThe home hero says 'you start with £50.00' and '50p of your credit' and the balance in the top bar ticks down as I scroll (£50.00 to £49.99 to £49.87), with no message. 'Nothing is blocked, ever' and no card appear only on Start here. Until then it reads as possible real money.[step 1](#step-1), `/` | confirmedFive of five asked what the £50 was. | [P9](/feedback/reviews/index.md#p9) |
| costs time | The typing terminal demo shows nothing useful and looks stuckOn the home page and on the policy page the terminal box sits at 'Install the b' or 'Install the' with a blinking cursor; it is big, mostly empty black and repeated three times. The promised 'the hook stops the read' moment never appeared in any screenshot, so it explains nothing.[step 2](#step-2), `/` | partlyA still screenshot cannot watch an animation: the demo is typing, not stuck. What holds: measured in the same browser, the refusal appears about eleven seconds after the demo comes into view. | [P17](/feedback/reviews/index.md#p17) |
| minor | Docs menu and status line are the company's internal papers, not user helpLooking for what the hook matches, the Docs dropdown offers the brief, memo, corrections, reality and team pages, and Start here carries a grey status paragraph with 'shipped v0.2.1' tags and 'SG Meter from api.newsroom.sgit.ai'. For a developer in a hurry this is noise sitting where he expects the answer.[step 12](#step-12), `/docs/` | confirmedThe Docs menu is the brief, the memo and how the site is built. | [P16](/feedback/reviews/index.md#p16) |

The whole study: [study S1](/feedback/synthetic/index.md). Every review and proposal: [the reviews](/feedback/reviews/index.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/synthetic/sam/)*
