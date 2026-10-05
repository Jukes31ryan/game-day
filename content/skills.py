"""Skill of the Day: one thing to practise at recess, in the yard or at
practice. A ball, a wall and a couple of shoes for cones is all any of
them need.

Each skill:
  s      soccer | football
  name   what it's called
  what   what it's for, in one line
  steps  three short steps
  goal   something to aim for today
  tip    one coaching tip

No heading drills: US Soccer's youth rules don't allow heading for players
10 and under. tools/make_pack.py refuses any skill that mentions it.
"""

SKILLS = []
def K(s, name, what, steps, goal, tip):
    SKILLS.append({"s": s, "name": name, "what": what, "steps": steps, "goal": goal, "tip": tip})

S, F = "soccer", "football"

# ─── Soccer ──────────────────────────────────────────────────────────────────
K(S, "Toe taps",
  "Quick touches on top of the ball. They make your feet fast and light.",
  ["Stand with the ball in front of you.",
   "Tap the top of the ball with the toes of one foot, then the other, like running in place.",
   "Stay on your toes and keep the ball still."],
  "30 taps without the ball rolling away.",
  "Look up every few taps. In a game you can't stare at the ball.")

K(S, "Inside-outside dribble",
  "Move the ball with the inside, then the outside, of the same foot. It keeps the ball close.",
  ["Push the ball sideways with the inside of your foot.",
   "Push it back with the outside of the same foot.",
   "Keep going while you walk forward, then try it jogging."],
  "Across the yard and back with your right foot only, then your left.",
  "Small touches. The ball should never be more than a step away.")

K(S, "Juggling",
  "Keep the ball in the air with your feet. Every touch teaches you control.",
  ["Drop the ball onto your laces.",
   "Kick it gently straight up. Let it bounce once if you need to.",
   "Try two touches in a row, then three."],
  "Beat your record. Put your best below.",
  "Lock your ankle and point your toes a little. A floppy foot sends the ball flying.")

K(S, "The Cruyff turn",
  "A fake kick that turns you the other way. Johan Cruyff made it famous at the 1974 World Cup.",
  ["Act like you're about to pass or shoot.",
   "Instead, drag the ball behind your standing leg with the inside of your kicking foot.",
   "Turn and go the other way."],
  "5 with each foot.",
  "Sell the fake. The bigger your pretend kick, the better it works.")

K(S, "The step-over",
  "Swing your foot around the ball without touching it, to fool a defender.",
  ["Dribble toward a shoe or a cone.",
   "Swing your right foot around the front of the ball, from the inside out, without touching it.",
   "Push the ball away with the outside of your left foot."],
  "10 step-overs, 5 each way.",
  "Drop your shoulder the same way as the fake. Defenders watch your body, not your feet.")

K(S, "The pull-back",
  "Stop the ball with the bottom of your foot and roll it back, to change direction fast.",
  ["Dribble forward.",
   "Put the sole of your foot on top of the ball and pull it back toward you.",
   "Turn and push it off in a new direction."],
  "10 pull-backs, using both feet.",
  "Keep your weight on your standing leg so you don't slip.")

K(S, "Sole rolls",
  "Roll the ball side to side under the bottom of your foot. Great for close control.",
  ["Put the sole of your foot on top of the ball.",
   "Roll it across in front of you.",
   "Stop it with your other foot and roll it back."],
  "20 rolls without losing the ball.",
  "Stay light on your toes, like a boxer.")

K(S, "Wall passes",
  "Pass against a wall and control the rebound. It's like having a teammate who never gets tired.",
  ["Stand a few big steps from a wall.",
   "Pass with the inside of your foot.",
   "Control it as it comes back, then pass again."],
  "20 passes in a row without missing.",
  "Use the inside of your foot. It's the biggest, flattest part.")

K(S, "First touch",
  "Control a pass so it stops a step in front of you, ready for your next move.",
  ["Pass hard against a wall, or ask someone to roll you the ball.",
   "As it arrives, let your foot give a little, like catching an egg.",
   "Push it a step to one side, away from an imaginary defender."],
  "10 good first touches in a row.",
  "Look over your shoulder before the ball arrives, so you know which way to go.")

K(S, "Shooting with your laces",
  "The most powerful way to shoot.",
  ["Plant your standing foot beside the ball, pointing at the target.",
   "Point your toes down and lock your ankle.",
   "Strike the middle of the ball with your laces and follow through."],
  "Hit a target, like a gap between two shoes, 5 times out of 10.",
  "Lean over the ball to keep your shot low. Leaning back sends it over the bar.")

K(S, "The chip",
  "A soft kick that lifts the ball over a defender or a goalkeeper.",
  ["Plant your foot next to the ball.",
   "Jab your toes under the bottom of the ball.",
   "Stop your foot quickly, with almost no follow-through."],
  "Chip the ball over a backpack 5 times.",
  "Lean back a little. It's the opposite of a laces shot.")

K(S, "The throw-in",
  "The legal way to put the ball back into play from the sideline.",
  ["Face the field, with both feet on the ground, on or behind the line.",
   "Hold the ball in both hands and take it all the way behind your head.",
   "Throw in one smooth motion, keeping both feet on the ground."],
  "10 legal throws to a target.",
  "If a foot comes off the ground, it's a foul throw and the other team gets the ball.")

K(S, "Goalkeeper's ready stance",
  "How keepers stand so they can dive either way.",
  ["Feet shoulder-width apart, knees bent, weight on the front of your feet.",
   "Hands out in front at waist height, palms facing forward.",
   "Shuffle side to side without crossing your feet."],
  "Have someone toss 10 balls to either side, and catch them.",
  "For a high ball, make a W shape with your thumbs and fingers behind it.")

K(S, "Weak-foot passing",
  "Practise with your other foot. Players who can use both feet are much harder to stop.",
  ["Find a wall.",
   "Pass with the inside of your weaker foot only.",
   "Control it with that same foot too."],
  "20 passes with your weaker foot.",
  "It will feel clumsy at first. That's how you know it's working.")

# ─── Football ────────────────────────────────────────────────────────────────
K(F, "Throwing a spiral",
  "A tight spiral flies further and is easier to catch.",
  ["Grip with your fingers on the laces, leaving a little gap between your palm and the ball.",
   "Step toward your target with your opposite foot and bring the ball up by your ear.",
   "Throw and snap your wrist down, so your thumb finishes pointing at the ground."],
  "10 spirals to a partner.",
  "Point your front shoulder at your target before you throw.")

K(F, "The diamond catch",
  "Catch with your hands, not your body. Hands are softer and surer.",
  ["Make a diamond shape with your thumbs and pointer fingers.",
   "Reach out to meet the ball, and watch it right into your hands.",
   "Squeeze, then pull it in to your chest."],
  "20 catches without trapping it against your body.",
  "For a ball below your waist, flip your hands so your pinkies touch.")

K(F, "High-pointing the ball",
  "Catch the ball at the highest point you can reach, before a defender can.",
  ["Watch the ball as it comes down.",
   "Jump early and reach up with both arms.",
   "Catch it at the top of your jump, then tuck it away as you land."],
  "10 jumping catches.",
  "Time your jump. Going up too late is the most common mistake.")

K(F, "High and tight",
  "Carry the ball so nobody can knock it loose.",
  ["Wrap your fingers over the front point of the ball.",
   "Tuck the back end into your armpit.",
   "Squeeze it against your ribs with your forearm."],
  "Run 10 sprints while someone tries to poke it out.",
  "Carry it in the arm furthest from the defender.")

K(F, "The backpedal",
  "How defensive backs run backwards while still watching the play.",
  ["Lean forward a little, shoulders over your toes.",
   "Take quick, short steps backward, pumping your arms.",
   "Keep your eyes forward the whole time."],
  "Backpedal 10 big steps and back again, 5 times, without stumbling.",
  "If you lean back, you'll fall over. Stay low and forward.")

K(F, "Quick feet",
  "Fast little steps, the footwork every player needs.",
  ["Lay out a line of sticks, shoes or chalk marks, about a foot apart.",
   "Run through, stepping once in each gap.",
   "Then try two feet in each gap."],
  "Count how many times your feet touch the ground in 10 seconds.",
  "Stay on the balls of your feet. Heels make you slow.")

K(F, "The slant route",
  "Three steps up, then a sharp cut toward the middle.",
  ["Run straight for three steps.",
   "Plant hard on your outside foot.",
   "Cut in at an angle, with your hands ready for the ball."],
  "Run it 5 times to each side, then try catching a pass on it.",
  "Make the cut sharp, like a letter V, not a curve.")

K(F, "The juke",
  "A quick fake that sends a defender the wrong way.",
  ["Run toward a defender or a cone.",
   "Plant on one foot and lean your body that way.",
   "Push off hard and burst the other way."],
  "5 jukes in each direction.",
  "Your head and shoulders sell the fake. Your feet just follow.")

K(F, "The three-step drop",
  "How quarterbacks back away from the line to make a quick throw.",
  ["Hold the ball at your chest.",
   "Take three steps back: a big one, then two shorter ones.",
   "Plant on the third step and throw."],
  "10 drops and throws.",
  "Keep the ball up at your chest the whole time, ready to throw.")

K(F, "Punting",
  "Kicking the ball out of your hands, to send it far down the field.",
  ["Hold the ball out in front of you, laces up.",
   "Take two steps and drop the ball. Don't toss it up.",
   "Kick it with your laces, toes pointed, and follow through high."],
  "5 punts that go further than your last one.",
  "A good drop makes a good punt. Practise just dropping it flat.")
