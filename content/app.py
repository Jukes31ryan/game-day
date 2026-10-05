"""Liam's edition: the structure around the content.

Module names, default morning, flavour tags, coach's cards, warm-ups and the
little lines of copy. Everything here replaces a block of the same name in
index.html (see make_pack.py), so the app's behaviour is untouched.
"""

# ─── Modules ─────────────────────────────────────────────────────────────────
# Step ids are permanent and shared with the main app. Only the words change.
STEPS = {
    1:  {"name": "Quote",   "plain": "Quote",        "t": "The Quote",     "s": "Words from the greats",
         "blurb": "A quote from a soccer or football great, and what it means.",
         "h1": "The Quote", "lead": "Words from soccer and football greats. Read it twice."},
    2:  {"name": "Joke",    "plain": "Joke",         "t": "The Joke",      "s": "Something to laugh at",
         "blurb": "Sports jokes, knock-knocks, riddles and dad jokes.",
         "h1": "The Joke", "lead": "Start the day laughing."},
    3:  {"name": "Story",   "plain": "Story",        "t": "The Story",     "s": "A one-minute story",
         "blurb": "True soccer and football stories, plus a few fables. About a minute each."},
    4:  {"name": "Zone",    "plain": "Breathing",    "t": "Get in the Zone", "s": "Breathe like a pro before a big moment",
         "blurb": "Slow breathing, the way players calm down before a penalty kick.",
         "h1": "Get in the zone", "lead": "Players breathe slow before a penalty kick. It calms you down and sharpens you up."},
    5:  {"name": "Coach",   "plain": "Coach's card", "t": "Coach's Card",  "s": "One rule to play by today",
         "blurb": "One rule from your coach's cards, a different one each day.",
         "h1": "Coach's card", "lead": "Today's rule. Say it out loud."},
    6:  {"name": "Plan",    "plain": "Game plan",    "t": "Game Plan",     "s": "What's on, top three, big goal",
         "blurb": "Write down what's happening today, pick your top three, and choose one big goal.",
         "core": True},
    7:  {"name": "Cross",   "plain": "Crossword",    "t": "The Crossword", "s": "A quick sports crossword",
         "blurb": "A small crossword with soccer and football words and easy clues.",
         "h1": "The Crossword", "lead": "Soccer and football words. Tap a square, type a letter. Stuck? Try the other direction."},
    14: {"name": "Warm-up", "plain": "Warm-up",      "t": "Warm-up",       "s": "Two easy minutes",
         "blurb": "Two easy minutes to wake your body up.",
         "h1": "Warm-up", "lead": "Two easy minutes to wake up. Stop if anything hurts."},
    15: {"name": "Trivia",  "plain": "Trivia",       "t": "Sports Trivia", "s": "Five questions a day",
         "blurb": "Five soccer and football questions a day, with a fun fact after each answer.",
         "h1": "Sports trivia", "lead": "Five questions. Take your best guess."},
}

# About ten minutes before school: body, brain, words, plan, laugh.
DEFAULT_FLOW = [14, 15, 1, 7, 5, 6, 2]

# The flavour tags steer trivia, quotes and stories together.
TAG_NAMES = {"soccer": "Soccer", "football": "Football", "more": "Other sports"}
TRV_SPORT = {"soccer": "Soccer", "football": "Football", "more": "Sports"}
TRV_CHEER = ["Nice one!", "Yes!", "Correct!", "You got it!", "Nailed it!", "Right on!", "Boom!"]
TRV_OOPS = ["Not quite.", "Close, but no.", "Good guess, but no.", "Missed that one."]

JOKE_KINDS = {"sport": "Sports joke", "dad": "Dad joke", "knock": "Knock knock",
              "riddle": "Riddle", "silly": "Silly"}

LAUNCH_LINES = [
    "Kickoff. Go get it.",
    "Warmed up and ready. Go have a great day.",
    "You've got a plan. Now go play it.",
    "Game face on. Let's go.",
    "That's the pre-game done. Time for the real thing.",
    "Big goal picked. Go score it.",
    "Ready. Set. Go!",
    "Coach says: you've got this.",
    "Brain on, body on. See you at the final whistle.",
    "Another day, another chance to get better.",
]

# ─── Coach's cards ───────────────────────────────────────────────────────────
# "Category | Line". Short, clear, and things a 10-year-old can actually do.
CARD_LIBRARY = [
    "Effort | Effort is the one thing you always get to choose.",
    "Effort | Hustle back on defense. Every time.",
    "Effort | Try your hardest when nobody is watching, too.",
    "Effort | The last lap counts as much as the first.",
    "Teammate | Be the teammate you'd want to have.",
    "Teammate | Pass to the open player, even if you could shoot.",
    "Teammate | Cheer loudest when a teammate scores.",
    "Teammate | When someone messes up, say \"next one\" and mean it.",
    "Mistakes | Next play. Mistakes are how you get better.",
    "Mistakes | Every great player has missed more shots than you've ever taken.",
    "Mistakes | If you're not making mistakes, you're not trying anything new.",
    "Practice | Practice the boring stuff. That's where great players come from.",
    "Practice | Ten minutes with the ball beats an hour of wishing.",
    "Practice | Use your weaker foot. It won't stay weak for long.",
    "Respect | Shake hands, win or lose.",
    "Respect | The ref is doing their best. Play on.",
    "Respect | Listen to your coach the first time.",
    "Respect | Be a good winner and a good loser.",
    "Body | Water, sleep and breakfast are part of training.",
    "Body | Warm up first. Muscles like a heads-up.",
    "Body | If something really hurts, tell a grown-up.",
    "Confidence | Ask for the ball.",
    "Confidence | Nervous means it matters. That's a good thing.",
    "Confidence | You don't have to be the best. Just be better than yesterday.",
    "Confidence | Try the move. The worst that happens is you learn something.",
    "School | Your brain is a muscle too. Train it.",
    "School | Homework first, then the fun stuff.",
    "School | Ask a question when you're stuck. Smart people do.",
    "Family | Say thanks to whoever drives you to practice.",
    "Family | Help out at home without being asked. Just once today.",
    "Kindness | Pick the kid who usually gets picked last.",
    "Kindness | Say one nice thing to someone today.",
]

# The starter set a brand-new Liam gets.
DEF_AFFIRMS = [
    "Effort | Effort is the one thing you always get to choose.",
    "Teammate | Be the teammate you'd want to have.",
    "Mistakes | Next play. Mistakes are how you get better.",
    "Practice | Practice the boring stuff. That's where great players come from.",
    "Respect | Shake hands, win or lose.",
    "Body | Water, sleep and breakfast are part of training.",
    "Confidence | Ask for the ball.",
    "School | Your brain is a muscle too. Train it.",
    "Family | Say thanks to whoever drives you to practice.",
]

# The second ready-made set: game rules, each one says when and what to do.
SHARP_CARDS = [
    "When you lose the ball | Win it back. Don't stand and watch.",
    "When you make a mistake | Say \"next play\" and get back in position.",
    "When a teammate messes up | Tell them \"good try\". They already feel bad.",
    "When you're nervous | Take three slow breaths. Then ask for the ball.",
    "When you win | Shake hands and say \"good game\" anyway.",
    "When you lose | Shake hands, then figure out one thing to practice.",
    "When the ref gets it wrong | Keep playing. Arguing never changed a call.",
    "When you're tired | That's when the extra effort counts most.",
]

# Nothing to protect: Liam's edition has no older set of cards to pin.
LEGACY_AFFIRMS = []

# ─── Breathing ───────────────────────────────────────────────────────────────
PATTERNS = {
    "calm": {"note": "Slow and steady, in and out. Nothing to count.",
             "phases": [["Breathe in", 4.4, 1], ["Hold", 0.7, 1], ["Breathe out", 4.4, 0], ["Hold", 0.7, 0]]},
    "box":  {"note": "Four counts each way, like drawing a box. Athletes use it before big moments.",
             "phases": [["Breathe in", 4, 1], ["Hold", 4, 1], ["Breathe out", 4, 0], ["Hold", 4, 0]]},
    "478":  {"note": "A long, slow breath out. Great for calming down when you're nervous.",
             "phases": [["Breathe in", 4, 1], ["Hold", 7, 1], ["Breathe out", 8, 0]]},
}

# ─── Warm-ups ────────────────────────────────────────────────────────────────
# New figures in the same style as the main app's, reusing its animations.
FIGS = {
    "jack": '<svg viewBox="0 0 100 90"><g class="fig-reach"><circle cx="50" cy="16" r="10"/><path d="M50 26v32"/>'
            '<path d="M50 32l-17-15M50 32l17-15"/><path d="M50 58l-15 26M50 58l15 26"/></g></svg>',
    "knee": '<svg viewBox="0 0 100 90"><circle cx="48" cy="15" r="10"/><path d="M48 25v33"/>'
            '<path d="M48 33l-15 13M48 33l13-12"/><path d="M48 58l-4 26"/>'
            '<g class="fig-reach"><path d="M48 58l16-2l-1 17"/></g></svg>',
    "kick": '<svg viewBox="0 0 100 90"><circle cx="50" cy="15" r="10"/><path d="M50 25v33"/>'
            '<path d="M50 33l-14 12M50 33l14 12"/><path d="M50 58l2 26"/>'
            '<g class="fig-reach"><path d="M50 58l-6 14l-14-6"/></g></svg>',
    "swing": '<svg viewBox="0 0 100 90"><circle cx="50" cy="15" r="10"/><path d="M50 25v33"/>'
             '<path d="M50 33l-17 7M50 33l17 7"/><path d="M50 58l-5 26"/>'
             '<g class="fig-sway" style="transform-origin:50px 58px"><path d="M50 58l12 24"/></g></svg>',
    "ankle": '<svg viewBox="0 0 100 90"><circle cx="46" cy="15" r="10"/><path d="M46 25v33"/>'
             '<path d="M46 33l-15 11M46 33l15 11"/><path d="M46 58l-2 26"/><path d="M46 58l14 10l-2 8"/>'
             '<g class="fig-roll" style="transform-origin:58px 76px"><path d="M58 76l7 1"/></g></svg>',
}

# One short warm-up. He doesn't need to choose a routine at 6:45am; he needs
# two easy minutes that wake his body up. Nothing jarring first thing.
ROUTINES = {
    "morning": {"name": "Morning warm-up", "note": "Two easy minutes to wake your body up. No rushing, it's early.", "moves": [
        ["Big reach", 20, "Reach both arms up to the ceiling and stretch as tall as you can.", "reach"],
        ["Arm circles", 20, "Big slow circles backward, then forward.", "shoulder"],
        ["Side bends", 20, "One arm up, lean slowly to the side. Then the other side.", "side"],
        ["March in place", 20, "Knees up, arms swinging. An easy march, not a sprint.", "knee"],
        ["Leg swings", 20, "Hold a wall or a chair. Swing one leg forward and back, then switch.", "swing"],
        ["Jumping jacks", 20, "Ten easy jumping jacks to finish. You're awake!", "jack"],
    ]},
}
