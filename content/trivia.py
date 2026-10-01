"""Liam's trivia bank.

Rules for what goes in:
  * stable facts only — rules, history, and records that are settled. No
    current rosters (players change clubs) and no running totals for active
    players, where the number would go stale mid-season.
  * the correct answer is written first; the app shuffles for display.
  * if a fact wasn't certain, it isn't here. Cutting beats hedging.

s = sport tag (soccer, football, basketball, baseball, more)
l = optional label shown on the card when the tag is too broad ("Hockey")
"""

Q = []
def T(s, q, right, w1, w2, w3, fact, l=None):
    d = {"s": s, "q": q, "c": [right, w1, w2, w3], "f": fact}
    if l: d["l"] = l
    Q.append(d)

S = "soccer"
# ─── Soccer: the rules ───────────────────────────────────────────────────────
T(S, "How many players does each soccer team have on the field?", "11", "9", "10", "12",
  "That includes the goalkeeper. Same number as an American football team!")
T(S, "How long is a professional soccer match, not counting added time?", "90 minutes", "60 minutes", "80 minutes", "100 minutes",
  "Two halves of 45 minutes. The referee adds extra minutes at the end of each half for time lost to injuries and subs.")
T(S, "Which player is allowed to use their hands inside their own penalty area?", "The goalkeeper", "The captain", "Any defender", "The striker",
  "Outside the penalty area, even the goalkeeper can't use their hands.")
T(S, "What color card does a referee show to send a player off?", "Red", "Yellow", "Green", "Blue",
  "Two yellow cards in the same game add up to a red, and the team plays with one fewer player.")
T(S, "How far is the penalty spot from the goal line?", "12 yards", "6 yards", "18 yards", "20 yards",
  "That's 11 meters. The goalkeeper has to keep at least part of one foot on the line until the ball is kicked.")
T(S, "The ball goes over the goal line, but not in the goal, and an attacker touched it last. What's the restart?", "A goal kick", "A corner kick", "A throw-in", "A penalty",
  "If a defender touched it last, the attacking team gets a corner kick instead.")
T(S, "A defender touches the ball last before it goes over their own goal line (not in the goal). What does the other team get?", "A corner kick", "A goal kick", "A penalty", "A free kick",
  "Corners are a great chance to score, especially with a big header.")
T(S, "How does a team restart play when the ball goes out over the sideline?", "A throw-in", "A kick-in", "A drop ball", "A corner kick",
  "The thrower has to use both hands, bring the ball from behind the head, and keep both feet on the ground.")
T(S, "How far do opponents have to stand from the ball at a free kick?", "10 yards", "5 yards", "15 yards", "20 yards",
  "That's 9.15 meters. Some referees spray a line of vanishing foam so everyone knows where to stand.")
T(S, "What is it called when a player scores three goals in one game?", "A hat-trick", "A three-peat", "A grand slam", "A triple-double",
  "The phrase started in cricket in the 1800s, when a bowler who took three wickets in a row was given a hat.")
T(S, "Two goals in one game by the same player is called a...?", "Brace", "Pair", "Double-double", "Clean sheet",
  "A brace is an old word for a pair, like a brace of pheasants.")
T(S, "When a goalkeeper doesn't let in a single goal all game, it's called a...?", "Clean sheet", "Hat-trick", "Brace", "Nutmeg",
  "In the USA it's also called a shutout.")
T(S, "What is a \"nutmeg\"?", "Kicking the ball between a defender's legs", "A spinning shot", "A long throw-in", "A diving header",
  "Players love doing it and hate having it done to them.")
T(S, "What is \"offside\"?", "Being closer to the goal than the last defender when the ball is passed to you", "Kicking the ball out of bounds", "Touching the ball with your hand", "Standing in the center circle at kickoff",
  "You can't be offside in your own half, or straight from a throw-in, goal kick or corner kick.")
T(S, "At kickoff, where is the ball placed?", "On the center spot", "On the penalty spot", "In the corner arc", "On the goal line",
  "Every player has to be in their own half until the ball is kicked.")
T(S, "How big is a full-size soccer goal?", "8 feet high, 24 feet wide", "6 feet high, 18 feet wide", "10 feet high, 30 feet wide", "8 feet high, 20 feet wide",
  "That's 2.44 meters by 7.32 meters. Kids' goals are smaller.")
T(S, "What's the half-circle on the edge of the penalty box for?", "Keeping players 10 yards from the penalty spot", "Marking where corners are taken", "Showing where the coach stands", "Nothing, it's just decoration",
  "It's called the penalty arc, or \"the D\".")
T(S, "How many substitutes can a team usually use in a top professional game today?", "5", "3", "2", "11",
  "For many years it was only 3. The limit went up to 5 in 2020.")
T(S, "What does \"VAR\" stand for?", "Video Assistant Referee", "Very Accurate Ref", "Video And Replay", "Viewing Angle Review",
  "VAR was first used at a men's World Cup in 2018 in Russia.")
T(S, "If a knockout World Cup game is tied after extra time, what happens?", "A penalty shootout", "The game is replayed", "A coin toss", "Both teams go through",
  "Each team takes five penalties. If it's still tied, they keep going one kick each until one team scores and the other misses.")
T(S, "What does the assistant referee (the linesman) carry?", "A flag", "A whistle", "A stopwatch", "A red card only",
  "They raise the flag for offside, throw-ins and fouls the referee might miss.")
T(S, "What is it called when a player accidentally scores in their own net?", "An own goal", "A backfire", "A reverse goal", "A back-heel",
  "It still counts, but for the other team.")
T(S, "What shapes make up the panels on the classic black-and-white soccer ball?", "Pentagons and hexagons", "Squares and triangles", "Circles and ovals", "Diamonds and stars",
  "12 black pentagons and 20 white hexagons, 32 panels in all. It was designed for the 1970 World Cup.")
T(S, "Where does the word \"soccer\" come from?", "A short way of saying \"association football\"", "An old word for kicking", "The name of the first team", "A sock-shaped ball used long ago",
  "English students in the 1800s loved shortening words, and \"association\" became \"soccer\".")
T(S, "Which body part are field players NOT allowed to play the ball with?", "Their hands and arms", "Their head", "Their chest", "Their knees",
  "A handball gives the other team a free kick, or a penalty if it happens in the box.")
T(S, "Traditionally, which shirt number does a team's starting goalkeeper wear?", "1", "10", "7", "9",
  "Goalkeepers also wear a different color from everyone else, so the referee can tell who's allowed to use their hands.")
T(S, "Pelé, Maradona and Messi all made which shirt number famous?", "10", "7", "9", "11",
  "The number 10 usually goes to a team's most creative attacking player.")

# ─── Soccer: the World Cup ───────────────────────────────────────────────────
T(S, "Which country has won the most men's World Cups?", "Brazil", "Germany", "Italy", "Argentina",
  "Brazil has won five: 1958, 1962, 1970, 1994 and 2002.")
T(S, "Which country won the 2022 men's World Cup in Qatar?", "Argentina", "France", "Brazil", "Croatia",
  "Argentina and France drew 3-3 in the final, and Argentina won the penalty shootout.")
T(S, "Who scored a hat-trick in the 2022 World Cup final, and still lost?", "Kylian Mbappé", "Lionel Messi", "Harry Kane", "Olivier Giroud",
  "It was only the second hat-trick ever in a men's World Cup final. The first was by England's Geoff Hurst in 1966.")
T(S, "How often is the men's FIFA World Cup played?", "Every 4 years", "Every 2 years", "Every 3 years", "Every year",
  "Qualifying takes almost the whole time in between.")
T(S, "Which country hosted the very first World Cup in 1930?", "Uruguay", "Brazil", "Italy", "England",
  "Uruguay won it too, beating Argentina 4-2 in the final.")
T(S, "Which three countries hosted the 2026 men's World Cup?", "USA, Canada and Mexico", "USA, Brazil and Argentina", "Canada, England and Ireland", "Mexico, Spain and Portugal",
  "It was the first World Cup with 48 teams. Before that, it had 32.")
T(S, "Which player is the only one to win three World Cups?", "Pelé", "Diego Maradona", "Ronaldo", "Lionel Messi",
  "Pelé won in 1958, 1962 and 1970. He was just 17 at the first one.")
T(S, "Which is the only country to play at every single men's World Cup?", "Brazil", "Germany", "Argentina", "Italy",
  "Brazil has never missed one, all the way back to 1930.")
T(S, "Before 2026, in what year did the USA host the men's World Cup?", "1994", "1986", "1998", "2002",
  "Brazil won it, beating Italy in the first World Cup final ever decided on penalties.")
T(S, "Which country won the 2018 World Cup in Russia?", "France", "Croatia", "Belgium", "England",
  "France beat Croatia 4-2 in the final. Kylian Mbappé scored in it at just 19 years old.")
T(S, "Which country won the 2014 World Cup in Brazil?", "Germany", "Argentina", "Brazil", "Netherlands",
  "Mario Götze scored the only goal of the final against Argentina, in extra time.")
T(S, "In the 2014 World Cup semi-final, Germany beat the home team by a famous score. Who and what was it?", "Brazil, 7-1", "Argentina, 5-0", "Spain, 4-3", "France, 6-2",
  "It happened in Brazil, in front of Brazil's own fans. Nobody could believe it.")
T(S, "Which country won the 2010 World Cup, the first one held in Africa?", "Spain", "Netherlands", "Germany", "Brazil",
  "Andrés Iniesta scored the winner against the Netherlands in extra time.")
T(S, "Zinedine Zidane scored two headers in the 1998 World Cup final for which country?", "France", "Italy", "Spain", "Algeria",
  "France beat Brazil 3-0, just outside Paris, to win their first World Cup.")
T(S, "Diego Maradona's famous \"Hand of God\" goal in 1986 was against which country?", "England", "Germany", "Brazil", "Italy",
  "Four minutes later he dribbled past almost the whole England team for what's called the Goal of the Century.")
T(S, "Which African country made it to the World Cup semi-finals in 2022, the first African team ever to do it?", "Morocco", "Senegal", "Ghana", "Cameroon",
  "Morocco beat Spain and Portugal on the way there.")
T(S, "Which Brazilian striker, nicknamed \"The Phenomenon\", scored eight goals at the 2002 World Cup?", "Ronaldo", "Neymar", "Ronaldinho", "Rivaldo",
  "He scored both goals in the final against Germany.")
T(S, "Who was the first player to score at five different men's World Cups?", "Cristiano Ronaldo", "Pelé", "Miroslav Klose", "Diego Maradona",
  "He scored at the 2006, 2010, 2014, 2018 and 2022 World Cups.")
T(S, "What is the \"Golden Boot\"?", "The award for a tournament's top goalscorer", "The trophy for the best goalkeeper", "The boots Pelé wore", "The World Cup trophy",
  "The best goalkeeper at a World Cup gets the Golden Glove.")
T(S, "Brazil got to keep the original World Cup trophy after winning it for the third time. What was it called?", "The Jules Rimet Trophy", "The Lombardi Trophy", "The Golden Ball", "The Stanley Cup",
  "It was named after the man who started the World Cup. Brazil won their third title in 1970.")
T(S, "Mexico City's Estadio Azteca hosted the World Cup final in 1970 and which other year?", "1986", "1994", "2002", "1978",
  "It hosted games at the 2026 World Cup too, making it the first stadium used at three men's World Cups.")

# ─── Soccer: women's game ────────────────────────────────────────────────────
T(S, "How many Women's World Cups have the USA won?", "4", "2", "3", "5",
  "They won in 1991, 1999, 2015 and 2019, more than any other country.")
T(S, "Which country won the 2023 Women's World Cup?", "Spain", "England", "USA", "Sweden",
  "Spain beat England 1-0 in the final in Sydney, Australia.")
T(S, "Who scored the most goals ever for the US women's national team?", "Abby Wambach", "Mia Hamm", "Alex Morgan", "Carli Lloyd",
  "Abby Wambach scored 184 international goals, a lot of them with her head.")
T(S, "Which team won the very first Women's World Cup in 1991?", "USA", "Norway", "Germany", "China",
  "The tournament was held in China.")
T(S, "Brandi Chastain scored the winning penalty in the 1999 Women's World Cup final. Where was it played?", "The Rose Bowl in California", "Wembley in London", "The Maracanã in Rio", "Yankee Stadium in New York",
  "More than 90,000 fans watched the USA beat China.")
T(S, "Mia Hamm starred for which national team?", "USA", "Canada", "Norway", "Brazil",
  "She won two World Cups and two Olympic gold medals.")

# ─── Soccer: players and clubs ───────────────────────────────────────────────
T(S, "In which country was Lionel Messi born?", "Argentina", "Spain", "Brazil", "Uruguay",
  "He moved to Spain when he was 13 to join Barcelona's youth academy.")
T(S, "Which country is Cristiano Ronaldo from?", "Portugal", "Spain", "Brazil", "Italy",
  "He grew up on Madeira, a small island in the Atlantic Ocean.")
T(S, "Which MLS club did Lionel Messi join in 2023?", "Inter Miami", "LA Galaxy", "Seattle Sounders", "Orlando City",
  "David Beckham is one of Inter Miami's owners.")
T(S, "What is the Ballon d'Or?", "An award for the best player in the world that year", "A famous stadium in France", "The World Cup trophy", "A French soccer club",
  "The name is French for \"Golden Ball\".")
T(S, "Which player has won the men's Ballon d'Or the most times?", "Lionel Messi", "Cristiano Ronaldo", "Pelé", "Zinedine Zidane",
  "Messi has won it eight times.")
T(S, "Who is the only goalkeeper ever to win the Ballon d'Or?", "Lev Yashin", "Gianluigi Buffon", "Manuel Neuer", "Iker Casillas",
  "He won it in 1963. People called him \"the Black Spider\" because he always wore black and seemed to have eight arms.")
T(S, "Which famous English player joined the LA Galaxy in 2007?", "David Beckham", "Wayne Rooney", "Harry Kane", "Frank Lampard",
  "It was huge news, and it helped make MLS more famous around the world.")
T(S, "Which club did Pelé play for in the USA?", "New York Cosmos", "LA Galaxy", "Seattle Sounders", "Chicago Fire",
  "He played there from 1975 to 1977 and helped make soccer popular in America.")
T(S, "Which US player is nicknamed \"Captain America\"?", "Christian Pulisic", "Landon Donovan", "Clint Dempsey", "Tim Howard",
  "He won the Champions League with Chelsea in 2021.")
T(S, "Harry Kane is the all-time top goalscorer for which national team?", "England", "Scotland", "Wales", "Ireland",
  "He passed Wayne Rooney's record in 2023.")
T(S, "Which country does Erling Haaland play for?", "Norway", "Sweden", "Denmark", "Germany",
  "His dad, Alf-Inge Haaland, also played in England's Premier League.")
T(S, "Which country does Kylian Mbappé play for?", "France", "Belgium", "Spain", "Cameroon",
  "He won the World Cup with France when he was only 19.")
T(S, "Which country is Mohamed Salah from?", "Egypt", "Morocco", "Senegal", "Algeria",
  "Fans in Egypt treat him like a superhero.")
T(S, "Which country did Cristiano Ronaldo win Euro 2016 with?", "Portugal", "Spain", "France", "Brazil",
  "He got injured early in the final and cheered his team on from the sideline. Portugal beat France 1-0.")
T(S, "Which country played \"Total Football\" in the 1970s, with Johan Cruyff as its star?", "The Netherlands", "Brazil", "Germany", "Spain",
  "The \"Cruyff turn\", a trick to spin away from a defender, is named after him.")
T(S, "What is the top soccer league in England called?", "The Premier League", "La Liga", "Serie A", "The Bundesliga",
  "It started in 1992, and it's watched in more countries than any other league.")
T(S, "La Liga is the top soccer league in which country?", "Spain", "Italy", "France", "Portugal",
  "Real Madrid and Barcelona are its two most famous clubs.")
T(S, "Serie A is the top soccer league in which country?", "Italy", "Spain", "Brazil", "Germany",
  "Juventus, AC Milan and Inter Milan all play in it.")
T(S, "The Bundesliga is the top soccer league in which country?", "Germany", "Austria", "Netherlands", "Switzerland",
  "Bayern Munich is its most successful club.")
T(S, "LA Galaxy, Seattle Sounders and Inter Miami all play in which league?", "MLS", "NWSL", "The Premier League", "La Liga",
  "Major League Soccer played its first season in 1996.")
T(S, "What is the name of the tournament for the best club teams in Europe?", "The Champions League", "The Gold Cup", "The Copa América", "The Premier League",
  "Its famous anthem plays before every game.")
T(S, "Which club has won the European Cup, now called the Champions League, more times than any other?", "Real Madrid", "Barcelona", "Bayern Munich", "Liverpool",
  "Their home stadium is the Santiago Bernabéu in Madrid.")
T(S, "Which club plays its home games at the Camp Nou?", "Barcelona", "Real Madrid", "Atlético Madrid", "Valencia",
  "It's one of the biggest stadiums in the world.")
T(S, "What are the big matches between Real Madrid and Barcelona called?", "El Clásico", "The Derby", "The Old Firm", "The Super Bowl",
  "The Old Firm is the rivalry between Celtic and Rangers in Scotland.")
T(S, "Which English club is nicknamed \"The Red Devils\"?", "Manchester United", "Liverpool", "Arsenal", "Chelsea",
  "They play at Old Trafford in Manchester.")
T(S, "Which London club is nicknamed \"The Gunners\"?", "Arsenal", "Chelsea", "Tottenham", "West Ham",
  "The club was started in 1886 by workers at the Royal Arsenal, a factory that made weapons.")
T(S, "Which club plays at Anfield and sings \"You'll Never Walk Alone\"?", "Liverpool", "Everton", "Manchester City", "Newcastle",
  "The whole stadium sings it together before big games.")
T(S, "Bayern Munich is a club from which country?", "Germany", "Austria", "Italy", "France",
  "Munich is in the south of Germany, near the Alps.")
T(S, "Which club is known as \"Barça\"?", "Barcelona", "Real Madrid", "Benfica", "Boca Juniors",
  "Their motto is \"More than a club.\"")
T(S, "Which tournament do the national teams of North and Central America and the Caribbean play in?", "The Gold Cup", "The Copa América", "The Euros", "The Asian Cup",
  "The USA and Mexico have won it more than anyone else.")
T(S, "Which country won Euro 2024?", "Spain", "England", "France", "Germany",
  "Spain beat England 2-1 in the final in Berlin.")
T(S, "Which country won the Copa América in both 2021 and 2024?", "Argentina", "Brazil", "Uruguay", "Colombia",
  "The 2021 win was Lionel Messi's first big trophy with Argentina.")
T(S, "France's national team is nicknamed \"Les Bleus\". What does it mean?", "The Blues", "The Kings", "The Roosters", "The Stars",
  "Italy's team is \"the Azzurri\", which also means the blues, and Spain's is \"La Roja\", the red one.")
T(S, "What color is Brazil's famous home shirt?", "Yellow", "Green", "Blue", "White",
  "Yellow with green trim. Brazil's team is often just called \"the Seleção\".")
T(S, "In which city is the famous Maracanã stadium?", "Rio de Janeiro", "Buenos Aires", "Madrid", "Mexico City",
  "It hosted the final of the World Cup in both 1950 and 2014.")
T(S, "What is Wembley?", "England's national stadium", "A famous English club", "A soccer trick", "The Premier League trophy",
  "It's in London and has a huge arch over it.")

F = "football"
# ─── American football: the rules ────────────────────────────────────────────
T(F, "How many points is a touchdown worth?", "6", "3", "7", "5",
  "After a touchdown, the team gets a chance to add 1 or 2 more points.")
T(F, "How many points is a field goal worth?", "3", "2", "1", "6",
  "The kick has to go between the uprights and over the crossbar.")
T(F, "How many points is a safety worth?", "2", "1", "3", "6",
  "A safety happens when the defense tackles the ball carrier in their own end zone.")
T(F, "After a touchdown, how many points is a successful kick through the uprights?", "1", "2", "3", "6",
  "It's called the extra point, or the point after touchdown.")
T(F, "Instead of kicking after a touchdown, a team can run or pass it in from close. What's that worth?", "2 points", "1 point", "3 points", "6 points",
  "It's called a two-point conversion. It's harder than kicking, so it's worth more.")
T(F, "How many yards does the offense need to gain to get a new first down?", "10", "5", "15", "20",
  "The two sticks on the sideline, connected by a chain, show exactly how far 10 yards is.")
T(F, "How many downs does the offense get to go 10 yards?", "4", "3", "5", "6",
  "Most teams punt on fourth down if they're far from a first down.")
T(F, "How many players does each team have on the field in the NFL?", "11", "9", "12", "10",
  "The same as soccer! But in football, teams swap in whole groups: one for offense, one for defense.")
T(F, "How long is an NFL field from one goal line to the other?", "100 yards", "80 yards", "120 yards", "90 yards",
  "Add the two 10-yard end zones and it's 120 yards long.")
T(F, "How long is an NFL game, on the game clock?", "60 minutes", "90 minutes", "48 minutes", "40 minutes",
  "Four quarters of 15 minutes. With all the stops, a game usually takes more than three hours.")
T(F, "What is it called when the defense tackles the quarterback behind the line of scrimmage?", "A sack", "A block", "A fumble", "A punt",
  "Sacks became an official NFL stat in 1982.")
T(F, "What is it called when a defender catches a pass meant for the other team?", "An interception", "A fumble", "A touchback", "A safety",
  "If they run it back for a touchdown, people call it a pick-six.")
T(F, "What is it called when a player drops the ball while it's still in play?", "A fumble", "An interception", "A sack", "A punt",
  "Either team can grab a fumble.")
T(F, "What color flag does a referee throw when there's a penalty?", "Yellow", "Red", "White", "Blue",
  "Coaches throw a red flag when they want to challenge a call.")
T(F, "What is the line where the ball is placed before each play called?", "The line of scrimmage", "The goal line", "The sideline", "The fifty",
  "Nobody on either team can cross it until the ball is snapped.")
T(F, "What is a \"Hail Mary\"?", "A long, hopeful pass at the very end of a half", "A kind of field goal", "A trick punt", "A penalty for holding",
  "Cowboys quarterback Roger Staubach made the name famous after a last-second winning pass in 1975.")
T(F, "What is a \"fair catch\"?", "Waving your arm so no one can hit you while you catch a punt", "Catching a pass with both feet in", "A catch the referee reviews", "Catching a fumble in the air",
  "The catch is safe, but the returner can't run with the ball after it.")
T(F, "What happens if an NFL game is tied after four quarters?", "They play overtime", "It ends in a tie right away", "A coin toss decides it", "They kick field goals until someone misses",
  "In the playoffs they keep playing until somebody wins.")
T(F, "Which position throws most of the passes?", "Quarterback", "Running back", "Tight end", "Linebacker",
  "The quarterback is often called the QB.")
T(F, "Which player kicks field goals?", "The kicker", "The quarterback", "The punter", "The center",
  "The punter is a different player. He kicks the ball away on fourth down.")

# ─── American football: history and teams ────────────────────────────────────
T(F, "What does NFL stand for?", "National Football League", "North Football League", "National Field League", "New Football League",
  "The league started in 1920.")
T(F, "What is the NFL's championship game called?", "The Super Bowl", "The World Series", "The Stanley Cup", "The Rose Bowl",
  "It's played in early February, and more people watch it than almost anything else on TV in America.")
T(F, "What is the Super Bowl trophy called?", "The Vince Lombardi Trophy", "The Stanley Cup", "The Heisman Trophy", "The Larry O'Brien Trophy",
  "It's named after the coach whose Green Bay Packers won the first two Super Bowls.")
T(F, "Which team won the very first Super Bowl, in January 1967?", "Green Bay Packers", "Kansas City Chiefs", "Dallas Cowboys", "New York Jets",
  "They beat the Kansas City Chiefs 35-10.")
T(F, "Which player has won the most Super Bowls?", "Tom Brady", "Joe Montana", "Peyton Manning", "Patrick Mahomes",
  "Seven: six with the New England Patriots and one with the Tampa Bay Buccaneers.")
T(F, "Tom Brady was picked 199th in the NFL Draft. Which team picked him?", "New England Patriots", "Tampa Bay Buccaneers", "Michigan Wolverines", "Miami Dolphins",
  "199 picks went by before anyone chose him. He went on to win more Super Bowls than any player ever.")
T(F, "Who has thrown for the most yards and touchdowns in NFL history?", "Tom Brady", "Peyton Manning", "Drew Brees", "Brett Favre",
  "He threw 649 touchdown passes in the regular season.")
T(F, "Who ran for the most yards in NFL history?", "Emmitt Smith", "Walter Payton", "Barry Sanders", "Jim Brown",
  "He ran for 18,355 yards, mostly with the Dallas Cowboys.")
T(F, "Who has the most receiving yards in NFL history?", "Jerry Rice", "Randy Moss", "Larry Fitzgerald", "Terrell Owens",
  "Almost 23,000 yards. Most people think he's the best receiver ever.")
T(F, "Which team finished the NFL's only perfect season, winning every game including the Super Bowl?", "1972 Miami Dolphins", "2007 New England Patriots", "1985 Chicago Bears", "1989 San Francisco 49ers",
  "They went 17-0. The 2007 Patriots won 18 in a row but lost the Super Bowl.")
T(F, "Which quarterback, nicknamed \"Joe Cool\", won four Super Bowls with the 49ers?", "Joe Montana", "Joe Namath", "Joe Burrow", "Joe Flacco",
  "He won all four Super Bowls he played in.")
T(F, "Patrick Mahomes won his first Super Bowl with which team?", "Kansas City Chiefs", "Buffalo Bills", "Dallas Cowboys", "Texas Tech",
  "He also played baseball growing up. His dad was a Major League pitcher.")
T(F, "Which team won the Super Bowl in February 2024?", "Kansas City Chiefs", "San Francisco 49ers", "Philadelphia Eagles", "Baltimore Ravens",
  "They beat the 49ers 25-22 in overtime, only the second Super Bowl ever to go to overtime.")
T(F, "Which team won the Super Bowl in February 2025?", "Philadelphia Eagles", "Kansas City Chiefs", "Buffalo Bills", "Detroit Lions",
  "They beat the Kansas City Chiefs 40-22.")
T(F, "Which team is the only one to play in four Super Bowls in a row?", "Buffalo Bills", "Dallas Cowboys", "New England Patriots", "Pittsburgh Steelers",
  "They got there four straight times in the early 1990s but didn't win any of them.")
T(F, "Peyton Manning won Super Bowls with the Colts and which other team?", "Denver Broncos", "Tennessee Titans", "New York Giants", "Kansas City Chiefs",
  "His younger brother Eli won two Super Bowls with the New York Giants.")
T(F, "Which two NFL teams host a game every Thanksgiving?", "Detroit Lions and Dallas Cowboys", "Chicago Bears and Green Bay Packers", "New York Giants and Jets", "Kansas City Chiefs and Denver Broncos",
  "The Lions have played on Thanksgiving since 1934.")
T(F, "The Green Bay Packers play at which famous stadium?", "Lambeau Field", "Soldier Field", "Arrowhead Stadium", "Lucas Oil Stadium",
  "The Packers are owned by their fans. No other NFL team is.")
T(F, "Fans of which NFL team wear foam \"cheesehead\" hats?", "Green Bay Packers", "Chicago Bears", "Minnesota Vikings", "Buffalo Bills",
  "Wisconsin, where Green Bay is, is famous for making cheese.")
T(F, "Which NFL team has a star on its helmet?", "Dallas Cowboys", "Houston Texans", "Arizona Cardinals", "New York Giants",
  "The Cowboys are often called \"America's Team\".")
T(F, "Which NFL team has a horseshoe on its helmet?", "Indianapolis Colts", "Denver Broncos", "Kansas City Chiefs", "Las Vegas Raiders",
  "A horseshoe is meant to bring good luck.")
T(F, "Walter Payton, one of the great running backs, had what nickname?", "Sweetness", "The Bus", "Prime Time", "Beast Mode",
  "He played for the Chicago Bears. The NFL's award for players who do good work in their community is named after him.")
T(F, "Super Bowls usually have Roman numeral names. Which one used a normal number instead?", "Super Bowl 50", "Super Bowl 10", "Super Bowl 25", "Super Bowl 100",
  "\"Super Bowl L\" would have looked strange, so the NFL wrote \"50\" instead.")
T(F, "How many teams are in the NFL?", "32", "30", "28", "36",
  "They're split into two conferences, the AFC and the NFC, and the winners meet in the Super Bowl.")
T(F, "Is the Super Bowl played in the same stadium every year?", "No, a different city hosts it each year", "Yes, always in Miami", "Yes, always in Los Angeles", "It's played at the home of the better team",
  "Cities are chosen years in advance.")

B = "basketball"
# ─── Basketball ──────────────────────────────────────────────────────────────
T(B, "How many players does each basketball team have on the court?", "5", "6", "7", "4",
  "Five players, but an NBA team can have up to 15 on the roster.")
T(B, "How many points is a shot from behind the three-point line worth?", "3", "2", "4", "1",
  "The NBA added the three-point line in 1979.")
T(B, "How many points is a free throw worth?", "1", "2", "3", "0",
  "The free-throw line is 15 feet from the basket.")
T(B, "How high off the ground is the rim of a basketball hoop?", "10 feet", "8 feet", "12 feet", "9 feet",
  "It's 10 feet in the NBA, in college, and in most school gyms.")
T(B, "Who invented basketball?", "James Naismith", "Michael Jordan", "Abner Doubleday", "Walter Camp",
  "He invented it in 1891 in Springfield, Massachusetts, using peach baskets as the hoops.")
T(B, "What did the very first basketball hoops use for baskets?", "Peach baskets", "Buckets", "Fishing nets", "Hats",
  "Someone had to climb up and get the ball out after every basket.")
T(B, "Who is the NBA's all-time leading scorer?", "LeBron James", "Kareem Abdul-Jabbar", "Michael Jordan", "Kobe Bryant",
  "He passed Kareem Abdul-Jabbar's record in 2023.")
T(B, "Michael Jordan won six NBA championships with which team?", "Chicago Bulls", "Los Angeles Lakers", "Boston Celtics", "Washington Wizards",
  "He won three in a row twice: 1991-93 and 1996-98.")
T(B, "Which two teams have won the most NBA championships?", "Boston Celtics and Los Angeles Lakers", "Chicago Bulls and Golden State Warriors", "New York Knicks and Miami Heat", "San Antonio Spurs and Detroit Pistons",
  "They've had a big rivalry for decades.")
T(B, "Who has made the most three-pointers in NBA history?", "Stephen Curry", "Ray Allen", "Klay Thompson", "James Harden",
  "He changed the way basketball is played. Now everyone shoots threes.")
T(B, "Wilt Chamberlain scored how many points in one NBA game in 1962?", "100", "81", "70", "62",
  "Nobody has matched it. The next best is Kobe Bryant's 81.")
T(B, "Kobe Bryant played all 20 of his NBA seasons with which team?", "Los Angeles Lakers", "Chicago Bulls", "Philadelphia 76ers", "Boston Celtics",
  "He won five championships with the Lakers.")
T(B, "What is it called when a player gets 10 or more in three different stats, like points, rebounds and assists?", "A triple-double", "A hat-trick", "A three-peat", "A grand slam",
  "Get 10 in two stats and it's a double-double.")
T(B, "What is \"traveling\" in basketball?", "Taking too many steps without dribbling", "Throwing the ball out of bounds", "Fouling a shooter", "Holding the ball too long",
  "The other team gets the ball.")
T(B, "How long does an NBA team have to shoot before the shot clock runs out?", "24 seconds", "30 seconds", "35 seconds", "10 seconds",
  "The shot clock was added in 1954 to stop teams from stalling.")
T(B, "How long is each quarter of an NBA game?", "12 minutes", "10 minutes", "15 minutes", "20 minutes",
  "College basketball uses two 20-minute halves instead.")
T(B, "The 1992 US Olympic basketball team, with Jordan, Magic and Bird, had what famous nickname?", "The Dream Team", "The Super Team", "The All-Stars", "The Avengers",
  "They played at the Barcelona Olympics and won every game by a lot.")
T(B, "Which country is Luka Dončić from?", "Slovenia", "Serbia", "Croatia", "Spain",
  "He started playing professionally in Spain when he was only 16.")
T(B, "Giannis Antetokounmpo, the \"Greek Freak\", plays for which national team?", "Greece", "Spain", "Italy", "Turkey",
  "He won the NBA championship with the Milwaukee Bucks in 2021.")
T(B, "Which country is Nikola Jokić from?", "Serbia", "Slovenia", "Greece", "Croatia",
  "He was picked 41st in the NBA Draft, and went on to win the league MVP award.")
T(B, "Victor Wembanyama plays for which national team?", "France", "Belgium", "Canada", "Spain",
  "He's more than 7 feet tall, one of the tallest players in the league.")
T(B, "Caitlin Clark broke the all-time NCAA Division I scoring record playing for which college?", "Iowa", "South Carolina", "UConn", "Stanford",
  "She scored more points than any player, man or woman, in Division I history.")
T(B, "What does WNBA stand for?", "Women's National Basketball Association", "World National Basketball Association", "Western National Basketball Association", "Women's New Basketball Alliance",
  "The WNBA played its first season in 1997.")

Y = "baseball"
# ─── Baseball ────────────────────────────────────────────────────────────────
T(Y, "How many strikes make an out?", "3", "2", "4", "5",
  "A foul ball counts as a strike, but usually can't be strike three.")
T(Y, "How many balls does a batter need to get a walk?", "4", "3", "5", "2",
  "A walk sends the batter to first base.")
T(Y, "How many innings are in a normal Major League game?", "9", "7", "10", "6",
  "If it's tied after nine, they keep playing extra innings.")
T(Y, "How many outs does each team get per inning?", "3", "4", "2", "5",
  "Three outs and the teams switch sides.")
T(Y, "How many players are on the field for the team in the field?", "9", "10", "11", "8",
  "Pitcher, catcher, four infielders and three outfielders.")
T(Y, "How far apart are the bases in Major League Baseball?", "90 feet", "60 feet", "100 feet", "75 feet",
  "The pitcher's mound is 60 feet, 6 inches from home plate.")
T(Y, "What is a home run with the bases loaded called?", "A grand slam", "A hat-trick", "A triple play", "A walk-off",
  "It scores four runs with one swing.")
T(Y, "What is Major League Baseball's championship called?", "The World Series", "The Super Bowl", "The Stanley Cup", "The Big Dance",
  "The first World Series was played in 1903.")
T(Y, "Which team has won the most World Series titles?", "New York Yankees", "Boston Red Sox", "Los Angeles Dodgers", "St. Louis Cardinals",
  "They've won 27, far more than anyone else.")
T(Y, "In 1947, Jackie Robinson broke baseball's color barrier with which team?", "Brooklyn Dodgers", "New York Yankees", "Boston Red Sox", "Chicago Cubs",
  "He was the Rookie of the Year that season.")
T(Y, "Which number is retired by every team in Major League Baseball, in honor of Jackie Robinson?", "42", "24", "7", "3",
  "On April 15 every year, every player in the league wears 42 for Jackie Robinson Day.")
T(Y, "Babe Ruth hit how many home runs in his career?", "714", "500", "762", "660",
  "Hank Aaron passed his record in 1974.")
T(Y, "Shohei Ohtani is famous for being a great hitter and also a great what?", "Pitcher", "Catcher", "Base stealer", "Coach",
  "Hardly anyone in the modern game has been a star at both. He's from Japan.")
T(Y, "Which Major League ballpark is the oldest, opened in 1912?", "Fenway Park", "Wrigley Field", "Yankee Stadium", "Dodger Stadium",
  "Its giant left-field wall is called the Green Monster.")
T(Y, "Which ballpark has ivy growing on its outfield walls?", "Wrigley Field", "Fenway Park", "Busch Stadium", "Oracle Park",
  "It's the home of the Chicago Cubs.")
T(Y, "In 2016, the Chicago Cubs won the World Series for the first time in how many years?", "108", "50", "86", "25",
  "Their last title before that was in 1908.")
T(Y, "Cal Ripken Jr. played how many games in a row without missing one?", "2,632", "1,000", "500", "3,500",
  "It took more than 16 years. People called him the Iron Man.")
T(Y, "What song do fans sing during the seventh-inning stretch?", "Take Me Out to the Ball Game", "The Star-Spangled Banner", "We Will Rock You", "Sweet Caroline",
  "It was written in 1908, by two men who had never been to a baseball game.")
T(Y, "Where is the Little League World Series played every year?", "Williamsport, Pennsylvania", "Cooperstown, New York", "Orlando, Florida", "Los Angeles, California",
  "Teams of kids from all over the world come to play.")
T(Y, "Where is the Baseball Hall of Fame?", "Cooperstown, New York", "Chicago, Illinois", "Boston, Massachusetts", "Williamsport, Pennsylvania",
  "It opened in 1939. Babe Ruth was in the very first group of players honored there.")

M = "more"
# ─── Hockey ──────────────────────────────────────────────────────────────────
T(M, "What trophy does the NHL champion win?", "The Stanley Cup", "The Lombardi Trophy", "The Gold Cup", "The Commissioner's Trophy",
  "Every player on the winning team gets to spend a day with the Cup.", "Hockey")
T(M, "How many players does each hockey team have on the ice, including the goalie?", "6", "5", "7", "11",
  "Teams swap players on the fly, often every minute or so.", "Hockey")
T(M, "What do hockey players hit instead of a ball?", "A puck", "A birdie", "A disc", "A shuttle",
  "Pucks are frozen before games so they don't bounce as much.", "Hockey")
T(M, "Which hockey player is known as \"The Great One\"?", "Wayne Gretzky", "Sidney Crosby", "Alex Ovechkin", "Connor McDavid",
  "He has more points than any player in NHL history.", "Hockey")
T(M, "In 2025, who broke Wayne Gretzky's record for the most NHL goals?", "Alex Ovechkin", "Sidney Crosby", "Connor McDavid", "Auston Matthews",
  "He scored goal number 895 in April 2025, passing Gretzky's 894.", "Hockey")
T(M, "How many periods are there in a hockey game?", "3", "4", "2", "5",
  "Each period is 20 minutes long.", "Hockey")
T(M, "Where does a hockey player go after getting a penalty?", "The penalty box", "The locker room", "The bench", "The press box",
  "Their team has to play one player short until the penalty is over.", "Hockey")
T(M, "What do hockey fans throw onto the ice when a player scores three goals?", "Hats", "Pucks", "Flowers", "Gloves",
  "That's why three goals is called a hat trick!", "Hockey")
T(M, "In the 1980 \"Miracle on Ice\", a team of US college players beat which hockey powerhouse?", "The Soviet Union", "Canada", "Sweden", "Finland",
  "They won 4-3, then beat Finland to win the Olympic gold medal.", "Hockey")
T(M, "The first organized indoor hockey game was played in 1875 in which country?", "Canada", "USA", "Russia", "Sweden",
  "It was played in Montreal.", "Hockey")

# ─── Olympics ────────────────────────────────────────────────────────────────
T(M, "How many rings are on the Olympic flag?", "5", "4", "6", "7",
  "They stand for the five parts of the world that take part in the Olympics.", "Olympics")
T(M, "Which swimmer has won the most Olympic gold medals ever?", "Michael Phelps", "Katie Ledecky", "Mark Spitz", "Caeleb Dressel",
  "He won 23 golds and 28 medals in total.", "Olympics")
T(M, "Usain Bolt, the fastest man ever over 100 meters, is from which country?", "Jamaica", "USA", "Kenya", "Canada",
  "His world record is 9.58 seconds, set in 2009.", "Olympics")
T(M, "What sport is Simone Biles famous for?", "Gymnastics", "Swimming", "Figure skating", "Track",
  "She's won more world and Olympic medals than any other gymnast in history.", "Olympics")
T(M, "Which city hosted the 2024 Summer Olympics?", "Paris", "Tokyo", "Los Angeles", "London",
  "It was the third time Paris hosted the Summer Olympics.", "Olympics")
T(M, "Which US city will host the 2028 Summer Olympics?", "Los Angeles", "New York", "Chicago", "Miami",
  "LA also hosted in 1932 and 1984.", "Olympics")
T(M, "Which country hosted the 2026 Winter Olympics?", "Italy", "Canada", "Japan", "Norway",
  "The games were shared between Milan and Cortina d'Ampezzo.", "Olympics")
T(M, "In which country did the ancient Olympic Games begin?", "Greece", "Italy", "Egypt", "China",
  "They were held at a place called Olympia, almost 2,800 years ago.", "Olympics")
T(M, "Jesse Owens won how many gold medals at the 1936 Olympics in Berlin?", "4", "2", "3", "5",
  "He won the 100 meters, 200 meters, long jump and the 4x100 relay.", "Olympics")
T(M, "Before he was famous as Muhammad Ali, he won an Olympic gold medal in 1960 in which sport?", "Boxing", "Wrestling", "Track", "Judo",
  "Back then his name was Cassius Clay.", "Olympics")
T(M, "Which sport made its Olympic debut at the Tokyo Olympics, held in 2021?", "Skateboarding", "Basketball", "Soccer", "Swimming",
  "Surfing and sport climbing were new that year too.", "Olympics")
T(M, "Katie Ledecky is one of the greatest ever in which sport?", "Swimming", "Tennis", "Gymnastics", "Diving",
  "She's famous for winning long freestyle races by huge margins.", "Olympics")
T(M, "Wilma Rudolph won three gold medals at the 1960 Olympics. What did doctors say when she was little?", "She might never walk normally", "She was too short to run", "She should play basketball", "She'd never learn to swim",
  "She had polio as a child and wore a leg brace. She grew up to be called the fastest woman in the world.", "Olympics")
T(M, "How long is a marathon?", "26.2 miles", "10 miles", "13.1 miles", "50 miles",
  "That's about 42 kilometers.", "Running")

# ─── Tennis, golf and more ───────────────────────────────────────────────────
T(M, "How many Grand Slam singles titles did Serena Williams win?", "23", "15", "18", "30",
  "Her sister Venus won seven.", "Tennis")
T(M, "Which famous tennis tournament is played on grass in London?", "Wimbledon", "The US Open", "The French Open", "The Australian Open",
  "Players have to wear almost all white.", "Tennis")
T(M, "How many Grand Slam tournaments are there in tennis each year?", "4", "3", "5", "6",
  "The Australian Open, the French Open, Wimbledon and the US Open.", "Tennis")
T(M, "Which man has won the most Grand Slam singles titles in tennis?", "Novak Djokovic", "Roger Federer", "Rafael Nadal", "Pete Sampras",
  "He's from Serbia, and he's won every one of the four Grand Slam tournaments more than once.", "Tennis")
T(M, "In tennis, what is a score of zero called?", "Love", "Nil", "Zip", "Duck",
  "Nobody is completely sure where it came from.", "Tennis")
T(M, "In golf, what is one under par on a hole called?", "A birdie", "An eagle", "A bogey", "An albatross",
  "Two under is an eagle. One over is a bogey.", "Golf")
T(M, "How many holes are in a standard round of golf?", "18", "9", "12", "20",
  "Many courses have a 9-hole version for shorter games.", "Golf")
T(M, "In the Tour de France bike race, what does the overall leader wear?", "A yellow jersey", "A green jersey", "A red helmet", "A gold medal",
  "The race is more than 2,000 miles long and lasts three weeks.", "Cycling")
T(M, "What sport uses a shuttlecock?", "Badminton", "Tennis", "Squash", "Volleyball",
  "It's also called a birdie.", "Badminton")
T(M, "What's the highest score you can get in a single game of bowling?", "300", "200", "100", "500",
  "It takes 12 strikes in a row.", "Bowling")
