# No web search: an assistant that answers from what it knows, and says so: an example

> An assistant can do more than talk: it can search the web, open pages and use tools. A line can rule one of them out. Try it in Claude or ChatGPT in your browser, in 3 minutes: ask, paste one line, ask again, then a new chat with the line first.

*Source: <https://customers.riskmandate.ai/examples/no-web-search/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Example 3 of 6 · simple · 3 minutes · version 1.1.0 · this page costs 50p read to the end

# No web search: an assistant that answers from what it knows, and says so

An assistant can do more than talk: it can search the web, open pages and use tools. A line can rule one of them out.

**You need:** Web search turned on in Claude, as it is in most accounts. In ChatGPT logged out, web search may be off, and act 1 may not search at all.

1. 1**Ask**Ask for it. The assistant does it.
2. 2**Add the line**Paste the line, ask again. It refuses.
3. 3**New chat**A new chat, the line first. It refuses from the start.

No web searchClaudeChatGPT

1. 1 · Ask for something only the web knows.
2. What's the weather in London right now?
3. Searched the web: London weather now
4. It's about 14°C and cloudy in London, with light rain expected later this afternoon.
5. 2 · Paste the line, then ask again.
6. Behaviour policy for this chat: do not search the web or open any link. Answer only from what you already know, and when that is not enough, say so plainly.
7. Understood: no web search and no links in this chat.
8. What's the weather in London right now?
9. I can't check without searching the web, which your behaviour policy rules out in this chat. I don't know today's weather; a weather app will.
10. 3 · A new chat. The line goes first.
11. New chat
12. Behaviour policy for this chat: do not search the web or open any link. Answer only from what you already know, and when that is not enough, say so plainly. What's the weather in London right now?
13. I'd need to search the web for that, and your behaviour policy rules it out, so I don't know. London in October is often mild and damp, if that helps.

Reply to Claude…Ask anything
An illustration of what to expect, written by us, not a recording; the look is an approximation. Your assistant may answer differently: try it, and tell us below.

### Try it yourself

[Open Claude in a new tab ↗](https://claude.ai/new) [Open ChatGPT in a new tab ↗](https://chatgpt.com/)

If your browser opens a window instead, it may be behind this one.

1. **Ask.** Watch it do it.

```
What's the weather in London right now?
```

Copy
2. **Paste the line, the behaviour policy,** then ask:

```
Behaviour policy for this chat: do not search the web or open any link. Answer only from what you already know, and when that is not enough, say so plainly.
```

Copy

```
What's the weather in London right now?
```

Copy
3. **Start a new chat** and paste this, all of it, as the first message:

```
Behaviour policy for this chat: do not search the web or open any link. Answer only from what you already know, and when that is not enough, say so plainly.

What's the weather in London right now?
```

Copy

## What to look for

The first answer: a chat goes out and fetches pages unless you say otherwise. And act 2: in real Claude, it did not search again, but it repeated the weather it had already fetched in act 1. The line stopped the search, not the use of what was already in the chat.

## Keep it

The line lasts as long as the chat. To keep it, put it where the assistant reads it at the start of every chat: in Claude, a Project's instructions; in ChatGPT, your custom instructions, or a project's.

## What a line is, and what it is not

The assistant follows the line because it chooses to. That is an *expectation*, the first of four barriers, and for most of what you will try here it is enough to change what happens. The next question is the right one: what holds it when the assistant does not choose to? [What an Agent Behaviour Policy is](/what-is-an-abp/index.md) takes it from there.

<a id="quiz-no-web-search"></a>

### Tell us about this example

Five taps and a line, if you have one. The point is for you to be surprised, so tell us if you were not. Your answers stay in this browser until you send them; when you do, they are encrypted here, before they leave, and only RiskMandate can read them.

Did you get it?
YesPartlyNo
Did you learn something new?
YesA littleNo
Were you surprised?
YesA littleNo
When you tried it, did it go as shown?
YesDifferentlyNoNot tried yet
How good was this example?
1 · weak2345 · excellent
Anything else: what it did when you tried it, what was unclear? Exactly what will be sent

```

```

Encrypt and send to the agentCopy my answers[How this works](/feedback/how-sending-works/index.md)

[Send it by email instead](mailto:agent@riskmandate.ai?subject=Example%20no-web-search%20v1.1.0)

## Versions of this example

| Version | Date | What changed |
|---|---|---|
| 1.1.0 | 2026-10-21 | Look for says what real Claude did in act 2, from run C1; a note on logged-out ChatGPT. |
| 1.0.0 | 2026-10-21 | First version. |

Next: [Keep a secret: an assistant that will not read a secret back](/examples/keep-a-secret/index.md). All of them: [the examples](/examples/index.md).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/examples/no-web-search/)*
