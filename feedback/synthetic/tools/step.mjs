// step.mjs : one action of a synthetic run, and the screenshot after it. The persona agent calls only this.
//   node step.mjs <run dir> start <url> <width> <height> [mobile]
//   node step.mjs <run dir> goto <path> | click <x> <y> | clicktext "<text>" | scroll <px> | back | look | end
// Prints the screenshot's path, the page's address and how far down it is. Open the screenshot and decide from it alone.
import { spawn } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const [runDir, cmd, ...args] = process.argv.slice(2)
if (!runDir || !cmd) { console.error('usage: node step.mjs <run dir> <action> [args]'); process.exit(2) }
fs.mkdirSync(runDir, { recursive: true })
const portFile = path.join(runDir, '.driver')

async function send(payload) {
  const port = fs.readFileSync(portFile, 'utf8').trim()
  const res  = await fetch(`http://127.0.0.1:${port}/`, { method: 'POST', body: JSON.stringify(payload) })
  const text = await res.text()
  if (!res.ok) { console.error(text); process.exit(1) }
  console.log(text)
}

if (cmd === 'start') {
  const [url, w, h, mobile] = args
  if (fs.existsSync(portFile)) { console.error('this run already has a browser; send actions, or `end` it first'); process.exit(1) }
  const driver = spawn(process.execPath, [path.join(path.dirname(fileURLToPath(import.meta.url)), 'driver.mjs'), runDir, w || '1440', h || '900', ...(mobile ? ['mobile'] : [])],
                       { detached: true, stdio: 'ignore', cwd: process.cwd() })
  driver.unref()
  for (let i = 0; i < 100 && !fs.existsSync(portFile); i++) await new Promise(r => setTimeout(r, 150))
  if (!fs.existsSync(portFile)) { console.error('the browser did not start'); process.exit(1) }
  await send({ cmd: 'start', args: [url] })
} else {
  if (!fs.existsSync(portFile)) { console.error('no browser for this run; `start` one first'); process.exit(1) }
  await send({ cmd, args })
}
