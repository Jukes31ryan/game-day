/* Upgrading from v3: his streak, wins, trivia record, Who Am I? points and
   skill bests all carry over, his sport choice comes with them, and the old
   day record doesn't confuse the new cards. */
import { start } from './lib.mjs';

const { p, chk, open, reload, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);

const V3 = {
  gdStreak: '7', gdDone: '2026-10-04', gdSaved: '1', gdGrace: '2026-09-20',
  gdHistory: JSON.stringify({ '2026-10-03': { done: 5 }, '2026-10-04': { done: 5 } }),
  gdTriv: JSON.stringify({ right: 40, n: 55, perfect: 3 }),
  gdWho: JSON.stringify({ played: 9, right: 7, pts: 18 }),
  gdSkill: JSON.stringify({ Juggling: 12, 'Toe taps': 30 }),
  gdSettings: JSON.stringify({ onboarded: true, tags: ['soccer'], affirms: ['A | B'], flow: [14, 15] }),
  gdTheme: 'dark',
  /* the same day's record, in v3's shape */
  'gdDay-2026-10-05': JSON.stringify({ winId: 3, triv: { r: 0, i: 2, picks: [0, 1], right: 1, n: 2 }, who: { r: 0, clues: 2 }, picks: [1, 2], status: { 14: 'done' } }),
  /* another app on the same site */
  flStreak: '40',
};

console.log('— coming from v3 —');
await open(V3);
chk('it opens without an error', true);
chk('his 7-win streak is still there', (await p.textContent('#streak')).includes('7 wins in a row'), await p.textContent('#streak'));
chk('his sport choice carried over (soccer)', await ev(() => S.sport) === 'soccer');
chk('he isn’t greeted like a new player', !(await p.isVisible('#jerseyHi')));
chk('today starts fresh on the new cards', (await p.textContent('#starCount')).trim() === '★ 0/7');
chk('the old day record didn’t light anything', (await p.$$('#tiles .tile.lit')).length === 0);

await ev(() => openCard('brain')); await p.waitForTimeout(150);
for (let i = 0; i < 3; i++) { await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(50); await p.click('#bz .fs-next'); await p.waitForTimeout(50) }
const triv = await ev(() => readJSON(KP + 'Triv', {}));
chk('his trivia record keeps counting from 40 of 55', triv.right === 43 && triv.n === 58, JSON.stringify(triv));
chk('and the card shows it', (await p.textContent('#bz')).includes('43 right out of 58'));
await p.click('#bzChips .chip[data-k="who"]'); await p.waitForTimeout(100);
await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(80);
const who = await ev(() => readJSON(KP + 'Who', {}));
chk('his Who Am I? points keep adding up', who.played === 10 && who.pts === 21, JSON.stringify(who));
chk('his skill bests are still his', JSON.stringify(await ev(() => readJSON(KP + 'Skill', {}))) === V3.gdSkill);

await ev(() => { ['warmup', 'fuel', 'brain', 'captain', 'checkin', 'recovery', 'lights'].forEach(id => markDone(id)) });
chk('a win today makes it 8', await ev(() => localStorage.getItem(KP + 'Streak')) === '8');
chk('the other app’s keys are untouched', await ev(() => localStorage.getItem('flStreak')) === '40');
await reload();
chk('and the setting migration runs only once', await ev(() => { S.sport = 'football'; saveS(); return true }) &&
  (await reload(), await ev(() => S.sport)) === 'football');

console.log('\n— v3 with football only, or both —');
await open({ gdSettings: JSON.stringify({ tags: ['football', 'more'] }) });
chk('football only means football', await ev(() => S.sport) === 'football');
await open({ gdSettings: JSON.stringify({ tags: ['soccer', 'football'] }) });
chk('both means both', await ev(() => S.sport) === 'both');

console.log('\n— brand new —');
await open();
chk('a new player starts as Liam #10, both sports', await ev(() => S.name === 'Liam' && S.num === 10 && S.sport === 'both'));
chk('with a no-pressure jersey hello', await p.isVisible('#jerseyHi'));
await p.click('#jerseyHi .btn3d'); await p.waitForTimeout(150);
chk('"Pick mine" opens Settings', await p.isVisible('#settings') && await p.isVisible('#setNum'));
await p.fill('#setName', 'Sam'); await p.fill('#setNum', '7');
await ev(() => go('home')); await p.waitForTimeout(150);
chk('and his jersey shows on the scoreboard', (await p.textContent('#boardDate')).includes('Sam #7'));
chk('the hello is gone for good', !(await p.isVisible('#jerseyHi')));

await done();
