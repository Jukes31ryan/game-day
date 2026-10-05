"""The Playbook: one soccer or football strategy a day, explained for a
10-year-old. Standard, well-established ideas only, the kind he'll hear a
commentator name or a coach use.

Each play:
  s     soccer | football
  name  what it's called
  what  one line: what it is
  how   2-3 short steps
  why   why it works, in plain words
  look  when he'll see it, or can use it himself
  d     the diagram, drawn by the app:
          "p": players  [team, x, y]   team "u" = his team, "t" = the other team
          "b": the ball [x, y]
          "a": arrows   [kind, x1, y1, x2, y2]   kind "pass" | "run" | "dribble"
        The field is 100 wide and 60 tall. His team always attacks to the right.
"""

PLAYS = []
def P(s, name, what, how, why, look, players, ball, arrows):
    PLAYS.append({"s": s, "name": name, "what": what, "how": how, "why": why, "look": look,
                  "d": {"p": players, "b": ball, "a": arrows}})

S, F = "soccer", "football"

# ─── Soccer ──────────────────────────────────────────────────────────────────
P(S, "The give-and-go",
  "Pass to a teammate, sprint past your defender, and get the ball straight back.",
  ["Pass the ball to a teammate.", "Sprint past the defender the moment you let it go.",
   "Your teammate passes it right back into the space in front of you."],
  "One defender can't follow the ball and you at the same time. Two quick passes beat him without any dribbling.",
  "Watch for it near the penalty box. It's also called a one-two, and you can use it in any small-sided game.",
  [["u", 40, 32], ["t", 52, 32], ["u", 56, 18]], [40, 32],
  [["pass", 40, 32, 55, 19], ["run", 41, 34, 70, 34], ["pass", 56, 19, 69, 32]])

P(S, "The overlap",
  "A teammate runs around the outside of the player with the ball.",
  ["The winger has the ball near the sideline, with a defender in front.",
   "A teammate sprints past on the outside.",
   "The winger slides the ball into that teammate's path."],
  "The defender has to choose: stay with the winger or chase the runner. Either way, someone gets free.",
  "Full-backs do this all the time. Look for a defender suddenly appearing in a wide attack.",
  [["u", 60, 16], ["t", 67, 18], ["u", 44, 8]], [60, 16],
  [["run", 45, 7, 80, 5], ["pass", 61, 15, 78, 6]])

P(S, "Switching the play",
  "A long pass from the crowded side of the field to the empty side.",
  ["Your team has the ball on one side, and lots of defenders have moved over.",
   "Look across the field for a teammate in space.",
   "Play a long pass over to them."],
  "Defenders slide toward the ball. Switching it fast catches them out, with lots of room on the other side.",
  "Look for a long diagonal pass across the field, then a player with time to run forward.",
  [["u", 40, 14], ["t", 48, 9], ["t", 50, 20], ["t", 56, 13], ["u", 62, 50]], [40, 14],
  [["pass", 41, 16, 61, 48]])

P(S, "The through ball",
  "A pass into the space behind the defenders, for a teammate to run onto.",
  ["A striker starts level with the last defender.",
   "As the striker starts running, the passer plays the ball into the gap behind the defense.",
   "The striker gets there first and is through on goal."],
  "Defenders are facing the wrong way. The striker is already running toward goal, so they can't catch up.",
  "Watch strikers like Haaland time their runs. If they go too early, they're offside.",
  [["u", 44, 30], ["t", 64, 20], ["t", 64, 40], ["u", 58, 36]], [44, 30],
  [["run", 59, 36, 81, 27], ["pass", 45, 30, 80, 27]])

P(S, "The press",
  "Chase the ball as a team the moment you lose it, to win it back near their goal.",
  ["As soon as the other team gets the ball, the closest player rushes them.",
   "Teammates close down the easy passes.",
   "The player with the ball runs out of time and makes a mistake."],
  "Winning the ball near their goal means you only have a short way to go to score.",
  "Liverpool under Jürgen Klopp and Barcelona under Pep Guardiola made it famous. Look for three players swarming the ball at once.",
  [["t", 80, 30], ["t", 88, 18], ["t", 88, 44], ["u", 68, 30], ["u", 74, 16], ["u", 74, 46]], [80, 30],
  [["run", 69, 30, 78, 30], ["run", 75, 17, 85, 20], ["run", 75, 45, 85, 42]])

P(S, "Staying compact",
  "When defending, the whole team stays close together.",
  ["Defenders and midfielders form two lines.",
   "Keep the lines close together, and move left and right as the ball moves.",
   "Leave no big gaps for the other team to pass through."],
  "If there are no gaps, the other team has to pass around you instead of through you, which is much harder.",
  "Watch a team defending a lead late in a game. Everyone is packed in front of their own goal.",
  [["u", 22, 18], ["u", 22, 26], ["u", 22, 34], ["u", 22, 42], ["u", 32, 20], ["u", 32, 30], ["u", 32, 40],
   ["t", 50, 30]], [50, 30],
  [])

P(S, "The offside trap",
  "Defenders step forward together just before a pass, leaving an attacker offside.",
  ["The defenders stand in a straight line.",
   "Just as the other team is about to pass, they all step up together.",
   "The attacker is suddenly behind them, and the flag goes up for offside."],
  "It wins the ball back without a tackle. But if one defender doesn't step up, the trick fails.",
  "Look for a line of defenders moving forward at the same moment, with their arms up appealing.",
  [["u", 28, 16], ["u", 28, 26], ["u", 28, 36], ["u", 28, 46], ["t", 32, 31], ["t", 46, 28]], [46, 28],
  [["run", 29, 16, 37, 16], ["run", 29, 26, 37, 26], ["run", 29, 36, 37, 36], ["run", 29, 46, 37, 46]])

P(S, "Using the width",
  "Keep players near both sidelines to stretch the other team out.",
  ["Two players stay very wide, near the sidelines.",
   "Defenders have to spread out to watch them.",
   "That opens gaps in the middle for passes and runs."],
  "A spread-out defense has holes. A bunched-up attack is easy to defend.",
  "When a coach shouts \"Get wide!\", this is why.",
  [["u", 60, 4], ["u", 60, 56], ["u", 48, 30], ["t", 64, 16], ["t", 64, 44], ["u", 70, 30]], [48, 30],
  [["pass", 49, 29, 69, 30]])

P(S, "The third-man run",
  "Player one passes to player two, who flicks it on for player three, who was already running.",
  ["Player one passes to player two.",
   "Player three starts running before that pass even arrives.",
   "Player two passes first time into player three's path."],
  "Defenders watch the ball and the player near it. The third player's run is the one nobody is watching.",
  "It's a move top teams practise over and over. It looks like magic when it works.",
  [["u", 36, 40], ["u", 52, 30], ["u", 46, 50], ["t", 56, 38]], [36, 40],
  [["pass", 37, 39, 51, 31], ["run", 47, 50, 72, 46], ["pass", 53, 31, 71, 45]])

P(S, "The near-post run",
  "On a cross, an attacker sprints to the post closest to the ball.",
  ["A winger gets ready to cross from near the end line.",
   "An attacker sprints toward the near post.",
   "The cross is whipped in low and hard, and the attacker gets there first."],
  "Defenders and goalkeepers expect the ball to come to the middle. A quick run to the near post gets there before them.",
  "Watch corner kicks and crosses: one player always darts to the front post.",
  [["u", 88, 8], ["u", 74, 30], ["t", 84, 37], ["t", 97, 30]], [88, 8],
  [["run", 75, 30, 92, 24], ["pass", 88, 9, 93, 23]])

P(S, "Shielding the ball",
  "Use your body to keep a defender away from the ball.",
  ["Stand sideways between the defender and the ball.",
   "Keep the ball on your far foot, away from them.",
   "Use your arm for balance, not to push, and wait for help or a gap."],
  "The defender can't reach the ball without pushing past you, and pushing is a foul.",
  "Big strikers do this with their back to goal to hold the ball until teammates arrive.",
  [["u", 50, 30], ["t", 44, 30], ["u", 64, 20]], [53, 30],
  [["pass", 54, 29, 63, 21]])

P(S, "The counter-attack",
  "Win the ball and attack fast, before the other team gets back.",
  ["Your team wins the ball in its own half.",
   "Pass forward quickly, as early as you can.",
   "Teammates sprint forward to join in while the other team is out of position."],
  "When a team attacks, its defenders move up. Win the ball then, and there's lots of space behind them.",
  "Some great goals come just seconds after a team was defending.",
  [["u", 28, 30], ["u", 50, 32], ["u", 40, 14], ["u", 40, 46], ["t", 33, 39], ["t", 74, 30]], [28, 30],
  [["pass", 29, 30, 48, 32], ["dribble", 52, 32, 64, 32], ["run", 41, 14, 74, 20], ["run", 41, 46, 74, 42]])

P(S, "First touch away from pressure",
  "Control the ball into open space, away from the defender.",
  ["Before the ball arrives, look over your shoulder to see where the defender is.",
   "Use your first touch to push the ball away from them.",
   "Now you have time to pass, shoot or dribble."],
  "A great first touch buys you time. A bad one gives the ball away.",
  "Watch midfielders take a quick look before the ball comes. That's how they know where to touch it.",
  [["u", 48, 30], ["t", 55, 26], ["u", 34, 30]], [48, 30],
  [["pass", 35, 30, 47, 30], ["dribble", 49, 31, 52, 42]])

P(S, "The pass back to reset",
  "When everything is blocked, pass backwards and start again.",
  ["You have the ball but defenders block every pass forward.",
   "Instead of forcing it, pass back to a teammate.",
   "They can switch the play or find a new way forward."],
  "Keeping the ball is better than losing it. A pass back isn't giving up, it's choosing a better moment.",
  "Top teams pass backward a lot. They're waiting for the defense to make a mistake.",
  [["u", 60, 30], ["t", 68, 21], ["t", 68, 39], ["t", 67, 30], ["u", 44, 30]], [60, 30],
  [["pass", 59, 30, 45, 30]])

P(S, "Playing out from the back",
  "The goalkeeper and defenders start attacks with short passes, not long kicks.",
  ["The goalkeeper rolls or passes the ball to a defender.",
   "The defenders pass between each other to find a free player.",
   "The ball moves up the field one pass at a time."],
  "A long kick is often lost. Short passes keep the ball and pull the other team out of shape.",
  "Watch the start of a goal kick: defenders spread wide and the keeper passes short.",
  [["u", 4, 30], ["u", 16, 14], ["u", 16, 46], ["u", 30, 30], ["t", 24, 20]], [4, 30],
  [["pass", 5, 31, 15, 45], ["pass", 17, 45, 29, 31]])

# ─── Football ────────────────────────────────────────────────────────────────
P(F, "The screen pass",
  "Let the rushers through, then throw a short pass to a player behind a wall of blockers.",
  ["The offensive line lets the defenders rush past toward the quarterback.",
   "Some linemen slip out to the side and set up in front of the running back.",
   "The quarterback flips a short pass to the running back behind those blockers."],
  "The defenders who rushed are now behind the play, and the blockers clear the way.",
  "Look for a pass that goes backward or sideways, then a running back with blockers in front.",
  [["u", 34, 30], ["u", 46, 26], ["u", 46, 34], ["u", 38, 42], ["t", 54, 26], ["t", 54, 34]], [34, 30],
  [["run", 53, 26, 40, 27], ["run", 53, 34, 41, 33], ["run", 47, 35, 58, 48], ["run", 39, 43, 52, 52], ["pass", 35, 31, 51, 51]])

P(F, "Play-action",
  "The quarterback fakes a handoff, then throws deep.",
  ["The quarterback pretends to hand the ball to the running back.",
   "The defense moves up to stop the run.",
   "The quarterback pulls the ball back and throws over their heads."],
  "If the defense believes it's a run, the receivers get open behind them.",
  "Look for the running back diving into the line without the ball, then a long pass.",
  [["u", 40, 30], ["u", 36, 38], ["u", 46, 8], ["t", 62, 28]], [40, 30],
  [["run", 37, 38, 47, 35], ["run", 61, 28, 55, 30], ["run", 47, 8, 84, 10], ["pass", 41, 29, 82, 11]])

P(F, "The blitz",
  "The defense sends extra players to rush the quarterback.",
  ["Usually only the defensive linemen rush the quarterback.",
   "On a blitz, linebackers or defensive backs rush too.",
   "There are more rushers than blockers, so someone gets a free run."],
  "It can lead to a sack. But fewer players are left to cover receivers, so it's risky.",
  "Look for a defender sprinting through the line the moment the ball is snapped.",
  [["u", 38, 30], ["u", 46, 25], ["u", 46, 35], ["t", 54, 25], ["t", 54, 35], ["t", 60, 12], ["t", 60, 48]], [38, 30],
  [["run", 59, 13, 41, 27], ["run", 59, 47, 41, 33]])

P(F, "Man or zone coverage",
  "Two ways to guard receivers: follow one player, or guard an area.",
  ["In man coverage, each defender sticks to one receiver wherever they go.",
   "In zone coverage, each defender guards a patch of the field.",
   "Quarterbacks look at the defense before the snap to figure out which it is."],
  "Man coverage is tight but can be beaten by a fast player. Zone leaves gaps between the areas.",
  "If a defender follows a receiver all the way across the field, that's man coverage.",
  [["u", 50, 10], ["u", 50, 50], ["t", 58, 10], ["t", 58, 50], ["u", 40, 30]], [40, 30],
  [["run", 51, 10, 80, 26], ["run", 59, 11, 78, 25], ["run", 51, 50, 80, 50], ["run", 59, 50, 78, 50]])

P(F, "The slant",
  "A receiver takes a few steps, then cuts sharply toward the middle.",
  ["The receiver runs straight for three steps.",
   "He plants his outside foot and cuts in at an angle.",
   "The quarterback throws it quickly, before the defender can react."],
  "It's fast and hard to stop. The receiver's body shields the ball from the defender.",
  "It's a quick pass you'll see a lot, especially when a team needs just a few yards.",
  [["u", 50, 12], ["t", 56, 12], ["u", 42, 30]], [42, 30],
  [["run", 51, 12, 58, 12], ["run", 58, 13, 72, 26], ["pass", 43, 29, 70, 25]])

P(F, "The option",
  "The quarterback watches one defender, then decides to keep the ball or pitch it.",
  ["The quarterback runs toward the edge with the running back behind him.",
   "He watches the defender on the end.",
   "If the defender comes at him, he pitches to the running back. If not, he keeps it and runs."],
  "Whatever the defender does is wrong. He can't stop two players at once.",
  "Running quarterbacks love it. Look for a quick sideways toss right before a tackle.",
  [["u", 40, 26], ["u", 36, 34], ["t", 60, 38]], [40, 26],
  [["run", 41, 27, 54, 38], ["run", 59, 38, 56, 38], ["run", 37, 35, 58, 54], ["pass", 54, 39, 56, 52]])

P(F, "The draw",
  "It looks like a pass, but it's a run up the middle.",
  ["The quarterback drops back like he's going to throw.",
   "The pass rushers charge upfield toward him.",
   "Then he hands the ball to the running back, who runs right through the gap they left."],
  "Rushers who are chasing the quarterback are out of position to stop a run.",
  "Look for a late handoff after the quarterback has already dropped back.",
  [["u", 40, 30], ["u", 40, 36], ["u", 46, 26], ["u", 46, 34], ["t", 54, 24], ["t", 54, 36], ["t", 64, 22]], [40, 30],
  [["run", 39, 30, 34, 30], ["run", 53, 23, 38, 20], ["run", 53, 37, 38, 42], ["run", 41, 35, 62, 33]])

P(F, "The QB sneak",
  "On a very short distance, the quarterback takes the snap and pushes straight ahead.",
  ["The offense needs only a yard or less.",
   "The quarterback takes the snap from under center.",
   "He lowers his shoulders and pushes straight forward behind the center."],
  "It's the fastest way to gain a tiny bit of ground. The ball is across the line before the defense can react.",
  "Look for it on fourth and inches, often near the goal line.",
  [["u", 43, 30], ["u", 47, 30], ["u", 47, 23], ["u", 47, 37], ["t", 53, 26], ["t", 53, 34]], [43, 30],
  [["run", 44, 30, 60, 30]])

P(F, "The two-minute drill",
  "A hurry-up offense at the end of a half, racing the clock.",
  ["The offense skips the huddle and plays fast.",
   "Receivers catch the ball and step out of bounds to stop the clock.",
   "The quarterback can spike the ball into the ground to stop the clock too."],
  "Every second counts. A team can go the length of the field in under two minutes.",
  "Watch the last two minutes of a close game. It's when the best quarterbacks shine.",
  [["u", 42, 30], ["u", 50, 10], ["t", 58, 10]], [42, 30],
  [["run", 51, 10, 66, 10], ["run", 66, 10, 72, 3], ["pass", 43, 29, 71, 4]])

P(F, "The onside kick",
  "A short kickoff the kicking team tries to get back.",
  ["The kicking team has to tell the referee first. In the NFL, surprise onside kicks aren't allowed.",
   "The kicker sends the ball bouncing along the ground. It has to go at least 10 yards before the kicking team can touch it.",
   "The kicking team races to grab it and keep the ball."],
  "If it works, they keep the ball right after kicking off. If it fails, the other team gets the ball much closer to scoring than usual.",
  "You'll usually see it when a team is behind late in the game and needs the ball back.",
  [["u", 38, 30], ["u", 40, 14], ["u", 40, 46], ["t", 56, 20], ["t", 56, 40]], [38, 30],
  [["dribble", 39, 29, 50, 25], ["run", 41, 14, 50, 21], ["run", 41, 46, 50, 29]])

P(F, "Double coverage",
  "Two defenders guard one dangerous receiver.",
  ["One defender stays close to the receiver underneath.",
   "A second defender stays deeper, over the top.",
   "The receiver has nowhere to go, short or long."],
  "It takes away the other team's best player. But it leaves someone else with only one defender.",
  "Look at where the defense puts two players. That's who they're most afraid of.",
  [["u", 50, 12], ["t", 57, 17], ["t", 76, 6], ["u", 40, 30]], [40, 30],
  [["run", 51, 12, 80, 13], ["run", 58, 17, 78, 17], ["run", 77, 6, 82, 9]])

P(F, "The red zone",
  "The area inside the other team's 20-yard line, close to scoring.",
  ["The field gets short, so there's less room for long passes.",
   "Teams use quick, accurate passes and strong runs.",
   "A field goal is good, but a touchdown is the real goal."],
  "A touchdown is worth 6 points plus a try for more. A field goal is only 3. So getting into the end zone matters.",
  "Listen for commentators saying a team is \"in the red zone\". It means they're close to scoring.",
  [["u", 74, 30], ["u", 86, 14], ["t", 90, 18], ["t", 88, 36]], [74, 30],
  [["run", 87, 14, 94, 22], ["pass", 75, 29, 93, 23]])

P(F, "The prevent defense",
  "Late in a game, the winning team plays deep to stop long passes.",
  ["Defenders back up far from the line.",
   "They let the offense complete short passes.",
   "They stop anything deep, so the clock keeps running."],
  "If you're ahead, giving up 5 yards is fine. Giving up a touchdown is not.",
  "Look for defenders standing very far back in the last minute of a close game.",
  [["u", 42, 30], ["u", 50, 12], ["u", 50, 48], ["t", 82, 12], ["t", 84, 30], ["t", 82, 48]], [42, 30],
  [["run", 51, 12, 60, 14], ["pass", 43, 29, 59, 15]])

P(F, "The hard count",
  "The quarterback changes the rhythm of his call to trick the defense into jumping early.",
  ["The quarterback shouts the snap count with a sudden loud change in his voice.",
   "A defender thinks the ball is about to be snapped and jumps across the line.",
   "That's a penalty, and the offense gets five free yards."],
  "Free yards without even running a play.",
  "Listen to the quarterback before the snap. Sometimes he yells \"Hut!\" extra loud on purpose.",
  [["u", 40, 30], ["u", 46, 24], ["u", 46, 30], ["u", 46, 36], ["t", 54, 24], ["t", 54, 34]], [46, 30],
  [["run", 53, 24, 48, 19]])

P(F, "The fake punt",
  "On fourth down, the team lines up to punt, then runs or passes instead.",
  ["The team lines up like it's going to punt the ball away.",
   "The defense drops back to catch the punt.",
   "Instead, the punter or another player runs or throws for the first down."],
  "The defense is set up for a kick, not a play, so there's lots of space.",
  "It's rare and risky, which is exactly why it surprises people.",
  [["u", 30, 30], ["u", 46, 26], ["u", 46, 34], ["u", 48, 8], ["t", 88, 30], ["t", 56, 24]], [30, 30],
  [["run", 49, 8, 68, 10], ["pass", 31, 29, 66, 11]])


# ---------------------------------------------------------------------------
# The strategies are coaching ideas. Where a play leans on a rule (offside,
# the onside kick, a false start, stopping the clock), the rule was checked
# here. tools/make_pack.py lists these in sources.html.
SRC = {
    "ifab_offside": ("IFAB: Law 11, Offside", "https://www.theifab.com/laws/latest/offside/"),
    "nfl_rules":    ("NFL Football Operations: rulebook", "https://operations.nfl.com/the-rules/nfl-rulebook/"),
    "nfl_2026":     ("ESPN: NFL rules changes for 2026, including onside kicks", "https://www.espn.com/nfl/story/_/id/49868175/nfl-rules-changes-2026-red-challenge-flags-kickoffs-penalties-hip-drop"),
    "press":        ("Gegenpressing", "https://en.wikipedia.org/wiki/Gegenpressing"),
}
RULES = {
    "The through ball": "ifab_offside",
    "The offside trap": "ifab_offside",
    "The press": "press",
    "The two-minute drill": "nfl_rules",
    "The onside kick": ("nfl_rules", "nfl_2026"),
    "The red zone": "nfl_rules",
    "The hard count": "nfl_rules",
    "The fake punt": "nfl_rules",
}
