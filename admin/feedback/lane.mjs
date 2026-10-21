#!/usr/bin/env node
// ═══════════════════════════════════════════════════════════════════════════════
// customers.riskmandate.ai — the feedback lane
// What Encrypt and send writes to: the `feedback` append lane of a private sgit vault on
// dev.send.sgraph.ai, named in feedback/lane.json with its public append token and the
// public key the browser encrypts to (sgit's hybrid envelope v2: AES-256-GCM, the key
// wrapped with RSA-OAEP SHA-256, the same as assets/envelope.js). Three commands:
//
//   FEEDBACK_KEY=<vault key> SG_SEND_ACCESS_TOKEN=<host credential> node admin/feedback/lane.mjs configure --vault <clone>
//   node admin/feedback/lane.mjs send "a line of text"                    # a test send, as a browser would; needs nothing secret
//   FEEDBACK_KEY=<vault key> node admin/feedback/lane.mjs drain --vault <clone> [--dry-run]
//
// configure registers the lane's anchor (the token's sha256) and the listing key's hash; it is
// the owner's call, so it needs the host credential. drain lists the lane with the listing key,
// fetches each file, decrypts it with the private key kept in the vault (encrypted at rest with a
// passphrase derived from the write key), files it under feedback-lane/inbox/<file>.eml with its
// .enc beside it, appends a line to feedback-lane/log.jsonl and marks it processed. Then commit
// and push the clone:  cd <clone> && sgit commit "drain: <n>" && sgit push --token "$SG_SEND_ACCESS_TOKEN"
// The vault key comes only from the environment and is never written anywhere.
// ═══════════════════════════════════════════════════════════════════════════════
import { readFileSync, writeFileSync, mkdirSync, existsSync, appendFileSync } from 'node:fs'
import { join, dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { createHmac, createHash, createPrivateKey, createPublicKey, privateDecrypt, publicEncrypt, createCipheriv, createDecipheriv, randomBytes, constants } from 'node:crypto'
import { execFileSync } from 'node:child_process'

const ROOT  = resolve(dirname(fileURLToPath(import.meta.url)), '../..')
const LANE  = JSON.parse(readFileSync(join(ROOT, 'feedback', 'lane.json'), 'utf8'))
const [cmd, ...rest] = process.argv.slice(2)
const arg   = (f, d) => { const i = rest.indexOf(f); return i >= 0 ? rest[i + 1] : d }
const sha   = (s) => createHash('sha256').update(s).digest('hex')

function derived() {
    const key = process.env.FEEDBACK_KEY
    if (!key) { console.error('FEEDBACK_KEY is not set'); process.exit(2) }
    const d = execFileSync(process.env.SGIT || 'sgit', ['vault', 'derive-keys', key], { encoding: 'utf8' })
    const vaultId = /vault_id:\s+(\S+)/.exec(d)[1], writeKey = /write_key:\s+([0-9a-f]+)/.exec(d)[1]
    if (vaultId !== LANE.vault) { console.error(`the key opens ${vaultId}; feedback/lane.json names ${LANE.vault}`); process.exit(2) }
    const hm = (l) => createHmac('sha256', Buffer.from(writeKey, 'hex')).update(l).digest('hex')
    return { vaultId, writeKey, hm, enumKey: hm('agent-contact/enum-key/v1') }
}

async function call(path, body, headers) {
    const r = await fetch(`${LANE.endpoint}/api/vault/append/${path}/${LANE.vault}`, { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: JSON.stringify(body) })
    const t = await r.text()
    if (!r.ok) throw new Error(`${path} → ${r.status} ${t.slice(0, 120).replace(/\s+/g, ' ')}`)
    return JSON.parse(t)
}

function seal(plaintext) {                                                        // the envelope a browser makes, for a test send
    const aes = randomBytes(32), iv = randomBytes(12)
    const c = createCipheriv('aes-256-gcm', aes, iv)
    const ct = Buffer.concat([c.update(plaintext, 'utf8'), c.final(), c.getAuthTag()])
    const w = publicEncrypt({ key: LANE.encrypt_pem, padding: constants.RSA_PKCS1_OAEP_PADDING, oaepHash: 'sha256' }, aes)
    const enc = Buffer.from(JSON.stringify({ v: 2, w: w.toString('base64'), i: iv.toString('base64'), c: ct.toString('base64') })).toString('base64')
    return Buffer.from(enc).toString('base64')
}

function open(content, priv) {
    const env = JSON.parse(Buffer.from(Buffer.from(content, 'base64').toString('utf8'), 'base64').toString('utf8'))
    if (env.v !== 2) throw new Error(`envelope v${env.v}`)
    const aes = privateDecrypt({ key: priv, padding: constants.RSA_PKCS1_OAEP_PADDING, oaepHash: 'sha256' }, Buffer.from(env.w, 'base64'))
    const c = Buffer.from(env.c, 'base64'), dc = createDecipheriv('aes-256-gcm', aes, Buffer.from(env.i, 'base64'))
    dc.setAuthTag(c.subarray(c.length - 16))
    return Buffer.concat([dc.update(c.subarray(0, c.length - 16)), dc.final()]).toString('utf8')
}

if (cmd === 'configure') {
    const { writeKey, enumKey } = derived()
    const token = process.env.SG_SEND_ACCESS_TOKEN
    if (!token) { console.error('SG_SEND_ACCESS_TOKEN is not set'); process.exit(2) }
    const lanes = JSON.parse(readFileSync(join(arg('--vault', 'customers-feedback'), 'feedback-lane', 'lanes.json'), 'utf8')).lanes
    if (lanes.feedback.anchor !== sha(LANE.append_token)) { console.error('the token in feedback/lane.json does not hash to the anchor in the vault'); process.exit(2) }
    console.log(await call('configure', { append_anchors: [sha(LANE.append_token)], enum_key_hash: sha(enumKey) }, { 'x-sgraph-vault-write-key': writeKey, 'x-sgraph-access-token': token }))
} else if (cmd === 'send') {
    const text = rest.join(' ') || 'a test send'
    const eml = ['From: test <site@customers.riskmandate.ai>', `To: agent <${LANE.to}>`, `Subject: Test send: ${text.slice(0, 60)}`, `Date: ${new Date().toUTCString()}`,
                 `Message-ID: <test-${Date.now()}@customers.riskmandate.ai>`, 'X-RM-Form: test', 'Content-Type: text/plain; charset=utf-8', '', text].join('\r\n')
    console.log(await call('write', { append_token: LANE.append_token, payload: seal(eml) }, {}))
} else if (cmd === 'drain') {
    const { hm, enumKey } = derived()
    const dir = arg('--vault', 'customers-feedback'), dry = rest.includes('--dry-run')
    const priv = createPrivateKey({ key: readFileSync(join(dir, 'feedback-lane', 'keys', 'feedback.encrypt.pem')), passphrase: hm('agent-contact/key-pass/feedback/v1') })
    const fp = 'sha256:' + sha(createPublicKey(priv).export({ type: 'spki', format: 'der' })).slice(0, 16)
    if (fp !== LANE.encrypt_to) { console.error(`the private key is ${fp}; feedback/lane.json says ${LANE.encrypt_to}`); process.exit(2) }
    const inbox = join(dir, 'feedback-lane', 'inbox'); mkdirSync(inbox, { recursive: true })
    let after = null, n = 0
    for (;;) {
        const page = await call('list', { include_content: false, ...(after ? { after_file_id: after } : {}) }, { 'x-sgraph-vault-enum-key': enumKey })
        const entries = page.entries || []
        for (const e of entries) {
            const f = await call('fetch', { inbox: e.inbox, file_ids: [e.file_id] }, { 'x-sgraph-vault-enum-key': enumKey })
            const content = f.files?.[0]?.content
            let eml = null, why = ''
            try { eml = open(content, priv) } catch (err) { why = String(err.message || err) }
            const base = join(inbox, e.file_id.replace(/\.enc$/, ''))
            const subject = eml ? (/^Subject: (.*)$/m.exec(eml) || [])[1] : null
            console.log(eml ? `${e.file_id}  ${subject}` : `${e.file_id}  could not open: ${why}`)
            if (!dry) {
                writeFileSync(base + '.enc', Buffer.from(content, 'base64').toString('utf8'))
                if (eml) writeFileSync(base + '.eml', eml)
                appendFileSync(join(dir, 'feedback-lane', 'log.jsonl'), JSON.stringify({ file: e.file_id, received: e.received, subject, result: eml ? 'opened' : 'quarantine', why }) + '\n')
                await call('mark-processed', { inbox: e.inbox, file_ids: [e.file_id] }, { 'x-sgraph-vault-enum-key': enumKey })
            }
            n++
        }
        if (!page.next_after && !page.has_more) break
        after = page.next_after || entries.at(-1)?.file_id
        if (!after) break
    }
    console.log(`${n} file(s)` + (dry ? ', nothing written (dry run)' : ', filed; now commit and push the clone'))
} else {
    console.error('usage: lane.mjs configure|send|drain  (see the header)')
    process.exit(2)
}
