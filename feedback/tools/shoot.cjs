// shoot.cjs <spec.json> <out dir> : the screenshots a review cites, element by element, from a copy of the site served locally (SITE, default http://127.0.0.1:8765).
// Each spec entry: {name, url, w, h, sel (a selector, or a list whose boxes are joined), pad, maxh, mobile, wait, motion}. Convert the PNGs to WebP into assets/feedback/<review id>/.
const { chromium } = require('playwright');
const fs = require('fs');
const [spec, out] = process.argv.slice(2);
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', headless: true });
  for (const s of JSON.parse(fs.readFileSync(spec, 'utf8'))) {
    const ctx = await browser.newContext({ viewport: { width: s.w, height: s.h }, isMobile: !!s.mobile, hasTouch: !!s.mobile, deviceScaleFactor: s.mobile ? 2 : 1, reducedMotion: s.motion ? 'no-preference' : 'reduce' });   // still by default; "motion": true to see what plays
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto((process.env.SITE || 'http://127.0.0.1:8765') + s.url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(s.wait || 400);
    let clip = null;
    if (s.sel) {
      const boxes = [];
      for (const sel of [].concat(s.sel)) { const el = page.locator(sel).first(); await el.scrollIntoViewIfNeeded(); boxes.push(await el.boundingBox()); }
      const sy = await page.evaluate(() => window.scrollY);
      const pad = s.pad ?? 16;
      const x0 = Math.max(0, Math.min(...boxes.map(b => b.x)) - pad), y0 = Math.max(0, Math.min(...boxes.map(b => b.y)) - pad + sy);
      const x1 = Math.min(s.w, Math.max(...boxes.map(b => b.x + b.width)) + pad), y1 = Math.max(...boxes.map(b => b.y + b.height)) + pad + sy;
      clip = { x: x0, y: y0, width: x1 - x0, height: Math.min(y1 - y0, s.maxh || 99999) };
    }
    await page.screenshot({ path: `${out}/${s.name}.png`, fullPage: !!clip, clip: clip || undefined });
    console.log(s.name, clip ? `${Math.round(clip.width)}x${Math.round(clip.height)}` : 'viewport', errors.length ? errors : 'ok');
    await ctx.close();
  }
  await browser.close();
})();
