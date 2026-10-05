"""Lights Out: one wind-down a day, read slowly with a breathing circle.

Each line goes with one slow breath: in while the circle grows, out while it
shrinks. They're sports visualizations, the kind athletes use to calm down
and picture success. They're guided imagination, not facts, so no sources;
and no claims about what they do to your brain.

[title, emoji, [lines]]
"""

SCRIPTS = [
    ["Replay your best play", "🎬", [
        "Get comfortable and let your body go heavy.",
        "Think of the best thing you did today. Big or small.",
        "Now play it back in slow motion, like a highlight.",
        "Notice where you were and what you did.",
        "Hear the cheer. Feel how good it felt.",
        "Keep that feeling and let your eyes get sleepy.",
    ]],
    ["The perfect free kick", "⚽", [
        "Picture the ball sitting still on the grass.",
        "You take a few steps back. The stadium goes quiet.",
        "You breathe in. You feel calm and ready.",
        "You run up and strike it clean.",
        "Watch it curl over the wall and into the corner.",
        "Goal. Let the cheer fade away into quiet.",
    ]],
    ["The perfect spiral", "🏈", [
        "Picture the football in your hand, fingers on the laces.",
        "You drop back. Everything slows down.",
        "You see your receiver break open.",
        "You step and throw. The ball spins in a perfect spiral.",
        "It drops right into their hands. Touchdown.",
        "Let the stadium lights dim, one by one.",
    ]],
    ["Rest after the big game", "🛌", [
        "Lie still, like you're resting after a big game.",
        "Let your feet and legs get heavy. They worked hard today.",
        "Let your belly rise and fall slowly.",
        "Let your shoulders drop and your arms go loose.",
        "Let your face relax, even your eyebrows.",
        "Your whole body is resting now. Good game.",
    ]],
    ["Calm at the penalty spot", "🥅", [
        "Picture yourself walking up to the penalty spot.",
        "Your heart is beating fast. That's okay.",
        "You take one slow breath in, and a long breath out.",
        "You pick your spot and you trust it.",
        "Your body feels calm and steady.",
        "Bring that calm with you into sleep.",
    ]],
    ["The diving catch", "🧤", [
        "Picture a long pass flying through the night sky.",
        "You're running, and everything feels easy.",
        "You stretch out, eyes on the ball.",
        "It lands softly in your hands.",
        "You roll on the grass and hold on tight.",
        "Feel how proud you are, and let your body rest.",
    ]],
    ["Game film", "📼", [
        "Pretend you're watching film of your day.",
        "Fast-forward to something that went well.",
        "Pause there. What did you do right?",
        "Now think of one thing you'll try tomorrow.",
        "Picture yourself doing it well.",
        "Turn off the screen. The film can wait until morning.",
    ]],
    ["Team huddle", "🤝", [
        "Picture your team in a huddle, arms around each other.",
        "Think of someone who helped you today.",
        "Say thank you to them in your head.",
        "Think of someone you helped too.",
        "Feel how good it is to be on a team.",
        "Break the huddle, and let sleep come.",
    ]],
    ["Practice in your mind", "🎯", [
        "Pick one skill you're working on.",
        "Picture yourself doing it slowly, step by step.",
        "Now picture it again, a little faster.",
        "See yourself doing it just right.",
        "Tomorrow, you'll try it for real.",
        "Let your body relax and rest now.",
    ]],
    ["Stadium lights out", "🏟️", [
        "Picture an empty stadium after the game.",
        "The crowd has gone home. It's quiet.",
        "One by one, the big lights switch off.",
        "Now it's just the stars above the field.",
        "The grass is cool and the air is still.",
        "Goodnight, stadium. Goodnight, you.",
    ]],
    ["The breakaway", "💨", [
        "Picture yourself with the ball and open field ahead.",
        "Your legs feel strong and light.",
        "The wind rushes past as you run.",
        "Nobody can catch you. You feel free.",
        "You cross the line and slow to a walk.",
        "Breathe slow. Let your legs rest now.",
    ]],
    ["Next play", "🔁", [
        "Think of something that didn't go your way today.",
        "That's okay. Everybody has plays like that.",
        "Picture yourself shaking it off, like a pro.",
        "Say to yourself: next play.",
        "Tomorrow is a brand new game.",
        "Let it go, and let yourself rest.",
    ]],
    ["Walk-off win", "🎉", [
        "Picture the last seconds of a close game.",
        "Everyone is watching. You feel calm.",
        "You make the winning play.",
        "Your teammates run to you, cheering.",
        "Soak in that feeling for a moment.",
        "Now let the celebration fade into a quiet night.",
    ]],
    ["Warm night on the field", "🌙", [
        "Picture lying on the soft grass of your favorite field.",
        "The sky above is full of stars.",
        "You can hear crickets and a gentle breeze.",
        "Your body sinks into the cool grass.",
        "Each breath out makes you a little sleepier.",
        "Close your eyes and rest.",
    ]],
]

# The breathing circle: seconds in, seconds out, for each line.
BREATH = [4, 6]
