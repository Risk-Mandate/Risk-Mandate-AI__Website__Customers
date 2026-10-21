// ── envelope.js — Encrypt and send: sgit's hybrid envelope, made in the browser, appended to the feedback lane ──
//
// The envelope (v2) matches sgit_ai's PKI hybrid_encrypt and riskmandate.ai's contact form: a fresh
// AES-256-GCM key and a 12-byte IV for the message, the key wrapped with RSA-OAEP (SHA-256) to the
// lane's public key; {v:2, w, i, c} as base64 fields; the .enc text is base64 of that JSON, and the
// lane payload is base64 of the .enc text. The lane is named in /feedback/lane.json, with its public
// append token, which can only add to the lane, and its public key, which can only encrypt; the page
// checks the key against its fingerprint before it uses it. Only the vault's own key, held by
// RiskMandate and not on this site, can read what arrives. What was sent, and when, is kept in this
// browser under riskmandate.customers.sent, for the account page; the text itself is not kept.
// How it works, for people: /feedback/how-sending-works/.

(function (root) {
    'use strict'
    const SENT = 'riskmandate.customers.sent'
    const te   = new TextEncoder()
    const b64  = (bytes) => { let s = ''; bytes = new Uint8Array(bytes); for (let i = 0; i < bytes.length; i++) s += String.fromCharCode(bytes[i]); return btoa(s) }
    const der  = (pem) => { const bin = atob(pem.replace(/-----[^-]+-----/g, '').replace(/\s+/g, '')); const out = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i); return out.buffer }
    const utf8b64 = (s) => b64(te.encode(s))

    async function fingerprint(pem) {
        const h = await crypto.subtle.digest('SHA-256', der(pem))
        return 'sha256:' + Array.from(new Uint8Array(h), (x) => x.toString(16).padStart(2, '0')).join('').slice(0, 16)
    }

    async function encrypt(pem, plaintext) {
        const pub = await crypto.subtle.importKey('spki', der(pem), { name: 'RSA-OAEP', hash: 'SHA-256' }, false, ['encrypt'])
        const aes = await crypto.subtle.generateKey({ name: 'AES-GCM', length: 256 }, true, ['encrypt'])
        const raw = await crypto.subtle.exportKey('raw', aes)
        const iv  = crypto.getRandomValues(new Uint8Array(12))
        const c   = await crypto.subtle.encrypt({ name: 'AES-GCM', iv, tagLength: 128 }, aes, te.encode(plaintext))
        const w   = await crypto.subtle.encrypt({ name: 'RSA-OAEP' }, pub, raw)
        const enc = utf8b64(JSON.stringify({ v: 2, w: b64(w), i: b64(iv), c: b64(c) }))
        return utf8b64(enc)
    }

    function remember(entry) {
        try {
            const all = JSON.parse(root.localStorage.getItem(SENT) || '[]')
            all.unshift(entry)
            root.localStorage.setItem(SENT, JSON.stringify(all.slice(0, 200)))
        } catch (e) { /* private window: fine */ }
    }

    // send({ form, subject, body, about }) → { ok, why }: encrypt in this browser and append to the lane
    async function send({ form, subject, body, about }) {
        const at = new Date().toISOString()
        try {
            if (!root.crypto || !crypto.subtle) throw new Error('this browser cannot encrypt here')
            const lane = await (await fetch('/feedback/lane.json', { cache: 'no-store' })).json()
            if (!lane || lane.status !== 'open' || !lane.append_token) throw new Error('the feedback lane is not open')
            if (await fingerprint(lane.encrypt_pem) !== lane.encrypt_to) throw new Error('the key does not match its fingerprint')
            const id  = `rm-customers-${form}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}@customers.riskmandate.ai`
            const eml = [`From: web form <site@customers.riskmandate.ai>`, `To: agent <${lane.to}>`, `Subject: ${subject.replace(/[\r\n]+/g, ' ')}`,
                         `Date: ${new Date().toUTCString()}`, `Message-ID: <${id}>`, `X-RM-Form: ${form}`, `X-RM-Page: ${location.pathname}`,
                         'Content-Type: text/plain; charset=utf-8', '', body].join('\r\n')
            const r = await fetch(`${lane.endpoint}/api/vault/append/write/${lane.vault}`, { method: 'POST', headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify({ append_token: lane.append_token, payload: await encrypt(lane.encrypt_pem, eml) }) })
            let j = null
            try { j = await r.json() } catch (e) { /* not JSON */ }
            if (!r.ok || !j || j.ok !== true) throw new Error(`the vault host answered ${r.status}`)
            remember({ at, form, about, ok: true, to: lane.encrypt_to })
            return { ok: true }
        } catch (err) {
            remember({ at, form, about, ok: false, why: String(err.message || err) })
            return { ok: false, why: String(err.message || err) }
        }
    }

    root.RMSend = { send, encrypt, fingerprint }
})(window)
