/* The Locker Room's daily rule. One of his locker-room rules a day, on a fixed
   rotation, under the quote. It used to be a card of its own (step 5); now it
   is half of the Locker Room (step 1), and these checks follow it there. */
import { chromium, BASE, OUT } from './lib.mjs';
const SS=OUT;
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});
const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));
let ok=true;
const chk=(n,c,x='')=>{if(!c)ok=false;console.log((c?'  ok  ':'FAIL  ')+n+(x?': '+x:''))};

const CARDS=['Effort | Hustle back on defense. Every time.','Teammate | Cheer loudest when a teammate scores.',
  'Practice | Use your weaker foot.','Respect | Shake hands, win or lose.','Body | Warm up first.'];

const boot=async(affirms)=>{
  await p.goto(BASE,{waitUntil:'domcontentloaded'});
  await p.evaluate(a=>{localStorage.clear();
    localStorage.setItem(KP+'Settings',JSON.stringify({onboarded:true,affirms:a}));
    localStorage.setItem(KP+'Done','2026-01-01');
    localStorage.setItem(KP+'History',JSON.stringify({'2026-01-01':1}));},affirms);
  await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(500);
};
const rule=async()=>(await p.textContent('#lrTxt')).trim();

// ───────── the Locker Room carries the rule ─────────
console.log('— the Locker Room —');
await boot(CARDS);
await p.evaluate(()=>go(1));await p.waitForTimeout(450);
chk('the quote is there',(await p.textContent('#sparkQ')).trim().length>10);
chk('and so is today\'s rule',(await rule()).length>5,await rule());
chk('under its own label',(await p.textContent('#lrCat')).trim()==='Today’s rule');
chk('the old coach\'s card is not a step any more',await p.evaluate(()=>!STEPS[5]&&!STEPS[6]));
chk('and the Locker Room is in the default morning',await p.evaluate(()=>DEFAULT_FLOW.indexOf(1)>=0));
await p.click('#s1 .foot .btn-go');await p.waitForTimeout(450);
chk('Continue completes the step',await p.evaluate(()=>statusOf(1))==='done');

// ───────── one rule a day, stable across a reload ─────────
console.log('\n— one rule a day —');
await boot(CARDS);
await p.evaluate(()=>go(1));await p.waitForTimeout(400);
const first=await rule();
const expect=await p.evaluate(()=>parsePair(S.affirms[dayOfYear()%S.affirms.length])[1]);
chk('the rule is the one the day picks',first===expect.trim(),first);
await p.evaluate(()=>newSpark());await p.waitForTimeout(200);
chk('a different quote leaves the rule alone',(await rule())===first);
await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(400);
await p.evaluate(()=>go(1));await p.waitForTimeout(400);
chk('same rule after a reload',(await rule())===first);

// ───────── the rotation covers everything ─────────
console.log('\n— the rotation —');
const seen=await p.evaluate(n=>{
  const out=[];
  for(let d=0;d<n;d++) out.push(S.affirms[(dayOfYear()+d)%S.affirms.length]);
  return out;
},CARDS.length);
chk('consecutive days cover every rule exactly once',
  new Set(seen).size===CARDS.length,String(new Set(seen).size)+' of '+CARDS.length);

// ───────── game rules keep their "When ..." ─────────
console.log('\n— the game rules set —');
await p.evaluate(()=>{localStorage.setItem(KP+'Settings',JSON.stringify({onboarded:true,affirms:SHARP_CARDS}))});
await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(400);
await p.evaluate(()=>go(1));await p.waitForTimeout(400);
const when=(await p.textContent('#lrCat')).trim();
chk('a game rule is labelled with its "When"',/^When /.test(when),when);
chk('and the rule reads as the answer to it',(await rule()).length>3&&!/^When /.test(await rule()));

// ───────── empty list ─────────
console.log('\n— no rules at all —');
await boot([]);
await p.evaluate(()=>{S.affirms=[];go(1)});await p.waitForTimeout(450);
chk('the rule strip hides rather than showing a blank',
  await p.evaluate(()=>$('lrRule').style.display==='none'));
chk('without throwing',errs.length===0,errs.join(';'));
chk('and Continue still completes the step',
  await p.evaluate(async()=>{document.querySelector('#s1 .foot .btn-go').click();
    await new Promise(r=>setTimeout(r,300));return statusOf(1)==='done'}));

// ───────── editing in Settings ─────────
console.log('\n— editing your rules —');
await boot(CARDS);
await p.evaluate(()=>{openSettings()});await p.waitForTimeout(350);
await p.evaluate(()=>{$('setAffirms').value='Only | One line now';saveSettings()});
await p.waitForTimeout(400);
await p.evaluate(()=>go(1));await p.waitForTimeout(400);
chk('the rule comes from the new list',(await rule())==='One line now',await rule());

// ───────── the journal names it ─────────
console.log('\n— the journal —');
await boot(CARDS);
await p.evaluate(()=>go(1));await p.waitForTimeout(400);
const shown=await rule();
const key=await p.evaluate(()=>todayKey());
await p.evaluate(()=>{saveDay();recordDay(todayKey())});
await p.evaluate(k=>openJournal(k),key);await p.waitForTimeout(450);
const jr=await p.textContent('#jrBody');
chk('the day names the rule you got',jr.indexOf(shown)>=0,shown);
chk('as today\'s rule',jr.indexOf('Today’s rule')>=0);
chk('and no pipe reaches the screen',jr.indexOf('|')<0);

await boot(CARDS);
await p.evaluate(()=>go(1));await p.waitForTimeout(500);
await p.screenshot({path:SS+'E0-locker-dawn.png'});
await p.evaluate(()=>toggleTheme());await p.waitForTimeout(400);
await p.screenshot({path:SS+'E1-locker-dusk.png'});

console.log('\n'+(errs.length?('ERRORS: '+errs.join(';')):'NO JS ERRORS'));
await b.close();
process.exit(ok&&!errs.length?0:1);
