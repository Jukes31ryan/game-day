"""Game Day's quotes: soccer and football greats, plus a few lines every sports
kid hears, each with a kid-level "What does this mean?".

Only lines reliably attributed to the person named. Famous "quotes" that were
really said by someone else, or that have no real source, are out.

Each entry: (quote, who, tags, meaning, question to think about)
tags: soccer, football, more
"""

QUOTES = [('Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, '
  'love of what you are doing.',
  'Pelé',
  ['soccer'],
  "Pelé is saying the best players didn't get lucky. They practiced, kept going when it was hard, and kept "
  'learning. The last part matters most: he says loving the game is what keeps you doing all the rest.',
  "What do you love doing so much that practicing it doesn't feel like work?"),
 ('The more difficult the victory, the greater the happiness in winning.',
  'Pelé',
  ['soccer'],
  'An easy win feels fine. A win you had to fight for, when you were losing or tired, feels amazing. So a '
  "hard game isn't bad news. It's the chance for the best kind of win.",
  "What's something hard you did that felt great when you finished it?"),
 ('Everything is practice.',
  'Pelé',
  ['soccer'],
  'Three words, and a big idea. Every game, every kickabout in the yard, every time you try something new, '
  "you're getting better. Nothing is wasted.",
  'What could you practice today without anyone telling you to?'),
 ('You have to fight to reach your dream. You have to sacrifice and work hard for it.',
  'Lionel Messi',
  ['soccer'],
  'Messi was small as a kid and needed medicine to help him grow. He moved to another country at 13 to chase '
  "soccer. Dreams don't just happen, he says. You work for them, and sometimes you give things up.",
  "What's your dream, and what's one small thing you can do for it this week?"),
 ('Talent without working hard is nothing.',
  'Cristiano Ronaldo',
  ['soccer'],
  'Lots of kids are talented. Ronaldo is famous for training harder than almost anyone, even when he was '
  'already a star. Talent is where you start. Work is what gets you somewhere.',
  'What are you naturally good at that you could get even better at?'),
 ('Playing football is very simple, but playing simple football is the hardest thing there is.',
  'Johan Cruyff',
  ['soccer'],
  "Cruyff was one of the smartest players ever. He means the best players don't show off. They make the easy "
  'pass at the right time. Keeping it simple sounds easy but takes real skill.',
  'When do you try to do too much, when something simple would work better?'),
 ('Every disadvantage has its advantage.',
  'Johan Cruyff',
  ['soccer'],
  "If you're small, you might be quicker. If you're new, you see things others miss. Cruyff says every "
  'weakness hides a strength if you look for it.',
  "What's something you think is a weakness that might secretly help you?"),
 ('I am a member of a team, and I rely on the team, I defer to it and sacrifice for it, because the team, '
  'not the individual, is the ultimate champion.',
  'Mia Hamm',
  ['soccer'],
  'Mia Hamm was one of the best players in the world, and she still said the team matters more than any one '
  'player. "Defer" means you let the team\'s needs come first.',
  "How can you help your team today, even when you're not the one scoring?"),
 ("Always work hard, never give up, and fight until the end because it's never really over until the whistle "
  'blows.',
  'Alex Morgan',
  ['soccer'],
  "Games have been won in the very last minute. If you give up early, you'll never know if you could have "
  "come back. Keep going until the ref says it's over.",
  'When did something turn around right at the end?'),
 ('Make failure your fuel.',
  'Abby Wambach',
  ['soccer'],
  'Fuel is what makes a car go. Wambach is saying that losing, or messing up, can push you to work harder '
  'next time, instead of making you quit.',
  "What's a time you messed up, that made you want to get better?"),
 ('Hard work will always overcome natural talent when natural talent does not work hard.',
  'Sir Alex Ferguson',
  ['soccer'],
  "Ferguson coached Manchester United for 26 years. He saw lots of gifted players who didn't try hard, and "
  'lots of hard workers who beat them. If you work hard, you can beat people who are more talented than you.',
  "What's something you got better at just by sticking with it?"),
 ("I've missed more than 9,000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to "
  "take the game-winning shot and missed. I've failed over and over and over again in my life. And that is "
  'why I succeed.',
  'Michael Jordan',
  ['more'],
  "The greatest basketball player ever missed a lot. He kept taking the shot anyway. You can't make the big "
  "shot if you're too scared of missing it.",
  "What would you try if you weren't worried about missing?"),
 ("You miss 100% of the shots you don't take.",
  'Wayne Gretzky',
  ['more'],
  "If you never shoot, you can never score. It's simple math. Gretzky, the greatest hockey scorer ever, is "
  'saying: take your chances.',
  'What\'s one "shot" you could take today, in class or at practice?'),
 ("It's not whether you get knocked down; it's whether you get up.",
  'Vince Lombardi',
  ['football'],
  "In football everyone gets knocked down, it's part of the game. Lombardi, who the Super Bowl trophy is "
  'named after, says what counts is getting back up.',
  'What knocked you down recently, and how did you get back up?'),
 ("Hard work beats talent when talent doesn't work hard.",
  'Tim Notke',
  ['more'],
  "Tim Notke was a high-school basketball coach. His line got famous because it's true: if you work harder "
  'than someone more talented, you can beat them.',
  'Where can hard work help you beat someone today?'),
 ('The day you think there is no improvements to be made is a sad one for any player.',
  'Lionel Messi',
  ['soccer'],
  'Even Messi, one of the best ever, always looks for ways to get better. The day you think you know it all, '
  'you stop improving.',
  "What's one thing you could still get better at, even if you're already good at it?"),
 ('Practice does not make perfect. Only perfect practice makes perfect.',
  'Vince Lombardi',
  ['football'],
  'Doing a drill the lazy way a hundred times just makes you good at the lazy way. Lombardi, the coach the '
  "Super Bowl trophy is named after, says it's how you practise that counts.",
  "What's one thing you could practise the right way today, even if it's slower?"),
 ('Perfection is not attainable, but if we chase perfection we can catch excellence.',
  'Vince Lombardi',
  ['football'],
  'Nobody plays a perfect game. But trying for perfect gets you somewhere really good, which is called '
  'excellence.',
  'What would "chasing perfect" look like in your next game or practice?'),
 ("Today I will do what others won't, so tomorrow I can accomplish what others can't.",
  'Jerry Rice',
  ['football'],
  'Jerry Rice ran up a steep hill near his home over and over in the summer, when other players were '
  "resting. That's how he became the greatest receiver ever.",
  "What could you do today that other kids won't bother to?"),
 ("Pressure is something you feel when you don't know what you're doing.",
  'Peyton Manning',
  ['football'],
  "Peyton Manning studied so hard that big moments didn't scare him. When you've practised something a lot, "
  'it feels less scary.',
  "What's something you used to be nervous about, that's easy now because you practised?"),
 ("When you're good at something, you'll tell everyone. When you're great at something, they'll tell you.",
  'Walter Payton',
  ['football'],
  "You don't need to brag. If you're really great, other people notice and say it for you.",
  "Who's someone great who doesn't brag about it?"),
 ('Enthusiasm is everything. It must be taut and vibrating like a guitar string.',
  'Pelé',
  ['soccer'],
  '"Taut" means pulled tight. Pelé says you should be excited and ready, like a guitar string that\'s ready '
  'to play a note.',
  'What gets you really excited to play?'),
 ("I've always believed that if you put in the work, the results will come.",
  'David Beckham',
  ['soccer'],
  'Beckham was famous for his free kicks, and he practised them for hours and hours as a kid. The results '
  'came because he put the work in first.',
  "What's something you're putting in the work on right now?"),
 ('We have to change from doubters to believers.',
  'Jürgen Klopp',
  ['soccer'],
  "Klopp said this on his first day as Liverpool's manager. He wanted fans and players to stop worrying "
  'about losing and start believing they could win. They went on to win the Champions League and the Premier '
  'League.',
  "What's something you could start believing you can do?"),
 ('You can overcome anything, if and only if you love something enough.',
  'Lionel Messi',
  ['soccer'],
  'Messi needed treatment to grow and had to move to another country as a kid. He says loving soccer is what '
  'got him through it.',
  "What do you love enough to keep going when it's hard?")]
