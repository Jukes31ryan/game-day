/* Game Day as its own app: its own name and storage, a good neighbour to the
   other apps on the same site, trivia that behaves, and nothing on the page a
   10-year-old shouldn't read. */
import { chromium, BASE, OUT } from './lib.mjs';
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const REPO = fileURLToPath(new URL('..', import.meta.url));
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const errs = []; p.on('pageerror', e => errs.push(e.message));
let ok = true;
const chk = (n, c, x = '') => { if (!c) ok = false; console.log((c ? '  ok  ' : 'FAIL  ') + n + (x ? ': ' + x : '')) };
const open = async clear => {
  await p.goto(BASE, { waitUntil: 'domcontentloaded' });
  if (clear) { await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'domcontentloaded' }) }
  await p.waitForTimeout(450);
};
const ADULT = /\b(drugs?|drunk|beer|wine|alcohol|booze|therap\w*|sex\w*|kill\w*|murder\w*|suicid\w*|die|died|dies|dying|death|dead|divorc\w*|damn|hell|crap|stupid|idiot|guns?|casino|gambl\w*|bet|bets|betting|odds|cigar\w*|smok\w*)\b/i;

// ───────── its own app ─────────
console.log('— its own app —');
await open(true);
chk('it is called Game Day', (await p.textContent('.mh-title')).trim() === 'Game Day');
chk('it says whose it is', (await p.textContent('.mh-tag')).trim() === "Liam's morning warm-up");
chk('the tab title matches', (await p.title()) === 'Game Day');
chk('its own storage prefix', await p.evaluate(() => KP) === 'gd');
chk('in pitch green', await p.evaluate(() => getComputedStyle(document.body).getPropertyValue('--accent').trim()) === '#2e6b3c');
const man = await (await p.request.get(BASE + 'manifest.webmanifest')).json();
chk('the home-screen name is Game Day', man.short_name === 'Game Day' && man.name === 'Game Day', man.short_name);
chk('it installs from its own folder', man.start_url === '.' && man.scope === '.');
const sw = await (await p.request.get(BASE + 'sw.js')).text();
chk('with its own offline cache', /const CACHE = 'game-day-v\d+'/.test(sw));
chk('the morning starts with a warm-up and trivia',
  await p.evaluate(() => FLOW[0] === 14 && FLOW[1] === 15), await p.evaluate(() => JSON.stringify(FLOW)));

// ───────── a good neighbour on a shared site ─────────
/* jukes31ryan.github.io hosts other apps too (Calibrate keeps fl* keys).
   Browser storage is shared by the whole site, so prove Game Day never
   touches anything that isn't its own. */
console.log('\n— sharing a site with other apps —');
await open(true);
await p.evaluate(() => {
  localStorage.setItem('flStreak', '40'); localStorage.setItem('flDone', '2026-09-29');
  localStorage.setItem('flSettings', JSON.stringify({ onboarded: true, affirms: ['Someone | Else’s card'] }));
  localStorage.setItem('flHistory', JSON.stringify({ '2026-09-29': 1 }));
});
const dump = () => p.evaluate(() => { const o = {}; for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); o[k] = localStorage.getItem(k) } return o });
const before = await dump();
await p.reload({ waitUntil: 'domcontentloaded' }); await p.waitForTimeout(400);
await p.evaluate(async () => {
  for (const n of FLOW) { go(n); await new Promise(r => setTimeout(r, 80)); mark(n, 'done') }
  finishDay();
});
await p.waitForTimeout(900);
const after = await dump();
const theirs = Object.keys(before).filter(k => k.indexOf('gd') !== 0);
chk('the other app’s keys are exactly as they were',
  theirs.length === 4 && theirs.every(k => after[k] === before[k]), theirs.filter(k => after[k] !== before[k]).join(','));
chk('a whole morning went under gd*', after.gdStreak === '1' && !!after.gdHistory, 'gdStreak=' + after.gdStreak);
chk('its streak didn’t pick up the other app’s 40', await p.evaluate(() => streakInfo().n) === 1);
chk('and it wrote nothing outside its prefix',
  Object.keys(after).filter(k => theirs.indexOf(k) < 0).every(k => k.indexOf('gd') === 0));
const exported = await p.evaluate(() => Object.keys(collectData().data));
chk('a backup holds only Game Day’s data', exported.length > 0 && exported.every(k => k.indexOf('gd') === 0), exported.join(','));
p.once('dialog', d => d.accept());
await p.evaluate(() => { openSettings(); applyImport(JSON.stringify({ app: 'first-light', data: { flStreak: '99' } })) });
await p.waitForTimeout(400);
chk('another app’s backup is refused', /different app/.test(await p.textContent('#backupMsg')), await p.textContent('#backupMsg'));
chk('and nothing changed', await p.evaluate(() => localStorage.getItem('flStreak')) === '40');

// ───────── offline, without clearing anyone else's cache ─────────
console.log('\n— offline —');
{
  const c2 = await b.newContext({ viewport: { width: 390, height: 844 } });
  const q = await c2.newPage();
  await q.goto(BASE, { waitUntil: 'load' });
  /* Another app's offline cache, as it would exist on Ryan's iPad. */
  await q.evaluate(async () => { const c = await caches.open('calibrate-v18'); await c.put('/first-light/index.html', new Response('other app')) });
  await q.evaluate(() => navigator.serviceWorker.ready).catch(() => {});
  await q.waitForTimeout(1000);
  await q.goto(BASE, { waitUntil: 'load' }); await q.waitForTimeout(600);
  const names = await q.evaluate(() => caches.keys());
  chk('Game Day keeps its own offline copy', names.some(k => /^game-day-v/.test(k)), names.join(', '));
  chk('and leaves another app’s cache alone', names.indexOf('calibrate-v18') >= 0, names.join(', '));
  await c2.setOffline(true);
  await q.goto(BASE, { waitUntil: 'domcontentloaded' }).catch(() => {}); await q.waitForTimeout(500);
  chk('it opens with no internet', ((await q.textContent('.mh-title').catch(() => '')) || '').trim() === 'Game Day');
  await c2.close();
}

// ───────── trivia ─────────
console.log('\n— trivia —');
await open(true);
const bank = await p.evaluate(() => TRIVIA);
chk('a real bank', bank.length >= 140, String(bank.length));
chk('every question has four different choices',
  bank.every(q => q.c.length === 4 && new Set(q.c.map(c => c.toLowerCase())).size === 4));
chk('and a fact to learn', bank.every(q => q.f && q.f.length > 20));
chk('no question asked twice', new Set(bank.map(q => q.q)).size === bank.length);
const bySport = {}; bank.forEach(q => bySport[q.s] = (bySport[q.s] || 0) + 1);
chk('only soccer, football, and a little of everything else', Object.keys(bySport).every(k => ['soccer', 'football', 'more'].indexOf(k) >= 0), JSON.stringify(bySport));
chk('soccer and football are most of it', (bySport.soccer + bySport.football) / bank.length >= 0.8, JSON.stringify(bySport));
/* The right answer is written first in the data. It must not be shown first. */
const pos = await p.evaluate(() => {
  const n = [0, 0, 0, 0];
  TRIVIA.forEach((q, qi) => { const order = shuffled([0, 1, 2, 3], todayKey() + ':' + qi); n[order.indexOf(0)]++ });
  return n;
});
chk('the right answer turns up in every position', pos.every(x => x > bank.length * 0.15), pos.join('/'));

const today = await p.evaluate(() => trvRound(0));
chk('five questions a day', today.length === 5);
await p.reload({ waitUntil: 'domcontentloaded' }); await p.waitForTimeout(400);
chk('the same five all day', JSON.stringify(await p.evaluate(() => trvRound(0))) === JSON.stringify(today));
const tomorrow = await p.evaluate(() => trvRound(0, dateKey(new Date(Date.now() + 864e5))));
chk('and five different ones tomorrow', tomorrow.every(i => today.indexOf(i) < 0));
const month = await p.evaluate(() => {
  const seen = [];
  for (let d = 0; d < 30; d++) seen.push(...trvRound(0, dateKey(new Date(Date.now() + d * 864e5))));
  return seen;
});
chk('a whole month of trivia without a repeat', new Set(month).size === month.length, new Set(month).size + ' of ' + month.length);

await p.evaluate(() => go(15)); await p.waitForTimeout(350);
const q0 = await p.evaluate(() => TRIVIA[trvRound(0)[0]]);
chk('it shows the question', (await p.textContent('#trvQ')).trim() === q0.q);
chk('with the sport on the card', (await p.textContent('#trvSport')).trim().length > 0);
chk('four choices to tap', (await p.$$('.trv-choice')).length === 4);
await p.locator('.trv-choice', { hasText: q0.c[0] }).first().click(); await p.waitForTimeout(400);
chk('the right answer lights up', await p.evaluate(() => !!document.querySelector('.trv-choice.right')));
chk('the fact appears', (await p.textContent('#trvFact')).indexOf(q0.f) >= 0);
chk('the score counts it', (await p.textContent('#trvScore')).trim() === 'Score 1 / 1');
await p.click('#trvNext'); await p.waitForTimeout(300);
const q1 = await p.evaluate(() => TRIVIA[trvRound(0)[1]]);
await p.locator('.trv-choice', { hasText: q1.c[1] }).first().click(); await p.waitForTimeout(400);
chk('a wrong answer is marked', await p.evaluate(() => !!document.querySelector('.trv-choice.wrong')));
chk('and shows which one was right', await p.evaluate(() => !!document.querySelector('.trv-choice.right')));
chk('and says it in words, not only colour', (await p.textContent('#trvFact')).indexOf(q1.c[0]) >= 0);
for (let i = 2; i < 5; i++) {
  await p.click('#trvNext'); await p.waitForTimeout(250);
  await p.locator('.trv-choice').first().click(); await p.waitForTimeout(250);
}
await p.click('#trvNext'); await p.waitForTimeout(400);
const done = await p.textContent('#trvDone');
chk('five in, a score', /\d \/ 5/.test(done), done.slice(0, 40));
chk('the step counts as done', await p.evaluate(() => statusOf(15)) === 'done');
chk('the all-time tally is kept', await p.evaluate(() => readJSON(KP + 'Triv', {}).n) === 5);
await p.click('text=Play 5 more'); await p.waitForTimeout(300);
const more = await p.evaluate(() => trvRound(1));
chk('five more are five new ones', more.every(i => today.indexOf(i) < 0));
await p.evaluate(() => { saveDay(); recordDay(todayKey()); openJournal(todayKey()) }); await p.waitForTimeout(400);
chk('the journal remembers the score', /Trivia\s*\d+ out of \d+ right/.test(await p.textContent('#jrBody')));
await p.evaluate(() => { S.tags = ['football']; saveS() });
chk('picking Football means football questions', await p.evaluate(() => trvRound(0).every(i => TRIVIA[i].s === 'football')));
await p.evaluate(() => { S.tags = []; saveS() });

// ───────── the warm-up: one short routine, nothing to choose ─────────
console.log('\n— the warm-up —');
await open(true);
await p.evaluate(() => go(14)); await p.waitForTimeout(300);
chk('one routine, so there is nothing to pick', await p.evaluate(() => Object.keys(ROUTINES).length === 1));
chk('and no routine picker on screen', !(await p.isVisible('#strChips')));
const secs = await p.evaluate(() => ROUTINES[Object.keys(ROUTINES)[0]].moves.reduce((t, m) => t + m[1], 0));
chk('about two minutes long', secs >= 90 && secs <= 180, secs + 's');
chk('every move has a figure', await p.evaluate(() => Object.values(ROUTINES)[0].moves.every(m => STRETCH_FIGS[m[3]])));

// ───────── fit for a 10-year-old ─────────
console.log('\n— fit for a 10-year-old —');
await open(true);
const shown = await p.evaluate(() => {
  const body = document.body.cloneNode(true);
  body.querySelectorAll('script,style').forEach(e => e.remove());
  return JSON.stringify([TRIVIA, DEF_QUOTES, QUOTE_NOTES, STORIES, STORY_NOTES, JOKES, JOKE_KINDS, CARD_LIBRARY, SHARP_CARDS,
    DEF_AFFIRMS, PUZZLES, ROUTINES, LAUNCH_LINES, STEPS, PATTERNS, TAG_NAMES]) + '\n' + body.textContent;
});
const hit = shown.match(ADULT);
chk('no adult words anywhere he can see', !hit, hit ? hit[0] + ' …' + shown.slice(Math.max(0, hit.index - 40), hit.index + 40) : '');
/* Code comments may mention where the engine came from; content may not. */
const src = readFileSync(REPO + 'index.html', 'utf8').replace(/\/\*[\s\S]*?\*\//g, '').replace(/<!--[\s\S]*?-->/g, '');
const GROWN_UP = ['Calibrate', 'Point the day', 'Mitch Hedberg', 'Sun Tzu', 'Marcus Aurelius', 'But first, Love', 'Puppy Love',
  'Grown-up life', 'Stand-up', 'I used to do drugs', 'Operating rules', 'taking up RAM', 'What&#8217;s important now'];
const leaked = GROWN_UP.filter(s => src.indexOf(s) >= 0);
chk('none of the grown-up app’s content ships here', leaked.length === 0, leaked.join(', '));
chk('no weekend crossword for a shelf that doesn’t exist', await p.evaluate(() => PUZZLES7.length === 0 && !cwIsWeekend()));
chk('every crossword word is five letters or fewer',
  await p.evaluate(() => PUZZLES.every(z => Object.keys(z.c).every(w => w.length <= 5))));

// ───────── the page matches its content files ─────────
console.log('\n— index.html matches content/ —');
let fresh = true, why = '';
try { execFileSync('python3', [REPO + 'tools/make_pack.py', '--check'], { stdio: 'pipe' }) }
catch (e) { fresh = false; why = String(e.stdout || e.stderr || e.message).trim().slice(0, 160) }
chk('content/ and index.html agree', fresh, why || 'run: python3 tools/make_pack.py');

await open(true);
await p.screenshot({ path: OUT + 'gameday-dash.png' });
console.log('\n' + (errs.length ? ('ERRORS: ' + errs.join(';')) : 'NO JS ERRORS'));
await b.close();
process.exit(ok && !errs.length ? 0 : 1);
