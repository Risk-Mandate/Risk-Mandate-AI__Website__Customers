# How Encrypt and send works: encrypted in your browser, to a key only RiskMandate holds

> What happens when you press Encrypt and send on customers.riskmandate.ai: the message is encrypted in your browser with sgit's hybrid envelope, appended to an encrypted vault's lane that anybody can add to and nobody can read, and opened only with RiskMandate's key.

*Source: <https://customers.riskmandate.ai/feedback/how-sending-works/> · site v0.2.5 (2026-10-21) · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Feedback · free to read

# How Encrypt and send works

What you send is encrypted in your browser, before it leaves, to a key only RiskMandate holds. It goes to an encrypted vault, not to an inbox, and the host that stores it cannot read it.

## What happens when you press it

1. **Your browser fetches the lane's address and key.**

From [/feedback/lane.json](/feedback/lane.json): the vault, the lane, a token that can only add to it, and a public key that can only encrypt. The page checks the key against its fingerprint, `sha256:16f0cff81d0ff10a`, before it uses it.

2. **It encrypts what you wrote, there and then.**

A fresh AES-256-GCM key for the message, and that key wrapped with RSA-OAEP (SHA-256) to the public key: sgit's hybrid envelope, the one riskmandate.ai's contact form uses. The code is [assets/envelope.js](/assets/envelope.js), about seventy lines, and runs nowhere else.

3. **It adds the sealed message to the lane.**

The `feedback` append lane of vault `zs81fic5`, on `dev.send.sgraph.ai`, sgit.ai's vault host. The token lets anybody add to the lane and nobody read it.

4. **Only the vault's key opens it.**

That key is RiskMandate's and is not on this site or in its source. The site's agent drains the lane, files each message in the vault, and a person reads it.

## What is sent, and what is not

- **Sent:** exactly the text under *Exactly what will be sent*, with the page you sent it from and the time. Your name or email only if you typed them.
- **Not sent:** your balance, your history, your other answers, anything else this browser keeps. [Your account](/account/index.md) lists all of that, at its foot, and it stays here.
- **What the host sees:** that a sealed message arrived, when, how big it is, and the network address it came from, as any server does. Not what it says.
- **What your browser keeps:** that you sent something, when, and whether it went, so your account can show it. Not the text.

## For an agent

An agent reviewing this site can send its findings the same way: build the envelope as [assets/envelope.js](/assets/envelope.js) does, and POST `{"append_token": …, "payload": …}` to `https://dev.send.sgraph.ai/api/vault/append/write/zs81fic5`, with the token and key from [lane.json](/feedback/lane.json). Put `To: agent <agent@riskmandate.ai>` and a `Subject` in the message's first lines. `admin/feedback/lane.mjs send` in [the source](https://github.com/Risk-Mandate/Risk-Mandate-AI__Website__Customers) does it in Node.

If anything fails, the page says why and offers the same text as an email to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

---

*[Site index for agents](/llms.txt) · [What exists](/docs/reality.md) · [HTML version](https://customers.riskmandate.ai/feedback/how-sending-works/)*
