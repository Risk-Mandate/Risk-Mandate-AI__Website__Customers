// driver.mjs : the browser one synthetic run looks through. step.mjs starts it, once per run, and sends it one action at a time.
// The browser stays open for the whole run, so the page under the persona's finger is the page in the last screenshot, and the
// meter's session survives between steps as it would in a tab. Only the local copy of the site is reachable, and only by GET;
// the two pinned APIs the site loads its code from are allowed, by GET. Everything else is refused and written down.
import { createRequire } from 'node:module'
import http from 'node:http'
import fs from 'node:fs'
import path from 'node:path'

const { chromium } = createRequire(import.meta.url)('playwright')   // CommonJS resolution, so NODE_PATH finds a global install

const [runDir, w, h, mobile] = process.argv.slice(2)
const SITE    = process.env.SYNTH_SITE || 'http://127.0.0.1:8765'
const ALLOWED = [SITE, 'https://api.newsroom.sgit.ai/', 'https://api.storyboards.sgit.ai/']
const capture = path.join(runDir, '_capture.json')
const log     = fs.existsSync(capture) ? JSON.parse(fs.readFileSync(capture, 'utf8')) : { site: SITE, viewport: `${w}x${h}`, mobile: !!mobile, steps: [], refused: [] }
const save    = () => fs.writeFileSync(capture, JSON.stringify(log, null, 2))

const browser = await chromium.launch({ executablePath: process.env.SYNTH_CHROMIUM || '/opt/pw-browsers/chromium', headless: true })
const context = await browser.newContext({ viewport: { width: +w, height: +h }, isMobile: !!mobile, hasTouch: !!mobile, deviceScaleFactor: mobile ? 2 : 1 })
await context.route('**/*', route => {
  const req = route.request()
  if (req.method() === 'GET' && ALLOWED.some(a => req.url().startsWith(a))) return route.continue()
  log.refused.push({ url: req.url(), method: req.method(), at: log.steps.length }); save()
  return route.abort('blockedbyclient')
})
let page = await context.newPage()
context.on('page', p => { page = p })                                            // a link that opens a new tab: the persona is now looking at it

async function settle() {
  try { await page.waitForLoadState('networkidle', { timeout: 8000 }) } catch {}
  await page.waitForTimeout(700)
}

async function shot(cmd, args, note = '') {
  const n    = log.steps.length + 1
  const file = String(n).padStart(2, '0') + '.png'
  await page.screenshot({ path: path.join(runDir, file) })
  const info = await page.evaluate(() => ({ url: location.href, title: document.title, scrollY: Math.round(scrollY), height: document.documentElement.scrollHeight })).catch(() => ({ url: page.url() }))
  log.steps.push({ n, cmd, args, file, note, ...info, at: new Date().toISOString() }); save()
  return `${path.join(runDir, file)}  ${info.url}  scrollY=${info.scrollY}/${info.height}${note ? '  ' + note : ''}`
}

async function act(cmd, args) {
  let note = ''
  if (cmd === 'start' || cmd === 'goto') {
    const url = /^https?:/.test(args[0]) ? args[0] : SITE + (args[0].startsWith('/') ? '' : '/') + args[0]
    await page.goto(url, { waitUntil: 'load' }).catch(e => { note = 'navigation failed: ' + e.message.split('\n')[0] })
  } else if (cmd === 'click') {
    await page.mouse.click(+args[0], +args[1])
  } else if (cmd === 'clicktext') {
    const target = page.getByText(args.join(' '), { exact: false }).locator('visible=true').first()   // the first match a person could see
    if (await target.count() === 0) note = 'no visible text matched'
    else await target.click({ timeout: 4000 }).catch(e => { note = 'click failed: ' + e.message.split('\n')[0] })
  } else if (cmd === 'scroll') {
    await page.mouse.wheel(0, +args[0])
  } else if (cmd === 'back') {
    await page.goBack({ waitUntil: 'load' }).catch(() => { note = 'nothing to go back to' })
  } else if (cmd !== 'look') {
    throw new Error(`unknown action ${cmd}`)
  }
  await settle()
  return shot(cmd, args, note)
}

const server = http.createServer((req, res) => {
  let body = ''
  req.on('data', c => body += c)
  req.on('end', async () => {
    const { cmd, args } = JSON.parse(body || '{}')
    if (cmd === 'end') { res.end('ended'); await browser.close(); server.close(); fs.rmSync(path.join(runDir, '.driver'), { force: true }); process.exit(0) }
    try { res.end(await act(cmd, args || [])) } catch (e) { res.statusCode = 500; res.end(String(e.message || e)) }
  })
})
server.listen(0, '127.0.0.1', () => fs.writeFileSync(path.join(runDir, '.driver'), String(server.address().port)))
