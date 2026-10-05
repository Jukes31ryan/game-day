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



trivia, quotes, jokes, app, plays, whoami, skills, fuel, challenges, sleep, mind = (load(n) for n in (
    'trivia', 'quotes', 'jokes', 'app', 'plays', 'whoami', 'skills', 'fuel', 'challenges', 'sleep', 'mind'))
puzzles = json.load(open(os.path.join(CONTENT, 'puzzles.json')))
errs = []
def check(ok, msg):
    if not ok: errs.append(msg)

SPORTS = {'soccer', 'football'}
TAGS = set(app.TAG_NAMES)

# ─── trivia ──────────────────────────────────────────────────────────────────
seen = set()
for i, q in enumerate(trivia.Q):
    check(q['s'] in TAGS, 'trivia %d: unknown sport %r' % (i, q['s']))
    check(len(q['c']) == 4 and len(set(c.lower() for c in q['c'])) == 4, 'trivia %d: need 4 different choices' % i)
    check(all(c.strip() for c in q['c']), 'trivia %d: empty choice' % i)
    check(q['q'].rstrip().endswith('?'), 'trivia %d: question has no question mark' % i)
    check(len(q['f']) > 20, 'trivia %d: fact too thin' % i)
    check(q['q'] not in seen, 'trivia %d: duplicate question' % i); seen.add(q['q'])

# ─── quotes (the home screen's quote of the day) ─────────────────────────────
DEF_QUOTES = []
for text, who, tags, meaning, question, _src in quotes.QUOTES:
    check('|' not in text and '|' not in who, 'quote has a pipe: ' + text[:40])
    DEF_QUOTES.append(text + ' | ' + who)
check(len(set(DEF_QUOTES)) == len(DEF_QUOTES), 'duplicate quote')

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

# ─── Fuel Up: the Food Group Sort ────────────────────────────────────────────
# Food is fuel. Nothing about body size, weight, calories or dieting, ever.
DIET = re.compile(r'\b(diet\w*|calori\w*|weigh\w*|skinny|fat|fatty|chubby|thin|slim\w*|lose|losing|burn\w*|junk)\b', re.I)
# Every fact names where it was checked: official health and nutrition sources only.
TRUSTED = re.compile(r'^https://([a-z0-9-]+\.)*(usda\.gov|myplate\.gov|nih\.gov|medlineplus\.gov|cdc\.gov|aasm\.org|ussoccer\.com)/')
GROUP_KEYS = [g['k'] for g in fuel.GROUPS]
check(GROUP_KEYS == ['fruit', 'veg', 'grain', 'protein', 'dairy'], 'fuel: MyPlate has five groups, in plate order')
for key, (name, url) in fuel.SRC.items():
    check(bool(TRUSTED.match(url)), 'fuel: source %s is not an official health source: %s' % (key, url))
srcs = lambda ks: all(k in fuel.SRC for k in ([ks] if isinstance(ks, str) else ks))
for g in fuel.GROUPS:
    check(srcs(g['src']) and len(g['does']) > 20 and len(g['tip']) > 15, 'fuel: group %s needs does, tip and a source' % g['k'])
check(len({f['n'] for f in fuel.FOODS}) == len(fuel.FOODS), 'fuel: duplicate food')
for f in fuel.FOODS:
    check(f['g'] and set(f['g']) <= set(GROUP_KEYS), 'fuel: %s has an unknown group' % f['n'])
    check(srcs(f['src']), 'fuel: %s has no source for its group' % f['n'])
    check(len(f['g']) == 1 or f['why'], 'fuel: %s is in two groups, so it has to say why' % f['n'])
for k in GROUP_KEYS:
    check(sum(1 for f in fuel.FOODS if k in f['g']) >= 4, 'fuel: group %s needs at least 4 foods' % k)
    check(len(fuel.NUGGETS.get(k, [])) >= 3, 'fuel: group %s needs at least 3 nuggets' % k)
for k, ns in fuel.NUGGETS.items():
    for t, src in ns:
        check(src in fuel.SRC, 'fuel: nugget without a source: %s' % t[:50])
check(len(fuel.QUIZ) >= 15, 'fuel: need at least 15 quiz questions')
for q, c, why, src in fuel.QUIZ:
    check(q.rstrip().endswith('?'), 'fuel quiz: no question mark: %s' % q[:50])
    check(2 <= len(c) <= 4 and len({x.lower() for x in c}) == len(c), 'fuel quiz: needs 2-4 different choices: %s' % q[:50])
    check(len(why) > 15 and srcs(src), 'fuel quiz: needs a why and a source: %s' % q[:50])
for t, src in fuel.EXTRAS:
    check(src in fuel.SRC, 'fuel: extra without a source: %s' % t[:50])
fuel_text = ([g['does'] for g in fuel.GROUPS] + [g['tip'] for g in fuel.GROUPS] + [f['n'] for f in fuel.FOODS] +
             [f['why'] for f in fuel.FOODS] + [t for ns in fuel.NUGGETS.values() for t, _ in ns] + [t for t, _ in fuel.EXTRAS] +
             [x for q, c, why, _ in fuel.QUIZ for x in [q, why] + c])
for v in fuel_text:
    m = DIET.search(v)
    check(not m, 'fuel: %r has no place in a kid\'s food card: %s' % (m.group(0) if m else '', v[:60]))

# ─── Recovery (sleep) ────────────────────────────────────────────────────────
for key, (name, url) in sleep.SRC.items():
    check(bool(TRUSTED.match(url)), 'sleep: source %s is not an official health source: %s' % (key, url))
check(len(sleep.FACTS) >= 10 and len({f for f, _ in sleep.FACTS}) == len(sleep.FACTS), 'sleep: need 10+ different facts')
for f, src in sleep.FACTS:
    check(src in sleep.SRC, 'sleep: fact without a source: %s' % f[:50])
for t, src in sleep.PLAN:
    check(src is None or src in sleep.SRC, 'sleep: plan item with an unknown source: %s' % t)
check(sleep.KID_HOURS == [9, 12], 'sleep: the AASM range for ages 6-12 is 9 to 12 hours')

# ─── Lights Out ──────────────────────────────────────────────────────────────
# Guided imagination, not facts: no claims about brains, studies or numbers.
check(len(mind.SCRIPTS) >= 10, 'mind: need 10+ wind-downs')
for title, emo, lines in mind.SCRIPTS:
    check(5 <= len(lines) <= 7, 'mind: %s needs 5-7 lines' % title)
    check(not re.search(r'\bstud(y|ies)\b|research|scientists|\bproven\b|\d+ ?%', ' '.join(lines), re.I),
          'mind: %s makes a claim; keep it to imagination' % title)

# ─── warm-ups ────────────────────────────────────────────────────────────────
src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
s, e = blocks(src)['STRETCH_FIGS'][0]
FIGS = json.loads(src[s:e]); FIGS.update(app.FIGS)
for key, r in list(app.ROUTINES.items()) + [('cool-down', app.COOLDOWN)]:
    for move in r['moves']:
        check(move[3] in FIGS, 'routine %s: no figure %r' % (key, move[3]))
        check(len(move) == 4 and move[1] > 0 and len(move[2]) > 10, 'routine %s: move %r needs a name, seconds and a cue' % (key, move[0]))

# ─── Captain's Card ──────────────────────────────────────────────────────────
# Advice, not facts: so no sources, and no made-up numbers either.
check(len({c[0] for c in challenges.CHALLENGES}) == len(challenges.CHALLENGES), 'captain: duplicate challenge')
for c in challenges.CHALLENGES:
    check(len(c) == 4 and all(len(x) > 3 for x in c), 'captain: %r needs a name, goal, how and why' % c[:1])
    check(not re.search(r'\d+ ?%|studies|research|scientists', ' '.join(c), re.I), 'captain: %s states a fact; keep it to advice' % c[0])

# ─── truth check: every fact names where it was checked ─────────────────────
URL = re.compile(r'^https://[a-z0-9.-]+\.[a-z]{2,}/')
def keys(k): return [k] if isinstance(k, str) else list(k)
def good_src(table, where):
    for k, v in table.items():
        check(isinstance(v, tuple) and len(v) == 2 and v[0].strip() and URL.match(v[1]),
              '%s: source %r needs a name and an https link' % (where, k))
good_src(trivia.SRC, 'trivia'); good_src(plays.SRC, 'plays'); good_src(skills.SRC, 'skills')
good_src(whoami.SRC, 'Who Am I?')
TRIVIA_SRC = []
for i, q in enumerate(trivia.Q):
    m = [k for p, k in trivia.CHECKED if q['q'].startswith(p)]
    check(len(m) == 1, 'trivia %d: needs exactly one source in CHECKED, has %d: %s' % (i, len(m), q['q'][:50]))
    if len(m) == 1:
        check(all(k in trivia.SRC for k in keys(m[0])), 'trivia %d: unknown source %r' % (i, m[0]))
        TRIVIA_SRC.append(keys(m[0]))
for w in whoami.WHOAMI:
    check(w['c'][0] in whoami.SRC, 'Who Am I? %r: no source' % w['c'][0])
check(set(whoami.SRC) <= {w['c'][0] for w in whoami.WHOAMI}, 'Who Am I?: a source for an answer that is not there')
PLAY_NAMES = {p['name'] for p in plays.PLAYS}
for name, k in plays.RULES.items():
    check(name in PLAY_NAMES and all(x in plays.SRC for x in keys(k)), 'plays: rule source for %r is broken' % name)
SKILL_NAMES = {k['name'] for k in skills.SKILLS}
for name, k in skills.FACTS.items():
    check(name in SKILL_NAMES and k in skills.SRC, 'skills: fact source for %r is broken' % name)
for q in quotes.QUOTES:
    check(len(q) == 6 and len(q[5]) == 2 and URL.match(q[5][1]), 'quote by %s has no source: %s' % (q[1], q[0][:40]))

# ─── fit for a 10-year-old ───────────────────────────────────────────────────
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
for name, obj in [('trivia', trivia.Q), ('quotes', DEF_QUOTES), ('jokes', jokes.JOKES), ('puzzles', puzzles),
                  ('warm-ups', app.ROUTINES), ('plays', plays.PLAYS), ('who am I', whoami.WHOAMI),
                  ('skills', skills.SKILLS), ('fuel', [fuel.GROUPS, fuel.FOODS, fuel.NUGGETS, fuel.EXTRAS, fuel.QUIZ]),
                  ('captain', [challenges.CHALLENGES, challenges.JOB_IDEAS]), ('cool-down', app.COOLDOWN),
                  ('sleep', [sleep.FACTS, sleep.PLAN]), ('mind', mind.SCRIPTS)]:
    scan(obj, name)

if errs:
    print('\n'.join(errs)); sys.exit('make_pack: %d problem(s), nothing written' % len(errs))

# ─── write ───────────────────────────────────────────────────────────────────
def js(v): return json.dumps(v, ensure_ascii=False, indent=None, separators=(',', ':'))
def lines(v):
    """One entry per line, so a diff of the pack is readable."""
    if isinstance(v, list):
        return '[\n' + ',\n'.join(js(x) for x in v) + '\n]' if v else '[]'
    if isinstance(v, dict):
        return '{\n' + ',\n'.join(js(str(k)) + ':' + js(x) for k, x in v.items()) + '\n}' if v else '{}'
    return js(v)

blocks_out = [
    ('DEF_QUOTES', DEF_QUOTES),
    ('FOOD_GROUPS', fuel.GROUPS), ('FOODS', fuel.FOODS), ('FOOD_NUGGETS', fuel.NUGGETS), ('FOOD_EXTRAS', fuel.EXTRAS),
    ('FOOD_SRC', {k: list(v) for k, v in fuel.SRC.items()}),
    ('FOOD_QUIZ', [{'q': q, 'c': c, 'why': why, 'src': src} for q, c, why, src in fuel.QUIZ]),
    ('TRIVIA', trivia.Q), ('TRV_SPORT', app.TRV_SPORT), ('TRV_CHEER', app.TRV_CHEER), ('TRV_OOPS', app.TRV_OOPS),
    ('WHOAMI', whoami.WHOAMI), ('PLAYS', plays.PLAYS), ('SKILLS', skills.SKILLS),
    ('JOKES', jokes.JOKES), ('JOKE_KINDS', app.JOKE_KINDS),
    ('PUZZLES', puzzles),
    ('PATTERNS', app.PATTERNS), ('STRETCH_FIGS', FIGS), ('ROUTINES', app.ROUTINES), ('COOLDOWN', app.COOLDOWN),
    ('CHALLENGES', challenges.CHALLENGES), ('JOB_IDEAS', challenges.JOB_IDEAS),
    ('SLEEP_FACTS', sleep.FACTS), ('SLEEP_PLAN', sleep.PLAN), ('SLEEP_SRC', {k: list(v) for k, v in sleep.SRC.items()}),
    ('KID_HOURS', sleep.KID_HOURS), ('MIND', mind.SCRIPTS), ('BREATH', mind.BREATH),
]
spans = blocks(src)
edits = []
for name, value in blocks_out:
    if len(spans.get(name, [])) != 1:
        fail('index.html has %d blocks named %s' % (len(spans.get(name, [])), name))
    edits.append((spans[name][0], lines(value)))
new = src
for (s, e), lit in sorted(edits, reverse=True):
    new = new[:s] + lit + new[e:]

# fonts: embedded so the look survives with no signal (SIL Open Font License)
import base64
FONTS = [('Lilita One', '400', 'LilitaOne-latin.woff2'), ('Nunito', '500 900', 'Nunito-latin.woff2')]
face = ''.join("@font-face{font-family:'%s';font-style:normal;font-weight:%s;font-display:swap;"
               "src:url(data:font/woff2;base64,%s) format('woff2')}\n" % (
                   fam, w, base64.b64encode(open(os.path.join(ROOT, 'fonts', f), 'rb').read()).decode())
               for fam, w, f in FONTS)
a, b = new.index('/*FONTS*/'), new.index('/*/FONTS*/')
new = new[:a] + '/*FONTS*/\n' + face + new[b:]

# ─── sources.html: every fact and where it was checked, for grown-ups ───────
SOURCES = os.path.join(ROOT, 'sources.html')
def sources_page():
    from html import escape as h
    def link(name, url): return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (h(url), h(name))
    def table(rows):
        return '<table>' + ''.join('<tr><td>%s</td><td>%s</td></tr>' % (a, b) for a, b in rows) + '</table>'
    def many(tab, ks): return ' · '.join(link(*tab[k]) for k in ks)
    sec = []
    sec.append(('Fuel Up: the food groups', '<p>Every food group, food placement, "Did you know?" and quiz answer '
                'was checked against these official sources.</p><ul>' +
                ''.join('<li>%s</li>' % link(n, u) for n, u in fuel.SRC.values()) + '</ul>'))
    sec.append(('Recovery: sleep', '<p>Every sleep fact and the 9 to 12 hour range for ages 6 to 12.</p><ul>' +
                ''.join('<li>%s</li>' % link(n, u) for n, u in sleep.SRC.values()) + '</ul>'))
    sec.append(('Sports Brain: trivia', table(
        (h(q['q']) + '<br><b>' + h(q['c'][0]) + '.</b> ' + h(q['f']), many(trivia.SRC, ks))
        for q, ks in zip(trivia.Q, TRIVIA_SRC))))
    sec.append(('Sports Brain: Who Am I?', table(
        ('<b>' + h(w['c'][0]) + '.</b> ' + h(' '.join(w['clues'])) + ' ' + h(w['f']), link(*whoami.SRC[w['c'][0]]))
        for w in whoami.WHOAMI)))
    sec.append(('Sports Brain: Playbook rules', '<p>The plays are standard coaching ideas. Where one depends on a '
                'rule, the rule was checked here.</p>' + table(
        (h(n), many(plays.SRC, keys(k))) for n, k in plays.RULES.items())))
    sec.append(('Sports Brain: skills', '<p>No heading drills: U.S. Soccer recommends no heading for players 10 '
                'and under.</p>' + table(
        [('Heading', link(*skills.SRC['heading']))] + [(h(n), link(*skills.SRC[k])) for n, k in skills.FACTS.items()])))
    sec.append(('Quote of the day', '<p>Only quotes traced to the person named. Where the popular wording differs '
                'from what was actually said, we use what was said.</p>' + table(
        ('“' + h(t) + '” <b>' + h(w) + '</b>', link(*src)) for t, w, _, _, _, src in quotes.QUOTES)))
    sec.append(('Not facts, on purpose', '<p>The Captain\'s Card challenges, the warm-ups and the Lights Out '
                'wind-downs are advice and imagination, not facts, so they carry no sources. The build refuses any '
                'of them that slips in a statistic or a "studies show".</p>'))
    body = ''.join('<h2>%s</h2>%s' % (h(t), b) for t, b in sec)
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Game Day Sources</title><meta name="color-scheme" content="light dark"><style>'
            ':root{--bg:#F6F8FC;--ink:#14213D;--mut:#5B6478;--card:#fff;--line:#DDE3EE;--a:#2F7BF0}'
            '@media (prefers-color-scheme:dark){:root{--bg:#0E1424;--ink:#EEF2FA;--mut:#A3ADC2;--card:#172036;--line:#2A3550;--a:#7FB0FF}}'
            'body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 ui-rounded,system-ui,-apple-system,sans-serif}'
            'main{max-width:760px;margin:0 auto;padding:20px 16px 60px}h1{margin:.2em 0}h2{margin:1.6em 0 .4em}'
            'p{color:var(--mut)}a{color:var(--a);overflow-wrap:anywhere}'
            'table{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden}'
            'td{padding:10px 12px;border-top:1px solid var(--line);vertical-align:top;font-size:15px}'
            'td:last-child{width:34%;font-size:14px}tr:first-child td{border-top:0}'
            'ul{background:var(--card);border-radius:12px;padding:12px 12px 12px 32px}li{margin:4px 0}'
            '@media (max-width:560px){td{display:block;width:auto!important}td:last-child{border-top:0;padding-top:0}}'
            '</style></head><body><main><p><a href="./">← Back to Game Day</a></p>'
            '<h1>Where our facts come from</h1><p>For grown-ups. Every fact in Game Day was checked before it '
            'went in, and the build refuses any fact without a source. Anything we couldn\'t confirm was cut. '
            'Spot something wrong? Tell us and we\'ll fix it.</p>' + body + '</main></body></html>\n')

page = sources_page()
old_page = open(SOURCES).read() if os.path.exists(SOURCES) else ''
if '--check' in sys.argv:
    if new != src or page != old_page:
        print('index.html or sources.html is out of date with content/. Run: python3 tools/make_pack.py'); sys.exit(1)
    print('index.html is up to date'); sys.exit(0)
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(new)
open(SOURCES, 'w', encoding='utf-8').write(page)
print('index.html: %d trivia, %d quotes, %d jokes, %d crosswords, %d plays, %d who-am-I, %d skills, '
      '%d foods, %d food nuggets' % (
    len(trivia.Q), len(DEF_QUOTES), len(jokes.JOKES), len(puzzles), len(plays.PLAYS), len(whoami.WHOAMI),
    len(skills.SKILLS), len(fuel.FOODS), sum(len(v) for v in fuel.NUGGETS.values())))
