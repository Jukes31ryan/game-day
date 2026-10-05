# ⚽ Game Day

> Liam's morning warm-up, built around what he loves: soccer and football.
> Two easy minutes of moving, five trivia questions, a Who Am I? guess, an easy
> crossword, one play to learn, one skill to try at recess, a word from the
> locker room, and a joke on the way out. About twelve minutes before school.

### **[https://jukes31ryan.github.io/Family-Meeting-Hub/game-day/](https://jukes31ryan.github.io/Family-Meeting-Hub/game-day/)**

This repo is the source. The live copy is published from the `game-day/` folder of
Family-Meeting-Hub, because Pages isn't switched on for this repo yet.

---

## For grown-ups

- **Add it to his home screen.** Open the link in Safari, then Share → Add to
  Home Screen. It shows up as *Game Day* with a soccer-ball icon, runs
  full-screen, and works offline. On iPhone and iPad this also protects his
  data: Safari deletes website storage after about a week away unless the site
  is on the home screen.
- **It's his own app.** Its streak, scores, cards and journal are kept apart
  from any other app on the same device, and a backup from another app won't
  restore into it.
- **Nothing leaves the device.** No accounts, no ads, no tracking, no network
  requests after the first load, no links out.
- **He can make it his.** After his first morning it offers to let him choose
  the parts he wants, their order, and his favourite sports (which steer the
  trivia, quotes and stories). Settings has the same options any time.

## What's in it

| | |
|---|---|
| **Warm-up** | One easy two-minute routine to wake up: reach, arm circles, side bends, march, leg swings, jumping jacks. Guided on a timer with animated figures. |
| **Trivia** | 150 questions a 10-year-old would know: 70 soccer, 59 NFL, and 21 on everyday sports (LeBron, home runs, the Olympic rings). Five a day, a fact after every answer, "5 more" if he wants them. A month before anything repeats. |
| **Who Am I?** | Guess a player or team from three clues, hardest first: 39 of them, from Messi, Mbappé and Mia Hamm to Mahomes, Jerry Rice, the Packers and Real Madrid. 3 points on the first clue, 2 on the second, 1 on the third, with an all-time total and "Play another". |
| **Crossword** | 30 easy 5×5 grids, mostly soccer and football words (team names, positions, plays), direct clues |
| **Playbook** | One play a day, out of 30 (15 soccer, 15 football): what it is, how it works step by step, why it works, where to watch for it, and a diagram of the players, runs and passes. The give-and-go, the overlap, pressing, the offside trap; the screen pass, play-action, the blitz, the onside kick. |
| **Skill of the Day** | One thing to try at recess or practice, out of 24: toe taps, the Cruyff turn, juggling, the step-over; throwing a spiral, the diamond catch, the juke. Three steps, a goal, a tip, and a box for how many he got, with his best kept for each skill. No heading drills: US Soccer doesn't allow heading for players 10 and under. |
| **Locker Room** | A quote from a soccer or football great (25 of them, each with "What does this mean?" in kid terms) and one of his locker-room rules for the day, from 32: effort, teammates, mistakes, practice, respect |
| **Joke** | 104 jokes: soccer and football jokes, knock-knocks, riddles, dad jokes and silly ones. Punchlines wait for a tap. |
| **Story** *(optional)* | 13 one-minute reads: true soccer and football stories (Messi, Pelé, Leicester, Tom Brady, Kurt Warner) and classic fables |
| **Get in the zone** *(optional)* | Slow breathing, the way players calm down before a penalty kick |
| **Post-match** | In the evening: did you try today's skill (and how many did you get), what are you grateful for, best play of the day |

Trivia is pitched at what a 10-year-old who watches soccer and the NFL would
know: rules he plays by, players he sees, teams and logos, recent World Cups
and Super Bowls. It only uses facts that won't change mid-season, with no
running totals for players who are still playing. Where a famous sports story is usually told wrong (Michael
Jordan wasn't cut from his school team, he was left on JV), Game Day tells it
the way it actually happened. Who Am I? follows the same rules: anything
about a player's club is pinned to a year ("joined Inter Miami in 2023").

## How it's built

A single self-contained `index.html` (vanilla HTML, CSS and JavaScript, no
framework, no build step to run it), plus `manifest.webmanifest`, `sw.js` and
icons so it installs and works offline.

The words are easier to read and edit as Python files in `content/`:

```
content/trivia.py      the trivia bank
content/whoami.py      Who Am I? players and teams, three clues each
content/plays.py       the Playbook, with each play's diagram as data
content/skills.py      Skill of the Day
content/quotes.py      quotes, with what each one means
content/stories.py     stories and their takeaways
content/jokes.py       jokes, by kind
content/words.py       crossword words and their clues
content/app.py         module names, default morning, locker-room rules, warm-ups
content/puzzles.json   the crosswords, made by tools/gen_cw.py
```

After editing any of them:

```
python3 tools/make_pack.py     # checks everything, then updates index.html
tests/run.sh                   # runs the browser tests
```

`make_pack.py` refuses to write anything if a trivia question is malformed, a
crossword clue gives away its answer, a Who Am I? clue names its own answer, a
play's diagram puts someone off the field, a skill involves heading the ball,
or any text trips the adult-word check.
New crosswords: `python3 tools/gen_cw.py content/words.py content/puzzles.json`.
New icon: edit `icon.svg`, then `node tools/render_icons.mjs .`

### Tests

Browser tests drive the real app in headless Chromium through Playwright
(`npm i -D playwright`, then `npx playwright install chromium`).

| Suite | Covers |
|-------|--------|
| `gameday` | Its own name and storage, leaving other apps' data and offline caches alone, trivia behaviour, an adult-word scan of everything on screen, and `index.html` matching `content/` |
| `nav` | Every screen names itself, Back says where it goes, the main button says what's next, and the phone's back gesture works |
| `firstrun` | A first visit lands in the app, not a setup wizard; setup is offered once, after a finished morning |
| `durable` | Persistent storage, the home-screen and backup reminders, export and import |
| `joke` | The mix of kinds, tap-to-reveal punchlines, "a different kind", and the journal |
| `cards` | The Playbook, Who Am I? and Skill of the Day: daily picks that hold all day and change tomorrow, every diagram drawing, the 3-2-1 scoring, personal bests; and the play and skill on home, the wrap-up, the evening and the journal |
| `soft` | The Locker Room's rule: one a day, rotating through his set |
| `crossword` | Every grid and clue |
| `regress` | Content counts, the morning order, the journal, settings, sport filters, the streak, the evening, and every screen in both themes |

## License

MIT
