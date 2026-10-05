#!/usr/bin/env python3
"""Check Game Day's content and write it into index.html.

    python3 tools/make_pack.py           check, then update index.html
    python3 tools/make_pack.py --check   exit 1 if index.html is out of date

The words live in content/*.py (and content/puzzles.json, from tools/gen_cw.py),
where they're easy to read and edit. This validates every item and only then
swaps the matching `const NAME=[...]` blocks inside index.html. Nothing is
written if a single check fails.
"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content')


def fail(msg):
    sys.exit('make_pack: ' + msg)


def literal_end(src, i):
    """src[i] opens a literal ([ { ' " `). Return the index just past its end,
    skipping strings, template strings and comments along the way."""
    q = src[i]
    if q in '\'"`':
        j = i + 1
        while j < len(src):
            if src[j] == '\\': j += 2; continue
            if src[j] == q: return j + 1
            j += 1
        fail('unterminated string at %d' % i)
    close = {'[': ']', '{': '}', '(': ')'}
    stack = [close[q]]
    j = i + 1
    while j < len(src):
        c = src[j]
        if c in '\'"`':
            j = literal_end(src, j); continue
        if src.startswith('//', j):
            j = src.index('\n', j); continue
        if src.startswith('/*', j):
            j = src.index('*/', j) + 2; continue
        if c in close:
            stack.append(close[c])
        elif c in ')]}':
            if c != stack.pop(): fail('mismatched %r at %d' % (c, j))
            if not stack: return j + 1
        j += 1
    fail('unterminated literal at %d' % i)


def blocks(src):
    """Every top-level `const NAME=<literal>;` in src, as {name: (start, end)}
    where start..end spans the literal alone."""
    out = {}
    for m in re.finditer(r'(?m)^const ([A-Z][A-Z0-9_]*)=', src):
        start = m.end()
        if src[start] not in '[{\'"`':
            continue
        end = literal_end(src, start)
        out.setdefault(m.group(1), []).append((start, end))
    return out



def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(CONTENT, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


trivia, quotes, stories, jokes, app, plays, whoami, skills = (load(n) for n in (
    'trivia', 'quotes', 'stories', 'jokes', 'app', 'plays', 'whoami', 'skills'))
puzzles = json.load(open(os.path.join(CONTENT, 'puzzles.json')))
errs = []
def check(ok, msg):
    if not ok: errs.append(msg)

TAGS = set(app.TAG_NAMES)

# ─── trivia ──────────────────────────────────────────────────────────────────
seen = set()
for i, q in enumerate(trivia.Q):
    check(q['s'] in TAGS, 'trivia %d: unknown sport %r' % (i, q['s']))
    check(len(q['c']) == 4 and len(set(c.lower() for c in q['c'])) == 4, 'trivia %d: need 4 different choices' % i)
    check(all(c.strip() for c in q['c']), 'trivia %d: empty choice' % i)
    check(q['q'].strip().endswith(('?', '...?')) or q['q'].rstrip().endswith('?'), 'trivia %d: question has no question mark' % i)
    check(len(q['f']) > 20, 'trivia %d: fact too thin' % i)
    check(q['q'] not in seen, 'trivia %d: duplicate question' % i); seen.add(q['q'])

# ─── quotes ──────────────────────────────────────────────────────────────────
DEF_QUOTES, QUOTE_TAGS, QUOTE_NOTES = [], {}, {}
for text, who, tags, meaning, question in quotes.QUOTES:
    check('|' not in text and '|' not in who, 'quote has a pipe: ' + text[:40])
    check(set(tags) <= TAGS, 'quote tag: ' + text[:40])
    check(text not in QUOTE_TAGS, 'duplicate quote: ' + text[:40])
    DEF_QUOTES.append(text + ' | ' + who)
    QUOTE_TAGS[text] = tags
    QUOTE_NOTES[text] = {'m': meaning, 'q': question}

# ─── stories ─────────────────────────────────────────────────────────────────
STORIES, STORY_TAGS, STORY_NOTES = [], {}, {}
for title, tags, body, takeaway, meaning, question in stories.STORIES:
    check(title not in STORY_TAGS, 'duplicate story: ' + title)
    check(set(tags) <= TAGS, 'story tag: ' + title)
    words = len(body.split())
    STORIES.append({'t': title, 'r': ('1 min read' if words < 230 else '2 min read'), 's': body, 'm': takeaway})
    STORY_TAGS[title] = tags
    STORY_NOTES[title] = {'m': meaning, 'q': question}

# ─── jokes ───────────────────────────────────────────────────────────────────
for j in jokes.JOKES:
    check(j['k'] in app.JOKE_KINDS, 'joke kind %r' % j['k'])
check(len({(j['q'], j['a']) for j in jokes.JOKES}) == len(jokes.JOKES), 'duplicate joke')

# ─── crosswords ──────────────────────────────────────────────────────────────
for i, p in enumerate(puzzles):
    check(len(p['r']) == 5 and all(len(r) == 5 for r in p['r']), 'puzzle %d not 5x5' % i)
    for w, c in p['c'].items():
        check(w.lower() not in c.lower(), 'puzzle %d: clue gives away %s' % (i, w))

# ─── the Playbook ────────────────────────────────────────────────────────────
SPORTS = {'soccer', 'football'}
KINDS = {'pass', 'run', 'dribble'}
on_field = lambda x, y: 0 <= x <= 100 and 0 <= y <= 60
check(len({p['name'] for p in plays.PLAYS}) == len(plays.PLAYS), 'duplicate play name')
for p in plays.PLAYS:
    n = 'play %r' % p['name']
    check(p['s'] in SPORTS, n + ': unknown sport')
    check(2 <= len(p['how']) <= 3 and all(x.strip() for x in p['how']), n + ': needs 2-3 steps')
    check(all(len(p[k]) > 20 for k in ('what', 'why', 'look')), n + ': what, why and look all need saying')
    d = p['d']
    check(any(t == 'u' for t, *_ in d['p']), n + ': no players from his team')
    check(all(t in 'ut' and on_field(x, y) for t, x, y in d['p']), n + ': a player is off the field')
    check(on_field(*d['b']), n + ': the ball is off the field')
    check(all(k in KINDS and on_field(x1, y1) and on_field(x2, y2) for k, x1, y1, x2, y2 in d['a']),
          n + ': an arrow is off the field or of an unknown kind')

# ─── Who Am I? ───────────────────────────────────────────────────────────────
check(len({w['c'][0] for w in whoami.WHOAMI}) == len(whoami.WHOAMI), 'Who Am I?: an answer appears twice')
for w in whoami.WHOAMI:
    n = 'Who Am I? %r' % w['c'][0]
    check(w['s'] in SPORTS, n + ': unknown sport')
    check(len(w['clues']) == 3 and all(len(c) > 15 for c in w['clues']), n + ': needs 3 clues')
    check(len(w['c']) == 4 and len({c.lower() for c in w['c']}) == 4, n + ': needs 4 different choices')
    check(len(w['f']) > 20, n + ': fact too thin')
    # the answer can't be named in a clue, or clue 1 is the giveaway
    for c in w['clues']:
        check(w['c'][0].lower() not in c.lower(), n + ': a clue names the answer')

# ─── Skill of the Day ────────────────────────────────────────────────────────
# No heading: US Soccer's youth rules don't allow it for players 10 and under.
# "Behind your head" is fine; heading the ball is not.
HEADING = re.compile(r'\bhead(ed|ing|er|ers)\b|\bheads? (the|it|a)\b', re.I)
check(len({k['name'] for k in skills.SKILLS}) == len(skills.SKILLS), 'duplicate skill name')
for k in skills.SKILLS:
    n = 'skill %r' % k['name']
    check(k['s'] in SPORTS, n + ': unknown sport')
    check(len(k['steps']) == 3 and all(x.strip() for x in k['steps']), n + ': needs 3 steps')
    check(len(k['goal']) > 8 and len(k['tip']) > 8, n + ': needs a goal and a tip')
    for v in [k['name'], k['what'], k['goal'], k['tip']] + k['steps']:
        check(not HEADING.search(v), n + ': no heading drills for under-11s')

# ─── cards and warm-ups ──────────────────────────────────────────────────────
for card in app.CARD_LIBRARY + app.DEF_AFFIRMS + app.SHARP_CARDS:
    check(card.count(' | ') == 1, 'card needs "Category | Line": ' + card)
check(set(app.DEF_AFFIRMS) <= set(app.CARD_LIBRARY), 'starter cards should come from the library')
src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
s, e = blocks(src)['STRETCH_FIGS'][0]
FIGS = json.loads(src[s:e]); FIGS.update(app.FIGS)
for key, r in app.ROUTINES.items():
    for move in r['moves']:
        check(move[3] in FIGS, 'routine %s: no figure %r' % (key, move[3]))
for n in app.DEFAULT_FLOW:
    check(n in app.STEPS, 'default flow has unknown step %d' % n)

# ─── fit for a 10-year-old ───────────────────────────────────────────────────
# A scan, not a substitute for reading it: this catches a line that slips in
# from the adult edition, or a word that would need an awkward conversation.
ADULT = re.compile(r"\b(drugs?|drunk|beer|wine|alcohol|booze|therap\w*|sex\w*|kill\w*|murder\w*|"
                   r"suicid\w*|die|died|dies|dying|death|dead|divorc\w*|damn|hell|crap|stupid|idiot|"
                   r"guns?|casino|gambl\w*|bet|bets|betting|odds|cigar\w*|smok\w*)\b", re.I)
def scan(obj, where):
    if isinstance(obj, str):
        m = ADULT.search(obj)
        check(not m, 'adult word %r in %s: %s' % (m.group(0) if m else '', where, obj[:70]))
    elif isinstance(obj, dict):
        for k, v in obj.items(): scan(k, where); scan(v, where)
    elif isinstance(obj, (list, tuple)):
        for v in obj: scan(v, where)
for name, obj in [('trivia', trivia.Q), ('quotes', quotes.QUOTES), ('stories', stories.STORIES),
                  ('jokes', jokes.JOKES), ('puzzles', puzzles), ('cards', app.CARD_LIBRARY + app.SHARP_CARDS),
                  ('warm-ups', app.ROUTINES), ('lines', app.LAUNCH_LINES), ('steps', app.STEPS),
                  ('plays', plays.PLAYS), ('who am I', whoami.WHOAMI), ('skills', skills.SKILLS)]:
    scan(obj, name)

if errs:
    print('\n'.join(errs)); sys.exit('make_pack: %d problem(s), nothing written' % len(errs))

# ─── write ───────────────────────────────────────────────────────────────────
def js(v): return json.dumps(v, ensure_ascii=False, indent=None, separators=(',', ':'))
def lines(v):
    """One entry per line, so a diff of the pack is readable."""
    if isinstance(v, list):
        return '[\n' + ',\n'.join(js(x) for x in v) + '\n]'
    if isinstance(v, dict):
        return '{\n' + ',\n'.join(js(str(k)) + ':' + js(x) for k, x in v.items()) + '\n}'
    return js(v)

blocks_out = [
    ('STEPS', app.STEPS), ('DEFAULT_FLOW', app.DEFAULT_FLOW), ('TAG_NAMES', app.TAG_NAMES),
    ('TRIVIA', trivia.Q), ('TRV_SPORT', app.TRV_SPORT), ('TRV_CHEER', app.TRV_CHEER), ('TRV_OOPS', app.TRV_OOPS),
    ('DEF_QUOTES', DEF_QUOTES), ('QUOTE_TAGS', QUOTE_TAGS), ('QUOTE_NOTES', QUOTE_NOTES),
    ('STORIES', STORIES), ('STORY_TAGS', STORY_TAGS), ('STORY_NOTES', STORY_NOTES),
    ('JOKES', jokes.JOKES), ('JOKE_KINDS', app.JOKE_KINDS),
    ('PUZZLES', puzzles), ('PUZZLES7', []),
    ('CARD_LIBRARY', app.CARD_LIBRARY), ('DEF_AFFIRMS', app.DEF_AFFIRMS), ('SHARP_CARDS', app.SHARP_CARDS),
    ('LEGACY_AFFIRMS', app.LEGACY_AFFIRMS),
    ('PATTERNS', app.PATTERNS), ('STRETCH_FIGS', FIGS), ('ROUTINES', app.ROUTINES),
    ('LAUNCH_LINES', app.LAUNCH_LINES),
    ('PLAYS', plays.PLAYS), ('WHOAMI', whoami.WHOAMI), ('SKILLS', skills.SKILLS),
]
# swap each block in place, from the end backwards so offsets stay valid
spans = blocks(src)
edits = []
for name, value in blocks_out:
    if len(spans.get(name, [])) != 1:
        fail('index.html has %d blocks named %s' % (len(spans.get(name, [])), name))
    edits.append((spans[name][0], lines(value)))
new = src
for (s, e), lit in sorted(edits, reverse=True):
    new = new[:s] + lit + new[e:]
if '--check' in sys.argv:
    if new != src:
        print('index.html is out of date with content/. Run: python3 tools/make_pack.py'); sys.exit(1)
    print('index.html is up to date'); sys.exit(0)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(new)
print('index.html: %d trivia, %d quotes, %d stories, %d jokes, %d crosswords, %d cards, '
      '%d plays, %d who-am-I, %d skills' % (
    len(trivia.Q), len(DEF_QUOTES), len(STORIES), len(jokes.JOKES), len(puzzles), len(app.CARD_LIBRARY),
    len(plays.PLAYS), len(whoami.WHOAMI), len(skills.SKILLS)))
