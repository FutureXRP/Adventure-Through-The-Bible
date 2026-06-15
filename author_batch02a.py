#!/usr/bin/env python3
"""Authoring source for Batch 2a (Exodus, part 1). Writes batch-02a.json."""
import json

batch = [
{
  "id": "plagues", "era": "exodus", "emoji": "🐸",
  "title": "The Ten Plagues", "date": "c. 1446 BC", "location": "Egypt",
  "connections": [
    {"title": "The Burning Bush", "storyId": "burning-bush", "reference": "Exodus 7:1",
     "why": "At the bush God promised to rescue his people, and now he sends Moses back to Pharaoh to make good on that promise."},
    {"title": "The First Passover", "storyId": "passover", "reference": "Exodus 11:1",
     "why": "Nine plagues could not move Pharaoh's heart. The tenth and final one is coming, and it changes everything."},
    {"title": "Through the Sea on Dry Ground", "storyId": "red-sea", "reference": "Exodus 14:4",
     "why": "Even after the plagues, Pharaoh chases the people to the sea, where God wins the very last word."}
  ],
  "tier1": {
    "book": "Exodus 7–11",
    "hook": "Ten times God told Pharaoh to let his people go. Ten times Pharaoh said no. And ten times Egypt learned that the God of Israel is stronger than any king on earth.",
    "story": [
      "God's people had been slaves in Egypt for four hundred years. So God sent Moses and his brother Aaron to stand before Pharaoh, the most powerful king in the world, with one message: \"This is what the Lord says. Let my people go.\" Pharaoh only sneered. \"Who is this Lord, that I should obey him? I do not know the Lord, and I will not let Israel go.\" And he made the slaves work even harder.",
      "So God said, \"Now Egypt will learn that I am the Lord.\" Aaron threw down his staff, and it became a snake. Pharaoh's magicians did the same with tricks of their own, but Aaron's snake swallowed every one of theirs. Still Pharaoh's heart stayed hard, and he would not listen.",
      "Then the plagues began. Moses stretched out his hand over the Nile, and the great river turned to blood. The fish died, and the water stank. Then frogs came swarming up out of the river, into the houses, the beds, the ovens, everywhere. Pharaoh begged Moses to take them away, but the moment they were gone, he changed his mind.",
      "So the troubles kept coming. Tiny gnats rose from the dust. Thick swarms of flies filled the air. Even Pharaoh's own magicians said, \"This is the finger of God.\" But here was the wonder: where God's people lived, in the land of Goshen, there were no flies at all. God was setting his people apart and keeping them safe.",
      "The animals of Egypt grew sick and died, but not one animal of Israel's was harmed. Painful sores broke out on the Egyptians. Then came hail like Egypt had never seen, mixed with fire, beating down everything in the fields. And still Pharaoh would not bend.",
      "Locusts came next, a living cloud of them, and they ate every green thing the hail had left. Pharaoh's own officials begged him, \"How long will you let this go on? Egypt is ruined. Let the people go!\" But Pharaoh refused.",
      "Then darkness fell over Egypt, a darkness so thick you could almost feel it, and for three days no one could see anyone else or even get up from where they sat. But in the homes of God's people, there was light. Pharaoh roared at Moses, \"Get out of my sight! If I ever see your face again, you will die.\" \"As you say,\" Moses answered. \"I will never see your face again.\"",
      "Every plague had toppled one of the things Egypt worshiped, the river, the land, the sun in the sky. One by one God showed that he alone is God. And he was about to do one last thing, the most terrible and the most wonderful of all, to finally set his people free."
    ],
    "devotional": {
      "bigIdea": "Pharaoh thought he was the most powerful person alive. But plague after plague, God showed that he alone is God, and that he had not forgotten the people who cried out to him. No king and no power on earth is stronger than God's love for the people he calls his own.",
      "questions": [
        "Again and again Pharaoh promised to obey and then changed his mind. Why do you think it is so hard to keep a promise once the trouble is over?",
        "While Egypt suffered, God kept his people safe in Goshen. When has God taken care of you in the middle of something hard?",
        "The Egyptians worshiped the river and the sun, and God showed he was stronger than all of them. What are some things people today treat as more important than God?"
      ]
    },
    "tags": ["God's power", "rescue", "Moses", "freedom", "Egypt"],
    "quiz": [
      {"question": "What message did God keep sending to Pharaoh?", "options": ["Let my people go", "Build me a temple", "Send me your gold"], "answer": 0, "explanation": ""},
      {"question": "What did the Nile River turn into?", "options": ["Sand", "Blood", "Ice"], "answer": 1, "explanation": ""},
      {"question": "What happened to God's people in Goshen during the plagues?", "options": ["They suffered the most", "They were kept safe", "They ran away to the desert"], "answer": 1, "explanation": "God set his people apart and protected them while Egypt was struck."},
      {"question": "How did Pharaoh keep responding after each plague?", "options": ["He obeyed right away", "He kept his heart hard and refused", "He asked Moses to be king"], "answer": 1, "explanation": ""},
      {"question": "What was God showing through all the plagues?", "options": ["That he alone is God, stronger than any king", "That Egypt was a nice place", "That Moses was magic"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Exodus 7-11",
    "hook": "God told Pharaoh to let his people go free. But Pharaoh kept saying no, so God showed him who was really in charge.",
    "story": [
      "God's people, the Israelites, had been slaves in Egypt for a very, very long time. They worked hard all day long, and they cried out to God to save them.",
      "So God sent Moses to the king of Egypt, who was called Pharaoh. Moses stood before him and said, \"God says, let my people go!\"",
      "But Pharaoh did not want to lose all his workers. He folded his arms and said, \"No! I will not let them go.\"",
      "So God sent troubles on Egypt called plagues. First, Moses held his hand over the river, and all the water turned to blood.",
      "Then frogs came hopping up out of the river, thousands and thousands of them, into the houses and the beds and even the ovens! After that came tiny biting bugs and clouds of buzzing flies.",
      "The farm animals got sick. The people got itchy, sore skin. Then big chunks of hail came crashing down from the sky, and hungry locusts ate up every green plant that was left.",
      "Last of all, darkness covered Egypt for three whole days, so dark that no one could even see their own hand. But where God's people lived, it stayed bright and sunny.",
      "Every single time, Moses said, \"Let God's people go.\" And every single time, Pharaoh was stubborn and said no. But God kept his own people safe through every plague.",
      "God was showing Pharaoh that he is stronger than any king in the whole world. And one more plague was coming, the one that would finally set the people free."
    ],
    "devotional": {
      "bigIdea": "Pharaoh thought he was the strongest. But God showed that he alone is God, and that he never forgets his people. Nothing is stronger than God.",
      "questions": [
        "Pharaoh kept saying no to God. Why do you think he was so stubborn?",
        "God kept his people safe through all the plagues. How does it feel to know God keeps you safe?",
        "What was the most surprising plague to you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God's power", "rescue", "freedom"],
    "quiz": [
      {"question": "What did Moses keep telling Pharaoh?", "options": ["Let God's people go", "Give me a crown", "Build a boat"], "answer": 0, "explanation": ""},
      {"question": "What did the river turn into?", "options": ["Blood", "Milk", "Sand"], "answer": 0, "explanation": ""},
      {"question": "Did God keep his own people safe during the plagues?", "options": ["Yes, he protected them", "No, he forgot them", "Only sometimes"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "passover", "era": "exodus", "emoji": "🐑",
  "title": "The First Passover", "date": "c. 1446 BC", "location": "Egypt",
  "connections": [
    {"title": "The Ten Plagues", "storyId": "plagues", "reference": "Exodus 12:29",
     "why": "Nine plagues failed to move Pharaoh. The tenth, on the night of the Passover, finally sets the people free."},
    {"title": "The Darkest Friday", "storyId": "crucifixion", "reference": "1 Corinthians 5:7",
     "why": "A spotless lamb died so death would pass over God's people, pointing ahead to Jesus, the Lamb of God who died to rescue us."},
    {"title": "The Night Before", "storyId": "last-supper", "reference": "Luke 22:15",
     "why": "Centuries later Jesus shared a Passover meal with his friends the night before he died, and gave it a brand new meaning."}
  ],
  "tier1": {
    "book": "Exodus 12",
    "hook": "One last plague would finally break Pharaoh's heart. And the only thing that could keep death away from a house that night was the blood of a lamb painted on the door.",
    "story": [
      "God told Moses there would be one final plague, the most dreadful of all. At midnight, the oldest son in every home in Egypt would die. After this, Pharaoh would not just let the people go, he would beg them to leave. But God had a way to keep his own people safe, and he gave them careful instructions.",
      "Every family was to choose a perfect young lamb, one with nothing wrong with it. They would gather as families, and that evening they would prepare the lamb. Then they were to take some of its blood and paint it on the sides and top of the door of their house.",
      "They were to roast the lamb and eat it together with bread made without yeast, because there would be no time to let bread rise. They were to eat it dressed and ready to travel, with their sandals on and their walking sticks in hand, ready to leave the moment the call came.",
      "\"When I pass through Egypt tonight,\" God said, \"and I see the blood on your door, I will pass over your house. The plague will not touch you.\" The blood on the doorway was a sign: inside this house are people who belong to God and trust him. They were safe, not because they were better than the Egyptians, but because of the blood of the lamb.",
      "At midnight the Lord passed through the land. In every home without blood on the door, the oldest son died, from the palace of Pharaoh to the poorest house in Egypt. A terrible cry rose across the whole country, for there was not a single home untouched. But in every home marked with blood, all were safe.",
      "That very night Pharaoh sent for Moses. \"Go!\" he cried. \"Take your people, take your flocks, take everything, and leave!\" The Egyptians pressed silver and gold and clothing into their hands and begged them to hurry. And so, after four hundred long years, God's people walked out of Egypt as free people.",
      "God told them to remember this night every single year, with a special meal, and to call it the Passover, because death had passed over them. Parents would tell their children the story again and again, so no one would ever forget how God had set them free.",
      "And there was more to it than they knew. Many years later, a man named John would look at Jesus and say, \"Look, the Lamb of God.\" Jesus would become the perfect Lamb, and his blood would rescue people from death forever. The very first Passover was pointing to him all along."
    ],
    "devotional": {
      "bigIdea": "God's people were not saved that night because they were better than anyone else. They were saved because of the blood of the lamb on their door. That first Passover was a picture of Jesus, the true Lamb of God, whose death rescues everyone who trusts in him.",
      "questions": [
        "The people had to trust God and put the blood on their doors before anything happened. When is it hard to trust God before you can see how things will turn out?",
        "God told the people to remember this night every year so they would never forget. What helps your family remember the good things God has done?",
        "Why do you think God wanted a perfect lamb, with nothing wrong with it, for the very first Passover?"
      ]
    },
    "tags": ["rescue", "the Lamb", "freedom", "trust", "Jesus"],
    "quiz": [
      {"question": "What were the families told to paint on their doors?", "options": ["The blood of a lamb", "Bright gold paint", "Their family name"], "answer": 0, "explanation": ""},
      {"question": "Why did they make bread without yeast?", "options": ["They had no flour", "There was no time to let it rise", "Yeast was against the rules"], "answer": 1, "explanation": "They had to be ready to leave Egypt in a hurry."},
      {"question": "What did God promise when he saw the blood on a door?", "options": ["He would pass over that house", "He would knock loudly", "He would send rain"], "answer": 0, "explanation": ""},
      {"question": "What did Pharaoh finally do that night?", "options": ["He told the people to leave", "He hid in his palace", "He chased them away with soldiers"], "answer": 0, "explanation": ""},
      {"question": "Who does the Passover lamb point ahead to?", "options": ["Jesus, the Lamb of God", "Moses", "Pharaoh"], "answer": 0, "explanation": "John called Jesus the Lamb of God, who rescues us the way the first lamb rescued Israel."}
    ]
  },
  "tier2": {
    "book": "Exodus 12",
    "hook": "On the night God set his people free, every family painted lamb's blood on their door, and the blood kept everyone inside safe.",
    "story": [
      "God said one last plague would finally set his people free. But first, he gave them a special way to stay safe that night.",
      "Each family was to pick a perfect little lamb. That evening they would gather together, and they would paint some of the lamb's blood on the sides and the top of their door.",
      "Then they cooked the lamb and ate it with flat bread. They put on their coats and their shoes and held their walking sticks, all ready to leave the very moment God said go.",
      "God told them, \"When I come through Egypt tonight and I see the blood on your door, I will pass right over your house. No harm will come to anyone inside.\"",
      "So the families waited inside, trusting God. And in the middle of the night, God passed through all of Egypt.",
      "Every single house that had blood on the door was safe, and everyone inside was protected. The blood showed that the people inside belonged to God.",
      "That very night, Pharaoh called for Moses and cried, \"Go! Take your families, take your animals, take everything, and leave!\" God's people were finally free.",
      "God told them to remember this special night every single year, with a special meal. They called it the Passover, because God had passed over them.",
      "And long, long after, a man named John would point to Jesus and say, \"Look, the Lamb of God!\" Jesus is the Lamb who keeps us safe forever."
    ],
    "devotional": {
      "bigIdea": "God's people were kept safe by the blood of the lamb on their door. That first Passover was a picture of Jesus, the Lamb of God, who keeps us safe.",
      "questions": [
        "The families had to trust God and paint the blood before anything happened. When is it hard for you to trust?",
        "God told them to remember this night every year. What is a special thing your family likes to remember?",
        "How do you think the families felt when morning came and they were safe?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["rescue", "the Lamb", "freedom"],
    "quiz": [
      {"question": "What did the families paint on their doors?", "options": ["A lamb's blood", "Gold stars", "Their names"], "answer": 0, "explanation": ""},
      {"question": "What did God promise when he saw the blood?", "options": ["He would pass over the house", "He would send snow", "He would knock"], "answer": 0, "explanation": ""},
      {"question": "What special meal did God tell them to remember each year?", "options": ["The Passover", "Breakfast", "A birthday"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "manna", "era": "exodus", "emoji": "🍞",
  "title": "Bread from Heaven", "date": "c. 1446 BC", "location": "The Wilderness",
  "connections": [
    {"title": "Through the Sea on Dry Ground", "storyId": "red-sea", "reference": "Exodus 16:3",
     "why": "Soon after God split the sea to save them, the people forgot, and grumbled that they would rather be back in Egypt."},
    {"title": "Water From the Rock", "storyId": "moses-water", "reference": "Exodus 17:6",
     "why": "Just as God sent bread when they were hungry, he sent water from a rock when they were thirsty, day after day."},
    {"title": "Five Loaves and Two Fish", "storyId": "feeding-5000", "reference": "John 6:35",
     "why": "God fed a whole nation with bread from heaven, pointing ahead to Jesus, who said, I am the bread of life."}
  ],
  "tier1": {
    "book": "Exodus 16",
    "hook": "Out in the desert with no food and no way to make any, the people were sure they would starve. So God did something no one had ever seen: he made breakfast fall from the sky.",
    "story": [
      "A month after walking out of Egypt, the people of Israel were deep in the desert, and their food was running out. Hungry and afraid, they grumbled against Moses and Aaron. \"We wish we had died back in Egypt! At least there we sat by pots of meat and ate all the bread we wanted. You brought us out here just to starve us all to death.\"",
      "God heard them, and he was kind. \"I will rain down bread from heaven for you,\" he told Moses. \"Each day the people are to go out and gather just enough for that day. In this way I will test whether they will trust me and follow my instructions.\"",
      "That evening, a great flock of quail covered the camp, so the people had meat to eat. And in the morning, there was dew all around. When the dew lifted, thin white flakes lay on the ground like frost. The people stared at it and asked each other, \"What is it?\" That became its name: manna, which means, what is it?",
      "Moses told them, \"This is the bread the Lord has given you to eat.\" It was white like a seed, and it tasted sweet, like wafers made with honey. Each family gathered what they needed, and here was the wonder: the one who gathered a lot did not have too much, and the one who gathered a little did not have too little. Everyone had just enough.",
      "Moses warned them not to keep any of it until morning. But some did not listen. They kept extra, and by morning it was full of worms and smelled awful. The manna would not be stored up. It came fresh each day, so each day the people had to trust God again.",
      "There was one exception. On the sixth day, they were to gather twice as much, because the seventh day was the Sabbath, a day of rest, and no manna would fall. That day, the extra they had saved stayed perfectly good. Yet some still went out on the Sabbath to look for it and found nothing at all.",
      "And God did not feed them this way for just a week or a month. Every single morning, for forty years, until they finally reached the land God had promised, the manna was there waiting on the ground.",
      "God could have given them a year's worth of food all at once. Instead he gave them one day at a time, so that every single morning they would remember they needed him, and every single morning they would find that he was faithful. Long after, Jesus would teach his friends to pray, give us this day our daily bread, and would call himself the true bread that came down from heaven."
    ],
    "devotional": {
      "bigIdea": "God did not hand his people a huge pile of food to last for years. He gave them just enough for one day, every day, so they would learn to trust him each morning. God still loves to give us what we need, one day at a time, and he is always faithful.",
      "questions": [
        "The people had just seen God split the sea, and yet they were grumbling again within a month. Why do you think we forget what God has done so quickly?",
        "God gave the people only enough for one day at a time. Why might that be better for them than getting everything at once?",
        "Jesus told us to pray, give us this day our daily bread. What do you need to trust God for today?"
      ]
    },
    "tags": ["God provides", "trust", "the wilderness", "grumbling", "daily bread"],
    "quiz": [
      {"question": "Why were the people grumbling against Moses?", "options": ["They were hungry and afraid", "They were tired of walking", "They wanted a king"], "answer": 0, "explanation": ""},
      {"question": "What did the word manna mean?", "options": ["Sweet bread", "What is it?", "Gift from the sky"], "answer": 1, "explanation": "The people asked, what is it?, when they first saw the white flakes."},
      {"question": "How much manna were they supposed to gather each day?", "options": ["Just enough for that day", "As much as they could carry", "A week's worth at a time"], "answer": 0, "explanation": ""},
      {"question": "What happened to the manna people tried to keep overnight?", "options": ["It turned to gold", "It filled with worms and went bad", "It doubled in size"], "answer": 1, "explanation": ""},
      {"question": "How long did God feed his people with manna?", "options": ["For one week", "For forty years, until the promised land", "For one winter"], "answer": 1, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Exodus 16",
    "hook": "There was no food in the desert, and the people were hungry and scared. So every single morning, God sent bread down from heaven.",
    "story": [
      "Out in the hot desert, the people of Israel ran out of food. They were hungry and afraid, and they began to grumble. \"We wish we were back in Egypt,\" they said, \"where we had plenty to eat!\"",
      "But God was very kind to them. He told Moses, \"I will send bread down from heaven for you, every single day.\"",
      "That evening, a big flock of birds called quail came to the camp, so the people had meat to eat for dinner.",
      "And the next morning, when the dew dried up, there were little white flakes all over the ground, like frost. The people had never seen anything like it.",
      "They asked each other, \"What is it?\" So they gave it that name: manna, which means, what is it? It was white like seeds and tasted sweet, like honey.",
      "God told them to gather just enough for that one day. But some people did not listen and kept extra overnight, and in the morning it was full of worms and smelled terrible.",
      "On the sixth day, God told them to gather twice as much, because the seventh day was a special day to rest, and no manna would fall. That day, the extra they saved stayed fresh and good.",
      "God did not send manna for just a few days. He sent it every single morning for forty years, until his people reached the land he had promised them.",
      "God gave his people exactly what they needed, one day at a time. He always took care of them, and he always will."
    ],
    "devotional": {
      "bigIdea": "God gave his people just enough food for each day, so they would trust him every morning. God still gives us what we need, one day at a time.",
      "questions": [
        "The people forgot how big God was and started to grumble. What helps you remember the good things God does?",
        "God gave them food one day at a time. What is something you can trust God for today?",
        "How would you feel if you woke up and found breakfast on the ground from God?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God provides", "trust", "the wilderness"],
    "quiz": [
      {"question": "What did God send down every morning?", "options": ["Bread called manna", "Rain", "Snow"], "answer": 0, "explanation": ""},
      {"question": "How much were the people supposed to gather each day?", "options": ["Just enough for that day", "As much as possible", "None at all"], "answer": 0, "explanation": ""},
      {"question": "How long did God feed them with manna?", "options": ["Forty years", "One day", "One week"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "golden-calf", "era": "exodus", "emoji": "🐂",
  "title": "The Golden Calf", "date": "c. 1446 BC", "location": "Mount Sinai",
  "connections": [
    {"title": "The Ten Commandments", "storyId": "ten-commandments", "reference": "Exodus 32:19",
     "why": "The people break the very first command, to worship God alone, before Moses even gets down the mountain with the stone tablets."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Exodus 34:6",
     "why": "Like the father who runs to his lost son, God shows himself to be slow to anger and full of love, forgiving a people who turned away."},
    {"title": "Water From the Rock", "storyId": "moses-water", "reference": "Exodus 17:6",
     "why": "Moses keeps standing between God and a stubborn people, pleading for them again and again on the long desert road."}
  ],
  "tier1": {
    "book": "Exodus 32",
    "hook": "Moses was up on the mountain with God for forty days. Down below, the people got tired of waiting, and decided to make themselves a god they could see.",
    "story": [
      "Moses had climbed up Mount Sinai to meet with God and receive his law, and he was gone a long time, forty days and forty nights. Down at the bottom of the mountain, the people grew restless. \"We do not know what has happened to this Moses who brought us out of Egypt,\" they said. \"Come on, make us gods who will lead us.\"",
      "They said this to Aaron, Moses' own brother. And instead of stopping them, Aaron gave in. \"Bring me your gold earrings,\" he said. The people took off their gold, and Aaron melted it down and shaped it into the statue of a calf.",
      "Then the people bowed down to the golden calf and shouted, \"These are your gods, Israel, who brought you up out of Egypt!\" They built an altar in front of it, threw a wild feast, and danced. Only weeks after promising to obey the living God, they were worshiping a lump of gold they had made with their own hands.",
      "Up on the mountain, God said to Moses, \"Go down. Your people have already turned away from me.\" God was angry, and he told Moses he could start over with him alone. But Moses did not want that. He begged God for the people, \"Lord, why should the Egyptians get to say you rescued them only to destroy them? Remember your promise to Abraham.\" And God listened to Moses.",
      "Moses came down the mountain carrying two stone tablets, written by the finger of God. But when he saw the calf and the wild dancing, his anger blazed. He threw the tablets to the ground, and they shattered to pieces at the foot of the mountain.",
      "Moses took the golden calf, melted it in the fire, ground it into powder, and dealt with the terrible thing the people had done. \"What did these people do to make you lead them into such a sin?\" he asked Aaron. Aaron made a weak excuse: \"I threw the gold into the fire, and out came this calf.\" As if no one had made it at all.",
      "The next day Moses went back up to God. \"These people have sinned a great sin,\" he prayed. \"But please, forgive them. And if you will not, then blot my name out of your book along with theirs.\" Moses loved the people so much he was willing to share their punishment to save them.",
      "And God, who had every right to walk away, chose mercy. He stayed with his people and led them onward. They had been quick to forget him, but he was slow to give up on them. That is who God is: slow to anger, and overflowing with love."
    ],
    "devotional": {
      "bigIdea": "The people forgot God almost as soon as he had rescued them, and traded him for a statue of gold. Yet when Moses pleaded for them, God chose to forgive and stay. We are all quick to forget God, but he is wonderfully slow to give up on us.",
      "questions": [
        "The people wanted a god they could see and touch. Why do you think it is tempting to trust in things we can see more than in God?",
        "Moses loved the people so much that he begged God to forgive them. Who is someone who prays for you like that?",
        "God had every reason to give up on the people, but he forgave them instead. How does it feel to know God is slow to give up on you?"
      ]
    },
    "tags": ["worship", "idols", "forgiveness", "Moses", "God's mercy"],
    "quiz": [
      {"question": "Why did the people want Aaron to make them a god?", "options": ["Moses had been gone a long time and they were tired of waiting", "They had lost their way", "God told them to"], "answer": 0, "explanation": ""},
      {"question": "What did Aaron make the idol out of?", "options": ["Wood", "Melted gold", "Clay"], "answer": 1, "explanation": ""},
      {"question": "What did Moses do when he saw the golden calf?", "options": ["He joined the dancing", "He threw down and broke the stone tablets", "He ran back up the mountain"], "answer": 1, "explanation": ""},
      {"question": "What did Moses do for the people afterward?", "options": ["He begged God to forgive them", "He left them in the desert", "He made a bigger statue"], "answer": 0, "explanation": ""},
      {"question": "What did God decide to do with his forgetful people?", "options": ["Forgive them and stay with them", "Send them back to Egypt", "Forget about them"], "answer": 0, "explanation": "God is slow to anger and full of love, even when we fail."}
    ]
  },
  "tier2": {
    "book": "Exodus 32",
    "hook": "While Moses was up on the mountain talking with God, the people grew tired of waiting and made a pretend god out of gold.",
    "story": [
      "Moses went up the tall mountain to meet with God and to get his rules for living. He was gone for a long, long time, forty days and forty nights.",
      "Down below, the people got tired of waiting. They went to Moses' brother Aaron and said, \"We do not know what happened to Moses. Make us a god we can see!\"",
      "So Aaron took their gold earrings, melted them in the fire, and shaped the gold into a shiny calf. The people bowed down low to it and had a big, wild party.",
      "But this was very, very wrong. They were forgetting the real God, who had just saved them from Egypt with his mighty power.",
      "Up on the mountain, God told Moses what the people were doing. So Moses hurried back down, carrying two flat stones with God's words written on them.",
      "When Moses saw the golden calf and the wild party, his heart filled with sadness and anger. He was so upset that he dropped the two stones, and they smashed into pieces on the ground.",
      "Moses melted the golden calf in the fire until there was nothing left of it. Then he asked Aaron, \"Why did you let the people do such a terrible thing?\"",
      "The next day, Moses went back up the mountain. \"Please forgive your people,\" he begged God. He loved them so much that he wanted to share their punishment.",
      "And God, who is slow to get angry and full of love, forgave the people and stayed with them. They had been quick to forget God, but God would not give up on them."
    ],
    "devotional": {
      "bigIdea": "The people forgot God and made a pretend god of gold. But when Moses asked God to forgive them, God did. God is patient and loving, even when we mess up.",
      "questions": [
        "The people made a god they could see. Why is it better to trust the real God we cannot see?",
        "Moses asked God to forgive his friends. Who prays for you?",
        "How does it feel to know God forgives us when we are sorry?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["worship", "forgiveness", "God's mercy"],
    "quiz": [
      {"question": "Why did the people make a golden calf?", "options": ["They were tired of waiting for Moses", "God asked them to", "They were hungry"], "answer": 0, "explanation": ""},
      {"question": "What did Moses do when he saw the calf?", "options": ["He dropped and broke the stone tablets", "He danced too", "He hid"], "answer": 0, "explanation": ""},
      {"question": "What did God do when Moses asked him to forgive the people?", "options": ["He forgave them", "He left them", "He got a new people"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "bronze-serpent", "era": "exodus", "emoji": "🐍",
  "title": "The Bronze Snake", "date": "c. 1407 BC", "location": "The Wilderness",
  "connections": [
    {"title": "The Darkest Friday", "storyId": "crucifixion", "reference": "John 3:14",
     "why": "Jesus said that just as Moses lifted the snake on a pole, he would be lifted up on the cross, so that all who look to him in trust would live."},
    {"title": "Water From the Rock", "storyId": "moses-water", "reference": "Numbers 21:5",
     "why": "Once again the people grumble on the hard desert road, and once again God answers their complaining with mercy."},
    {"title": "Bread from Heaven", "storyId": "manna", "reference": "Numbers 21:5",
     "why": "The people complain about the very manna God sends them each day, forgetting that it is a daily gift from heaven."}
  ],
  "tier1": {
    "book": "Numbers 21",
    "hook": "The people complained against God one too many times, and snakes came into the camp. But God gave them a strange cure: just look, and live.",
    "story": [
      "The people of Israel had been traveling through the wilderness for many years, and the road was long and hard. Once again they lost their patience and spoke against God and against Moses. \"Why did you bring us out here to die?\" they cried. \"There is no bread, there is no water, and we are sick of this miserable food!\" They were complaining about the very manna God sent fresh from heaven every morning.",
      "They had everything they truly needed, and still they grumbled. This time, venomous snakes came in among the people. Many were bitten, and many died, and the camp was filled with fear.",
      "The people came running to Moses. \"We have sinned,\" they admitted. \"We spoke against the Lord and against you. Please pray that he will take the snakes away.\" So Moses prayed for the people who had just been complaining about him.",
      "God answered, but his answer was strange. He did not simply take the snakes away. \"Make a snake and put it up on a pole,\" he told Moses. \"Anyone who has been bitten can look at it and live.\"",
      "So Moses made a snake out of shining bronze and lifted it high on a pole in the middle of the camp. And it happened just as God had said. When anyone who had been bitten looked up at the bronze snake, they did not die. They lived.",
      "There was no medicine to take and nothing to do but look. It was so simple that some people may have thought it was foolish and refused. But everyone who trusted God enough to look up was healed.",
      "Many, many years later, Jesus spoke about that very pole in the desert. \"Just as Moses lifted up the snake in the wilderness,\" he said, \"so the Son of Man must be lifted up, so that everyone who believes in him will have eternal life.\" On the cross, Jesus would be lifted up high, and all who look to him in trust would be saved."
    ],
    "devotional": {
      "bigIdea": "God told the people to do something simple, just look, and live. All they had to bring was trust. In the same way, we are not saved by trying hard enough or being good enough. We are saved by looking to Jesus, who was lifted up for us.",
      "questions": [
        "The people had everything they needed and still complained. When do you find yourself grumbling about good things God has given you?",
        "God's cure was so simple that some might have thought it was silly. Why is it sometimes hard to trust a simple gift instead of trying to fix things ourselves?",
        "Jesus said he would be lifted up like the bronze snake. What does it mean to look to Jesus when you need help?"
      ]
    },
    "tags": ["trust", "healing", "Jesus", "the cross", "the wilderness"],
    "quiz": [
      {"question": "What were the people complaining about this time?", "options": ["The food and water God gave them", "The hot sun", "Their long clothes"], "answer": 0, "explanation": ""},
      {"question": "What came into the camp because of their grumbling?", "options": ["A sandstorm", "Venomous snakes", "Wild lions"], "answer": 1, "explanation": ""},
      {"question": "What did God tell Moses to make?", "options": ["A bronze snake on a pole", "A golden calf", "A big wall"], "answer": 0, "explanation": ""},
      {"question": "What did people have to do to be healed?", "options": ["Take medicine", "Look up at the bronze snake", "Run away"], "answer": 1, "explanation": "All they had to bring was trust, and they would live."},
      {"question": "Who did Jesus say the lifted-up snake pointed to?", "options": ["Himself, lifted up on the cross", "Moses", "Pharaoh"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Numbers 21",
    "hook": "When snakes came into the camp, God gave the people a surprising way to be saved. All they had to do was look up.",
    "story": [
      "The people of Israel had been traveling through the desert for a long, long time, and they were getting grumpy. They complained against God again, even about the good food he sent them every day.",
      "This time, snakes came slithering into the camp, and many people got hurt and were very scared.",
      "The people ran to Moses and said, \"We are sorry! We should not have complained against God. Please ask him to help us.\" So Moses prayed for the people.",
      "God gave Moses a surprising answer. He said, \"Make a snake out of shiny bronze, and put it up high on a tall pole.\"",
      "God promised, \"Anyone who has been hurt can look up at the bronze snake, and they will get better.\"",
      "So Moses made the bronze snake and lifted it high on the pole, right in the middle of the camp.",
      "There was no medicine to take and nothing hard to do. The people who were hurt just looked up at the snake, and they got well again.",
      "All they had to bring was trust. Looking up was their way of saying, God, I believe you can save me.",
      "Long, long after, Jesus said that he would be lifted up high too, so that everyone who looks to him would be saved. When we need help, we can always look to Jesus."
    ],
    "devotional": {
      "bigIdea": "All the people had to do was look up and trust God, and they were saved. We are saved the same way, by looking to Jesus.",
      "questions": [
        "The people complained even about good things. What is something good God has given you to be thankful for?",
        "God's cure was just to look up. Why is it good that God makes the way simple?",
        "What does it mean to you to look to Jesus when you are scared?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["trust", "healing", "the cross"],
    "quiz": [
      {"question": "What came into the camp when the people grumbled?", "options": ["Snakes", "Bears", "Birds"], "answer": 0, "explanation": ""},
      {"question": "What did God tell Moses to put up on a pole?", "options": ["A bronze snake", "A flag", "A lamp"], "answer": 0, "explanation": ""},
      {"question": "What did the people do to get better?", "options": ["Looked up at the snake", "Ran away fast", "Took medicine"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-02a.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-02a.json with {len(batch)} stories.")
