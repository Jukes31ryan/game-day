/* Game Day as its own app: its own name and storage, a good neighbour to the
   other apps on the same site, works offline, and nothing on the page a
   10-year-old shouldn't read. */
import { chromium, BASE, start } from './lib.mjs';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const REPO = fileURLToPath(new URL('..', import.meta.url));
const { b, p, chk, open, reload, shot, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);
const ADULT = /\b(drugs?|drunk|beer|wine|alcohol|booze|therap\w*|sex\w*|kill\w*|murder\w*|suicid\w*|die|died|dies|dying|death|dead|divorc\w*|damn|hell|crap|stupid|idiot|guns?|casino|gambl\w*|bet|bets|betting|odds|cigar\w*|smok\w*)\b/i;

// ───────── its own app ─────────
console.log('— its own app —');
await open();
chk('the tab title is Game Day', (await p.title()) === 'Game Day');
chk('its own storage prefix', await ev(() => KP) === 'gd');
chk('it is v4.3', await ev(() => APP_VERSION) === 'v4.3');
const man = await (await p.request.get(BASE + 'manifest.webmanifest')).json();
chk('the home-screen name is Game Day', man.short_name === 'Game Day' && man.name === 'Game Day');
chk('it installs from its own folder', man.start_url === '.' && man.scope === '.');
/* Chrome decides "already installed" by the manifest id (start_url when there
   is none). Game Day names its own, so it never matches another app's. */
const id = new URL(man.id, new URL(man.start_url, BASE + 'manifest.webmanifest')).href;
chk('with an install identity of its own', id === BASE + '?app=game-day', id);
chk('that no other app on the site shares', !/first-light/.test(id) && id !== BASE);
/* Older workers served the manifest cache-first by its plain URL; a versioned
   link makes them miss and fetch the current one (with its id). */
const cdp = await p.context().newCDPSession(p);
const am = await cdp.send('Page.getAppManifest');
chk('the page links a versioned manifest', /manifest\.webmanifest\?v=\d+$/.test(am.url), am.url);
chk('and Chrome reads Game Day’s own id from it', JSON.parse(am.data).id === './?app=game-day' && am.errors.length === 0);
chk('installable: standalone, with 192 and 512 icons', man.display === 'standalone' && ['192x192', '512x512'].every(z => man.icons.some(i => i.sizes === z)));
const sw = await (await p.request.get(BASE + 'sw.js')).text();
chk('its offline cache is game-day-v7', /const CACHE = 'game-day-v7'/.test(sw));
chk('and it keeps the facts page offline too', sw.includes("'./sources.html'"));
chk('the fonts are inside the page, so they work offline', await ev(() => [...document.styleSheets].some(s => [...s.cssRules].some(r => r.cssText.includes('Lilita One') && r.cssText.includes('data:font/woff2')))));
chk('and loaded', await ev(async () => { await document.fonts.ready; return document.fonts.check('24px "Lilita One"') && document.fonts.check('900 16px Nunito') }));

// ───────── a good neighbour on a shared site ─────────
/* jukes31ryan.github.io hosts other apps too (Calibrate keeps fl* keys). */
console.log('\n— sharing a site with other apps —');
const theirs = { flStreak: '40', flDone: '2026-10-04', flSettings: JSON.stringify({ onboarded: true }), flHistory: JSON.stringify({ '2026-10-04': 1 }) };
await open(theirs);
await ev(() => CARDS.forEach(c => markDone(c.id)));
const after = await ev(() => Object.fromEntries(Object.keys(localStorage).map(k => [k, localStorage.getItem(k)])));
chk('the other app’s keys are exactly as they were', Object.entries(theirs).every(([k, v]) => after[k] === v));
chk('a whole day went under gd*', after.gdStreak === '1' && Object.keys(after).filter(k => !(k in theirs)).every(k => k.startsWith('gd')), Object.keys(after).join(','));
chk('its streak didn’t pick up the other app’s 40', (await ev(() => streakInfo().n)) === 1);
await ev(() => go('settings')); await p.waitForTimeout(150);
const [dl] = await Promise.all([p.waitForEvent('download'), p.click('text=Save backup')]);
const backup = JSON.parse(readFileSync(await dl.path(), 'utf8'));
chk('a backup holds only Game Day’s data', backup.app === 'game-day' && Object.keys(backup.data).length > 0 && Object.keys(backup.data).every(k => k.startsWith('gd')));
await p.setInputFiles('#settings input[type=file]', { name: 'x.json', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify({ app: 'first-light', data: { flStreak: '99' } })) });
await p.waitForTimeout(200);
chk('another app’s backup is refused', (await p.textContent('#backupMsg')).includes('isn’t a Game Day backup'));
chk('and nothing changed', await ev(() => localStorage.getItem('flStreak')) === '40');
await ev(() => localStorage.clear());
p.once('dialog', d => d.accept());
await p.setInputFiles('#settings input[type=file]', { name: 'b.json', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify(backup)) });
await p.waitForTimeout(400); await p.clock.runFor(1000); await p.waitForTimeout(400);
chk('his own backup restores', await ev(() => localStorage.getItem('gdStreak')) === '1');

// ───────── settings ─────────
console.log('\n— settings —');
await open();
await ev(() => go('settings')); await p.waitForTimeout(150);
chk('no grown-up text boxes of data: just name and number', (await p.$$('#settings input.txt-in:not([type=time]), #settings textarea')).length === 1);
await p.click('#setSport button[data-v="soccer"]');
await reload();
chk('settings keep', await ev(() => S.sport === 'soccer'));
chk('one look, so no theme setting', (await p.$$('#setTheme')).length === 0);
await ev(() => go('settings')); await p.waitForTimeout(150);
const link = await p.getAttribute('#settings a[href="sources.html"]', 'href');
chk('Settings links to every fact and its source', link === 'sources.html');
await shot('settings');

// ───────── offline, without clearing anyone else's cache ─────────
console.log('\n— offline —');
{
  const c2 = await b.newContext({ viewport: { width: 390, height: 844 } });
  const q = await c2.newPage();
  await q.goto(BASE, { waitUntil: 'load' });
  await q.evaluate(async () => { const c = await caches.open('calibrate-v18'); await c.put('/first-light/index.html', new Response('other app')) });
  await q.evaluate(() => navigator.serviceWorker.ready).catch(() => {});
  await q.waitForTimeout(1200);
  await q.goto(BASE, { waitUntil: 'load' }); await q.waitForTimeout(500);
  await q.goto(BASE + 'sources.html', { waitUntil: 'load' }); await q.waitForTimeout(500);
  const names = await q.evaluate(() => caches.keys());
  chk('Game Day keeps its own offline copy', names.includes('game-day-v7'), names.join(', '));
  chk('and leaves another app’s cache alone', names.includes('calibrate-v18'));
  const shell = await q.evaluate(async () => (await (await caches.open('game-day-v7')).match('./index.html')).text());
  chk('opening the facts page doesn’t replace the app', shell.includes('const KP="gd"'));
  /* A changed manifest reaches a phone that already has the worker. */
  const fresh = await q.evaluate(async () => {
    const reg = await navigator.serviceWorker.ready;
    const c = await caches.open('game-day-v7');
    await c.put('./manifest.webmanifest', new Response('{"id":"stale"}', { headers: { 'content-type': 'application/manifest+json' } }));
    return !!navigator.serviceWorker.controller && (await (await fetch('manifest.webmanifest', { cache: 'no-store' })).json()).id;
  });
  chk('the manifest comes from the network, not a stale cache', fresh === './?app=game-day', String(fresh));
  await c2.setOffline(true);
  await q.goto(BASE, { waitUntil: 'domcontentloaded' }).catch(() => {}); await q.waitForTimeout(500);
  const offMan = await q.evaluate(async () => (await (await fetch('manifest.webmanifest')).json()).id).catch(() => null);
  chk('and is still there offline', offMan === './?app=game-day', String(offMan));
  chk('it opens with no internet', ((await q.textContent('.board-title').catch(() => '')) || '').trim() === 'GAME DAY');
  await q.goto(BASE + 'sources.html', { waitUntil: 'domcontentloaded' }).catch(() => {}); await q.waitForTimeout(300);
  chk('and so does the facts page', ((await q.textContent('h1').catch(() => '')) || '').includes('Where our facts come from'));
  await c2.close();
}

// ───────── fit for a 10-year-old ─────────
console.log('\n— fit for a 10-year-old —');
await open();
const shown = await ev(() => {
  const body = document.body.cloneNode(true);
  body.querySelectorAll('script,style').forEach(e => e.remove());
  return JSON.stringify([TRIVIA, DEF_QUOTES, JOKES, PUZZLES, ROUTINES, COOLDOWN, PLAYS, WHOAMI, SKILLS, FOODS, FOOD_GROUPS,
    FOOD_NUGGETS, FOOD_QUIZ, CHALLENGES, JOB_IDEAS, SLEEP_FACTS, SLEEP_PLAN, MIND]) + '\n' + body.textContent;
});
const hit = shown.match(ADULT);
chk('no adult words anywhere he can see', !hit, hit ? hit[0] + ' …' + shown.slice(Math.max(0, hit.index - 40), hit.index + 40) : '');
const src = readFileSync(REPO + 'index.html', 'utf8').replace(/\/\*[\s\S]*?\*\//g, '').replace(/<!--[\s\S]*?-->/g, '');
const GROWN_UP = ['Calibrate', 'Point the day', 'Mitch Hedberg', 'Sun Tzu', 'Marcus Aurelius', 'journal', 'Journal', 'affirm'];
const leaked = GROWN_UP.filter(s => src.indexOf(s) >= 0);
chk('none of the grown-up app ships here', leaked.length === 0, leaked.join(', '));
chk('no weight, calorie or diet talk in Fuel Up', !/\b(diet\w*|calori\w*|weigh\w*|skinny|junk)\b/i.test(await ev(() => JSON.stringify([FOODS, FOOD_GROUPS, FOOD_NUGGETS, FOOD_QUIZ]))));
chk('no heading drills for a 10-year-old', !/\bhead(ed|ing|er|ers)\b/i.test(await ev(() => JSON.stringify(SKILLS))));
chk('responsibilities, not chores', !/chore/i.test(src.replace(/\/\/.*$/gm, '')));

await done();
