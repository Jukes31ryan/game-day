"""Crossword vocabulary for Liam: words a 10-year-old knows, each with a clue.

A generator can fill a grid but it can't write clues, so every word here gets
its clue when it's added. Sports words start with * and the generator favours
them. Clues never contain their own answer (tools/gen_cw.py checks).
"""

RAW = """
*BALL: You kick it, throw it or bounce it
*GOAL: What a striker wants to score
*KICK: What you do to a soccer ball
*TEAM: A group of players on the same side
*SHOT: A try at scoring
*PASS: Kick or throw the ball to a teammate
*SAVE: What a goalkeeper makes when they stop a shot
*RACE: A contest to see who's fastest
*JUMP: Leap off the ground for a header
*GAME: A match you play to win
*PLAY: Have fun in a game
*WINS: Victories
*TIED: Level, with the same score
*CLUB: A soccer team, like Barcelona or Liverpool
*NETS: Goals have them behind the posts
*LINE: A chalk mark on the field
*YARD: 3 feet, or 10 of them gets a first down
*FANS: People cheering in the stands
*HALF: 45 minutes of a soccer game
*BOOT: A soccer shoe, or a big kick
*SHIN: Front of your leg, below the knee
*TURF: Grass, or fake grass, on a field
*FOUL: Breaking a rule in a game
*CARD: A ref shows a yellow or red one
*FLAG: A referee throws a yellow one in football
*PADS: Football players wear these for protection
*GOLD: First-place medal
*PUNT: Kick the football away on fourth down
*SNAP: How the center starts a football play
*RUSH: Run with the football
*SACK: Tackle the quarterback
*ZONE: The end ___, where touchdowns happen
*KNEE: Joint in the middle of your leg
*SPIN: Turn around quickly
*DIVE: A goalkeeper's leap to make a save
*REFS: They blow the whistle, for short
HOME: Where you live
*BEAT: Win against
*LOST: Didn't win
*WING: Player who runs up the side of the field
*CAPS: Games played for your country, in soccer
*KITS: A team's uniforms, in soccer
*DRAW: A tie game, in soccer
*HEAD: Where your helmet or cap goes
*CUPS: Trophies shaped like big bowls
*JOGS: Runs slowly
*COACH: Person who trains the team
*SCORE: How many points or goals each team has
*FIELD: Where soccer and football are played
*PITCH: A soccer field, in England
*MATCH: A game between two teams
*SHOTS: Tries at the goal
*KICKS: Does what a punter does
*CATCH: Grab the ball out of the air
*THROW: What a quarterback does with the ball
*BLITZ: When lots of defenders rush the quarterback
*DOWNS: Four chances to go 10 yards, in football
*GLOVE: A goalkeeper wears one on each hand
*TEAMS: The Chiefs and the Eagles, for example
*CLEAT: A spiky soccer or football shoe
*BENCH: Where substitutes sit
*PUNTS: Kicks on fourth down
*CROWD: All the fans together
*FINAL: The last and biggest game
*TITLE: A championship
*ARENA: A big indoor stadium
*CHEER: Shout for your team
*SPORT: Soccer or football, for example
*RACES: Contests of speed
*SAVES: A goalkeeper's great stops
*STAND: Get up on your feet
*CLOCK: The game ___ counts down
PLATE: You eat dinner off it
*SOCKS: Long ones cover shin guards
*BOOTS: Soccer shoes
*SHOES: Sneakers, for example
*TOWEL: Dry off after the game with one
*WATER: Fill your bottle with it before practice
*SQUAD: The whole team
*RIVAL: A team you really want to beat
*FOULS: Rule breaks
*CARDS: Yellow and red ones
*FLAGS: Linesmen wave them
*POINT: A field goal is worth three of these
*CHAMP: Winner, for short
*PRIZE: Something you win
*FIRST: Gold-medal place
*THIRD: Bronze-medal place
*SPEED: What a fast winger has
*QUICK: Fast
*POWER: Strength
*JUMPS: Leaps
GREEN: Color of grass
*TOTAL: The final ___ of points
*GOALS: More than one score in soccer
*CROSS: A pass from the side into the box
*CHIP: A soft shot lifted over the goalie
*POST: A shot can hit it and bounce out
*AREA: The penalty ___
*TRAP: Stop the ball dead with your foot
*TOUCH: Your first ___ is how you control the ball
*CLUBS: Real Madrid and Barcelona are famous ones
*DERBY: A game between two teams from the same city
*EXTRA: ___ time comes after 90 minutes in a tied knockout game
*BRACE: Two goals by the same player
*HIKE: What the quarterback shouts before the snap
*RAMS: NFL team from Los Angeles with horns on the helmet
*BILLS: Buffalo's NFL team
*JETS: New York NFL team in green
*LIONS: Detroit's NFL team
*COLTS: Indianapolis's NFL team
*HAWKS: Seattle Sea___
*RAVEN: The bird Baltimore's NFL team is named after
*EAGLE: Philadelphia's team is the ___s
*BEARS: Chicago's NFL team
*CHIEF: Kansas City's team is the ___s
*SAINT: New Orleans's team is the ___s
*GIANT: New York's NFL team is the ___s
*STEEL: Pittsburgh's team is the ___ers
*SHOOT: Try to score
*DRILL: A practice exercise
*KICKS: Punts and field goals
*LEAGUE: .
CAKE: A birthday treat with candles
MILK: White drink from a cow
BIRD: It has feathers and wings
FISH: It swims and has fins
FROG: Green animal that hops and croaks
TREE: It has a trunk and leaves
RAIN: Water falling from clouds
SNOW: Cold white flakes
WIND: Moving air
STAR: It twinkles at night
MOON: It lights up the night sky
BOOK: You read it
DESK: A table for schoolwork
SHOE: You wear it on your foot
SOCK: It goes on before your shoe
COAT: Warm jacket
DOOR: You open it to go in
ROOM: A bed___ or a class___
BELL: It rings at school
LAMP: A light on a table
BEAR: Big furry animal that loves honey
LION: King of the jungle
DUCK: It quacks
GOAT: Animal with horns, or the greatest of all time
WOLF: It howls at the moon
DEER: Animal with antlers
SEAL: It barks and swims
CRAB: It walks sideways on the beach
NEST: A bird's home
SEED: A plant grows from it
LEAF: Green part of a tree
ROSE: A red flower with thorns
CORN: Yellow vegetable on a cob
RICE: Tiny white grains you eat
SOUP: Hot food you eat with a spoon
EGGS: Scrambled breakfast food
PIES: Apple and pumpkin desserts
BEES: They make honey
ANTS: Tiny insects at a picnic
BUGS: Insects
WORM: Wiggly animal in the dirt
MAPS: They show you where to go
SHIP: A big boat
BOAT: It floats on water
CARS: They drive on roads
BLUE: Color of the sky
PINK: Light red color
GRAY: Color of a rain cloud
TALL: Very high
FAST: Quick
SLOW: Not fast
WARM: A little bit hot
COLD: Like ice
DARK: Not light
KITE: You fly it on a windy day
TOYS: Things to play with
SONG: Music you sing
DRUM: You bang it to make a beat
BAND: Group of musicians
FARM: Where cows and pigs live
BARN: Farm building for animals
CAVE: A hole in a mountain
HILL: A small mountain
LAKE: Big area of fresh water
POND: Where ducks swim
SAND: What beaches are made of
ROCK: A stone
GIFT: A present
PEAR: Green fruit shaped like a light bulb
PLUM: Small purple fruit
LIME: Green citrus fruit
BEAN: Jelly ___
TACO: Folded tortilla with a filling
NOSE: You smell with it
EARS: You hear with them
EYES: You see with them
HAND: It has five fingers
FOOT: It has five toes
TOES: Wiggly things on your feet
HAIR: It grows on your head
KING: Ruler with a crown
HERO: Someone brave who saves the day
NAME: What people call you
WORD: A group of letters that means something
NOTE: A short message
TIME: What a clock tells you
DAYS: There are seven in a week
YEAR: Twelve months
WEEK: Seven days
NOON: 12 o'clock in the day
HOUR: Sixty minutes
OVEN: Where you bake cookies
SOAP: You wash your hands with it
BATH: Tub full of water
NAPS: Short sleeps
DOGS: Puppies grow into these
CATS: Pets that purr
PETS: Animals that live with you
BONE: A dog loves to chew one
TAIL: A dog wags it
WAVE: Say hi with your hand, or ride one in the sea
FIRE: Hot flames
SALT: Shake it on your fries
LOUD: Very noisy
NICE: Kind and friendly
KIND: Nice to others
CALM: Relaxed and quiet
IDEA: A thought
MATH: Adding and subtracting subject
READ: Look at words in a book
TEST: A quiz at school
QUIZ: A short test
GRIN: A big smile
HUGS: Big squeezes
SING: Make music with your voice
SPOT: A small dot
DOTS: Small round spots
NEAT: Tidy
LIST: Things written one under another
PAGE: One side of paper in a book
PARK: Place with swings and slides
CITY: Big town
TOWN: Small city
ROAD: Cars drive on it
BUSY: Lots to do
EASY: Not hard
HARD: Not easy
OPEN: Not closed
SHUT: Closed
HELP: Give a hand
GLAD: Happy
PLAN: What you'll do
PICK: Choose
MOVE: Go somewhere
STEP: One stair, or one move of your foot
LEAD: Be in front
EARN: Get by working
TRUE: Not false
WISH: Something you hope for
ZERO: Nothing, as a number
FOUR: Two plus two
FIVE: Fingers on one hand
NINE: One less than ten
APPLE: Red or green fruit
BREAD: You make toast from it
CHAIR: You sit on it
TABLE: You eat dinner at it
HOUSE: A home
MOUSE: Small animal that squeaks
HORSE: Animal you can ride
TIGER: Big striped cat
ZEBRA: Striped animal like a horse
SHARK: Ocean hunter with a fin
WHALE: Biggest animal in the ocean
SNAKE: Long animal that slithers
OTTER: Playful animal that floats on its back
CAMEL: Desert animal with humps
PANDA: Black-and-white bear
KOALA: Australian animal that eats leaves
LLAMA: Fluffy animal from South America
PIZZA: Cheesy food cut in slices
TACOS: Crunchy shells with fillings
PASTA: Spaghetti, for example
SALAD: Lettuce dish
CANDY: Sweet treat
JUICE: Orange ___
MANGO: Sweet tropical fruit
LEMON: Sour yellow fruit
GRAPE: Small round fruit in bunches
PEACH: Fuzzy fruit
BERRY: Straw___ or blue___
TOAST: Crispy bread
HONEY: Sweet stuff bees make
CREAM: Ice ___
SUGAR: It makes things sweet
OCEAN: Huge body of salt water
RIVER: Water that flows to the sea
BEACH: Sandy place by the sea
STORM: Wild weather
CLOUD: White fluffy thing in the sky
RAINY: Wet weather
SUNNY: Bright weather
SNOWY: Weather for sledding
PLANT: It grows in soil
GRASS: Green stuff on a lawn
TREES: A forest has lots
SEEDS: Plant them to grow flowers
EARTH: Our planet
WORLD: The whole planet
SPACE: Where astronauts go
ORBIT: Path around a planet
ROBOT: Machine that can move by itself
TRAIN: It runs on tracks
TRUCK: Big vehicle for carrying things
PLANE: It flies in the sky
BOATS: They float
WHEEL: A bike has two
CLASS: A group of students
PAPER: You write on it
BOOKS: Things in a library
STORY: A tale
MUSIC: Songs and tunes
PIANO: Instrument with black and white keys
DRUMS: Instruments you hit with sticks
SONGS: You sing them
DANCE: Move to music
PARTY: A birthday celebration
GAMES: Things you play
BLOCK: A toy building brick
CHESS: Game with kings and queens
HAPPY: Glad
SMILE: A happy face
LAUGH: What you do at a joke
FUNNY: Makes you laugh
BRAVE: Not scared
SMART: Clever
GIANT: Very big
LARGE: Big
SMALL: Little
QUIET: Not loud
NOISE: A loud sound
SOUND: Something you hear
LIGHT: Not dark
NIGHT: When it's dark
EARLY: Before it's late
LATER: Not now
TODAY: This day
MONTH: About four weeks
YEARS: Birthdays count them
WATCH: A clock on your wrist
PHONE: You call people on it
VIDEO: Something you watch on a screen
MOVIE: A film
COMIC: Funny book with pictures
MAGIC: Tricks with a wand
GHOST: Spooky thing that says boo
QUEEN: A king's partner
CROWN: A king wears it
SWORD: A knight's weapon
BEAST: A big wild animal
HANDS: You clap with them
TEETH: You brush them
MOUTH: You talk with it
BRAIN: You think with it
HEART: It pumps blood
BONES: Your skeleton is made of them
SHIRT: You wear it on top
PANTS: You wear them on your legs
SCARF: Wrap it around your neck
BLACK: Darkest color
WHITE: Color of snow
BROWN: Color of chocolate
THREE: One more than two
SEVEN: Days in a week
EIGHT: Legs on a spider
SHAPE: A circle is one
CLEAN: Not dirty
SLEEP: What you do at night
DREAM: A story in your sleep
LEARN: Find out something new
WRITE: Use a pencil
SPELL: Say the letters of a word
PAINT: Color with a brush
SHARE: Give some to others
TRUST: Believe in someone
PROUD: Feeling good about what you did
READY: All set
STEAM: Hot water vapor
FRUIT: Apples and bananas
LUNCH: Midday meal
SNACK: A small bite between meals
PLATE: You eat off it
SPOON: You eat soup with it
TOWER: A tall building
BRICK: A block for building walls
FENCE: It goes around a yard
GRADE: Fourth or fifth, at school
"""

WORDS = {}
SPORT = set()
for line in RAW.strip().splitlines():
    word, clue = line.split(':', 1)
    word, clue = word.strip(), clue.strip()
    sport = word.startswith('*')
    word = word.lstrip('*')
    if clue == '.' or not word.isalpha() or not (3 <= len(word) <= 5):
        continue                      # placeholders and anything off-size
    if word in WORDS:
        continue                      # first clue wins (PLATE is listed twice)
    WORDS[word] = clue
    if sport:
        SPORT.add(word)
