/* Shared by every browser test: where Playwright is, where the app is served,
   and where screenshots go. Override with PLAYWRIGHT, BASE_URL, or PORT. */
import { mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

async function loadPlaywright(){
  const tries=[process.env.PLAYWRIGHT,'playwright','/opt/node22/lib/node_modules/playwright/index.mjs'].filter(Boolean);
  for(const t of tries){try{return await import(t)}catch(e){}}
  console.error('Playwright not found. Run `npm i -D playwright` or set PLAYWRIGHT=/path/to/playwright/index.mjs');
  process.exit(2);
}
export const { chromium } = await loadPlaywright();
export const BASE = process.env.BASE_URL || ('http://127.0.0.1:'+(process.env.PORT||8885)+'/');
export const OUT = fileURLToPath(new URL('./out/', import.meta.url));
mkdirSync(OUT,{recursive:true});

/* One browser, one phone-size page, a checklist, and a clock we control.
   `at` is the local time the page thinks it is ("07:30" or a full date). */
export async function start({ at = '2026-10-05T07:30:00', width = 390, height = 844 } = {}) {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width, height }, serviceWorkers: 'block' });
  const p = await ctx.newPage();
  await p.clock.install({ time: new Date(at.length <= 5 ? '2026-10-05T' + at + ':00' : at) });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  let ok = true;
  const chk = (n, c, x = '') => { if (!c) ok = false; console.log((c ? '  ok  ' : 'FAIL  ') + n + (x ? ': ' + x : '')) };
  /* Unless told it's a fresh device, the player has already done setup as Liem. */
  const open = async (seed, { fresh = false } = {}) => {
    const s = Object.assign(fresh ? {} : { gdKid: JSON.stringify({ setup: true, name: 'Liem' }) }, seed || {});
    await p.goto(BASE, { waitUntil: 'domcontentloaded' });
    await p.evaluate(s => { localStorage.clear(); for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v) }, s);
    await p.reload({ waitUntil: 'domcontentloaded' });
    await p.waitForTimeout(150);
  };
  const reload = async () => { await p.reload({ waitUntil: 'domcontentloaded' }); await p.waitForTimeout(150) };
  const shot = name => p.screenshot({ path: OUT + name + '.png' });
  const done = async () => {
    console.log('\n' + (errs.length ? 'ERRORS: ' + errs.join('; ') : 'NO JS ERRORS'));
    await b.close();
    process.exit(ok && !errs.length ? 0 : 1);
  };
  return { b, ctx, p, chk, open, reload, shot, done };
}
