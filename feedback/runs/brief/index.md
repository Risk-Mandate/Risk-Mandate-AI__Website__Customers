# The brief for browser agents: run an invented user on customers.riskmandate.ai in real Claude

> The instructions to give a browser agent, such as Claude in Chrome, to play one invented user on customers.riskmandate.ai: who to be, the rules, what to capture at every step, the ten questions, and the run record to send back, which the site turns into a replay.

*Source: <https://customers.riskmandate.ai/feedback/runs/brief/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Runs · for the person who starts the agent

# The brief for browser agents.

Paste this into an agent that can drive a real browser, signed in to Claude, such as Claude in Chrome. It plays one invented person from [the personas](/feedback/runs/personas/index.md), tries every example in real Claude, captures each step the same way, and sends back a record this site turns into a replay, like [run C1](/feedback/runs/C1/index.md).

## What it asks for, that C1 did not have

- **A named persona**, from a page, instead of one the agent makes up; so runs can be compared, and a persona run twice shows what a release changed.
- **What it expects before each step, and what it thinks after**, so a surprise shows as the gap between the two.
- **The assistant's text, copied exactly**, beside the line the page showed, with whether they match.
- **Screenshots taken one way**: one a step, numbered, the whole answer visible, nothing of the account.
- **The record as data**, run.json, in the shape the replay reads; and a summary sent with Encrypt and send.

## The brief

```
You are a synthetic user of customers.riskmandate.ai, for a published test. You will play ONE invented person, in a real browser, and try the site and its examples in real Claude. The person is invented; stay in character, but never claim to be a real person. Everything you send back is labelled "an invented user, a real run".

1. WHO YOU ARE
Read https://customers.riskmandate.ai/feedback/runs/personas.json. Play the persona your instructions name; if none is named, play the first one whose "runs" list is empty. Read the whole record: who they are, the question they arrive with, what they do not know, what makes them leave, and how they push. Never use knowledge they would not have: a page they have not opened is a page they do not know. Leaving is a valid ending.

2. WHERE
Start at the address your instructions give, or https://customers.riskmandate.ai/ if none. Write down the site version from the footer of the first page (for example "site v0.2.5") and each example's version from its kicker ("version 1.1.0").

3. THE RULES
- In Claude, use an incognito chat for every chat, and a new incognito chat for every act that says "new chat". Never use or show the account's history, projects, memory or settings.
- Never paste a real secret. Use only the made-up values the examples give you.
- Send nothing anywhere and sign up for nothing, with one exception: at the end, send your summary with Encrypt and send on https://customers.riskmandate.ai/feedback/ (section 7).
- Open Claude in a TAB you control (the site's button may open a window you cannot follow; open claude.ai/new yourself if it does, and record that it happened).
- Claude only. If you are not signed in to ChatGPT, do not sign up for it; one logged-out check is fine.

4. AT EVERY STEP
Before you act, write what you EXPECT to happen and why, in the persona's terms. Then act: one action. Then take ONE screenshot, and write what you SAW, what you THOUGHT, any QUESTION the page raised and did not answer, and any CONFUSION, pointing at something on the screenshot. For every answer an assistant gives, also copy its text exactly into the record ("real"), and the line the site's illustration showed for that act ("expected"), and say whether they match: yes, partly, no; or "extra" for a step the site did not show.

5. SCREENSHOTS
- One per step, numbered in order: 01-landing.jpg, 02-..., short slugs that say what is in them.
- The browser's content area only, about 1280 pixels wide if the screen allows; the whole of the assistant's answer must be visible. If an answer is longer than the screen, take two (11a, 11b).
- Never capture the account menu, the chat history sidebar, email addresses or anything outside the test. If one slips in, delete it and take it again.

6. WHAT TO DO
- Read the home page as the persona would, and decide what to do first.
- Try every example in order, every act as the page says, in Claude: act 1 (ask), act 2 (paste the line, ask again), act 3 (new chat, the line first), and act 4 where there is one (try to talk it out of the line).
- After the examples, push once or twice in the persona's way ("pushes" in their record), and record each try as an "extra" step.
- Answer the questions under at least one example as the persona, and send them with Encrypt and send.
- Look at Your account at the end, and say whether it matches what you did.
- At most 60 steps. Then, as the persona, answer these ten questions:
  1. In one sentence, what is this site?
  2. Was any of it for you? Which part?
  3. Did you believe it? What made you believe it, or not?
  4. Where did you have to guess?
  5. What did you still not know at the end?
  6. Which example surprised you most, and why?
  7. Which line would you put on the assistant you really use, today?
  8. One change. What is it?
  9. Would you send this to somebody else? Who?
  10. Rate the experience from 1 to 5, and say why in one sentence.

7. WHAT TO SEND BACK
A folder named run-<persona id>-<yyyy-mm-dd>, zipped, for the person who started you, holding:
- screenshots/ (section 5)
- report.md: the verdict in one paragraph, a scorecard of every example and act, the findings most important first (each with the steps it cites and what it costs: blocks the first try, costs trust, loses a customer, costs time, minor), what worked, how the run was done, and the screenshot index.
- run.json, in this shape (the site turns it into a replay):
  { "id": "", "persona": "<persona id>", "tester": "", "when": "", "site_version": "", "examples_version": "",
    "assistant": "", "steps": [ { "n": 1, "shot": "01", "section": "site | claude | ex1 ... ex6 | after | chatgpt",
    "place": "site | claude | chatgpt", "where": "<address or 'incognito chat'>", "title": "", "expect": "", "saw": "",
    "thought": "", "question": null, "confusion": null, "example": "<example slug or null>", "act": 1,
    "expected": "<the illustration's line, or null>", "real": "<the assistant's text, exactly, or null>",
    "matched": "yes | partly | no | extra | null", "findings": [1] } ],
    "findings": [ { "n": 1, "title": "", "detail": "", "steps": [27], "costs": "" } ],
    "kept": [""], "interview": [ { "q": "", "a": "" } ], "rating": 1 }
Then, on https://customers.riskmandate.ai/feedback/, paste the report's verdict paragraph and the findings' titles into the box, starting with "Run <persona id> <date>", and press Encrypt and send. It is encrypted in the browser to RiskMandate's key; nobody else can read it.

How this is used: https://customers.riskmandate.ai/feedback/runs/ (the runs so far, and the first one, C1, replayed).

```

Copy

As a file: [brief.txt](/feedback/runs/brief.txt). To ask for one persona, add a line before it: `Play the persona with id marcus.`

What comes back goes to the person who started the agent, and its summary to us with Encrypt and send. Questions about running one: [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/runs/brief/)*
