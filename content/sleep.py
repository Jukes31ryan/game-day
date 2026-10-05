"""Recovery: why sleep matters for a young athlete, and tonight's game plan.

Every fact names the official source it was checked against. tools/make_pack.py
refuses a fact without one. No amounts beyond the official hour ranges, and no
celebrity "this pro sleeps 12 hours" stories we can't check.
"""

SRC = {
    "aasm":    ("American Academy of Sleep Medicine: Pediatric sleep recommendations",
                "https://aasm.org/recharge-with-sleep-pediatric-sleep-recommendations-promoting-optimal-health/"),
    "nhlbi_how":("NIH NHLBI: How Much Sleep Is Enough?", "https://www.nhlbi.nih.gov/health/sleep/how-much-sleep"),
    "nhlbi_effects":("NIH NHLBI: How Sleep Affects Your Health", "https://www.nhlbi.nih.gov/health/sleep-deprivation/health-effects"),
    "nhlbi_guide":("NIH NHLBI: Your Guide to Healthy Sleep", "https://www.nhlbi.nih.gov/files/docs/public/sleep/healthy_sleep.pdf"),
    "cdc":     ("CDC: About Sleep", "https://cdc.gov/sleep/about_sleep/sleep_hygiene.html"),
}

# The official ranges, used for the bedtime check: (from age, to age, [min, max] hours).
# Kids pick their age at setup; the app doesn't offer ages under 6.
HOURS = [(6, 12, [9, 12]), (13, 18, [8, 10])]     # AASM

# One a day, in Recovery. [fact, source]
FACTS = [
    ("Kids ages 6 to 12 need 9 to 12 hours of sleep every night.", "aasm"),
    ("When you're a teenager, you'll need 8 to 10 hours of sleep a night.", "aasm"),
    ("During deep sleep, your body releases a hormone that helps kids grow and builds muscle.", "nhlbi_guide"),
    ("Sleep is when your body repairs itself after a hard day of playing.", "nhlbi_guide"),
    ("Sleep helps your brain learn. It makes the memories from your day stronger, like the move you practiced.", "nhlbi_effects"),
    ("Your immune system needs sleep to help you stay healthy.", "nhlbi_effects"),
    ("Kids who don't get enough sleep can have trouble paying attention, and can feel cranky.", "nhlbi_effects"),
    ("Getting the sleep you need is linked to better attention, learning and memory.", "aasm"),
    ("Going to bed and getting up at the same time every day, even on weekends, helps you sleep better.", "cdc"),
    ("A dark, quiet, cool bedroom helps you sleep.", "cdc"),
    ("Being active during the day helps you sleep at night.", "cdc"),
    ("Turn off screens at least 30 minutes before bed.", "cdc"),
    ("Caffeine can keep you awake, so skip soda and tea with caffeine in the evening.", "cdc"),
    ("Sleep affects almost every part of your body, from your brain to your heart and lungs.", "nhlbi_effects"),
]

# Tonight's game plan: tap each one when it's done. [text, source or None]
PLAN = [
    ("Screens off 30 minutes before bed", "cdc"),
    ("Room dark, quiet and cool", "cdc"),
    ("Same bedtime as last night", "cdc"),
    ("Bag and gear ready for tomorrow", None),
]
