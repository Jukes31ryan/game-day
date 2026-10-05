/* Upgrading: his streak, wins, trivia record, Who Am I? points and skill
   bests all carry over, his sport choice comes with them, he gets the
   first-use setup once (filled in with what he had), and v4's wrongly
   spelled default name doesn't survive. */
import { start } from './lib.mjs';

const { p, chk, open, reload, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);
const finishSetup = async name => {
  if (name != null) await p.fill('#suName', name);
  for (let i = 0; i < 3; i++) { await p.click('#suNext'); await p.waitForTimeout(120) }
};

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
await open(V3, { fresh: true });
chk('he gets the setup once', await p.isVisible('#setup') && !(await p.isVisible('#home')));
chk('it waits for his name', await p.isDisabled('#suNext'));
await p.fill('#suName', 'Liem'); await p.click('#suNext'); await p.waitForTimeout(100);
chk('with his sport already picked (soccer)', (await p.textContent('#suSport .on')).includes('Soccer'));
await p.click('#suNext'); await p.click('#suNext'); await p.waitForTimeout(200);
chk('then his 7-win streak is still there', (await p.textContent('#streak')).includes('7 wins in a row'), await p.textContent('#streak'));
chk('under his name', (await p.textContent('#hello')).trim() === 'Morning, Liem!');
chk('today starts fresh on the new cards', (await p.textContent('#starCount')).trim() === '★ 0/7');
chk('the old day record didn’t light anything', (await p.$$('#tiles .tile.lit')).length === 0);

await ev(() => openCard('brain')); await p.waitForTimeout(150);
for (let i = 0; i < 3; i++) { await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(50); await p.click('#bz .fs-next'); await p.waitForTimeout(50) }
const triv = await ev(() => readJSON(KP + 'Triv', {}));
chk('his trivia record keeps counting from 40 of 55', triv.right === 43 && triv.n === 58, JSON.stringify(triv));
await p.click('#bzChips .chip[data-k="who"]'); await p.waitForTimeout(100);
await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(80);
const who = await ev(() => readJSON(KP + 'Who', {}));
chk('his Who Am I? points keep adding up', who.played === 10 && who.pts === 21, JSON.stringify(who));
chk('his skill bests are still his', JSON.stringify(await ev(() => readJSON(KP + 'Skill', {}))) === V3.gdSkill);
await ev(() => { ['warmup', 'fuel', 'brain', 'captain', 'checkin', 'recovery', 'lights'].forEach(id => markDone(id)) });
chk('a win today makes it 8', await ev(() => localStorage.getItem(KP + 'Streak')) === '8');
chk('the other app’s keys are untouched', await ev(() => localStorage.getItem('flStreak')) === '40');
await reload();
chk('setup doesn’t come back', await p.isVisible('#home') && !(await p.isVisible('#setup')));
chk('and the old sport doesn’t override a new choice', await ev(() => { S.sport = 'football'; saveS(); return true }) &&
  (await reload(), await ev(() => S.sport)) === 'football');

console.log('\n— coming from v4, with its default name —');
await open({ gdKid: JSON.stringify({ name: 'Liam', num: 10, color: '#E53935', sport: 'football', wake: '07:00', bed: '21:00', sound: true, haptics: true, picked: true }),
  gdStreak: '7', gdDone: '2026-10-04' }, { fresh: true });
chk('he gets the setup once', await p.isVisible('#setup'));
chk('and the misspelled default name is gone', (await p.inputValue('#suName')) === '' && await ev(() => S.name) === '');
chk('his jersey color carried over', await ev(() => S.color) === '#E53935');
await finishSetup('Liem');
chk('his sport and bedtime carried over', await ev(() => S.sport === 'football' && S.bed === '21:00' && S.wake === '07:00'));
chk('the streak is still 7', (await p.textContent('#streak')).includes('7 wins in a row'));
chk('and he’s Liem now', (await p.textContent('#hello')).trim() === 'Morning, Liem!' && !(await ev(() => JSON.stringify(S))).includes('Liam'));
chk('the old flag is cleaned up', !('picked' in await ev(() => readJSON(KP + 'Kid', {}))));

console.log('\n— v3 with football only, or both —');
await open({ gdSettings: JSON.stringify({ tags: ['football', 'more'] }) }, { fresh: true });
chk('football only means football', await ev(() => S.sport) === 'football');
await open({ gdSettings: JSON.stringify({ tags: ['soccer', 'football'] }) }, { fresh: true });
chk('both means both', await ev(() => S.sport) === 'both');

await done();
