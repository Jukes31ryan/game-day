/* The morning: Warm-up, Fuel Up, Sports Brain and the Captain's Card, each
   lighting its tile on the scoreboard, ending on Kickoff. */
import { start } from './lib.mjs';

const { p, chk, open, reload, shot, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);
const isDone = id => ev(id => isDone(id), id);
const next = async () => { await p.click('#cardNext'); await p.waitForTimeout(200) };

// ───────── home, first thing ─────────
console.log('— home in the morning —');
await open();
chk('it says good morning to him', /^Morning, Liem!$/.test((await p.textContent('#hello')).trim()), await p.textContent('#hello'));
chk('in the day-game theme', await ev(() => document.body.dataset.theme) === 'day');
chk('his name and number are on the scoreboard', (await p.textContent('#boardDate')).includes('Liem #10'));
await shot('pre-home');
chk('six tiles on the scoreboard, none lit', (await p.$$('#tiles .tile')).length === 6 && (await p.$$('#tiles .tile.lit')).length === 0);
chk('the big button starts Pre-Game', (await p.textContent('#cta')).trim() === 'Start Pre-Game ▶');
chk('there is a quote of the day', (await p.textContent('#quoteT')).length > 10 && (await p.textContent('#quoteA')).length > 2);
chk('Post-Game cards say Tonight', (await p.$$('#half2 .when')).length === 3);

// ───────── warm-up ─────────
console.log('\n— warm-up —');
await p.click('#cta'); await p.waitForTimeout(200);
chk('the button opens the warm-up', (await p.textContent('#heroH')).trim() === 'Warm-up');
const secs = await ev(() => wu.r.moves.reduce((t, m) => t + m[1], 0));
chk('about two minutes', secs >= 90 && secs <= 180, secs + 's');
chk('every move has a figure', await ev(() => wu.r.moves.every(m => STRETCH_FIGS[m[3]])));
await p.click('#wuBtn');
await p.clock.runFor(20000);
chk('the timer runs', await ev(() => wu.i >= 1 || wu.left < wu.r.moves[0][1]));
await p.click('#wuBtn'); const paused = await ev(() => [wu.i, wu.left]);
await p.clock.runFor(5000);
chk('and pauses', JSON.stringify(await ev(() => [wu.i, wu.left])) === JSON.stringify(paused));
await p.click('#wuBtn');
await p.clock.runFor(secs * 1000 + 2000);
chk('finishing it lights Move', await isDone('warmup'));
chk('the Next button names the next card', (await p.textContent('#cardNext')).trim() === 'Done! Next: Fuel Up ▶');

// ───────── Fuel Up ─────────
console.log('\n— Fuel Up —');
await next();
chk('Fuel Up is next', (await p.textContent('#heroH')).trim() === 'Fuel Up');
chk('its Next button waits until the game is over', await ev(() => $('card').classList.contains('gated')) && !(await p.isVisible('#cardNext')));
chk('with a way to skip it', await p.isVisible('#cbody .skip-link'));
const items = await ev(() => fsRound(0));
chk('six questions: three foods to sort, three quiz', items.length === 6 && items.filter(i => i.t === 'sort').length === 3);
chk('one of the foods is a tricky one', await ev(it => it.some(i => i.t === 'sort' && FOODS[i.i].why), items));
for (let i = 0; i < 6; i++) {
  const right = await ev(it => it.t === 'sort' ? FOODS[it.i].g[0] : '0', items[i]);
  await p.click('#fsCard [data-a="' + right + '"]'); await p.waitForTimeout(80);
  if (i === 0) {
    chk('a right answer says so', (await p.textContent('.fs-head')).includes('Yes!'));
    chk('and teaches a "Did you know?"', (await p.textContent('.dyk')).includes('Did you know?'));
    await shot('pre-fuel');
  }
  await p.click('.fs-next'); await p.waitForTimeout(60);
}
chk('six right is a perfect score', (await p.textContent('.fs-big')).trim() === '6 / 6');
chk('with the group of the day', (await p.textContent('.spot h3')).length > 3);
chk('finishing lights Fuel', await isDone('fuel'));
chk('and lets him move on', await ev(() => !$('card').classList.contains('gated')) && await p.isVisible('#cardNext'));
chk('his food tally is kept', (await ev(() => readJSON(KP + 'Food', {}))).n === 6);
await p.click('text=Play 6 more'); await p.waitForTimeout(100);
const r1 = await ev(() => fsRound(1)[0]);
const wrong = await ev(it => FOOD_GROUPS.map(g => g.k).find(k => FOODS[it.i].g.indexOf(k) < 0), r1);
await p.click('#fsCard [data-a="' + wrong + '"]'); await p.waitForTimeout(80);
chk('a wrong answer is marked ✗', (await p.textContent('.gbtn.wrong')).startsWith('✗'));
chk('and the right one ✓', (await p.textContent('.gbtn.right')).startsWith('✓'));
chk('in words, not only color', (await p.textContent('.fs-head')).includes('Not quite'));
chk('the extra round has different foods', await ev(() => fsRound(1)[0].i !== fsRound(0)[0].i || fsRound(1)[0].t !== fsRound(0)[0].t));

// ───────── Sports Brain ─────────
console.log('\n— Sports Brain —');
await next();
chk('Sports Brain is next', (await p.textContent('#heroH')).trim() === 'Sports Brain');
chk('Monday is trivia day', await ev(() => brainToday()) === 'trivia' && (await p.textContent('#bzHead')).includes('Trivia'));
const today = await ev(() => trvRound(0));
chk('three questions', today.length === 3);
for (let i = 0; i < 3; i++) {
  await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(60);
  if (i === 0) chk('each answer shows its fact', (await p.textContent('#bz .dyk')).length > 20);
  await p.click('#bz .fs-next'); await p.waitForTimeout(60);
}
chk('three right', (await p.textContent('#bz .fs-big')).trim() === '3 / 3');
chk('finishing lights Learn', await isDone('brain'));
chk('the all-time tally is kept', (await ev(() => readJSON(KP + 'Triv', {}))).n === 3);
await reload();
chk('the same three all day', JSON.stringify(await ev(() => trvRound(0))) === JSON.stringify(today));
chk('and three new ones on "Play 3 more"', await ev(t => trvRound(1).every(i => t.indexOf(i) < 0), today));
await ev(() => { S.sport = 'football'; saveS() });
chk('Favorite sport: Football means football questions', await ev(() => trvRound(0).every(i => TRIVIA[i].s === 'football')));
await ev(() => { S.sport = 'both'; saveS() });

await ev(() => openCard('brain')); await p.waitForTimeout(150);
await p.click('#bzChips .chip[data-k="who"]'); await p.waitForTimeout(100);
chk('Who Am I? is a tap away', (await p.textContent('#bzHead')).includes('Who Am I?'));
chk('it starts with one clue', (await p.$$('#bz .who-clue.locked')).length === 2);
await p.click('text=Show clue 2'); await p.waitForTimeout(60);
await p.click('#bz .qbtn[data-a="0"]'); await p.waitForTimeout(80);
chk('right on clue 2 is 2 points', (await ev(() => readJSON(KP + 'Who', {}))).pts === 2);
await p.click('#bzChips .chip[data-k="play"]'); await p.waitForTimeout(100);
chk('the Playbook draws its play', (await p.$$('#bz .pb-wrap .pb-svg')).length === 1);
await p.click('#bzChips .chip[data-k="skill"]'); await p.waitForTimeout(100);
await p.fill('#skCount', '14'); await p.click('text=Save'); await p.waitForTimeout(60);
chk('a skill best is saved', Object.values(await ev(() => readJSON(KP + 'Skill', {}))).includes(14));
await p.click('#bzChips .chip[data-k="cross"]'); await p.waitForTimeout(150);
chk('and the crossword opens', (await p.$$('#cwGrid > *')).length >= 25);

// ───────── Captain's Card ─────────
console.log('\n— Captain’s Card —');
await ev(() => openCard('captain')); await p.waitForTimeout(150);
const ch = await ev(() => CHALLENGES[capState().ch]);
chk('today’s challenge, with a how', (await p.textContent('.ch-name')).trim() === ch[0] && (await p.textContent('#cbody')).includes(ch[2]));
await p.fill('#jobIn', 'Feed Biscuit'); await p.press('#jobIn', 'Enter'); await p.waitForTimeout(60);
await p.click('#jobIdeas .chip:has-text("Homework")'); await p.waitForTimeout(60);
await p.fill('#jobIn', 'homework'); await p.press('#jobIn', 'Enter'); await p.waitForTimeout(60);
chk('he writes his own assignments, and quick-adds', (await p.$$('#jobs .job')).length === 2);
chk('no doubles', (await ev(() => capState().jobs.map(j => j.t))).join('|') === 'Feed Biscuit|Homework');
chk('it never calls them chores', !/chore/i.test(await p.textContent('#cbody')));
await shot('pre-captain');
await reload();
chk('they’re still there after a reload', (await ev(() => capState().jobs.length)) === 2);
await ev(() => openCard('captain')); await p.waitForTimeout(150);
await next();
chk('Pre-Game ends on Kickoff', (await p.textContent('#finalBody .final-h')).trim() === 'Kickoff!');
chk('with a joke for the road', await p.isVisible('#jokeBtn'));
await p.click('#jokeBtn'); await p.waitForTimeout(60);
chk('that tells the punchline', await p.isVisible('#jokeA'));
await ev(() => go('home')); await p.waitForTimeout(150);
chk('four stars after the morning', (await p.textContent('#starCount')).trim() === '★ 4/7');
chk('Move, Fuel and Learn lit; the armband half', (await p.$$('#tiles .tile.lit')).length === 3 && (await p.$$('#tiles .tile.half')).length === 1);
chk('the button says Post-Game opens later', (await p.textContent('#cta')).includes('after school'));
await shot('pre-home-after');

await done();
