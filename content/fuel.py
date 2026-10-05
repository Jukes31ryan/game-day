"""Fuel Up: the Food Group Sort.

The point, in one line a 10-year-old can say back: there are five food
groups (fruits, vegetables, grains, protein and dairy), and each one does a
job for your body. MyPlate's headline rule rides along: make half your plate
fruits and vegetables.

Every day he sorts six foods into their MyPlate group. Each answer shows a
"Did you know?" nugget about that group. The tricky ones (corn, popcorn,
beans, soy milk) are there on purpose, because they teach the most.

Every placement and every fact below carries the source it was checked
against. tools/make_pack.py refuses anything without one.

House rules:
  - Food is for playing, growing and thinking. No body size, weight,
    calorie or diet talk. make_pack bans the words.
  - No amounts (cups and ounces depend on age, sex and activity).
  - Foods MyPlate leaves out of the five groups (butter, cream cheese, soda,
    candy) aren't in the game at all, rather than being forced into one.
"""

# ─── sources, all checked ────────────────────────────────────────────────────
SRC = {
    "groups":   ("USDA: All About MyPlate Food Groups", "https://www.usda.gov/about-usda/news/blog/back-basics-all-about-myplate-food-groups"),
    "halfplate":("USDA MyPlate for Kids: Make Half Your Plate Fruits and Vegetables", "https://www.fna.usda.gov/tn/myplate-kids-make-half-your-plate-fruits-and-vegetables-poster"),
    "since2011":("USDA: MyPlate's first anniversary", "https://www.usda.gov/about-usda/news/press-releases/2012/05/30/usdas-myplate-celebrates-its-first-anniversary"),
    "fruit":    ("USDA MyPlate: Fruits", "https://www.myplate.gov/eat-healthy/fruits"),
    "veg":      ("USDA Food Buying Guide: Vegetables (MyPlate subgroups)", "https://foodbuyingguide.fns.usda.gov/FoodComponents/ResourceVegetables"),
    "beans":    ("USDA MyPlate: Beans, Peas, and Lentils", "https://www.myplate.gov/eat-healthy/protein-foods/beans-and-peas"),
    "whole":    ("USDA: Make Half Your Grains Whole Grains", "https://snaped.fns.usda.gov/sites/default/files/documents/familymeals_makehalfyourgrainswhole.pdf"),
    "popcorn":  ("USDA ARS: Popcorn, a Healthy, Whole Grain Snack", "https://www.ars.usda.gov/plains-area/gfnd/gfhnrc/docs/news-articles/2021/popcorn-a-healthy-whole-grain-snack/"),
    "protein":  ("USDA MyPlate: Vary Your Protein Routine", "https://www.myplate.gov/sites/default/files/2022-04/TipSheet_5_VaryYourProteinRoutine.pdf"),
    "dairy":    ("USDA: Get Your Dairy", "https://snaped.fns.usda.gov/sites/default/files/documents/familymeals_getyourdairy.pdf"),
    "protein_body": ("MedlinePlus (NIH): Protein in diet", "https://medlineplus.gov/ency/article/002467.htm"),
    "carbs":    ("MedlinePlus (NIH): Carbohydrates", "https://medlineplus.gov/ency/patientinstructions/000321.htm"),
    "calcium":  ("NIH Office of Dietary Supplements: Calcium", "https://ods.od.nih.gov/factsheets/Calcium-Consumer/"),
    "vitd":     ("NIH: Calcium and Vitamin D, Important for Bone Health", "https://www.niams.nih.gov/health-topics/calcium-and-vitamin-d-important-bone-health"),
    "vita":     ("NIH Office of Dietary Supplements: Vitamin A", "https://ods.od.nih.gov/factsheets/VitaminA-Consumer/"),
    "vitc":     ("NIH Office of Dietary Supplements: Vitamin C", "https://ods.od.nih.gov/pdf/factsheets/vitaminc-Consumer.pdf"),
    "iron":     ("NIH Office of Dietary Supplements: Iron", "https://ods.od.nih.gov/pdf/factsheets/iron-consumer.pdf"),
    "potassium":("NIH Office of Dietary Supplements: Potassium", "https://ods.od.nih.gov/factsheets/Potassium-Consumer/"),
}

# ─── the five groups ─────────────────────────────────────────────────────────
# "does": what the group does for his body. "tip": MyPlate's own advice for it.
GROUPS = [
    {"k": "fruit", "name": "Fruits", "c": "#F0443A",
     "does": "Fruits give you vitamins, like vitamin C, plus potassium and fiber.",
     "tip": "Make half your plate fruits and veggies, and eat mostly whole fruit, not juice.",
     "src": ["fruit", "halfplate"]},
    {"k": "veg", "name": "Vegetables", "c": "#22A845",
     "does": "Veggies give you vitamins, like vitamin A for your eyes, plus fiber.",
     "tip": "Vary your veggies: eat lots of different colors.",
     "src": ["vita", "beans", "groups"]},
    {"k": "grain", "name": "Grains", "c": "#F08A1C",
     "does": "Grains give you carbohydrates, your body's main source of energy.",
     "tip": "Make at least half your grains whole grains.",
     "src": ["carbs", "whole"]},
    {"k": "protein", "name": "Protein", "c": "#8B5CF6",
     "does": "Protein helps your body build and repair muscles and other tissue.",
     "tip": "Vary your protein: try beans, eggs, fish, nuts and more.",
     "src": ["protein_body", "protein"]},
    {"k": "dairy", "name": "Dairy", "c": "#2F7BF0",
     "does": "Dairy gives you calcium, which builds strong bones and teeth.",
     "tip": "Choose milk, yogurt, cheese or fortified soy milk.",
     "src": ["calcium", "dairy"]},
]

# ─── the foods ───────────────────────────────────────────────────────────────
# [emoji, name, groups, why, source]. "groups" lists every right answer.
# "why" is shown after the answer, for the ones that surprise people.
F = []
def food(emoji, name, groups, src, why=""):
    F.append({"e": emoji, "n": name, "g": groups, "why": why, "src": src})

for e, n in [("🍎", "Apple"), ("🍌", "Banana"), ("🍓", "Strawberries"), ("🫐", "Blueberries"),
             ("🍊", "Orange"), ("🍇", "Grapes"), ("🍉", "Watermelon"), ("🍍", "Pineapple"),
             ("🥭", "Mango"), ("🍑", "Peach")]:
    food(e, n, ["fruit"], "fruit")
food("🍇", "Raisins", ["fruit"], "fruit", "Dried fruit counts as fruit. So does fresh, frozen and canned.")
food("🧃", "100% orange juice", ["fruit"], "fruit", "100% fruit juice counts as fruit. Whole fruit gives you more fiber, though.")

for e, n in [("🥦", "Broccoli"), ("🥬", "Spinach"), ("🥕", "Carrots"), ("🫑", "Bell pepper"), ("🥒", "Cucumber")]:
    food(e, n, ["veg"], "veg")
food("🍠", "Sweet potato", ["veg"], "veg", "Sweet potatoes are a red-and-orange vegetable, like carrots.")
food("🍅", "Tomato", ["veg"], "veg", "MyPlate counts tomatoes as a red-and-orange vegetable.")
food("🌽", "Corn", ["veg"], "veg", "Corn is a vegetable. It's a starchy vegetable, like potatoes and peas.")
food("🥔", "Potato", ["veg"], "veg", "Potatoes are vegetables. MyPlate calls them starchy vegetables.")
food("🫛", "Green peas", ["veg"], "veg", "Green peas are a starchy vegetable.")

food("🫘", "Black beans", ["veg", "protein"], "beans",
     "Trick question! Beans count as a vegetable or a protein. Both answers are right.")
food("🍲", "Lentil soup", ["veg", "protein"], "beans",
     "Lentils are on two teams: they count as a vegetable or a protein. Both answers are right.")

for e, n in [("🍞", "Bread"), ("🍚", "Rice"), ("🍝", "Pasta"), ("🥯", "Bagel"), ("🥞", "Pancakes"),
             ("🫓", "Tortilla"), ("🧇", "Waffle"), ("🥨", "Pretzel"), ("🍜", "Noodles"), ("🥣", "Cereal")]:
    food(e, n, ["grain"], "groups")
food("🌾", "Oatmeal", ["grain"], "whole", "Oatmeal is a whole grain.")
food("🍿", "Popcorn", ["grain"], "popcorn", "Popcorn is a whole grain. It's corn, but the dried kernels count as a grain.")

for e, n in [("🥚", "Eggs"), ("🍗", "Chicken"), ("🐟", "Fish"), ("🍤", "Shrimp"), ("🦃", "Turkey"), ("🥩", "Steak")]:
    food(e, n, ["protein"], "protein")
food("🥜", "Peanut butter", ["protein"], "protein", "Peanut butter and other nut butters are in the Protein group.")
food("🌻", "Sunflower seeds", ["protein"], "protein", "Nuts and seeds count as protein foods.")

for e, n in [("🥛", "Milk"), ("🧀", "Cheese")]:
    food(e, n, ["dairy"], "dairy")
food("🥄", "Yogurt", ["dairy"], "dairy", "Yogurt is made from milk and has calcium, so it's Dairy.")
food("🥛", "Soy milk", ["dairy"], "dairy", "Fortified soy milk counts in the Dairy group too.")

FOODS = F

# ─── Did you know? ───────────────────────────────────────────────────────────
# Shown after each answer, for that food's group. They rotate.
NUGGETS = {
    "fruit": [
        ("Fruit can be fresh, frozen, canned or dried, and it all counts.", "fruit"),
        ("Whole fruit gives you more fiber than juice, so MyPlate says to eat mostly whole fruit.", "fruit"),
        ("Oranges and strawberries have vitamin C. Your body uses it to heal cuts and scrapes.", "vitc"),
        ("Bananas have potassium. Your muscles need it to work.", "potassium"),
        ("MyPlate says to make half your plate fruits and vegetables.", "halfplate"),
    ],
    "veg": [
        ("Carrots and sweet potatoes have vitamin A. Your eyes need it to see.", "vita"),
        ("MyPlate sorts veggies into teams: dark green, red and orange, beans and peas, starchy, and other.", "veg"),
        ("Broccoli and spinach are on the dark green team.", "veg"),
        ("Corn, potatoes and green peas are starchy vegetables.", "veg"),
        ("MyPlate says to make half your plate fruits and vegetables.", "halfplate"),
    ],
    "grain": [
        ("Grains give you carbohydrates, your body's main source of energy.", "carbs"),
        ("A whole grain keeps all three parts of the seed: the bran, the germ and the endosperm.", "whole"),
        ("Popcorn is a whole grain!", "popcorn"),
        ("MyPlate says to make at least half your grains whole grains, like oatmeal and brown rice.", "whole"),
    ],
    "protein": [
        ("Protein helps your body build and repair muscles.", "protein_body"),
        ("Iron, in meat and beans, helps your blood carry oxygen to your muscles.", "iron"),
        ("Beans, peas and lentils are on two teams. They count as a vegetable or a protein.", "beans"),
        ("Protein foods aren't just meat. Eggs, beans, nuts, seeds and tofu count too.", "protein"),
    ],
    "dairy": [
        ("Almost all the calcium in your body is in your bones and teeth.", "calcium"),
        ("Vitamin D helps your body soak up calcium.", "vitd"),
        ("Butter and cream cheese are made from milk, but they're not in the Dairy group. They have little calcium.", "dairy"),
        ("Fortified soy milk counts in the Dairy group too.", "dairy"),
    ],
}

# The round's sign-off line, under the group spotlight.
EXTRAS = [
    ("MyPlate replaced the old food pyramid in 2011.", "since2011"),
]
