# ⚽ Game Day

> A game-day plan for a kid who loves sports. A good day runs like a game:
> **Pre-Game** in the morning (warm up, fuel up, train your sports brain, lead
> yourself), and **Post-Game** at night (check in, recover, wind down). Each card
> lights a tile on their scoreboard; light them all and they win the day.
>
> Built for Liem, a 10-year-old who loves soccer and football, and open to any
> kid: the first time it opens, it asks their name, jersey, favorite sport and age.

### **[https://jukes31ryan.github.io/Family-Meeting-Hub/game-day/](https://jukes31ryan.github.io/Family-Meeting-Hub/game-day/)**

This repo is the source. The live copy is published from the `game-day/` folder of
Family-Meeting-Hub, because Pages isn't switched on for this repo yet.

---

## For grown-ups

- **Share the link with anyone.** On first use, a kid sets up their own Game
  Day in three quick steps: name, jersey number and color; soccer, football or
  both (which steers trivia, Who Am I?, plays and skills); and age with bedtime
  and wake-up. The age picks the sleep range that applies (AASM: 9 to 12 hours
  for ages 6 to 12, 8 to 10 for 13 to 18). All of it can be changed later in
  Settings.
- **Put it on the home screen.** Android (Chrome): ⋮ → *Add to Home screen* →
  *Install*. iPhone or iPad (Safari): Share → *Add to Home Screen*. It runs
  full-screen and works offline. On iPhone and iPad this also protects the
  data: Safari deletes website storage after about a week away unless the site
  is on the home screen.
- **It installs as its own app.** Its manifest sets its own `id`, so Chrome
  never mistakes it for another app on jukes31ryan.github.io (like Calibrate),
  and its worker always fetches the manifest fresh. If Chrome only offers a
  shortcut, remove any older Game Day icon (press and hold → Uninstall),
  reopen the link, and install again.
- **Every fact is checked.** Food, sleep, trivia, players, rules and quotes each
  name the source they were checked against, and the build refuses a fact
  without one. Anything that couldn't be confirmed was cut. The full list is in
  the app (Settings → *See every fact and its source*) and in `sources.html`.
- **It's his own app.** Its streak and scores are kept apart from any other app
  on the same site, and a backup from another app won't restore into it.
- **Nothing leaves the device.** No accounts, no ads, no tracking.
- **Upgrading keeps the streak**, wins, trivia record, Who Am I? points, skill
  bests and sport choice. An existing player sees the setup once, filled in
  with what they had.

## The day

The plan underneath is MEEES (Meditate, Educate, Exercise, Eat right, Sleep
well) plus leading himself. On screen each part gets a kid word: **Move, Fuel,
Learn, Lead, Sleep, Chill**.

**1st Half: Pre-Game** (morning, about 7 minutes)

| Card | What it is |
|---|---|
| **Warm-up** (Move) | A two-minute routine on a timer with animated figures. Three rotate by day: morning, soccer and football. |
| **Fuel Up** (Fuel) | The Food Group Challenge: six quick questions a day. Sort a food into its MyPlate group (fruits, vegetables, grains, protein, dairy), including tricky ones like corn, popcorn and beans, plus quiz questions. Every answer teaches a "Did you know?". 48 foods, 22 nuggets, 20 quiz questions, all checked against USDA MyPlate and NIH. No calories, weight or diet talk, ever. |
| **Sports Brain** (Learn) | One brain workout a day, a different kind each day, with the rest a tap away: **Trivia** (151 questions: 71 soccer, 59 NFL, 21 other sports; three a day), **Who Am I?** (39 players and teams, three clues, 3-2-1 points), **Playbook** (30 plays with diagrams), **Skill of the Day** (24 things to try at recess, personal bests kept; no heading drills, per U.S. Soccer) and a **crossword** (30 mini grids). |
| **Captain's Card** (Lead) | Today's challenge, one character play a day out of 32 (*Be attentive. How: when a teacher or parent is talking to you, stop, look at them, and don't talk until they're done.*), and **My assignments**: he writes in what he's responsible for today. |
| **Kickoff** | A joke for the road (104 of them). |

**2nd Half: Post-Game** (after school, about 6 minutes)

| Card | What it is |
|---|---|
| **Check-in** (Lead) | He ticks off his assignments, rates today's challenge (Nailed it / Sort of / Tomorrow), and can add the best moment of his day. |
| **Recovery** (Sleep) | A sleep fact (14, from AASM, NIH and CDC), their bedtime against the hours kids their age need, tonight's game plan, and a one-minute cool-down. |
| **Lights Out** (Chill) | A sports visualization read one line per slow breath with a breathing circle (14 of them: the perfect free kick, replay your best play, a locker-room body scan), ending on goodnight. |

Rewards stay simple: a star per card, a win for all seven, and a streak of wins
with one grace day a week. A quote of the day (10, each traced to the person
named) sits on the home screen.

## How it's built

A single self-contained `index.html` (vanilla HTML, CSS and JavaScript, no
framework), plus `manifest.webmanifest`, `sw.js`, icons and the generated
`sources.html`. The fonts, Lilita One and Nunito (SIL Open Font License), are
embedded in the page so the look works offline.

The words live in `content/`, where they're easy to read and edit:

```
content/fuel.py        food groups, foods, "Did you know?" nuggets, quiz, sources
content/sleep.py       sleep facts, tonight's plan, sources
content/mind.py        Lights Out wind-downs
content/challenges.py  Captain's Card challenges and quick-add assignments
content/trivia.py      trivia, with a source for every question
content/whoami.py      Who Am I? players and teams, with sources
content/plays.py       the Playbook (diagrams as data), with rule sources
content/skills.py      Skill of the Day
content/quotes.py      quotes, each with where it was checked
content/jokes.py       jokes
content/words.py       crossword words and clues
content/app.py         warm-up and cool-down routines
content/puzzles.json   crosswords, made by tools/gen_cw.py
```

After editing any of them:

```
python3 tools/make_pack.py     # checks everything, then writes index.html and sources.html
tests/run.sh                   # runs the browser tests
```

`make_pack.py` refuses to write anything if a fact has no source, a food or
sleep source isn't an official health site, food text mentions diet, weight or
calories, a skill involves heading the ball, a challenge or wind-down slips in a
statistic or "studies show", a clue gives away its answer, a play's diagram puts
someone off the field, or any text trips the adult-word check.

### Tests

Browser tests drive the real app in headless Chromium through Playwright, on a
controlled clock.

| Suite | Covers |
|-------|--------|
| `setup` | First use: a name is required, the jersey previews live, the sport steers trivia, the age sets the sleep range, it never asks twice, and Settings can change it all |
| `pregame` | Home in the morning, the jersey hello, the warm-up timer, the Food Group Challenge (right and wrong answers, score, extra rounds), Sports Brain (daily picks, sport filter, Who Am I? scoring, Playbook, skill bests, crossword), assignments, Kickoff and the scoreboard |
| `postgame` | Home in the evening, Check-in, bedtime math, tonight's plan, the cool-down, Lights Out, a win, and the streak with its grace day |
| `migrate` | Upgrading from v3 or v4 keeps the streak, records, bests and settings, shows setup once, and drops v4's default name |
| `gameday` | Its own name, storage and offline cache, leaving other apps alone, backup and restore, settings, the facts page offline, and an adult-word scan of everything he can see |

## License

MIT
