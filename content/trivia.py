"""Game Day's trivia: things a 10-year-old who loves soccer and football
would know, or could work out, and learn something from.

Rules for what goes in:
  * mostly soccer and the NFL, plus a small slice of everyday sports anyone his
    age has heard of (LeBron, home runs, the Olympic rings);
  * kid-level: rules he plays by, players he watches, teams, logos, recent
    World Cups and Super Bowls. Not history-buff trivia;
  * stable facts only: no running totals for active players, and anything
    about where a player plays is pinned to when they joined;
  * if a fact wasn't certain, it isn't here.

The correct answer is written first; the app shuffles for display.
s = soccer | football | more     l = label for "more" questions ("Basketball")
"""

Q = []
def T(s, q, right, w1, w2, w3, fact, l=None):
    d = {"s": s, "q": q, "c": [right, w1, w2, w3], "f": fact}
    if l: d["l"] = l
    Q.append(d)

S, F, M = "soccer", "football", "more"

# SOCCER
T(S, 'How many players does each soccer team have on the field?', '11', '9', '10', '12',
  'That includes the goalkeeper. Same number as an American football team!')
T(S, 'How long is a professional soccer match, not counting added time?', '90 minutes', '60 minutes', '80 minutes', '100 minutes',
  'Two halves of 45 minutes. The referee adds extra minutes at the end of each half for time lost to injuries and subs.')
T(S, 'Which player is allowed to use their hands inside their own penalty area?', 'The goalkeeper', 'The captain', 'Any defender', 'The striker',
  "Outside the penalty area, even the goalkeeper can't use their hands.")
T(S, 'What color card does a referee show to send a player off?', 'Red', 'Yellow', 'Green', 'Blue',
  'Two yellow cards in the same game add up to a red, and the team plays with one fewer player.')
T(S, 'How far is the penalty spot from the goal line?', '12 yards', '6 yards', '18 yards', '20 yards',
  "That's 11 meters. The goalkeeper has to keep at least part of one foot on the line until the ball is kicked.")
T(S, "The ball goes over the goal line, but not in the goal, and an attacker touched it last. What's the restart?", 'A goal kick', 'A corner kick', 'A throw-in', 'A penalty',
  'If a defender touched it last, the attacking team gets a corner kick instead.')
T(S, 'A defender touches the ball last before it goes over their own goal line (not in the goal). What does the other team get?', 'A corner kick', 'A goal kick', 'A penalty', 'A free kick',
  'Corners are a great chance to score, especially with a big header.')
T(S, 'How does a team restart play when the ball goes out over the sideline?', 'A throw-in', 'A kick-in', 'A drop ball', 'A corner kick',
  'The thrower has to use both hands, bring the ball from behind the head, and keep both feet on the ground.')
T(S, 'What is it called when a player scores three goals in one game?', 'A hat-trick', 'A three-peat', 'A grand slam', 'A triple-double',
  'The phrase started in cricket in the 1800s, when a bowler who took three wickets in a row was given a hat.')
T(S, "When a goalkeeper doesn't let in a single goal all game, it's called a...?", 'Clean sheet', 'Hat-trick', 'Brace', 'Nutmeg',
  "In the USA it's also called a shutout.")
T(S, 'What is a "nutmeg"?', "Kicking the ball between a defender's legs", 'A spinning shot', 'A long throw-in', 'A diving header',
  'Players love doing it and hate having it done to them.')
T(S, 'What is "offside"?', 'Being closer to the goal than the last defender when the ball is passed to you', 'Kicking the ball out of bounds', 'Touching the ball with your hand', 'Standing in the center circle at kickoff',
  "You can't be offside in your own half, or straight from a throw-in, goal kick or corner kick.")
T(S, 'At kickoff, where is the ball placed?', 'On the center spot', 'On the penalty spot', 'In the corner arc', 'On the goal line',
  'Every player has to be in their own half until the ball is kicked.')
T(S, 'How many substitutes can a team usually use in a top professional game today?', '5', '3', '2', '11',
  'For many years it was only 3. The limit went up to 5 in 2020.')
T(S, 'What does "VAR" stand for?', 'Video Assistant Referee', 'Very Accurate Ref', 'Video And Replay', 'Viewing Angle Review',
  "VAR was first used at a men's World Cup in 2018 in Russia.")
T(S, 'If a knockout World Cup game is tied after extra time, what happens?', 'A penalty shootout', 'The game is replayed', 'A coin toss', 'Both teams go through',
  "Each team takes five penalties. If it's still tied, they keep going one kick each until one team scores and the other misses.")
T(S, 'What does the assistant referee (the linesman) carry?', 'A flag', 'A whistle', 'A stopwatch', 'A red card only',
  'They raise the flag for offside, throw-ins and fouls the referee might miss.')
T(S, 'What is it called when a player accidentally scores in their own net?', 'An own goal', 'A backfire', 'A reverse goal', 'A back-heel',
  'It still counts, but for the other team.')
T(S, 'Which body part are field players NOT allowed to play the ball with?', 'Their hands and arms', 'Their head', 'Their chest', 'Their knees',
  'A handball gives the other team a free kick, or a penalty if it happens in the box.')
T(S, "Traditionally, which shirt number does a team's starting goalkeeper wear?", '1', '10', '7', '9',
  "Goalkeepers also wear a different color from everyone else, so the referee can tell who's allowed to use their hands.")
T(S, 'Pelé, Maradona and Messi all made which shirt number famous?', '10', '7', '9', '11',
  "The number 10 usually goes to a team's most creative attacking player.")
T(S, "Which country has won the most men's World Cups?", 'Brazil', 'Germany', 'Italy', 'Argentina',
  'Brazil has won five: 1958, 1962, 1970, 1994 and 2002.')
T(S, "Which country won the 2022 men's World Cup in Qatar?", 'Argentina', 'France', 'Brazil', 'Croatia',
  'Argentina and France drew 3-3 in the final, and Argentina won the penalty shootout.')
T(S, 'Who scored a hat-trick in the 2022 World Cup final, and still lost?', 'Kylian Mbappé', 'Lionel Messi', 'Harry Kane', 'Olivier Giroud',
  "It was only the second hat-trick ever in a men's World Cup final. The first was by England's Geoff Hurst in 1966.")
T(S, "How often is the men's FIFA World Cup played?", 'Every 4 years', 'Every 2 years', 'Every 3 years', 'Every year',
  'Qualifying takes almost the whole time in between.')
T(S, "Which three countries hosted the 2026 men's World Cup?", 'USA, Canada and Mexico', 'USA, Brazil and Argentina', 'Canada, England and Ireland', 'Mexico, Spain and Portugal',
  'It was the first World Cup with 48 teams. Before that, it had 32.')
T(S, 'Which player is the only one to win three World Cups?', 'Pelé', 'Diego Maradona', 'Ronaldo', 'Lionel Messi',
  'Pelé won in 1958, 1962 and 1970. He was just 17 at the first one.')
T(S, 'What is the "Golden Boot"?', "The award for a tournament's top goalscorer", 'The trophy for the best goalkeeper', 'The boots Pelé wore', 'The World Cup trophy',
  'The best goalkeeper at a World Cup gets the Golden Glove.')
T(S, "How many Women's World Cups have the USA won?", '4', '2', '3', '5',
  'They won in 1991, 1999, 2015 and 2019, more than any other country.')
T(S, 'In which country was Lionel Messi born?', 'Argentina', 'Spain', 'Brazil', 'Uruguay',
  "He moved to Spain when he was 13 to join Barcelona's youth academy.")
T(S, 'Which country is Cristiano Ronaldo from?', 'Portugal', 'Spain', 'Brazil', 'Italy',
  'He grew up on Madeira, a small island in the Atlantic Ocean.')
T(S, 'Which MLS club did Lionel Messi join in 2023?', 'Inter Miami', 'LA Galaxy', 'Seattle Sounders', 'Orlando City',
  "David Beckham is one of Inter Miami's owners.")
T(S, "What is the Ballon d'Or?", 'An award for the best player in the world that year', 'A famous stadium in France', 'The World Cup trophy', 'A French soccer club',
  'The name is French for "Golden Ball".')
T(S, "Which player has won the men's Ballon d'Or the most times?", 'Lionel Messi', 'Cristiano Ronaldo', 'Pelé', 'Zinedine Zidane',
  'Messi has won it eight times.')
T(S, 'Which US player is nicknamed "Captain America"?', 'Christian Pulisic', 'Landon Donovan', 'Clint Dempsey', 'Tim Howard',
  'He won the Champions League with Chelsea in 2021.')
T(S, 'Harry Kane is the all-time top goalscorer for which national team?', 'England', 'Scotland', 'Wales', 'Ireland',
  "He passed Wayne Rooney's record in 2023.")
T(S, 'Which country does Erling Haaland play for?', 'Norway', 'Sweden', 'Denmark', 'Germany',
  "His dad, Alf-Inge Haaland, also played in England's Premier League.")
T(S, 'Which country does Kylian Mbappé play for?', 'France', 'Belgium', 'Spain', 'Cameroon',
  'He won the World Cup with France when he was only 19.')
T(S, 'Which country is Mohamed Salah from?', 'Egypt', 'Morocco', 'Senegal', 'Algeria',
  'Fans in Egypt treat him like a superhero.')
T(S, 'What is the top soccer league in England called?', 'The Premier League', 'La Liga', 'Serie A', 'The Bundesliga',
  "It started in 1992, and it's watched in more countries than any other league.")
T(S, 'La Liga is the top soccer league in which country?', 'Spain', 'Italy', 'France', 'Portugal',
  'Real Madrid and Barcelona are its two most famous clubs.')
T(S, 'LA Galaxy, Seattle Sounders and Inter Miami all play in which league?', 'MLS', 'NWSL', 'The Premier League', 'La Liga',
  'Major League Soccer played its first season in 1996.')
T(S, 'What is the name of the tournament for the best club teams in Europe?', 'The Champions League', 'The Gold Cup', 'The Copa América', 'The Premier League',
  'Its famous anthem plays before every game.')
T(S, 'Which club has won the European Cup, now called the Champions League, more times than any other?', 'Real Madrid', 'Barcelona', 'Bayern Munich', 'Liverpool',
  'Their home stadium is the Santiago Bernabéu in Madrid.')
T(S, 'Which club plays its home games at the Camp Nou?', 'Barcelona', 'Real Madrid', 'Atlético Madrid', 'Valencia',
  "It's one of the biggest stadiums in the world.")
T(S, 'What are the big matches between Real Madrid and Barcelona called?', 'El Clásico', 'The Derby', 'The Old Firm', 'The Super Bowl',
  'The Old Firm is the rivalry between Celtic and Rangers in Scotland.')
T(S, 'Which English club is nicknamed "The Red Devils"?', 'Manchester United', 'Liverpool', 'Arsenal', 'Chelsea',
  'They play at Old Trafford in Manchester.')
T(S, 'Which London club is nicknamed "The Gunners"?', 'Arsenal', 'Chelsea', 'Tottenham', 'West Ham',
  'The club was started in 1886 by workers at the Royal Arsenal, a factory that made weapons.')
T(S, 'Which club plays at Anfield and sings "You\'ll Never Walk Alone"?', 'Liverpool', 'Everton', 'Manchester City', 'Newcastle',
  'The whole stadium sings it together before big games.')
T(S, 'Bayern Munich is a club from which country?', 'Germany', 'Austria', 'Italy', 'France',
  'Munich is in the south of Germany, near the Alps.')
T(S, 'Which club is known as "Barça"?', 'Barcelona', 'Real Madrid', 'Benfica', 'Boca Juniors',
  'Their motto is "More than a club."')
T(S, "What color is Brazil's famous home shirt?", 'Yellow', 'Green', 'Blue', 'White',
  'Yellow with green trim. Brazil\'s team is often just called "the Seleção".')
# FOOTBALL
T(F, 'How many points is a touchdown worth?', '6', '3', '7', '5',
  'After a touchdown, the team gets a chance to add 1 or 2 more points.')
T(F, 'How many points is a field goal worth?', '3', '2', '1', '6',
  'The kick has to go between the uprights and over the crossbar.')
T(F, 'How many points is a safety worth?', '2', '1', '3', '6',
  'A safety happens when the defense tackles the ball carrier in their own end zone.')
T(F, 'After a touchdown, how many points is a successful kick through the uprights?', '1', '2', '3', '6',
  "It's called the extra point, or the point after touchdown.")
T(F, "Instead of kicking after a touchdown, a team can run or pass it in from close. What's that worth?", '2 points', '1 point', '3 points', '6 points',
  "It's called a two-point conversion. It's harder than kicking, so it's worth more.")
T(F, 'How many yards does the offense need to gain to get a new first down?', '10', '5', '15', '20',
  'The two sticks on the sideline, connected by a chain, show exactly how far 10 yards is.')
T(F, 'How many downs does the offense get to go 10 yards?', '4', '3', '5', '6',
  "Most teams punt on fourth down if they're far from a first down.")
T(F, 'How many players does each team have on the field in the NFL?', '11', '9', '12', '10',
  'The same as soccer! But in football, teams swap in whole groups: one for offense, one for defense.')
T(F, 'How long is an NFL field from one goal line to the other?', '100 yards', '80 yards', '120 yards', '90 yards',
  "Add the two 10-yard end zones and it's 120 yards long.")
T(F, 'How long is an NFL game, on the game clock?', '60 minutes', '90 minutes', '48 minutes', '40 minutes',
  'Four quarters of 15 minutes. With all the stops, a game usually takes more than three hours.')
T(F, 'What is it called when the defense tackles the quarterback behind the line of scrimmage?', 'A sack', 'A block', 'A fumble', 'A punt',
  'Sacks became an official NFL stat in 1982.')
T(F, 'What is it called when a defender catches a pass meant for the other team?', 'An interception', 'A fumble', 'A touchback', 'A safety',
  'If they run it back for a touchdown, people call it a pick-six.')
T(F, "What is it called when a player drops the ball while it's still in play?", 'A fumble', 'An interception', 'A sack', 'A punt',
  'Either team can grab a fumble.')
T(F, "What color flag does a referee throw when there's a penalty?", 'Yellow', 'Red', 'White', 'Blue',
  'Coaches throw a red flag when they want to challenge a call.')
T(F, 'What is the line where the ball is placed before each play called?', 'The line of scrimmage', 'The goal line', 'The sideline', 'The fifty',
  'Nobody on either team can cross it until the ball is snapped.')
T(F, 'What is a "Hail Mary"?', 'A long, hopeful pass at the very end of a half', 'A kind of field goal', 'A trick punt', 'A penalty for holding',
  'Cowboys quarterback Roger Staubach made the name famous after a last-second winning pass in 1975.')
T(F, 'What is a "fair catch"?', 'Waving your arm so no one can hit you while you catch a punt', 'Catching a pass with both feet in', 'A catch the referee reviews', 'Catching a fumble in the air',
  "The catch is safe, but the returner can't run with the ball after it.")
T(F, 'What happens if an NFL game is tied after four quarters?', 'They play overtime', 'It ends in a tie right away', 'A coin toss decides it', 'They kick field goals until someone misses',
  'In the playoffs they keep playing until somebody wins.')
T(F, 'Which position throws most of the passes?', 'Quarterback', 'Running back', 'Tight end', 'Linebacker',
  'The quarterback is often called the QB.')
T(F, 'Which player kicks field goals?', 'The kicker', 'The quarterback', 'The punter', 'The center',
  'The punter is a different player. He kicks the ball away on fourth down.')
T(F, 'What does NFL stand for?', 'National Football League', 'North Football League', 'National Field League', 'New Football League',
  'The league started in 1920.')
T(F, "What is the NFL's championship game called?", 'The Super Bowl', 'The World Series', 'The Stanley Cup', 'The Rose Bowl',
  "It's played in early February, and more people watch it than almost anything else on TV in America.")
T(F, 'What is the Super Bowl trophy called?', 'The Vince Lombardi Trophy', 'The Stanley Cup', 'The Heisman Trophy', "The Larry O'Brien Trophy",
  "It's named after the coach whose Green Bay Packers won the first two Super Bowls.")
T(F, 'Which player has won the most Super Bowls?', 'Tom Brady', 'Joe Montana', 'Peyton Manning', 'Patrick Mahomes',
  'Seven: six with the New England Patriots and one with the Tampa Bay Buccaneers.')
T(F, 'Who has thrown for the most yards and touchdowns in NFL history?', 'Tom Brady', 'Peyton Manning', 'Drew Brees', 'Brett Favre',
  'He threw 649 touchdown passes in the regular season.')
T(F, 'Patrick Mahomes won his first Super Bowl with which team?', 'Kansas City Chiefs', 'Buffalo Bills', 'Dallas Cowboys', 'Texas Tech',
  'He also played baseball growing up. His dad was a Major League pitcher.')
T(F, 'Which team won the Super Bowl in February 2024?', 'Kansas City Chiefs', 'San Francisco 49ers', 'Philadelphia Eagles', 'Baltimore Ravens',
  'They beat the 49ers 25-22 in overtime, only the second Super Bowl ever to go to overtime.')
T(F, 'Which team won the Super Bowl in February 2025?', 'Philadelphia Eagles', 'Kansas City Chiefs', 'Buffalo Bills', 'Detroit Lions',
  'They beat the Kansas City Chiefs 40-22.')
T(F, 'Which two NFL teams host a game every Thanksgiving?', 'Detroit Lions and Dallas Cowboys', 'Chicago Bears and Green Bay Packers', 'New York Giants and Jets', 'Kansas City Chiefs and Denver Broncos',
  'The Lions have played on Thanksgiving since 1934.')
T(F, 'Fans of which NFL team wear foam "cheesehead" hats?', 'Green Bay Packers', 'Chicago Bears', 'Minnesota Vikings', 'Buffalo Bills',
  'Wisconsin, where Green Bay is, is famous for making cheese.')
T(F, 'Which NFL team has a star on its helmet?', 'Dallas Cowboys', 'Houston Texans', 'Arizona Cardinals', 'New York Giants',
  'The Cowboys are often called "America\'s Team".')
T(F, 'Which NFL team has a horseshoe on its helmet?', 'Indianapolis Colts', 'Denver Broncos', 'Kansas City Chiefs', 'Las Vegas Raiders',
  'A horseshoe is meant to bring good luck.')
T(F, 'How many teams are in the NFL?', '32', '30', '28', '36',
  "They're split into two conferences, the AFC and the NFC, and the winners meet in the Super Bowl.")
T(F, 'Is the Super Bowl played in the same stadium every year?', 'No, a different city hosts it each year', 'Yes, always in Miami', 'Yes, always in Los Angeles', "It's played at the home of the better team",
  'Cities are chosen years in advance.')
# GENERAL
T(M, 'How many players does each basketball team have on the court?', '5', '6', '7', '4',
  'Five players, but an NBA team can have up to 15 on the roster.', 'Basketball')
T(M, 'How many points is a shot from behind the three-point line worth?', '3', '2', '4', '1',
  'The NBA added the three-point line in 1979.', 'Basketball')
T(M, "Who is the NBA's all-time leading scorer?", 'LeBron James', 'Kareem Abdul-Jabbar', 'Michael Jordan', 'Kobe Bryant',
  "He passed Kareem Abdul-Jabbar's record in 2023.", 'Basketball')
T(M, 'Michael Jordan won six NBA championships with which team?', 'Chicago Bulls', 'Los Angeles Lakers', 'Boston Celtics', 'Washington Wizards',
  'He won three in a row twice: 1991-93 and 1996-98.', 'Basketball')
T(M, 'Who has made the most three-pointers in NBA history?', 'Stephen Curry', 'Ray Allen', 'Klay Thompson', 'James Harden',
  'He changed the way basketball is played. Now everyone shoots threes.', 'Basketball')
T(M, 'What is "traveling" in basketball?', 'Taking too many steps without dribbling', 'Throwing the ball out of bounds', 'Fouling a shooter', 'Holding the ball too long',
  'The other team gets the ball.', 'Basketball')
T(M, 'How many strikes make an out?', '3', '2', '4', '5',
  "A foul ball counts as a strike, but usually can't be strike three.", 'Baseball')
T(M, 'How many innings are in a normal Major League game?', '9', '7', '10', '6',
  "If it's tied after nine, they keep playing extra innings.", 'Baseball')
T(M, 'What is a home run with the bases loaded called?', 'A grand slam', 'A hat-trick', 'A triple play', 'A walk-off',
  'It scores four runs with one swing.', 'Baseball')
T(M, "What is Major League Baseball's championship called?", 'The World Series', 'The Super Bowl', 'The Stanley Cup', 'The Big Dance',
  'The first World Series was played in 1903.', 'Baseball')
T(M, 'Shohei Ohtani is famous for being a great hitter and also a great what?', 'Pitcher', 'Catcher', 'Base stealer', 'Coach',
  "Hardly anyone in the modern game has been a star at both. He's from Japan.", 'Baseball')
T(M, 'What trophy does the NHL champion win?', 'The Stanley Cup', 'The Lombardi Trophy', 'The Gold Cup', "The Commissioner's Trophy",
  'Every player on the winning team gets to spend a day with the Cup.', 'Hockey')
T(M, 'What do hockey players hit instead of a ball?', 'A puck', 'A birdie', 'A disc', 'A shuttle',
  "Pucks are frozen before games so they don't bounce as much.", 'Hockey')
T(M, 'Which hockey player is known as "The Great One"?', 'Wayne Gretzky', 'Sidney Crosby', 'Alex Ovechkin', 'Connor McDavid',
  'He has more points than any player in NHL history.', 'Hockey')
T(M, 'How many rings are on the Olympic flag?', '5', '4', '6', '7',
  'They stand for the five parts of the world that take part in the Olympics.', 'Olympics')
T(M, 'Which swimmer has won the most Olympic gold medals ever?', 'Michael Phelps', 'Katie Ledecky', 'Mark Spitz', 'Caeleb Dressel',
  'He won 23 golds and 28 medals in total.', 'Olympics')
T(M, 'Usain Bolt, the fastest man ever over 100 meters, is from which country?', 'Jamaica', 'USA', 'Kenya', 'Canada',
  'His world record is 9.58 seconds, set in 2009.', 'Olympics')
T(M, 'What sport is Simone Biles famous for?', 'Gymnastics', 'Swimming', 'Figure skating', 'Track',
  "She's won more world and Olympic medals than any other gymnast in history.", 'Olympics')
T(M, 'Which US city will host the 2028 Summer Olympics?', 'Los Angeles', 'New York', 'Chicago', 'Miami',
  'LA also hosted in 1932 and 1984.', 'Olympics')
T(M, 'How many holes are in a standard round of golf?', '18', '9', '12', '20',
  'Many courses have a 9-hole version for shorter games.', 'Golf')
T(M, "What's the highest score you can get in a single game of bowling?", '300', '200', '100', '500',
  'It takes 12 strikes in a row.', 'Bowling')

# ─── New: soccer things kids his age talk about ──────────────────────────────
T(S, "What does a yellow card mean?", "It's a warning", "You're sent off", "Your team scores", "It's halftime",
  "Get a second yellow in the same game and it turns into a red, and you have to leave the field.")
T(S, "What happens if a player gets two yellow cards in one game?", "They're sent off", "Nothing", "Their team gets a penalty", "They sit out five minutes",
  "Two yellows make a red. Their team has to play the rest of the game with one fewer player.")
T(S, "What do soccer players wear under their socks to protect their legs?", "Shin guards", "Knee pads", "Ankle weights", "Leg bands",
  "They're required in real games, even for professionals.")
T(S, "Why does the referee add extra minutes at the end of each half?", "To make up for time lost to injuries, subs and delays", "To give the losing team a chance", "Because the clock runs slow", "So fans can buy snacks",
  "It's called stoppage time, or added time. The fourth official holds up a board showing how many minutes.")
T(S, "What does MLS stand for?", "Major League Soccer", "Main League Soccer", "Most Liked Sport", "Major League Stadiums",
  "It's the top league in the USA and Canada.")
T(S, "What color is Inter Miami's famous home shirt?", "Pink", "Green", "Orange", "Purple",
  "Pink with black. When Messi joined, fans everywhere wanted one.")
T(S, "Before joining Inter Miami, which club did Lionel Messi play two seasons for?", "Paris Saint-Germain", "Manchester City", "Real Madrid", "Juventus",
  "Before that, he spent his whole career at Barcelona, from when he was 13.")
T(S, "Lionel Messi played most of his career for which club?", "Barcelona", "Real Madrid", "Manchester United", "Bayern Munich",
  "He scored more than 600 goals for Barcelona.")
T(S, "Which English club did Erling Haaland join in 2022?", "Manchester City", "Liverpool", "Arsenal", "Chelsea",
  "He scored 36 Premier League goals in his first season, a new record.")
T(S, "What is Erling Haaland's famous goal celebration?", "Sitting cross-legged like he's meditating", "A backflip", "Sucking his thumb", "Pretending to call someone on the phone",
  "It looks like meditation, and it's become his trademark.")
T(S, "When Cristiano Ronaldo scores, he jumps, spins and shouts what?", "Siu!", "Goal!", "Olé!", "Vamos!",
  "It sounds like \"sí\", Spanish for \"yes\". Kids all over the world copy it.")
T(S, "Which English club did Mohamed Salah join in 2017?", "Liverpool", "Chelsea", "Arsenal", "Tottenham",
  "Fans sing songs about him at Anfield.")
T(S, "Which club did Kylian Mbappé join in 2024?", "Real Madrid", "Barcelona", "Liverpool", "Bayern Munich",
  "He'd played for Paris Saint-Germain before that.")
T(S, "The FIFA video games got a new name in 2023. What are they called now?", "EA Sports FC", "FIFA Ultimate", "World Soccer", "Goal 24",
  "The games are made by EA Sports. FC stands for Football Club.")
T(S, "What is the US men's national soccer team often called?", "The USMNT", "The Stars", "The Eagles", "The Patriots",
  "The women's team is the USWNT.")
T(S, "Which country hosted the 2022 World Cup?", "Qatar", "Brazil", "Russia", "USA",
  "It was played in November and December, because summer in Qatar is too hot.")
T(S, "Which club plays its home games at Old Trafford?", "Manchester United", "Manchester City", "Liverpool", "Arsenal",
  "Fans call it the Theatre of Dreams.")
T(S, "What is a free kick?", "A kick given to a team after the other team commits a foul", "A kick anyone can take at any time", "A kick at the start of the game", "A practice kick before the match",
  "The other team's players have to stand at least 10 yards away.")

# ─── New: NFL things kids his age know ───────────────────────────────────────
T(F, "How many points is a touchdown plus the extra point?", "7", "6", "8", "9",
  "That's why so many football scores end in 7s, like 14, 21 and 28.")
T(F, "On TV, there's a yellow line across the field. What is it?", "The first-down line, drawn by a computer", "A line painted on the grass", "A laser on the field", "A rope the referees hold",
  "The players can't see it. It only shows up on TV. It was first used in 1998.")
T(F, "Which player snaps the ball to the quarterback?", "The center", "The kicker", "The tight end", "The safety",
  "The snap starts every play.")
T(F, "What is the area at each end of the field where touchdowns are scored called?", "The end zone", "The goal box", "The red zone", "The sideline",
  "Each end zone is 10 yards deep.")
T(F, "When a referee raises both arms straight up, what does it mean?", "A score, like a touchdown", "A penalty", "A timeout", "The game is over",
  "It also means a field goal or extra point was good.")
T(F, "Tom Brady won his last Super Bowl with which team?", "Tampa Bay Buccaneers", "New England Patriots", "Las Vegas Raiders", "Miami Dolphins",
  "He was 43 years old. It was the first time a team won the Super Bowl in its own stadium.")
T(F, "Seattle Seahawks fans are known by what nickname?", "The 12th Man", "The Flock", "The Sea Squad", "The Hawk Nation",
  "Football teams have 11 players on the field, and the fans are so loud they're like a 12th.")
T(F, "Which NFL team has a lightning bolt on its helmet?", "Los Angeles Chargers", "Tennessee Titans", "Houston Texans", "Carolina Panthers",
  "The lightning bolt goes all the way back to the 1960s.")
T(F, "Which NFL team's stadium has a big pirate ship that fires cannons?", "Tampa Bay Buccaneers", "Miami Dolphins", "Seattle Seahawks", "New Orleans Saints",
  "The cannons go off when the Bucs score.")
T(F, "What is the Heisman Trophy for?", "The best college football player of the year", "The Super Bowl winner", "The best NFL coach", "The longest field goal",
  "The trophy is a statue of a player stiff-arming a tackler.")
T(F, "Which NFL team puts its logo on only one side of the helmet?", "Pittsburgh Steelers", "Dallas Cowboys", "Green Bay Packers", "Chicago Bears",
  "Only the right side. They tried it on one side first, and it stuck.")
T(F, "The Baltimore Ravens are named after a famous poem. Who wrote it?", "Edgar Allan Poe", "Dr. Seuss", "Shel Silverstein", "Robert Frost",
  "Poe lived in Baltimore. His poem is called \"The Raven\".")
T(F, "Which player catches passes and runs long routes down the field?", "Wide receiver", "Center", "Kicker", "Linebacker",
  "Running backs and tight ends catch passes too.")
T(F, "Who blocks to protect the quarterback?", "The offensive line", "The cornerbacks", "The kickers", "The referees",
  "There are five of them, and they're usually the biggest players on the team.")
T(F, "In the NFL Draft, which team usually gets the very first pick?", "The team with the worst record", "The Super Bowl winner", "The team with the best record", "A random team",
  "It's meant to help the weakest teams get better.")
T(F, "What is the two-minute warning?", "A break when there are 2 minutes left in each half", "A penalty for being slow", "Two minutes before kickoff", "A warning for arguing with the referee",
  "Teams use it to plan their last plays.")
T(F, "A football is often nicknamed what?", "A pigskin", "A melon", "A rocket", "A cowhide",
  "Footballs are actually made of cowhide leather now.")
T(F, "How many laces are on an NFL football?", "8", "4", "6", "12",
  "The laces help the quarterback grip the ball and make it spin.")
T(F, "The Denver Broncos' stadium is nicknamed after the city's height. What's it called?", "Mile High", "Sky Field", "Mountain Dome", "Cloud Nine",
  "Denver is one mile above sea level. The air is thinner, so kicks fly a little farther.")
T(F, "In February 2020, Patrick Mahomes won his first Super Bowl by beating which team?", "San Francisco 49ers", "Philadelphia Eagles", "Buffalo Bills", "Tampa Bay Buccaneers",
  "The Chiefs were losing in the fourth quarter and came back to win 31-20.")
T(F, "Travis Kelce became famous playing which position for the Chiefs?", "Tight end", "Quarterback", "Kicker", "Running back",
  "A tight end blocks like a lineman and catches passes like a receiver.")
T(F, "Which NFL team plays in Jacksonville, Florida?", "Jaguars", "Panthers", "Dolphins", "Buccaneers",
  "Florida has three NFL teams: the Jaguars, the Dolphins and the Buccaneers.")
T(F, "What is the kick that starts each half called?", "The kickoff", "The punt", "The field goal", "The extra point",
  "A kickoff also happens after every touchdown and field goal.")
T(F, "What is a pick-six?", "An interception returned for a touchdown", "A six-yard run", "The sixth pick in the draft", "A field goal from six yards",
  "\"Pick\" is another word for an interception, and a touchdown is worth 6.")
T(F, "What is the Pro Bowl?", "The NFL's all-star game", "The first game of the season", "A bowling game for players", "The college championship",
  "Fans, players and coaches vote on who gets picked.")
