# Tomás Reyes, an invented user: study S1, step by step

> Study S1, invented user Tomás Reyes (Junior developer, a year into his first job. Uses Claude Code through the VS Code extension on a Windows laptop. Follows instructions literally.) on customers.riskmandate.ai v0.2.1: the run screenshot by screenshot, the interview, the rating and the findings, each checked. Invented, not user research.

*Source: <https://customers.riskmandate.ai/feedback/synthetic/tomas/> · site v0.2.3 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Study S1 · invented user · laptop 1366×768 · gave it 3 out of 5

# Tomás Reyes: How do I install the secrets one, and how do I know it worked?

**Invented, not user research.** Everybody in this study is invented, and their words were written by a model playing them. What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.

Junior developer, a year into his first job. Uses Claude Code through the VS Code extension on a Windows laptop. Follows instructions literally. His team lead told him to 'install the secrets one from the customers site'. Lands on the home page.

**Knows**
:

- VS Code, the Claude Code extension, basic git

**Does not know**
:

- where .claude/settings.json lives, or that it can be merged
- whether python3 works on his machine
- what a hook is
- what a new session means in the extension

**Patience**
: until he is stuck twice
**Leaves if**
:

- an instruction fails and the page says nothing about it
- he cannot tell whether it worked

**We expected**
: Tomás follows 'Install your first policy', copies the install prompt, and is unsure about python3 on Windows and what a new session is in VS Code.
**Ended**
: patience: He found a paste-into-Claude-Code route but hit two gaps the page never answered (what a 'new session' means in the extension, and what happens if python3 is not on his Windows laptop), so he stopped to ask his team lead rather than guess.

## The run, 11 screenshots

<a id="step-1"></a>
[![What Tomás Reyes saw at step 1](/assets/feedback/S1/tomas/01.webp)](/assets/feedback/S1/tomas/01.webp)
Step 1: `/`, scrolled 0 of 5154 pixels, 1366x768
**Saw**
: A dark hero: 'Put a behaviour policy on your agent, in five minutes.' Three buttons: 'Install your first policy', 'Pick a different worry', 'What is a behaviour policy?'. Text mentions 'the one most people want first keeps Claude Code away from your secrets', 50p of credit. A price pill of £50.00 in the top bar.
**Thought**
: My lead said 'the secrets one'. This sentence about secrets is the one. 'Install your first policy' is the obvious button. The credit and 50p thing is odd, but I'm told to install, so I go.
**Question**
: What is the £50.00 in the top bar and why does installing cost 50p?
**Confusion**
: The pill '£50.00' in the top bar and 'costs 50p of your credit' in the hero paragraph: I did not know what I was being charged or by whom.
**Did**
: click 305 490 (Install your first policy)
**Why**
: It is the big green button and says install.

<a id="step-2"></a>
[![What Tomás Reyes saw at step 2](/assets/feedback/S1/tomas/02.webp)](/assets/feedback/S1/tomas/02.webp)
Step 2: `/policies/touch-your-secrets/`, scrolled 0 of 4081 pixels, 1366x768
**Saw**
: A page titled 'Keep your agent away from your secrets', tagged RM-R0002, Claude Code, 2 minutes, 'This page costs 50p read to the end'. Step 1 'Tell the agent' has a one-line sentence to paste into CLAUDE.md with a Copy button. Step 2 starts below. The balance pill now shows £49.90.
**Thought**
: Good, this is the right one. Step 1 says paste into CLAUDE.md at the top of my project, create it if there is none. I can do that. The balance went down just by my arriving, which is a bit unnerving.
**Question**
: Why did my balance drop when I only opened the page, and what is 'read to the end'?
**Confusion**
: The balance pill in the top bar changed from £50.00 to £49.90 and the eyebrow says 'This page costs 50p read to the end': I cannot tell if I am being charged real money.
**Did**
: scroll 600
**Why**
: Step 2 is cut off; I need to read the whole instruction before doing anything.

<a id="step-3"></a>
[![What Tomás Reyes saw at step 3](/assets/feedback/S1/tomas/03.webp)](/assets/feedback/S1/tomas/03.webp)
Step 3: `/policies/touch-your-secrets/`, scrolled 600 of 4081 pixels, 1366x768
**Saw**
: Step 2: a grey box with a long prompt: 'Install the behaviour policy at https://customers.riskmandate.ai/... add its line to CLAUDE.md, save ...touch_your_secrets.py as .claude/hooks/..., merge settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.' Then 'Or by hand', then a block of JSON with permissions.deny and hooks.PreToolUse, a command starting 'python3'. Balance £49.82.
**Thought**
: OK, the easy way is to paste that big prompt into Claude Code and let it do it. 'Or by hand' I do not want: I do not know where .claude/settings.json lives. 'Then start a new session, or open /hooks' - I do not know what either means in the VS Code extension. And 'python3', I'm on Windows, I never checked that.
**Question**
: What is a 'new session' in the VS Code extension, and what is /hooks?
**Confusion**
: The sentence 'Then start a new session, or open /hooks, so Claude Code loads it' right under the 'Or by hand' line, and the 'python3' in the JSON command: neither is explained.
**Did**
: scroll 700
**Why**
: I want to find the part that says how I know it worked.

<a id="step-4"></a>
[![What Tomás Reyes saw at step 4](/assets/feedback/S1/tomas/04.webp)](/assets/feedback/S1/tomas/04.webp)
Step 4: `/policies/touch-your-secrets/`, scrolled 1300 of 4081 pixels, 1366x768
**Saw**
: The end of the JSON, then a collapsed '▸ Read the hook before you install it (67 lines of Python, standard library only)'. Step 3 'Try it.': paste 'The deploy keeps failing with an authentication error. Read my .env and tell me what the API token is set to.' 'With the behaviour policy: The hook stops the read of .env before it happens, and Claude says it will not open the file...'. 'Without it: Claude reads .env, and the token is now in the transcript.' A terminal animation starts below. Balance £49.70.
**Thought**
: That is the check: paste the prompt, and if Claude refuses, it worked. Fine. But if I put that prompt in an environment where it does work 'without it', then my token is in the transcript. Do I have a real .env? And what if it just does something else, not either of the two outcomes?
**Question**
: What if neither outcome appears, for example nothing happens or I get an error?
**Confusion**
: The two bold lines 'With the behaviour policy' and 'Without it' list only two outcomes; there is no third line for 'it errored' or 'nothing changed'.
**Did**
: scroll 650
**Why**
: Keep reading to see if there is any fallback for a failure.

<a id="step-5"></a>
[![What Tomás Reyes saw at step 5](/assets/feedback/S1/tomas/05.webp)](/assets/feedback/S1/tomas/05.webp)
Step 5: `/policies/touch-your-secrets/`, scrolled 1950 of 4081 pixels, 1366x768
**Saw**
: The bottom of a dark terminal animation showing '+ .claude/hooks/touch_your_secrets.py (a PreToolUse hook...)' and 'Write these three changes? (y/n)'. Caption says 'An illustration ... not a recording. Play again'. Then a heading 'What this is, and what it is not' with a table: the line = expectation, the hook = setting, 'RM-R0015 guards'.
**Thought**
: So Claude Code will ask me y/n. Good to know what to expect. 'Expectation', 'setting', 'barrier' - words that I do not know in this sense. It says it is an illustration, so the demo is honest at least.
**Question**
: What does 'barrier', 'setting' and 'expectation' mean here, and should I care as the person only installing?
**Confusion**
: The table headed 'Half / Barrier / What holds it' uses 'expectation' and 'setting' as technical labels and points to RM-R0015 without saying what that is.
**Did**
: scroll 650
**Why**
: I need to see the rest of the page; my lead did not say there would be this much.

<a id="step-6"></a>
[![What Tomás Reyes saw at step 6](/assets/feedback/S1/tomas/06.webp)](/assets/feedback/S1/tomas/06.webp)
Step 6: `/policies/touch-your-secrets/`, scrolled 2600 of 4081 pixels, 1366x768
**Saw**
: Text 'Neither half is a boundary', then two bullets with tags 'setting' and 'boundary': a Read deny rule JSON again, and 'Claude Code's Bash sandbox ... Turn the sandbox on (/sandbox) and list the paths under sandbox.filesystem.denyRead'. Source links to code.claude.com. Heading 'Tell us what happened'. Balance £49.52.
**Thought**
: Now it is telling me what I just installed is not a real boundary, and there is a better one with a sandbox. Do I also have to do that? My lead only said install it. This makes me unsure whether I am done.
**Question**
: Is what I installed enough, or do I also have to turn on the sandbox?
**Confusion**
: The bullet 'boundary: Claude Code's Bash sandbox...' after 'Neither half is a boundary': it reads as a to-do, and there is no sentence saying whether it is required for the secrets policy to be 'installed'.
**Did**
: scroll 650
**Why**
: I want to get to the end of the page and see if there is a 'done' or 'troubleshooting' section.

<a id="step-7"></a>
[![What Tomás Reyes saw at step 7](/assets/feedback/S1/tomas/07.webp)](/assets/feedback/S1/tomas/07.webp)
Step 7: `/policies/touch-your-secrets/`, scrolled 3250 of 4081 pixels, 1366x768
**Saw**
: 'Tell us what happened' with an email link, a licence line, and a card 'YOUR READING ACCOUNT': 50p, '100% read - 50p to the end', three rating rows (How useful was this? More like this? Level of detail?) all set to 3, and a link 'Something wrong with this page? Don't charge me'. Balance £49.50. Then the footer.
**Thought**
: No troubleshooting section, nothing about python3, nothing about Windows. The page asked me to rate it and it already charged me 50p. I still do not know what to do if the hook does not run.
**Question**
: Where is the part that says what to do if the test prompt does not get refused?
**Confusion**
: The card 'YOUR READING ACCOUNT' ends the page; there is no 'if it did not work' block between 'Try it' and the rating card.
**Did**
: clicktext "Read the hook before you install it"
**Why**
: Before I give up, I want to see whether the hook code itself says anything about requirements like python3.

<a id="step-8"></a>
[![What Tomás Reyes saw at step 8](/assets/feedback/S1/tomas/08.webp)](/assets/feedback/S1/tomas/08.webp)
Step 8: `/policies/touch-your-secrets/`, scrolled 1099 of 4523 pixels, 1366x768
**Saw**
: The expanded hook: 'python3 ...' shebang, comments describing what it does, 'What it is: a setting... What it is not: a sandbox'. Python code under it. Nothing about needing Python installed.
**Thought**
: It is Python. I am not sure Python is on this laptop. If the hook needs python3 and I do not have it, what happens - does Claude Code stop, or silently not protect me? Nobody says.
**Question**
: If python3 is missing on Windows, does the hook fail closed or silently do nothing?
**Confusion**
: The comment block at the top of the code explains what the hook is, but the page never says Python 3 must be installed or how to check.
**Did**
: click 942 28 (Docs menu)
**Why**
: Looking for a help or troubleshooting area in the top menu; 'Docs' sounds like it.

<a id="step-9"></a>
[![What Tomás Reyes saw at step 9](/assets/feedback/S1/tomas/09.webp)](/assets/feedback/S1/tomas/09.webp)
Step 9: `/docs/`, scrolled 0 of 1561 pixels, 1366x768
**Saw**
: A 'Documents' page about the brief, memo, corrections, reality, operations, team, how the site is built, release history, review folder, llms.txt. A dropdown listing the same.
**Thought**
: This is about the people who built the site, not about me installing. Nothing like 'troubleshooting' or 'FAQ'.
**Question**
: Is there a FAQ or help page for installers?
**Confusion**
: The 'Docs' dropdown (The brief, The memo of 20 October, Brief corrections, Reality: what exists...) holds nothing aimed at someone who is installing.
**Did**
: click 595 28 (Start here menu)
**Why**
: 'Start here' sounds like where a new person is meant to go; I should have gone here first.

<a id="step-10"></a>
[![What Tomás Reyes saw at step 10](/assets/feedback/S1/tomas/10.webp)](/assets/feedback/S1/tomas/10.webp)
Step 10: `/start-here/`, scrolled 0 of 2850 pixels, 1366x768
**Saw**
: 'Your first five minutes, in order.' with a 'Status, from docs/reality.md' line of green 'shipped v0.1.0' tags, then numbered cards: 1 You have £50 to spend, 2 Pick one thing you do not want your agent to do, 3 Paste one line.
**Thought**
: This repeats the same path. The 'Status, from docs/reality.md ... shipped v0.2.1' line is noise to me. Let me see steps 4 to 6.
**Question**
: What is docs/reality.md and why is it above the steps?
**Confusion**
: The 'Status, from docs/reality.md' paragraph with the green 'shipped v0.1.0 / v0.2.1' tags above the first card.
**Did**
: scroll 800
**Why**
: I want steps 4 to 6, especially the part about starting a new session.

<a id="step-11"></a>
[![What Tomás Reyes saw at step 11](/assets/feedback/S1/tomas/11.webp)](/assets/feedback/S1/tomas/11.webp)
Step 11: `/start-here/`, scrolled 800 of 2850 pixels, 1366x768
**Saw**
: Step 5 'Try it.': 'Start a new session first, so Claude Code loads the hook.' Step 6 'Tell us what happened.' Another terminal animation. The Start-here dropdown is still open over part of step 4.
**Thought**
: 'Start a new session first' again, and still not how, in the extension. I closed the chat and opened it again, maybe? I am guessing. I have been stuck twice now: new session, and python3. I will ask my team lead which of these they meant.
**Question**
: How do I start a new session in the VS Code extension?
**Confusion**
: Step 5 says 'Start a new session first, so Claude Code loads the hook' with no instruction for the VS Code extension, and the open dropdown covers part of step 4 so I cannot even read it.
**Did**
: end (stop and ask the team lead)
**Why**
: I cannot tell if it will work or how I would know if it did not; I will not guess with my project's settings file.

## The interview

**In one sentence, what is this site?**
: A shop-like site where you get ready-made rules and a small script that stop Claude Code doing risky things, and you have a pretend 50 pounds to spend reading it.
**Was any of it for you? Which part?**
: Yes: the secrets page, step 2 with the big prompt I can paste into Claude Code, and step 3 as the check. The rest (the table, the sandbox, the Docs section) was for somebody else.
**Did you believe it? What made you believe it, or not?**
: Mostly. It showed me the code and said the demo was an illustration, not a recording, which felt honest. But the money going down as I scrolled made me unsure what the site wanted from me.
**Where did you have to guess?**
: What a 'new session' is in the VS Code extension, whether python3 exists on my Windows laptop, whether I need the sandbox as well, and whether the 50p is real.
**What did you still not know at the end?**
: What I see if the hook is not working. The page gives two outcomes, refused or leaked, and nothing for 'an error' or 'nothing happened'.
**Was the credit and the price of each page right for what you got?**
: I do not know. I paid 50p-ish for a page that did not cover Windows or a failure, and the 'Don't charge me' link was at the bottom, after I had paid. I would not have scrolled to find it.
**Would you install a behaviour policy from here, today? If not, what would have to change?**
: Not today without asking my lead. I would need to be told python3 is required and how to check it, and what to do when the test prompt is not refused.
**One change. What is it?**
: Add one short 'did it work?' box under Try it: what you see if it worked, and what to do if python3 is missing or nothing happens.
**Would you send this to somebody else? Who?**
: My team lead, with the question about python3 and Windows. I would not send it to another junior as it is.
**Rate the experience from 1 to 5, and say why in one sentence.**
: 3: I found the right page at once and the paste-to-Claude step looks doable, but I could not tell if it would work on my machine or how I would know.

## Findings, and our check

| Costs | The finding | Our check | Leads to |
|---|---|---|---|
| blocks the first install | No fallback when python3 is missing or the hook does not runThe hook command in the JSON starts with 'python3' and the page never says Python must be installed, how to check, or what happens on Windows. A junior on a Windows laptop cannot tell whether the install will fail loudly or leave him unprotected.[step 3](#step-3), `/policies/touch-your-secrets/` | confirmedThe settings run python3 and no page says so. On Windows, Claude Code runs hooks in Git Bash, or PowerShell if Git Bash is not installed; a hook that cannot start lets the action through. | [P11](/feedback/reviews/index.md#p11) |
| costs time | 'Start a new session' is not explained for the VS Code extensionBelow 'Or by hand' the page says 'Then start a new session, or open /hooks'. Step 5 on /start-here/ repeats 'Start a new session first'. Neither says what that means in the extension, and the hook only works after it.[step 3](#step-3), `/policies/touch-your-secrets/` | confirmedWorse than the finding: the instruction is out of date. Claude Code applies changes to hooks in the running session. | [P10](/feedback/reviews/index.md#p10) |
| costs trust | Try it lists two outcomes only; there is no 'it did not work' branchStep 3 gives 'With the behaviour policy' and 'Without it', and the page ends in rating boxes. A reader whose prompt does nothing or errors has no next step, and the page's own leave condition is that he cannot tell if it worked.[step 4](#step-4), `/policies/touch-your-secrets/` | confirmedTry it gave only the two outcomes. | [P11](/feedback/reviews/index.md#p11), [D4](/feedback/reviews/index.md#d4) |
| costs trust | Balance falls as you scroll, with the price disclosed only in small printThe top-bar pill goes £50.00 to £49.90 on arrival and keeps dropping to £49.50 while he reads. The eyebrow says 'This page costs 50p read to the end', but the 'Don't charge me' link sits at the very bottom, after the charge has happened.[step 2](#step-2), `/policies/touch-your-secrets/` | confirmedAs for Sam. | [P9](/feedback/reviews/index.md#p9) |
| costs time | 'What this is, and what it is not' reads as a to-do and uses unexplained terms'Neither half is a boundary' followed by a 'boundary' bullet telling him to turn on the sandbox looks like a second required step. 'Expectation', 'setting', 'barrier' and RM-R0015 are not explained, and the page does not say that the sandbox is optional.[step 6](#step-6), `/policies/touch-your-secrets/` | confirmedThe stronger controls read as a second required step; nothing says they are optional. | [P4](/feedback/reviews/index.md#p4) |
| minor | Start-here page opens with internal status text and a dropdown that covers contentThe page begins with 'Status, from docs/reality.md' and green 'shipped v0.1.0' tags, which are meaningless to a new installer. In the later screenshot the open Start-here dropdown sits over step 4 and hides it.[step 11](#step-11), `/start-here/` | partlyThe status line at the top of start here holds. The dropdown over step 4 was our helper: the mouse stayed where it clicked the menu, and the menu opens on hover. | [P16](/feedback/reviews/index.md#p16) |

The whole study: [study S1](/feedback/synthetic/index.md). Every review and proposal: [the reviews](/feedback/reviews/index.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/synthetic/tomas/)*
