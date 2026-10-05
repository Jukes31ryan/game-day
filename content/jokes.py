"""Game Day's jokes: clean, silly, and plenty of sports.

Kinds: sport, dad, knock (knock-knock), riddle, silly (anti-jokes and nonsense).
Every joke with a setup holds the punchline back for a tap.
"""

JOKES = []
def J(k, q, a):
    JOKES.append({"k": k, "q": q, "a": a})

# ─── Sports jokes ────────────────────────────────────────────────────────────
for q, a in [
    ("Why did the soccer player bring string to the game?", "So he could tie the score."),
    ("Why can't Cinderella play soccer?", "Because she always runs away from the ball."),
    ("What candy do goalkeepers hate?", "Butterfingers."),
    ("Why did the soccer ball quit the team?", "It was tired of being kicked around."),
    ("What's a ghost's favorite soccer position?", "Ghoul-keeper."),
    ("Why did the chicken get a red card?", "Fowl play."),
    ("What lights up a soccer stadium?", "A soccer match."),
    ("Why was the soccer field wet?", "The players kept dribbling on it."),
    ("Why don't grasshoppers watch soccer?", "They prefer cricket."),
    ("What did the bumblebee striker say after scoring?", "Hive scored!"),
    ("How do you stop squirrels playing soccer in your yard?", "Hide the ball. It drives them nuts."),
    ("Why did the soccer player go to the bank?", "To check his balance."),
    ("Why are soccer players so good at school?", "They know how to use their heads."),
    ("Why did the football coach go to the bank?", "To get his quarterback."),
    ("What's a football player's favorite dessert?", "Turnovers."),
    ("What did the football say to the kicker?", "I get a kick out of you!"),
    ("Where do football players go when they need new uniforms?", "New Jersey."),
    ("How did the soccer field turn into a triangle?", "Somebody took a corner."),
    ("Why did the football player bring a ladder to the game?", "He heard his team was going to the next level."),
    ("What's a quarterback's favorite kind of pizza?", "Any kind, as long as it's delivered on time."),
    ("Why did the soccer ball go to the doctor?", "It was feeling a little deflated."),
    ("Which insect is terrible at football?", "The fumble bee."),
    ("Why was the stadium so cool?", "It was full of fans."),
    ("Why did the referee bring a pencil to the game?", "To draw the match."),
]:
    J("sport", q, a)

# ─── Dad jokes ───────────────────────────────────────────────────────────────
for q, a in [
    ("Why don't skeletons fight each other?", "They don't have the guts."),
    ("What do you call a fake noodle?", "An impasta."),
    ("Why did the scarecrow win an award?", "He was outstanding in his field."),
    ("What do you call a fish with no eyes?", "A fsh."),
    ("What did the ocean say to the beach?", "Nothing. It just waved."),
    ("Why do cows wear bells?", "Because their horns don't work."),
    ("What's brown and sticky?", "A stick."),
    ("Why did the math book look so sad?", "It had too many problems."),
    ("What do you call cheese that isn't yours?", "Nacho cheese."),
    ("Why don't eggs tell jokes?", "They'd crack each other up."),
    ("What do you call a dinosaur with a huge vocabulary?", "A thesaurus."),
    ("How do you throw a party in space?", "You planet."),
    ("Why couldn't the leopard play hide and seek?", "Because he was always spotted."),
    ("Where do you learn to make ice cream?", "Sundae school."),
    ("What do you call an alligator in a vest?", "An investigator."),
    ("What time is it when you go to the dentist?", "Tooth-hurty."),
    ("What do you call a bear with no teeth?", "A gummy bear."),
    ("What do you call a sleeping dinosaur?", "A dino-snore."),
    ("Why did the teddy bear say no to dessert?", "It was already stuffed."),
    ("What do you call a dog that does magic tricks?", "A labracadabrador."),
    ("Why did the kid eat his homework?", "The teacher said it was a piece of cake."),
    ("Why did the kid throw the clock out the window?", "To see time fly."),
    ("Why did the cookie go to the nurse?", "It felt crummy."),
    ("What do you call a bear standing in the rain?", "A drizzly bear."),
    ("What did one wall say to the other wall?", "I'll meet you at the corner."),
    ("Why can't your nose be 12 inches long?", "Because then it would be a foot."),
    ("What do you call a fish wearing a bow tie?", "Sofishticated."),
    ("Why was six afraid of seven?", "Because seven eight nine."),
    ("What do you call a cow with no legs?", "Ground beef."),
    ("Why did the banana go to the doctor?", "It wasn't peeling well."),
    ("What do you call a pile of cats?", "A meow-tain."),
    ("What did the left eye say to the right eye?", "Between you and me, something smells."),
    ("What do you call a snowman with a six-pack?", "An abdominal snowman."),
    ("What does a cloud wear under its raincoat?", "Thunderwear."),
    ("Why did the tomato turn red?", "It saw the salad dressing."),
    ("What do you call a factory that makes okay products?", "A satisfactory."),
]:
    J("dad", q, a)

# ─── Knock knock ─────────────────────────────────────────────────────────────
for who, a in [
    ("Lettuce", "Lettuce in, it's cold out here!"),
    ("Boo", "Don't cry, it's only a joke!"),
    ("Cow says", "No silly, a cow says MOO!"),
    ("Olive", "Olive you, and I miss you!"),
    ("Tank", "You're welcome!"),
    ("Atch", "Bless you!"),
    ("Nobel", "Nobel, that's why I knocked!"),
    ("Canoe", "Canoe help me with my homework?"),
    ("Orange", "Orange you going to let me in?"),
    ("Figs", "Figs the doorbell, it's broken!"),
    ("Justin", "Justin time for breakfast!"),
    ("Luke", "Luke through the peephole and find out!"),
    ("Wooden shoe", "Wooden shoe like to hear another joke?"),
    ("Ref", "Ref-use to open this door and it's a yellow card!"),
    ("Water", "Water you doing? Let's go play!"),
    ("Howard", "Howard you like to go to the game?"),
]:
    J("knock", "Knock knock. Who's there? " + who + ". " + who + " who?", a)
J("knock", "Knock knock. Who's there? Interrupting cow. Interrupting c—", "MOO!")

# ─── Riddles ─────────────────────────────────────────────────────────────────
for q, a in [
    ("What has ears but can't hear?", "A cornfield."),
    ("What gets wetter the more it dries?", "A towel."),
    ("What has hands but can't clap?", "A clock."),
    ("What has a neck but no head?", "A bottle."),
    ("What can you catch but not throw?", "A cold."),
    ("What has one eye but can't see?", "A needle."),
    ("What goes up but never comes down?", "Your age."),
    ("What has lots of keys but can't open a single door?", "A piano."),
    ("The more you take, the more you leave behind. What are they?", "Footsteps."),
    ("What has a head and a tail but no body?", "A coin."),
    ("What can travel all around the world while staying in one corner?", "A stamp."),
    ("What has to be broken before you can use it?", "An egg."),
    ("What belongs to you, but other people use it more than you do?", "Your name."),
    ("What kind of room has no doors or windows?", "A mushroom."),
    ("What's full of holes but still holds water?", "A sponge."),
    ("What runs around a whole soccer field but never moves?", "The white lines."),
    ("What goes up and down but never moves?", "The stairs."),
]:
    J("riddle", q, a)

# ─── Silly ───────────────────────────────────────────────────────────────────
for q, a in [
    ("What's red and bad for your teeth?", "A brick."),
    ("What's green and has wheels?", "Grass. I lied about the wheels."),
    ("What do you call a boomerang that doesn't come back?", "A stick."),
    ("Why did the chicken cross the road?", "To get to the other side. That's it. That's the whole joke."),
    ("Two muffins are in an oven. One says, \"Is it hot in here?\"", "The other one says, \"Aaah! A talking muffin!\""),
    ("What's orange and sounds like a parrot?", "A carrot."),
    ("What do you call a deer with no eyes?", "No idea."),
    ("What's big, gray and doesn't matter?", "An irrelephant."),
    ("A horse walks into a bar.", "Ouch! It should have looked where it was going."),
    ("What do you call a fly with no wings?", "A walk."),
]:
    J("silly", q, a)
