/* First use, for any kid: name and jersey, favorite sport, age and bedtime.
   Then it's theirs, and it never asks again. */
import { start } from './lib.mjs';

const { p, chk, open, reload, shot, done } = await start({ at: '07:30' });
const ev = (f, a) => p.evaluate(f, a);

console.log('— a brand-new player —');
await open(null, { fresh: true });
chk('it opens on setup, not the scoreboard', await p.isVisible('#setup') && !(await p.isVisible('#home')));
chk('nobody is named yet', await ev(() => S.name) === '' && (await p.inputValue('#suName')) === '');
chk('Next waits for a name', await p.isDisabled('#suNext'));
await shot('setup-1-empty');
await p.fill('#suName', 'Liem');
chk('a name lets him go on', !(await p.isDisabled('#suNext')));
await p.fill('#suNum', '7');
await p.click('#suColors .sw[data-c="#E53935"]');
chk('the jersey shows his number and color as he picks', (await p.textContent('#suJersey b')).trim() === '7' && (await p.innerHTML('#suJersey')).includes('#E53935'));
await shot('setup-1');
await p.click('#suNext'); await p.waitForTimeout(100);

chk('step 2 asks what he plays', (await p.textContent('#suBody .su-h')).includes('love to play'));
await p.click('#suSport button[data-v="football"]');
await shot('setup-2');
await p.click('#suBack'); await p.waitForTimeout(80);
chk('Back keeps what he typed', (await p.inputValue('#suName')) === 'Liem');
await p.click('#suNext'); await p.waitForTimeout(80);
chk('and what he picked', (await p.textContent('#suSport .on')).includes('Football'));
await p.click('#suNext'); await p.waitForTimeout(100);

chk('step 3 asks his age', (await p.textContent('#suBody .su-h')).includes('How old'));
chk('ages 6 to 15+', (await p.$$('#suAge button')).length === 10);
chk('8:45 PM to 6:45 AM at 10 is right in 9 to 12 hours', (await p.textContent('#suHours')).includes('✅ That’s 10 hours of sleep. Kids your age need 9 to 12.'));
await p.click('#suAge button[data-v="14"]'); await p.waitForTimeout(60);
chk('at 14 the range is 8 to 10 (AASM, ages 13 to 18)', (await p.textContent('#suHours')).includes('need 8 to 10'));
await p.fill('#suBed', '22:00'); await p.dispatchEvent('#suBed', 'change'); await p.waitForTimeout(60);
chk('a later bedtime updates the hours', (await p.textContent('#suHours')).includes('8¾ hours'));
await shot('setup-3');
chk('the last button says Let’s play', (await p.textContent('#suNext')).includes('Let’s play'));
await p.click('#suNext'); await p.waitForTimeout(250);

chk('then it’s his scoreboard', await p.isVisible('#home') && (await p.textContent('#hello')).trim() === 'Morning, Liem!');
chk('with his jersey', (await p.textContent('#boardDate')).includes('Liem #7') && (await p.innerHTML('#jersey')).includes('#E53935'));
chk('everything he chose is saved', await ev(() => S.setup && S.sport === 'football' && S.age === 14 && S.bed === '22:00'));
chk('his sport steers the trivia', await ev(() => trvRound(0).every(i => TRIVIA[i].s === 'football')));
await reload();
chk('it never asks again', await p.isVisible('#home') && !(await p.isVisible('#setup')));

await ev(() => openCard('recovery')); await p.waitForTimeout(150);
chk('Recovery uses his age: 8¾ hours is in 8 to 10', (await p.textContent('#cbody')).includes('✅ That’s right in the 8 to 10 hours'));
await ev(() => go('settings')); await p.waitForTimeout(150);
await p.click('#setAge button[data-v="10"]'); await p.waitForTimeout(80);
chk('Settings can change his age', await ev(() => S.age) === 10);
await ev(() => openCard('recovery')); await p.waitForTimeout(150);
chk('and Recovery follows (8¾ is short of 9 to 12)', (await p.textContent('#cbody')).includes('less than the 9 to 12'));
await ev(() => go('settings')); await p.waitForTimeout(150);
await p.fill('#setName', '');
await ev(() => go('home')); await p.waitForTimeout(150);
chk('with no name, it still cheers him on', (await p.textContent('#hello')).trim() === 'Morning, Champ!');

await done();
