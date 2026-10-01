# ⚽ Game Day

> Liam's morning warm-up. A real warm-up, five sports trivia questions, a quote
> from a sports legend, an easy crossword, a coach's card, a game plan for the
> day, and a joke on the way out. About ten minutes before school.

### **[https://jukes31ryan.github.io/game-day/](https://jukes31ryan.github.io/game-day/)**

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
| **Warm-up** | Soccer warm-up, wake-up, and before-practice routines, guided on a timer with animated figures |
| **Trivia** | 212 multiple-choice questions: soccer, the NFL, basketball, baseball, hockey, the Olympics and more. Five a day, a fact after every answer, "5 more" if he wants them. Forty-two days before anything repeats. |
| **Quote** | 42 quotes from Pelé, Messi, Mia Hamm, Jordan, Gretzky, Serena Williams, Jackie Robinson, Muhammad Ali, John Wooden and more, each with "What does this mean?" in kid terms |
| **Crossword** | 30 easy 5×5 grids, mostly sports words, direct clues |
| **Coach's card** | One rule a day from 32: effort, teammates, mistakes, practice, respect, school, family |
| **Game plan** | What's on today, pick the top three, choose one big goal |
| **Joke** | 115 jokes: sports jokes, knock-knocks, riddles, dad jokes and silly ones. Punchlines wait for a tap. |
| **Story** *(optional)* | 20 one-minute reads: true sports stories and classic fables |
| **Get in the zone** *(optional)* | Slow breathing, the way players calm down before a penalty kick |
| **Post-match** | In the evening: did you hit your big goal, what are you grateful for, best play of the day |

Trivia only uses facts that won't change mid-season: rules, history and
settled records. No current rosters, and no running totals for players who
are still playing. Where a famous sports story is usually told wrong (Michael
Jordan wasn't cut from his school team, he was left on JV), Game Day tells it
the way it actually happened.

## How it's built

A single self-contained `index.html` (vanilla HTML, CSS and JavaScript, no
framework, no build step to run it), plus `manifest.webmanifest`, `sw.js` and
icons so it installs and works offline.

The words are easier to read and edit as Python files in `content/`:

```
content/trivia.py      the trivia bank
content/quotes.py      quotes, with what each one means
content/stories.py     stories and their takeaways
content/jokes.py       jokes, by kind
content/words.py       crossword words and their clues
content/app.py         module names, default morning, coach's cards, warm-ups
content/puzzles.json   the crosswords, made by tools/gen_cw.py
```

After editing any of them:

```
python3 tools/make_pack.py     # checks everything, then updates index.html
tests/run.sh                   # runs the browser tests
```

`make_pack.py` refuses to write anything if a trivia question is malformed, a
crossword clue gives away its answer, or any text trips the adult-word check.
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
| `soft` | One coach's card a day, rotating through the set |
| `crossword` | Every grid and clue |
| `regress` | Content counts, the morning order, carry-over, the journal, settings, sport filters, the streak, the evening, and every screen in both themes |

## License

MIT
