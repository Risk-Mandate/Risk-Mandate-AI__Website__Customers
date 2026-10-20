// ── validate.test.js — the gate's checks against fake fixtures and the real tree ──
//
// Runs under `node --test tests/unit/`. The fake secrets below are assembled at
// runtime from pieces so that this file never contains a value the tripwire
// would match; the tripwire scans tests/ too, as it should. This file is exempt
// from the house-words check for the same reason: it names the words.

'use strict'

const test   = require('node:test')
const assert = require('node:assert/strict')
const path   = require('node:path')

const V = require(path.join(__dirname, '..', '..', 'admin', 'build', 'validate.js'))

const trips = (text) => V.LEAK_PATTERNS.filter(p => p.re.test(text)).map(p => p.name)

test('leak tripwire: catches each fake shape', () => {
    const fakes = {
        'sgit vault key'             : 'sgit_private_' + 'vault_' + 'FAKEFAKEFAKE0000',
        'sgit read key'              : 'sgit_private_' + 'read_' + 'FAKEFAKEFAKE0000',
        'sgit write token'           : 'sgit_' + 'write_' + 'FAKEFAKEFAKE0000',
        'sgit passphrase:vault_id'   : 'apple-banana-cherry' + ':' + '12345678-1234-1234-1234-123456789abc',
        'AWS access key id'          : 'AK' + 'IA' + 'FAKEFAKEFAKEFAKE',
        'GitHub token'               : 'gh' + 'p_' + 'F'.repeat(36),
        'sk- API key'                : 'sk-' + 'or-' + 'FAKE'.repeat(8),
        'PEM private key block'      : '-----BEGIN ' + 'RSA PRIVATE KEY-----',
        'Slack token'                : 'xox' + 'b-' + '1234-FAKEFAKEFAKE',
        'Google OAuth client secret' : 'GOC' + 'SPX-' + 'FAKEFAKEFAKEFAKE',
        'service-account JSON'       : '"private_' + 'key_id": "abc"',
        'append token (64 hex)'      : 'append_' + 'token": "' + 'a'.repeat(64),
        'bare 12-digit number'       : 'account ' + '1234567890' + '12' + ' here',
    }
    for (const [name, value] of Object.entries(fakes)) {
        assert.ok(trips(value).includes(name), `${name} should trip on ${value}`)
    }
})

test('leak tripwire: does not trip on the shapes the docs write about', () => {
    const benign = [
        'the prefix `sgit_private_vault_` is shown on the entry',
        'AWS `AKIA/ASIA`, GitHub `gh[pousr]_`, `sk-`/`sk-ant-`',
        'sha256:0a60b38e069682f98c906a36d21dff8665d54a6048cc4f8bd21dca445892e7df',
        '217,266 lines and 1,234,567,890,123 bytes',
    ]
    for (const text of benign) assert.deepEqual(trips(text), [], `should not trip: ${text}`)
})

test('house words: each rule trips on its shape and not on the allowed form', () => {
    const bad = [
        ['ADP', 'the A' + 'DP for this agent'],
        ['the policy', 'read ' + 'the policy first'],
        ['rung', 'the next ' + 'rung of the ladder'],
        ['score', 'the agent was ' + 'rated 7/10'],
        ['out of 100', 'a result of 80 ' + 'out of 100'],
        ['behavior', 'agent ' + 'behavior policy'],
        ['beta users', 'our ' + 'beta users liked it'],
    ]
    for (const [label, text] of bad) assert.equal(V.wordProblems('x.md', text).length, 1, `${label} should trip: ${text}`)
    const good = [
        'the ABP, spelled out as Agent Behaviour Policy at first use',
        'the behaviour policy beside the prompt; a policy beside the prompt',
        'the seven steps of the ladder',
        'an Agent Behaviour Policy carries no score',
        'the lead authorised it; the licence is the instrument',
        'customers, not beta users',
        'the policy beside the prompt',
    ]
    for (const text of good) assert.deepEqual(V.wordProblems('x.md', text), [], `should not trip: ${text}`)
})

test('house words: the verbatim brief and the memo are exempt', () => {
    assert.ok(V.WORD_EXEMPT.includes('docs/brief/our-first-customers.md'))
    assert.ok(V.WORD_EXEMPT.includes('docs/brief/memos/'))
})

test('headingSlug follows GitHub anchors', () => {
    assert.equal(V.headingSlug('Shipped (12)'), 'shipped-12')
    assert.equal(V.headingSlug('Customers, not beta users'), 'customers-not-beta-users')
    assert.equal(V.headingSlug('What a human must do'), 'what-a-human-must-do')
})

test('isInternalLink', () => {
    assert.equal(V.isInternalLink('/admin/'), true)
    assert.equal(V.isInternalLink('../index.md'), true)
    assert.equal(V.isInternalLink('#top'), true)
    assert.equal(V.isInternalLink('https://riskmandate.ai/'), false)
    assert.equal(V.isInternalLink('mailto:x@example.com'), false)
    assert.equal(V.isInternalLink('//cdn.example/x.js'), false)
})

test('resolveLink maps directories to index.html and keeps fragments', () => {
    assert.deepEqual(V.resolveLink('admin/index.html', '/'), { rel : 'index.html', fragment : null })
    assert.deepEqual(V.resolveLink('admin/index.html', '/admin/'), { rel : 'admin/index.html', fragment : null })
    assert.deepEqual(V.resolveLink('admin/versions.html', '../docs/ops/release.md#the-version'), { rel : 'docs/ops/release.md', fragment : 'the-version' })
})

test('nextVersionOk: next minor, patch, or major .0.0', () => {
    assert.equal(V.nextVersionOk(null, '0.1.0'), true)
    assert.equal(V.nextVersionOk('0.1.0', '0.2.0'), true)
    assert.equal(V.nextVersionOk('0.2.0', '0.2.1'), true)
    assert.equal(V.nextVersionOk('0.9.3', '1.0.0'), true)
    assert.equal(V.nextVersionOk('0.1.0', '0.3.0'), false)
    assert.equal(V.nextVersionOk('0.1.0', '0.1.2'), false)
})

test('every check passes on the real tree', () => {
    for (const check of V.CHECKS) {
        assert.deepEqual(check.run(V.ROOT), [], `check ${check.n} ${check.name}`)
    }
})
