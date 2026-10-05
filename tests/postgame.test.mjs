/* The evening: Check-in, Recovery and Lights Out. A full scoreboard is a
   win, and wins in a row are the streak (with one grace day a week). */
import { start } from './lib.mjs';

const { p, chk, open, reload, shot, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);
const isDone = id => ev(id => isDone(id), id);
const next = async () => { await p.click('#cardNext'); await p.waitForTimeout(200) };
const TODAY = '2026-10-05';
const morning = async seed => {
  await open(Object.assign({ gdKid: JSON.stringify({ picked: true }) }, seed || {}));
  await ev(() => {
    ['warmup', 'fuel', 'brain', 'captain'].forEach(id => DAY.done[id] = Date.now());
    capState().jobs = [{ t: 'Homework', done: false }, { t: 'Feed Biscuit', done: false }];
    saveDay();
  });
};
const evening = async () => { await p.clock.setSystemTime(new Date(TODAY + 'T19:00:00')); await reload() };

// ───────── the evening ─────────
console.log('— home in the evening —');
await morning();
await evening();
chk('it says good evening', /^Evening, Liam!$/.test((await p.textContent('#hello')).trim()));
chk('still the sky-blue look at night', await ev(() => document.body.dataset.theme) === 'day');
chk('the big button starts Post-Game', (await p.textContent('#cta')).trim() === 'Start Post-Game ▶');
await shot('post-home');

// ───────── Check-in ─────────
console.log('\n— Check-in —');
await p.click('#cta'); await p.waitForTimeout(200);
chk('Check-in comes first', (await p.textContent('#heroH')).trim() === 'Check-in');
chk('his assignments come back to tick off', (await p.$$('#jobs .job .tick')).length === 2);
await p.click('#jobs .job:first-child .tick'); await p.waitForTimeout(60);
await p.click('#rate button[data-k="great"]'); await p.waitForTimeout(60);
await p.fill('#hlIn', 'Scored at recess');
await shot('post-checkin');
await reload(); await ev(() => openCard('checkin')); await p.waitForTimeout(150);
const cap = await ev(() => capState());
chk('ticks, rating and highlight all keep', cap.jobs[0].done && !cap.jobs[1].done && cap.rating === 'great' && cap.highlight === 'Scored at recess');
chk('and show again', (await p.$$('#jobs .job.done')).length === 1 && (await p.$$('#rate button.on')).length === 1);
await next();
chk('finishing it counts', await isDone('checkin'));
await ev(() => renderHome());
chk('and fills the captain’s armband', (await p.$$('#tiles .tile.cap.lit')).length === 1);

// ───────── Recovery ─────────
console.log('\n— Recovery —');
chk('Recovery is next', (await p.textContent('#heroH')).trim() === 'Recovery');
chk('a sourced sleep fact', await ev(() => SLEEP_FACTS.some(f => $('cbody').textContent.includes(f[0]))));
chk('8:45 PM to 6:45 AM is 10 hours', (await p.textContent('.bed-big')).includes('8:45 PM') && (await p.textContent('#cbody')).includes('10 hours'));
chk('which is in the 9 to 12 hours kids his age need', (await p.textContent('#cbody')).includes('✅'));
await ev(() => { S.bed = '22:30'; saveS() }); await ev(() => openCard('recovery')); await p.waitForTimeout(100);
chk('10:30 PM is 8¼ hours, and it says that’s too few', (await p.textContent('#cbody')).includes('8¼ hours') && (await p.textContent('#cbody')).includes('less than the 9 to 12'));
await ev(() => { S.bed = '20:45'; saveS() }); await ev(() => openCard('recovery')); await p.waitForTimeout(100);
await p.click('#sleepPlan .tick[data-i="0"]'); await p.waitForTimeout(60);
chk('tonight’s plan ticks and keeps', (await ev(() => sleepState().plan[0])) === true);
const cool = await ev(() => wu.r.moves.reduce((t, m) => t + m[1], 0));
await p.click('#wuBtn'); await p.clock.runFor(cool * 1000 + 2000);
chk('the cool-down finishes Recovery', await isDone('recovery'));

// ───────── Lights Out ─────────
console.log('\n— Lights Out —');
await next();
chk('Lights Out is last', (await p.textContent('#heroH')).trim() === 'Lights Out');
const lines = await ev(() => lo.sc[2].length);
await p.click('#loBtn'); await p.clock.runFor(10500);
chk('one line per slow breath', (await ev(() => lo.i)) === 1);
await shot('post-lights');
await p.clock.runFor(lines * 10000 + 1000);
chk('it ends on goodnight', (await p.textContent('#loLine')).startsWith('Goodnight, Liam.'));
chk('and lights Chill', await isDone('lights'));
chk('all seven is a win', await ev(() => isWin()));
chk('the first win starts a streak', await ev(() => localStorage.getItem(KP + 'Streak')) === '1' && await ev(() => localStorage.getItem(KP + 'Done')) === TODAY);
await next();
chk('the day ends on Goodnight', (await p.textContent('#finalBody .final-h')).trim() === 'Goodnight, Liam');
chk('and says he won it', (await p.textContent('#finalBody')).includes('You won the day'));
await ev(() => go('home')); await p.waitForTimeout(150);
chk('the whole scoreboard is lit', (await p.$$('#tiles .tile.lit')).length === 6);
chk('the button celebrates', (await p.textContent('#cta')).includes('You won the day'));
chk('1 win in a row', (await p.textContent('#streak')).includes('1 win in a row'));
await shot('post-won');

// ───────── the streak ─────────
console.log('\n— the streak —');
const winWith = async seed => {
  await p.clock.setSystemTime(new Date(TODAY + 'T07:30:00'));
  await morning(seed); await evening();
  await ev(() => { ['checkin', 'recovery', 'lights'].forEach(id => markDone(id)) });
  return ev(() => [+localStorage.getItem(KP + 'Streak'), localStorage.getItem(KP + 'Grace')]);
};
let [n, g] = await winWith({ gdStreak: '4', gdDone: '2026-10-04' });
chk('a win the day after a win adds one', n === 5 && !g, n + '');
[n, g] = await winWith({ gdStreak: '4', gdDone: '2026-10-03' });
chk('one missed day is saved by the grace day', n === 5 && g === TODAY, n + ' ' + g);
[n, g] = await winWith({ gdStreak: '4', gdDone: '2026-10-03', gdGrace: '2026-10-01' });
chk('but only once a week', n === 1, n + '');
[n, g] = await winWith({ gdStreak: '9', gdDone: '2026-10-01' });
chk('three days off starts over', n === 1, n + '');
await p.clock.setSystemTime(new Date(TODAY + 'T07:30:00'));
await open({ gdStreak: '6', gdDone: '2026-10-02', gdKid: JSON.stringify({ picked: true }) });
chk('a streak that has already ended shows as cold', (await p.textContent('#streak')).includes('Win today'));
await open({ gdStreak: '6', gdDone: '2026-10-04', gdKid: JSON.stringify({ picked: true }) });
chk('a live streak shows its count before today’s win', (await p.textContent('#streak')).includes('6 wins in a row'));
await ev(() => { ['warmup', 'fuel', 'brain', 'captain', 'checkin', 'recovery'].forEach(id => markDone(id)) });
chk('six of seven is not a win yet', await ev(() => localStorage.getItem(KP + 'Done')) === '2026-10-04');

await done();
