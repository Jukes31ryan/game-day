"""Who Am I? One player or team a day, guessed from three clues.

Each entry:
  s      soccer | football
  clues  three clues, hardest first, easiest last
  c      [the answer, then three wrong choices]   (the app shuffles them)
  f      a fact shown after the guess

The same rules as the trivia: only facts that won't change. Anything about
a player's club is pinned to a year, and no running totals for players who
are still playing.
"""

WHOAMI = []
def W(s, clues, answer, w1, w2, w3, fact):
    WHOAMI.append({"s": s, "clues": clues, "c": [answer, w1, w2, w3], "f": fact})

S, F = "soccer", "football"

# ─── Soccer players ──────────────────────────────────────────────────────────
W(S, ["I was born in Rosario, Argentina, in 1987.",
      "I played for Barcelona for 17 seasons, then joined Inter Miami in 2023.",
      "I captained Argentina to win the 2022 World Cup."],
  "Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé",
  "By 2023 Messi had won the Ballon d'Or, the award for the world's best player, 8 times. Nobody else has won it more than 5.")

W(S, ["I was born on the island of Madeira, in Portugal.",
      "I've played for Manchester United, Real Madrid and Juventus.",
      "When I score, I jump, spin and shout \"Siuuu!\""],
  "Cristiano Ronaldo", "Lionel Messi", "Kylian Mbappé", "Mohamed Salah",
  "He has scored more goals for his country than any other man in history.")

W(S, ["I grew up in Bondy, just outside Paris.",
      "I scored a hat-trick in the 2022 World Cup final, and my team still lost.",
      "I won the World Cup with France in 2018, when I was only 19."],
  "Kylian Mbappé", "Antoine Griezmann", "Erling Haaland", "Vinícius Júnior",
  "In 2018 he became the second teenager to score in a World Cup final. The first was Pelé, in 1958.")

W(S, ["My dad, Alf-Inge, also played in England's Premier League.",
      "Before Manchester City, I scored lots of goals for Borussia Dortmund in Germany.",
      "I'm a giant striker from Norway."],
  "Erling Haaland", "Harry Kane", "Kevin De Bruyne", "Martin Ødegaard",
  "He scored 36 goals in his first Premier League season, 2022-23, a record for one season.")

W(S, ["I grew up in a small village in Egypt.",
      "I played in Italy for Fiorentina and Roma.",
      "I joined Liverpool in 2017, and fans call me the Egyptian King."],
  "Mohamed Salah", "Sadio Mané", "Riyad Mahrez", "Son Heung-min",
  "He scored 32 Premier League goals in his first season at Liverpool, a record at the time.")

W(S, ["I came through the youth team at Tottenham Hotspur.",
      "In 2023 I moved to Bayern Munich in Germany.",
      "I'm the all-time top goal scorer for England's men."],
  "Harry Kane", "Jude Bellingham", "Wayne Rooney", "Bukayo Saka",
  "He passed Wayne Rooney to become England's top scorer in March 2023.")

W(S, ["I was born in Hershey, Pennsylvania, the chocolate town.",
      "I played for Dortmund and Chelsea, then joined AC Milan in 2023.",
      "I'm a USA star, and fans call me Captain America."],
  "Christian Pulisic", "Weston McKennie", "Tyler Adams", "Landon Donovan",
  "In 2021 he became the first American man to play in a Champions League final, and he won it with Chelsea.")

W(S, ["My real name is Edson Arantes do Nascimento.",
      "I played most of my career for Santos, then finished with the New York Cosmos.",
      "I'm the only player to win three World Cups, for Brazil."],
  "Pelé", "Diego Maradona", "Ronaldinho", "Garrincha",
  "He was only 17 when he won his first World Cup, in 1958.")

W(S, ["I wore number 7 for Manchester United.",
      "I joined LA Galaxy in 2007, and later became an owner of Inter Miami.",
      "A movie was named after the way I curved my free kicks."],
  "David Beckham", "Wayne Rooney", "Steven Gerrard", "Frank Lampard",
  "The movie is \"Bend It Like Beckham\", from 2002.")

W(S, ["I won four college championships with North Carolina.",
      "I won the World Cup with the USA in 1991 and 1999.",
      "When I retired in 2004, I had scored more international goals than any player ever, man or woman."],
  "Mia Hamm", "Abby Wambach", "Alex Morgan", "Megan Rapinoe",
  "She scored 158 goals for the USA.")

W(S, ["I started at Santos, the same club as Pelé.",
      "In 2017 I moved from Barcelona to Paris Saint-Germain for a world-record fee.",
      "In 2023 I passed Pelé to become Brazil's all-time top scorer."],
  "Neymar", "Vinícius Júnior", "Ronaldinho", "Kaká",
  "His move to PSG cost about 222 million euros, more than double the record at the time.")

W(S, ["I grew up in a poor neighbourhood near Buenos Aires.",
      "I led Napoli to their first Italian league title, in 1987.",
      "I captained Argentina to win the 1986 World Cup, and scored the \"Hand of God\" goal."],
  "Diego Maradona", "Lionel Messi", "Pelé", "Gabriel Batistuta",
  "Four minutes after the \"Hand of God\", he dribbled past five England players to score a goal later voted the Goal of the Century.")

W(S, ["I started at Birmingham City, and they retired my number 22 when I was 17.",
      "I played for Borussia Dortmund in Germany.",
      "I joined Real Madrid in 2023, and I play in England's midfield."],
  "Jude Bellingham", "Phil Foden", "Bukayo Saka", "Declan Rice",
  "He played his first game for England in 2020, when he was 17.")

W(S, ["I was born in Spain in 2007.",
      "I came through La Masia, Barcelona's famous academy.",
      "At 16, I became the youngest player ever to score at a European Championship."],
  "Lamine Yamal", "Pedri", "Gavi", "Nico Williams",
  "Spain won that tournament, Euro 2024. He turned 17 the day before the final.")

# ─── Football players ────────────────────────────────────────────────────────
W(F, ["My dad was a Major League Baseball pitcher.",
      "I played college football at Texas Tech.",
      "I'm the Kansas City Chiefs quarterback, famous for no-look passes."],
  "Patrick Mahomes", "Josh Allen", "Joe Burrow", "Lamar Jackson",
  "He won three Super Bowls in five seasons: after the 2019, 2022 and 2023 seasons.")

W(F, ["I was the 199th pick in the 2000 NFL Draft.",
      "I played college football at Michigan.",
      "I won six Super Bowls with the Patriots and one with the Buccaneers."],
  "Tom Brady", "Peyton Manning", "Aaron Rodgers", "Drew Brees",
  "When he retired in 2023, his seven Super Bowl wins were more than any NFL team had.")

W(F, ["I played college football at Cincinnati.",
      "My brother Jason was a center for the Philadelphia Eagles.",
      "I'm a tight end who catches passes from Patrick Mahomes."],
  "Travis Kelce", "George Kittle", "Rob Gronkowski", "Tyreek Hill",
  "In February 2023 he and Jason became the first brothers to play against each other in a Super Bowl.")

W(F, ["I played college football at Tennessee.",
      "My dad Archie and my brother Eli were NFL quarterbacks too.",
      "I won Super Bowls with the Indianapolis Colts and the Denver Broncos."],
  "Peyton Manning", "Eli Manning", "Tom Brady", "Drew Brees",
  "He threw 55 touchdown passes in 2013, the most ever in one season.")

W(F, ["I played college football at Mississippi Valley State.",
      "I won three Super Bowls with the San Francisco 49ers.",
      "Lots of people call me the greatest wide receiver ever."],
  "Jerry Rice", "Randy Moss", "Larry Fitzgerald", "Calvin Johnson",
  "He holds the NFL records for most career catches, receiving yards and receiving touchdowns.")

W(F, ["I won the Heisman Trophy at Louisville in 2016.",
      "I was the last pick of the first round in the 2018 draft.",
      "I'm the Baltimore Ravens quarterback, and one of the fastest runners ever at my position."],
  "Lamar Jackson", "Jalen Hurts", "Josh Allen", "Kyler Murray",
  "In 2019 he became only the second player ever voted MVP by every single voter.")

W(F, ["I played college football at Wyoming.",
      "I'm 6 feet 5 inches tall and famous for hurdling over defenders.",
      "I'm the quarterback of the Buffalo Bills."],
  "Josh Allen", "Patrick Mahomes", "Joe Burrow", "Justin Herbert",
  "He was voted the NFL's Most Valuable Player for the 2024 season.")

W(F, ["I won a college national championship at LSU in 2019.",
      "My touchdown dance, the Griddy, got copied all over the world.",
      "I'm a wide receiver for the Minnesota Vikings."],
  "Justin Jefferson", "Ja'Marr Chase", "CeeDee Lamb", "Tyreek Hill",
  "In 2022 he led the NFL with 1,809 receiving yards and was named Offensive Player of the Year.")

W(F, ["I played college football at Penn State.",
      "I started my NFL career with the New York Giants.",
      "In 2024 I ran for over 2,000 yards for the Philadelphia Eagles."],
  "Saquon Barkley", "Derrick Henry", "Christian McCaffrey", "Jalen Hurts",
  "The Eagles won the Super Bowl at the end of that 2024 season.")

# ─── Teams ───────────────────────────────────────────────────────────────────
W(F, ["We won the first two Super Bowls ever played.",
      "Our fans wear foam cheese on their heads.",
      "We play at Lambeau Field in Green Bay, Wisconsin."],
  "Green Bay Packers", "Chicago Bears", "Minnesota Vikings", "Detroit Lions",
  "The Packers are the only NFL team owned by their fans, not by one rich owner.")

W(F, ["We play in Arlington, Texas, under a giant video board.",
      "We have a blue star on our helmets.",
      "People call us \"America's Team\"."],
  "Dallas Cowboys", "Houston Texans", "Philadelphia Eagles", "New York Giants",
  "The nickname \"America's Team\" came from a team highlight film in 1979.")

W(F, ["Our logo comes from a symbol used by the steel industry.",
      "Our fans wave the Terrible Towel.",
      "We play in Pittsburgh, in black and gold."],
  "Pittsburgh Steelers", "Baltimore Ravens", "Cleveland Browns", "Cincinnati Bengals",
  "The Steelers are the only NFL team with their logo on just one side of the helmet.")

W(F, ["We started out in Dallas, as the Dallas Texans.",
      "Our stadium, Arrowhead, is one of the loudest in the world.",
      "Patrick Mahomes is our quarterback."],
  "Kansas City Chiefs", "Las Vegas Raiders", "Denver Broncos", "Los Angeles Chargers",
  "In 2014 Chiefs fans set a world record for the loudest crowd roar at an outdoor stadium.")

W(F, ["Our fans call themselves the 12th Man.",
      "In 2011 our crowd cheered so hard for a touchdown run that it showed up on an earthquake sensor.",
      "We play in Seattle, in blue and bright green."],
  "Seattle Seahawks", "San Francisco 49ers", "Los Angeles Rams", "Arizona Cardinals",
  "That run, by Marshawn Lynch, is called the \"Beast Quake\".")

W(F, ["We play in Foxborough, Massachusetts.",
      "Bill Belichick coached us for 24 seasons.",
      "Tom Brady won six Super Bowls with us."],
  "New England Patriots", "New York Jets", "New York Giants", "Buffalo Bills",
  "With Belichick as coach, the Patriots played in nine Super Bowls.")

W(F, ["Our fans call themselves Bills Mafia.",
      "Our stadium gets some of the most snow in the NFL.",
      "Josh Allen is our quarterback."],
  "Buffalo Bills", "Miami Dolphins", "New York Jets", "Green Bay Packers",
  "In the early 1990s they played in four Super Bowls in a row, the only team ever to do it.")

W(F, ["Our stadium has a pirate ship in it that fires cannons when we score.",
      "We were the first team to win a Super Bowl in our own stadium, in 2021.",
      "Tom Brady won his seventh Super Bowl with us."],
  "Tampa Bay Buccaneers", "Miami Dolphins", "Jacksonville Jaguars", "Carolina Panthers",
  "That Super Bowl win was Tom Brady's first season in Tampa.")

W(S, ["We started playing in MLS in 2020.",
      "David Beckham is one of our owners.",
      "Lionel Messi joined us in 2023."],
  "Inter Miami", "LA Galaxy", "Orlando City", "Atlanta United",
  "Weeks after Messi arrived in 2023, they won the Leagues Cup, the club's first trophy.")

W(S, ["Our motto is \"More than a club\".",
      "Our stadium is the Camp Nou.",
      "We play in red and blue stripes, and Messi spent 17 seasons with us."],
  "Barcelona", "Real Madrid", "Atlético Madrid", "Sevilla",
  "Their academy, La Masia, produced Messi, Xavi, Iniesta and Lamine Yamal.")

W(S, ["Our stadium is the Santiago Bernabéu.",
      "We play in all white and are nicknamed Los Blancos.",
      "We've won the Champions League more times than any other club."],
  "Real Madrid", "Barcelona", "Bayern Munich", "Juventus",
  "They won the first five European Cups in a row, from 1956 to 1960.")

W(S, ["Our stadium is Anfield.",
      "Our anthem is \"You'll Never Walk Alone\".",
      "We play in red, in the English city where the Beatles came from."],
  "Liverpool", "Everton", "Manchester United", "Chelsea",
  "Fans have sung \"You'll Never Walk Alone\" before home games since the 1960s.")

W(S, ["Sir Alex Ferguson managed us for 26 years.",
      "Our stadium, Old Trafford, is nicknamed the Theatre of Dreams.",
      "We're the Red Devils."],
  "Manchester United", "Manchester City", "Liverpool", "Arsenal",
  "Under Ferguson they won 13 Premier League titles.")

W(S, ["We're nicknamed the Gunners.",
      "We play at the Emirates Stadium in north London.",
      "In 2003-04 we went a whole Premier League season without losing."],
  "Arsenal", "Chelsea", "Tottenham Hotspur", "West Ham United",
  "That team is called the Invincibles: 26 wins, 12 draws, no losses.")

W(S, ["We have played in every men's World Cup ever held.",
      "We wear yellow shirts and blue shorts.",
      "Pelé won three World Cups with us."],
  "Brazil", "Argentina", "Portugal", "Colombia",
  "Pelé, Ronaldo, Ronaldinho and Neymar all played for Brazil.")

W(S, ["We wear light blue and white stripes.",
      "Diego Maradona led us to the 1986 World Cup.",
      "Messi captained us to the 2022 World Cup."],
  "Argentina", "Uruguay", "Brazil", "Spain",
  "The 2022 final against France ended 3-3, and Argentina won on penalties. Many call it the best final ever.")
