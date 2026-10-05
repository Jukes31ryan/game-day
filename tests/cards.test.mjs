/* Game Day's own cards: the Playbook (17), Who Am I? (16) and Skill of the Day
   (18), and the places they show up around the app: home, the wrap-up, the
   evening, the journal and setup. Plus the upgrade that brings them into a
   morning saved before they existed. */
import { chromium, BASE, OUT } from './lib.mjs';
const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});
const p=await ctx.newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));
let ok=true;
const chk=(n,c,x='')=>{if(!c)ok=false;console.log((c?'  ok  ':'FAIL  ')+n+(x?': '+x:''))};
const boot=async(settings)=>{
  await p.goto(BASE,{waitUntil:'domcontentloaded'});
  await p.evaluate(s=>{localStorage.clear();
    if(s)localStorage.setItem(KP+'Settings',JSON.stringify(s));
    localStorage.setItem(KP+'Done','2026-01-01');
    localStorage.setItem(KP+'History',JSON.stringify({'2026-01-01':1}));},settings||{onboarded:true});
  await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(450);
};
const txt=async sel=>((await p.textContent(sel))||'').trim();
const tomorrow=()=>{const d=new Date();d.setDate(d.getDate()+1);return d.toISOString().slice(0,10)};

// ───────── the Playbook ─────────
console.log('— the Playbook —');
await boot();
await p.evaluate(()=>go(17));await p.waitForTimeout(450);
const play=await p.evaluate(()=>PLAYS[pbIndex()]);
chk('today\'s play is on screen',await txt('#pbName')===play.name,play.name);
chk('with what it is',await txt('#pbWhat')===play.what);
chk('how it works, step by step',await p.evaluate(()=>document.querySelectorAll('#pbHow li').length)===play.how.length);
chk('why it works',await txt('#pbWhy')===play.why);
chk('and where to look for it',await txt('#pbLook')===play.look);
chk('and a diagram with every player and the ball',
  await p.evaluate(()=>document.querySelectorAll('#pbDiagram .pb-u,#pbDiagram .pb-t,#pbDiagram .pb-ball').length)===play.d.p.length+1);
chk('the diagram has a key',(await txt('#pbDiagram .pb-key')).indexOf('Your team')>=0);
chk('the day records it',await p.evaluate(()=>DAY.play)===play.name);
await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(400);
await p.evaluate(()=>go(17));await p.waitForTimeout(350);
chk('same play all day, even after a reload',await txt('#pbName')===play.name);
const tmr=await p.evaluate(t=>PLAYS[gdDaily(PLAYS,'plays',0,t)].name,tomorrow());
chk('and a different one tomorrow',tmr!==play.name,tmr);
const month=await p.evaluate(()=>{const seen=new Set();
  for(let i=0;i<PLAYS.length;i++){const d=new Date();d.setDate(d.getDate()+i);
    seen.add(gdDaily(PLAYS,'plays',0,dateKey(d)))}
  return seen.size});
chk('no play repeats until every play has had a day',month===await p.evaluate(()=>PLAYS.length),month+' distinct');
await p.click('text=Another play');await p.waitForTimeout(300);
const other=await txt('#pbName');
chk('"Another play" shows a different one',other!==play.name,other);
chk('and not tomorrow\'s, which would then repeat',other!==tmr);
chk('the day records the one he looked at last',await p.evaluate(()=>DAY.play)===other);
const drawn=await p.evaluate(()=>PLAYS.map(pl=>{
  const doc=new DOMParser().parseFromString(pbSvg(pl).replace(/<div[\s\S]*$/,''),'image/svg+xml');
  const bad=doc.querySelector('parsererror');
  return {n:pl.name,ok:!bad&&doc.querySelectorAll('.pb-u,.pb-t,.pb-ball').length===pl.d.p.length+1&&
    doc.querySelectorAll('path.pb-a').length===pl.d.a.length}}).filter(x=>!x.ok).map(x=>x.n));
chk('every play\'s diagram draws',drawn.length===0,drawn.join(', '));
await p.screenshot({path:OUT+'C0-playbook-dawn.png'});
await p.evaluate(()=>toggleTheme());await p.waitForTimeout(350);
await p.screenshot({path:OUT+'C1-playbook-dusk.png'});
chk('and it draws in dusk too',await p.evaluate(()=>{
  const c=document.querySelector('#pbDiagram .pb-u');return getComputedStyle(c).fill!==getComputedStyle(document.querySelector('#pbDiagram .pb-grass')).fill}));

// ───────── Who Am I? ─────────
console.log('\n— Who Am I? —');
const clues=()=>p.evaluate(()=>document.querySelectorAll('#whoClues .who-clue:not(.locked)').length);
const answer=async right=>{await p.evaluate(r=>{
  const e=WHOAMI[whoIdx(whoState().r)];
  const want=r?e.c[0]:e.c[1];
  [...document.querySelectorAll('#whoChoices .trv-choice')].find(b=>b.textContent.indexOf(want)>=0).click()},right);
  await p.waitForTimeout(350)};
await boot();
await p.evaluate(()=>go(16));await p.waitForTimeout(400);
chk('it starts with one clue',await clues()===1);
chk('and all four choices',await p.evaluate(()=>document.querySelectorAll('#whoChoices .trv-choice').length)===4);
chk('worth 3 points now',(await txt('#whoPts')).indexOf('3 points')>=0,await txt('#whoPts'));
await p.click('#whoMoreClue');await p.waitForTimeout(200);
chk('"Show clue 2" shows the second',await clues()===2);
await p.click('#whoMoreClue');await p.waitForTimeout(200);
chk('and then the third',await clues()===3);
chk('after which there are no more to ask for',await p.evaluate(()=>$('whoMoreClue').style.display==='none'));
await answer(true);
chk('right on clue 3 is 1 point',await p.evaluate(()=>DAY.who.got)===1);
chk('it completes the step',await p.evaluate(()=>statusOf(16))==='done');
chk('and shows the fact',(await txt('#whoFact')).length>20);

await boot();
await p.evaluate(()=>go(16));await p.waitForTimeout(400);
await answer(true);
chk('right on the first clue is 3 points',await p.evaluate(()=>DAY.who.got)===3);
chk('the all-time total keeps it',await p.evaluate(()=>readJSON(KP+'Who',{}).pts)===3);
const first=await p.evaluate(()=>WHOAMI[DAY.who.idx].c[0]);
await p.reload({waitUntil:'domcontentloaded'});await p.waitForTimeout(400);
await p.evaluate(()=>go(16));await p.waitForTimeout(350);
chk('a reload keeps the answer, and can\'t be replayed',
  await p.evaluate(()=>[...document.querySelectorAll('#whoChoices .trv-choice')].every(b=>b.disabled)));
await p.click('text=Play another');await p.waitForTimeout(350);
const second=await p.evaluate(()=>WHOAMI[whoIdx(whoState().r)].c[0]);
chk('"Play another" brings a new one',second!==first,second);
chk('starting again from one clue',await clues()===1);
await p.click('#whoMoreClue');await p.waitForTimeout(150);
await answer(true);
chk('scored 2 on clue 2',await p.evaluate(()=>DAY.who.got)===2);
chk('the total adds up',await p.evaluate(()=>readJSON(KP+'Who',{}).pts)===5);
chk('the day still remembers the first answer',await p.evaluate(()=>whoLine(DAY.who.first)).then(l=>l.indexOf(first)>=0));

await boot();
await p.evaluate(()=>go(16));await p.waitForTimeout(400);
await answer(false);
chk('a wrong guess scores nothing',await p.evaluate(()=>DAY.who.got)===0);
chk('and shows the right answer',
  await p.evaluate(()=>document.querySelector('#whoChoices .trv-choice.right span').textContent===WHOAMI[DAY.who.idx].c[0]));
chk('with every clue revealed',await clues()===3);
await p.screenshot({path:OUT+'C2-whoami-dawn.png'});

// ───────── Skill of the Day ─────────
console.log('\n— Skill of the Day —');
await boot();
await p.evaluate(()=>go(18));await p.waitForTimeout(400);
const skill=await p.evaluate(()=>SKILLS[skIndex()]);
chk('today\'s skill is on screen',await txt('#skName')===skill.name,skill.name);
chk('in three steps',await p.evaluate(()=>document.querySelectorAll('#skSteps li').length)===3);
chk('with a goal and a tip',await txt('#skGoal')===skill.goal&&await txt('#skTip')===skill.tip);
await p.fill('#skCount','12');await p.click('#skSave');await p.waitForTimeout(250);
chk('saving a number keeps it for today',await p.evaluate(()=>DAY.skillN)===12);
chk('and as his best for this skill',await p.evaluate(n=>readJSON(KP+'Skill',{})[n],skill.name)===12);
chk('and completes the step',await p.evaluate(()=>statusOf(18))==='done');
await p.fill('#skCount','8');await p.click('#skSave');await p.waitForTimeout(250);
chk('a lower number doesn\'t lower the best',await p.evaluate(n=>readJSON(KP+'Skill',{})[n],skill.name)===12);
chk('and says so',(await txt('#skBest')).indexOf('still 12')>=0,await txt('#skBest'));
await p.fill('#skCount','15');await p.click('#skSave');await p.waitForTimeout(250);
chk('a higher one is a new best',(await txt('#skBest')).indexOf('New best')>=0,await txt('#skBest'));
await p.fill('#skCount','');await p.click('#skSave');await p.waitForTimeout(150);
chk('an empty box asks for a number instead of saving zero',await p.evaluate(()=>DAY.skillN)===15);
chk('no skill is a heading drill (not allowed for under-11s)',
  await p.evaluate(()=>SKILLS.every(k=>!/\bhead(ed|ing|er|ers)\b|\bheads? (the|it|a)\b/i.test(JSON.stringify(k)))));
await p.screenshot({path:OUT+'C3-skill-dawn.png'});

// ───────── around the app ─────────
console.log('\n— home, wrap-up and journal —');
await boot();
await p.evaluate(()=>go(0));await p.waitForTimeout(400);
const names=await p.evaluate(()=>({play:PLAYS[pbIndex()].name,skill:SKILLS[skIndex()].name}));
chk('home shows today\'s play',await txt('#todayPlayT')===names.play);
chk('and today\'s skill',await txt('#todaySkillT')===names.skill);
chk('and no empty big-goal box anywhere',
  await p.evaluate(()=>!document.getElementById('winFrame')&&document.body.innerText.toLowerCase().indexOf('big goal')<0));
await p.click('#todayPlay');await p.waitForTimeout(400);
chk('tapping the play opens the Playbook',await p.evaluate(()=>document.querySelector('.scr.on').id)==='s17');
await p.evaluate(()=>go(0));await p.waitForTimeout(300);
await p.click('#todaySkill');await p.waitForTimeout(400);
chk('tapping the skill opens Skill of the Day',await p.evaluate(()=>document.querySelector('.scr.on').id)==='s18');
await p.fill('#skCount','9');await p.click('#skSave');await p.waitForTimeout(200);
await p.evaluate(()=>go(16));await p.waitForTimeout(300);
await answer(true);
await p.evaluate(()=>go(8));await p.waitForTimeout(400);
const recap=await txt('#recapBox');
chk('the wrap-up has the play',recap.indexOf(names.play)>=0);
chk('the skill, with his number',recap.indexOf(names.skill)>=0&&recap.indexOf('You got: 9')>=0);
chk('and Who Am I?',recap.indexOf('Who Am I?')>=0&&recap.indexOf('on clue 1')>=0,recap.slice(0,200));
chk('and no plan to fill in',recap.indexOf('Top 3')<0&&recap.toLowerCase().indexOf('big goal')<0);
await p.evaluate(()=>openJournal(todayKey(),8));await p.waitForTimeout(400);
const jr=await txt('#jrBody');
chk('the journal keeps the play',jr.indexOf(names.play)>=0);
chk('the skill and his number',jr.indexOf(names.skill)>=0&&jr.indexOf('He got 9')>=0);
chk('and Who Am I?',jr.indexOf('Who Am I?')>=0);

// an old day, from before the Playbook, still reads
const old='2026-09-01';
await p.evaluate(k=>{localStorage.setItem(KP+'Day-'+k,JSON.stringify({win:'Ace the spelling test',
  status:{5:'done',6:'done'},software:'Effort | Hustle back on defense.',eve:{hit:'yes'}}));recordDay(k)},old);
await p.evaluate(k=>openJournal(k),old);await p.waitForTimeout(400);
const ojr=await txt('#jrBody');
chk('a day from before still shows its big goal',ojr.indexOf('Ace the spelling test')>=0);
chk('and its rule',ojr.indexOf('Hustle back on defense.')>=0);

// ───────── setup ─────────
console.log('\n— setup —');
await boot();
await p.evaluate(()=>openOnboard());await p.waitForTimeout(400);
const page0=await txt('#obBody');
['Who Am I?','The Playbook','Skill of the Day','Locker Room','The Story','Get in the Zone']
  .forEach(t=>chk('offers '+t,page0.indexOf(t)>=0));
chk('and no longer the to-do list or the separate coach\'s card',
  page0.indexOf('Game Plan')<0&&page0.indexOf('Coach\'s Card')<0);
chk('Story and Breathing are off by default',await p.evaluate(()=>FLOW.indexOf(3)<0&&FLOW.indexOf(4)<0));
for(let i=0;i<3;i++){await p.click('#obNext');await p.waitForTimeout(250)}
chk('the rules page is the locker-room rules',await txt('#obTitle')==='Your locker-room rules.');

// ───────── the upgrade ─────────
console.log('\n— a morning saved before the new cards —');
await boot({onboarded:true,flow:[14,15,1,7,5,6,2]});
chk('the old default becomes the new one',
  await p.evaluate(()=>JSON.stringify(FLOW)===JSON.stringify(DEFAULT_FLOW)),await p.evaluate(()=>JSON.stringify(FLOW)));
chk('and is saved, so it only happens once',await p.evaluate(()=>readJSON(KP+'Settings',{}).flowV)===3);
await boot({onboarded:true,flow:[14,3,1,5,6,2]});
chk('an optional card he switched on stays, before the joke; cards he switched off stay off',
  await p.evaluate(()=>JSON.stringify(FLOW))==='[14,16,17,18,1,3,2]',await p.evaluate(()=>JSON.stringify(FLOW)));
await boot({onboarded:true,flow:[17,2],flowV:3});
chk('a morning saved since is left exactly as it is',await p.evaluate(()=>JSON.stringify(FLOW))==='[17,2]');
await boot({});
chk('a brand-new Game Day gets the new morning',
  await p.evaluate(()=>JSON.stringify(FLOW))==='[14,15,16,7,17,18,1,2]',await p.evaluate(()=>JSON.stringify(FLOW)));

console.log('\n'+(errs.length?('ERRORS: '+errs.join(';')):'NO JS ERRORS'));
await b.close();
process.exit(ok&&!errs.length?0:1);
