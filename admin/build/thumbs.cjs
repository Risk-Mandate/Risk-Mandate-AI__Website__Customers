// thumbs.cjs : the pictures on the home page's cards, so a reader sees where each one goes before they click (R002).
// Each is the first screen of its page under the header, or the element named, from a local copy (SITE, default
// http://127.0.0.1:8765), at 1280 wide, saved as a 640x400 WebP in assets/cards/. Run it after a page they show changes:
//   node admin/build/thumbs.cjs
const { chromium } = require('playwright')
const { execFileSync } = require('child_process')
const path = require('path')
const SITE = process.env.SITE || 'http://127.0.0.1:8765'
const OUT  = path.join(__dirname, '..', '..', 'assets', 'cards')
const CARDS = [
  { name: 'what-is-an-abp', url: '/what-is-an-abp/', sel: '.sb-host', wait: 6000 },
  { name: 'examples',       url: '/examples/' },
  { name: 'start-here',     url: '/start-here/' },
  { name: 'feedback',       url: '/feedback/' },
]
;(async () => {
  const browser = await chromium.launch({ executablePath: process.env.SYNTH_CHROMIUM || '/opt/pw-browsers/chromium' })
  for (const c of CARDS) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1, reducedMotion: 'reduce' })
    await page.goto(SITE + c.url, { waitUntil: 'networkidle' })
    await page.waitForTimeout(c.wait || 500)
    let clip = { x: 0, y: 113, width: 1280, height: 800 }
    if (c.sel) { const b = await page.locator(c.sel).first().boundingBox(); clip = { x: b.x, y: b.y, width: b.width, height: b.width * 10 / 16 } }
    const png = path.join(OUT, c.name + '.png')
    await page.screenshot({ path: png, clip, fullPage: true })
    execFileSync('python3', ['-c', `from PIL import Image; im = Image.open(${JSON.stringify(png)}).convert('RGB').resize((640, 400), Image.LANCZOS); im.save(${JSON.stringify(png.replace(/\.png$/, '.webp'))}, 'WEBP', quality=72, method=6)`])
    require('fs').unlinkSync(png)
    console.log(c.name)
    await page.close()
  }
  await browser.close()
})()
