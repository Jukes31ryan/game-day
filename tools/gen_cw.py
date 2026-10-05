#!/usr/bin/env python3
"""Generate small crosswords from a clued vocabulary.

    tools/gen_cw.py content/words.py content/puzzles.json [--count 30] [--seed 7]

The vocabulary module must define WORDS {WORD: clue} and SPORT {WORD, ...}.
Output is a JSON list in the app's own shape: {"r": [rows], "c": {WORD: clue}}.

Grids are open shapes where each word crosses only two or three others, which
suits a young solver far better than a dense 5x5. Every white square belongs
to at least one clued entry, and there are no two-letter words.

Filling is a backtracking search, one entry at a time, always taking next the
entry most constrained by what's already placed. (Ordering by crossings rather
than by length is what made the old adult generator fast enough to be useful.)
"""
import importlib.util, json, random, sys

# '#' is a block. All 5x5; each white cell is in at least one run of 3+.
PATTERNS = [
    ["#....",
     "#.#.#",
     ".....",
     "#.#.#",
     "....#"],
    ["....#",
     "#.#.#",
     ".....",
     "#.#.#",
     "#...."],
    [".....",
     "#.#.#",
     ".....",
     "#.#.#",
     "....."],
    [".#.#.",
     ".....",
     ".#.#.",
     ".....",
     ".#.#."],
    ["#.#.#",
     ".....",
     "#.#.#",
     ".....",
     "#.#.#"],
]


def slots(pat):
    """Runs of 3+ white cells: (cells, 'A'|'D')."""
    n, out = len(pat), []
    for r in range(n):
        c = 0
        while c < n:
            if pat[r][c] == '#': c += 1; continue
            s = c
            while c < n and pat[r][c] != '#': c += 1
            if c - s >= 3: out.append(([(r, x) for x in range(s, c)], 'A'))
    for c in range(n):
        r = 0
        while r < n:
            if pat[r][c] == '#': r += 1; continue
            s = r
            while r < n and pat[r][c] != '#': r += 1
            if r - s >= 3: out.append(([(x, c) for x in range(s, r)], 'D'))
    return out


def check_pattern(pat):
    n = len(pat)
    assert all(len(row) == n for row in pat), 'ragged pattern'
    covered = {cell for cells, _ in slots(pat) for cell in cells}
    white = {(r, c) for r in range(n) for c in range(n) if pat[r][c] != '#'}
    assert covered == white, 'white squares outside any entry: %s' % sorted(white - covered)
    lines = list(pat) + [''.join(pat[r][c] for r in range(n)) for c in range(n)]
    for line in lines:                                   # no 2-letter runs either way
        assert all(len(run) != 2 for run in line.split('#')), 'two-letter run in %r' % line


def fill(pat, words, sport, rng, budget=20000):
    ss = slots(pat)
    by_len = {}
    for w in words:
        by_len.setdefault(len(w), []).append(w)
    grid, used, placed = {}, set(), [None] * len(ss)
    steps = [0]

    def fits(i, w):
        return all(grid.get(cell, ch) == ch for cell, ch in zip(ss[i][0], w))

    def next_slot():
        best, best_n = None, None
        for i, (cells, _) in enumerate(ss):
            if placed[i] is not None: continue
            n = sum(1 for w in by_len[len(cells)] if w not in used and fits(i, w))
            if best is None or n < best_n: best, best_n = i, n
        return best

    def go():
        steps[0] += 1
        if steps[0] > budget: return False
        i = next_slot()
        if i is None: return True
        cands = [w for w in by_len[len(ss[i][0])] if w not in used and fits(i, w)]
        rng.shuffle(cands)
        cands.sort(key=lambda w: w not in sport)          # sports words first, stable
        for w in cands:
            saved = {cell: grid.get(cell) for cell in ss[i][0]}
            for cell, ch in zip(ss[i][0], w): grid[cell] = ch
            placed[i] = w; used.add(w)
            if go(): return True
            placed[i] = None; used.discard(w)
            for cell, ch in saved.items():
                if ch is None: grid.pop(cell, None)
                else: grid[cell] = ch
        return False

    if not go(): return None
    n = len(pat)
    rows = [''.join('#' if pat[r][c] == '#' else grid[(r, c)] for c in range(n)) for r in range(n)]
    return rows, placed


def main():
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    count = int(a[a.index('--count') + 1]) if '--count' in a else 30
    seed = int(a[a.index('--seed') + 1]) if '--seed' in a else 7
    spec = importlib.util.spec_from_file_location('vocab', a[0])
    v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
    for w, c in v.WORDS.items():
        if w.lower() in c.lower(): sys.exit('clue gives away its answer: %s: %s' % (w, c))
    for p in PATTERNS: check_pattern(p)
    rng = random.Random(seed)

    # Many candidates per shape, then choose: most sports words, least reuse.
    pool = []
    for p in PATTERNS:
        got = 0
        for _ in range(400):
            res = fill(p, v.WORDS, v.SPORT, rng)
            if res and tuple(res[0]) not in {tuple(x[0]) for x in pool}:
                pool.append(res); got += 1
            if got >= 60: break
        print('pattern %s: %d fills' % (p[0], got), file=sys.stderr)
    uses, chosen = {}, []
    per_shape = {}
    while len(chosen) < count and pool:
        def score(res):
            rows, ws = res
            shape = tuple('#' if ch == '#' else '.' for row in rows for ch in row)
            return (sum(w in v.SPORT for w in ws) * 3
                    - sum(uses.get(w, 0) for w in ws) * 4
                    - per_shape.get(shape, 0) * 2)
        pool.sort(key=score, reverse=True)
        rows, ws = pool.pop(0)
        if any(uses.get(w, 0) >= 2 for w in ws): continue      # no word more than twice
        shape = tuple('#' if ch == '#' else '.' for row in rows for ch in row)
        per_shape[shape] = per_shape.get(shape, 0) + 1
        for w in ws: uses[w] = uses.get(w, 0) + 1
        chosen.append({'r': rows, 'c': {w: v.WORDS[w] for w in sorted(ws)}})
    rng.shuffle(chosen)
    json.dump(chosen, open(a[1], 'w'), indent=1)
    print('%d puzzles, %d distinct words, %d sports entries' % (
        len(chosen), len(uses), sum(1 for p in chosen for w in p['c'] if w in v.SPORT)), file=sys.stderr)


if __name__ == '__main__':
    main()
