#!/usr/bin/env python3
"""Authoring source for Batch 2b (end of wilderness + early Promised Land). Writes batch-02b.json."""
import json

batch = [
{
  "id": "spies", "era": "exodus", "emoji": "🍇",
  "title": "The Twelve Spies", "date": "c. 1446 BC", "location": "The Edge of Canaan",
  "connections": [
    {"title": "The Walls Come Down", "storyId": "jericho", "reference": "Numbers 14:30",
     "why": "Only Caleb and Joshua trusted God here, and forty years later Joshua is the one who finally leads Israel into the land."},
    {"title": "Crossing the Jordan River", "storyId": "jordan", "reference": "Numbers 14:24",
     "why": "The fearful generation never entered the land, but their children, led by Joshua, cross the river and go in."},
    {"title": "Through the Sea on Dry Ground", "storyId": "red-sea", "reference": "Numbers 14:11",
     "why": "God had already split the sea for these people, yet they still would not trust him with the giants ahead."}
  ],
  "tier1": {
    "book": "Numbers 13–14",
    "hook": "God brought his people right to the edge of the promised land and told them to go in. Twelve spies went to look first. Ten came back terrified, and two came back trusting God.",
    "story": [
      "After all their years in the desert, the people of Israel finally stood at the edge of Canaan, the good land God had promised to give them. God told Moses to choose twelve men, one leader from each tribe, and send them ahead to explore the land.",
      "For forty days the twelve spies walked all through Canaan. The land was every bit as wonderful as God had said, flowing with milk and honey. They cut down a single cluster of grapes so enormous that it took two men to carry it on a pole between them, and they brought back pomegranates and figs too.",
      "When they came back, all twelve agreed the land was rich and beautiful. But then ten of them began to spread fear. \"The people who live there are powerful, and their cities have walls as high as the sky. There are even giants! Next to them we felt like tiny grasshoppers, and that is how they saw us too.\"",
      "The people heard this and panicked. But two of the spies, Caleb and Joshua, tore their clothes in distress and tried to calm them. \"The land is excellent! If the Lord is pleased with us, he will bring us safely in and give it to us. Do not be afraid of the people there. The Lord is with us!\"",
      "But the people would not listen. They wept all night long. They grumbled against Moses and even talked about choosing a new leader to take them back to slavery in Egypt. After everything God had done, they trusted their fear more than they trusted him.",
      "God was deeply grieved. \"How long will these people refuse to trust me, after all the wonders I have done?\" Because they would not believe him, that whole grown-up generation would not enter the promised land. They would wander in the wilderness for forty years, one year for every day the spies had explored.",
      "Only two men would live to enter the land: Caleb and Joshua, the two who had trusted God. The giants the spies feared were real. But so was God, who had flattened Egypt and split the sea. Ten men looked at the giants and forgot how big God was. Two men looked at God and were not afraid of any giant. That is the difference faith makes."
    ],
    "devotional": {
      "bigIdea": "Ten spies and two spies saw exactly the same giants. The difference was not the size of the giants. It was that Caleb and Joshua remembered how big their God was. Faith does not pretend the giants are small. It trusts that God is bigger.",
      "questions": [
        "The ten spies and the two spies saw the same land and the same giants. Why do you think they came back with such different reports?",
        "The people had seen God split the sea, yet they were still afraid. What helps you remember what God has done when you feel scared?",
        "What is a giant, a big scary thing, that you are facing right now? What would it look like to trust that God is bigger?"
      ]
    },
    "tags": ["faith", "fear", "trust", "courage", "God's promises"],
    "quiz": [
      {"question": "How many spies did Moses send into Canaan?", "options": ["Three", "Twelve", "Forty"], "answer": 1, "explanation": "One leader was chosen from each of the twelve tribes."},
      {"question": "What did the spies bring back to show how rich the land was?", "options": ["A giant cluster of grapes", "A bag of gold", "A lion"], "answer": 0, "explanation": ""},
      {"question": "What scared ten of the spies?", "options": ["The deserts", "The powerful people and giants", "The long walk"], "answer": 1, "explanation": ""},
      {"question": "Which two spies trusted God and said, do not be afraid?", "options": ["Aaron and Miriam", "Caleb and Joshua", "Moses and Pharaoh"], "answer": 1, "explanation": ""},
      {"question": "Why did that generation not get to enter the promised land?", "options": ["They got lost", "They refused to trust God", "They did not like the fruit"], "answer": 1, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Numbers 13-14",
    "hook": "God's people came right up to the edge of the wonderful new land God promised them. Twelve men went to explore it, but only two of them trusted God.",
    "story": [
      "After many years in the desert, God's people finally came to the edge of the new land God had promised to give them.",
      "God told Moses to send twelve men ahead to explore the land and see what it was like.",
      "For forty days the men walked all around the land. It was beautiful and full of good food. They even found a bunch of grapes so big that it took two men to carry it on a pole!",
      "But when they came back, ten of the men were scared. \"There are giants in that land,\" they said, \"and huge cities with tall walls. We can never go in there!\"",
      "When the people heard this, they got very afraid, and they cried all night long.",
      "But two of the men, Caleb and Joshua, were brave. \"Do not be afraid!\" they said. \"God is with us. He will help us go in and live there.\"",
      "Sadly, the people listened to their fear instead of trusting God. So they had to wait out in the desert for a long, long time.",
      "But Caleb and Joshua had trusted God, and one day they got to go into the good land. The giants were big, but God was even bigger.",
      "When we feel scared, we can remember that God is bigger than anything that frightens us."
    ],
    "devotional": {
      "bigIdea": "Everyone saw the same giants. But Caleb and Joshua remembered that God was even bigger than the giants. We can trust that God is bigger than anything that scares us.",
      "questions": [
        "Why do you think the ten men were so scared?",
        "Caleb and Joshua were brave because they trusted God. What is something scary that God can help you with?",
        "How do you remember that God is with you when you feel afraid?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["faith", "fear", "courage"],
    "quiz": [
      {"question": "What did the men bring back to show the land was good?", "options": ["A giant bunch of grapes", "A pile of rocks", "A baby lion"], "answer": 0, "explanation": ""},
      {"question": "Which two men trusted God and were brave?", "options": ["Caleb and Joshua", "Moses and Aaron", "Adam and Eve"], "answer": 0, "explanation": ""},
      {"question": "What should we remember when we are scared?", "options": ["God is bigger than anything", "We should run away", "Giants always win"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "balaam", "era": "exodus", "emoji": "🫏",
  "title": "Balaam's Donkey", "date": "c. 1407 BC", "location": "Moab",
  "connections": [
    {"title": "A Promise as Big as the Stars", "storyId": "abraham", "reference": "Genesis 12:3",
     "why": "God told Abraham he would bless those who blessed his family and curse those who cursed them, and now no one can curse what God has blessed."},
    {"title": "The Burning Bush", "storyId": "burning-bush", "reference": "Numbers 22:28",
     "why": "Just as God once spoke from a bush that would not burn up, here he speaks through the mouth of a donkey, using the unexpected to get our attention."},
    {"title": "Through the Sea on Dry Ground", "storyId": "red-sea", "reference": "Numbers 23:23",
     "why": "The same God who fought for his people at the sea now protects them from a curse they never even knew was coming."}
  ],
  "tier1": {
    "book": "Numbers 22–24",
    "hook": "A frightened king tried to hire a famous prophet to curse God's people. But God used the most unlikely teacher in the world to stop him: a talking donkey.",
    "story": [
      "The people of Israel had camped near the land of Moab, and Balak, the king of Moab, was terrified of them. There were so many of them, and he had heard what their God could do. So Balak sent for a famous prophet named Balaam, offering him a fortune to come and place a curse on Israel.",
      "That night God spoke to Balaam. \"Do not go with them, and do not curse those people, for they are blessed.\" So Balaam sent the messengers away. But King Balak only sent more important men, with promises of even greater riches. And Balaam, who loved a reward, wanted to go.",
      "God allowed him to go but gave a clear warning: \"Say only what I tell you to say.\" So Balaam saddled his donkey in the morning and set off. But God was angry that Balaam's heart was set on money, and an angel of the Lord stood in the road to block his way, holding a flashing sword.",
      "Balaam could not see the angel, but his donkey could. She turned off the road into a field to get away. Balaam, seeing nothing, beat her and forced her back. Further on, the path narrowed between two walls, and the angel stood there again. The donkey pressed against the wall, crushing Balaam's foot, and he beat her again.",
      "The third time, in a place so narrow there was nowhere to turn, the donkey simply lay down underneath him. Balaam was furious and beat her once more. Then the Lord did an astonishing thing: he opened the donkey's mouth, and she spoke. \"What have I done to make you beat me three times?\"",
      "Balaam was so angry he argued back, as if talking with a donkey were perfectly normal. \"You have made a fool of me!\" The donkey answered, \"Am I not the same donkey you have ridden all your life? Have I ever done anything like this to you before?\" \"No,\" Balaam admitted.",
      "Then God opened Balaam's eyes, and he finally saw the angel standing in the road with the drawn sword, and he fell facedown. \"Your donkey saw me and turned away three times,\" the angel said. \"If she had not, I would have struck you down by now.\" A donkey had seen what the great prophet was too blind to see.",
      "Balaam went on, but every time he opened his mouth to curse Israel, only blessings came out. Again and again he tried, and again and again God turned his words into blessing. King Balak was furious, but there was nothing anyone could do. No one on earth can curse the people God has chosen to bless."
    ],
    "devotional": {
      "bigIdea": "A king with a pile of gold could not curse God's people, because God had blessed them, and no power on earth can undo what God has done. God even used a donkey to protect a man who was too stubborn to see. God watches over his people, even from dangers they never know about.",
      "questions": [
        "Balaam could not see the angel, but the donkey could. When has someone smaller or less important than you actually seen something true that you missed?",
        "God protected Israel from a curse they did not even know was coming. How does it feel to know God protects you from things you cannot see?",
        "Balaam knew the right thing to do but wanted the reward so badly he went anyway. When is it hard to do the right thing because you want something?"
      ]
    },
    "tags": ["God's protection", "blessing", "obedience", "God's power", "humility"],
    "quiz": [
      {"question": "What did King Balak want Balaam to do?", "options": ["Curse God's people", "Become king", "Build a city"], "answer": 0, "explanation": ""},
      {"question": "Who could see the angel blocking the road?", "options": ["Balaam", "The donkey", "King Balak"], "answer": 1, "explanation": "The donkey saw the angel and turned away to save Balaam's life."},
      {"question": "What amazing thing did God let the donkey do?", "options": ["Fly", "Talk", "Turn invisible"], "answer": 1, "explanation": ""},
      {"question": "What happened every time Balaam tried to curse Israel?", "options": ["Only blessings came out", "Nothing happened", "He fell asleep"], "answer": 0, "explanation": ""},
      {"question": "What is the big lesson of the story?", "options": ["Donkeys are smart", "No one can curse the people God has blessed", "Money makes you happy"], "answer": 1, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Numbers 22-24",
    "hook": "A king wanted a man named Balaam to say bad words against God's people. But God had a very surprising helper to stop him: a donkey that could talk!",
    "story": [
      "God's people set up their camp near a land called Moab. The king of Moab was very afraid of them, because there were so many of them.",
      "So the king sent for a man named Balaam. He offered Balaam lots of money to come and say bad, cursing words against God's people.",
      "But God told Balaam, \"Do not curse them. They are my people, and they are blessed.\" Still, Balaam wanted the money. So he got on his donkey and started to go anyway.",
      "God was not happy about this. So an angel with a shiny sword stood right in the middle of the road. But only the donkey could see the angel, not Balaam!",
      "To stay safe, the donkey kept turning away from the angel. But Balaam could not see why, so he hit his donkey to make her keep going. This happened three times.",
      "Then God did something amazing. He let the donkey talk! \"Why are you hitting me?\" she asked Balaam.",
      "Then God let Balaam see the angel too. Balaam was very sorry. His donkey had been keeping him safe the whole time.",
      "After that, every time Balaam tried to say bad words about God's people, only good and happy words came out instead!",
      "No one can curse the people God has blessed. God was taking care of his people, even when they did not know it."
    ],
    "devotional": {
      "bigIdea": "A king with lots of money could not hurt God's people, because God was protecting them. God even used a talking donkey to keep Balaam safe. God watches over us all the time.",
      "questions": [
        "Only the donkey could see the angel. Has anyone smaller than you ever noticed something you missed?",
        "God protected his people from something they did not even know about. How does it feel that God is watching over you?",
        "What was the most surprising part of this story to you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God's protection", "blessing", "God's power"],
    "quiz": [
      {"question": "What did the king want Balaam to do?", "options": ["Say bad words against God's people", "Build a boat", "Sing a song"], "answer": 0, "explanation": ""},
      {"question": "Who could see the angel in the road?", "options": ["The donkey", "Balaam", "The king"], "answer": 0, "explanation": ""},
      {"question": "What surprising thing did God let the donkey do?", "options": ["Talk", "Fly", "Dance"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "jordan", "era": "promised-land", "emoji": "🌊",
  "title": "Crossing the Jordan River", "date": "c. 1406 BC", "location": "The Jordan River",
  "connections": [
    {"title": "Through the Sea on Dry Ground", "storyId": "red-sea", "reference": "Joshua 4:23",
     "why": "Forty years earlier God split the sea for their parents, and now he stops a flooding river so the children can cross on dry ground."},
    {"title": "The Walls Come Down", "storyId": "jericho", "reference": "Joshua 6:1",
     "why": "The first thing waiting on the far side of the river is the great walled city of Jericho, Israel's first test in the new land."},
    {"title": "The Twelve Spies", "storyId": "spies", "reference": "Joshua 3:7",
     "why": "This is the generation the fearful spies never believed in, the children who grew up and finally trusted God enough to go in."}
  ],
  "tier1": {
    "book": "Joshua 3–4",
    "hook": "Forty years after the Red Sea, a brand new generation stood at the edge of a flooded river with no bridge and no boats. God was about to prove he was the very same God who had saved their parents.",
    "story": [
      "Moses had died, and now a man named Joshua led the people. The long forty years of wandering were finally over. A whole new generation stood at the banks of the Jordan River, the last thing standing between them and the promised land. But it was harvest season, and the river was flooding, wide and deep and rushing fast.",
      "God told Joshua how they would cross. The priests would go first, carrying the ark of the covenant, the special golden chest that showed God was with his people. They would carry it right to the edge of the water and step in.",
      "\"Today,\" God promised Joshua, \"I will begin to make you great in the eyes of all Israel, so they will know that I am with you just as I was with Moses.\"",
      "So the priests carried the ark down to the flooding river and stepped in. And the very moment their feet touched the water, the river stopped. Far upstream the water piled up in a great heap, and the riverbed in front of them turned to dry ground.",
      "The priests stood still in the middle of the riverbed, holding the ark, while the entire nation walked across the dry ground to the other side. It was exactly as their parents had done at the Red Sea, a whole new generation seeing that God had not changed at all.",
      "Then God told Joshua to choose twelve men, one from each tribe, and have each carry a large stone up out of the middle of the river. They piled the stones into a memorial on the far bank.",
      "\"In the future,\" Joshua said, \"when your children ask, what do these stones mean? you will tell them how the Lord your God stopped the waters of the Jordan so you could cross. These stones will remind us forever.\"",
      "When the priests finally carried the ark up out of the riverbed, the waters came rushing back and the Jordan flooded its banks again. The same God who saved the parents had saved the children. And he gave them a pile of stones so they would always remember to tell the story."
    ],
    "devotional": {
      "bigIdea": "The parents saw God split the sea. Forty years later, the children saw God stop the river. God set up a pile of stones so that one day their own children would ask about it, and the story would keep getting told. God wants every generation to know what he has done.",
      "questions": [
        "The priests had to step into the flooding water before it stopped. Why do you think God waited until their feet were wet?",
        "God told them to set up stones so children would ask about them. What is a story about God that you want to remember and tell others?",
        "This was a new generation seeing God do what their parents had seen. Who first told you the stories about God?"
      ]
    },
    "tags": ["faith", "God's faithfulness", "remembering", "new beginnings", "Joshua"],
    "quiz": [
      {"question": "Who led the people now that Moses had died?", "options": ["Joshua", "Aaron", "Caleb"], "answer": 0, "explanation": ""},
      {"question": "What did the priests carry into the river first?", "options": ["A boat", "The ark of the covenant", "A pile of stones"], "answer": 1, "explanation": "The ark showed that God himself was leading them across."},
      {"question": "What happened when the priests' feet touched the water?", "options": ["The river stopped and piled up", "It started to rain", "Fish jumped out"], "answer": 0, "explanation": ""},
      {"question": "Why did they pile up twelve stones?", "options": ["To build a wall", "To help everyone remember what God did", "To mark a grave"], "answer": 1, "explanation": ""},
      {"question": "What earlier miracle was this just like?", "options": ["The crossing of the Red Sea", "The fall of Jericho", "The flood of Noah"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Joshua 3-4",
    "hook": "God's people came to a big river they had to cross to reach their new home. The river was deep and wide, but God made a dry path right through the middle.",
    "story": [
      "After many years, God's people came to a big river called the Jordan. They needed to cross it to reach the new home God had promised them.",
      "But the river was very deep and fast, and there was no bridge and no boats.",
      "Their new leader was a brave man named Joshua. God told him, \"Have the priests carry the special golden chest into the river first.\"",
      "So the priests carried the golden chest down to the water and stepped in.",
      "The very moment their feet touched the river, the water stopped flowing! It piled up far away, and the ground in the middle of the river became dry.",
      "Then all of God's people walked across the river on the dry ground, and they stayed perfectly safe and dry.",
      "God told them to pile up twelve big stones on the other side, to help everyone remember this amazing day.",
      "Whenever children would ask, \"What are these stones for?\" their parents could tell them the story of how God stopped the river.",
      "God had stopped the sea for their parents, and now he stopped the river for them. God was showing he would always take care of his people."
    ],
    "devotional": {
      "bigIdea": "God stopped a whole river so his people could cross safely. He gave them stones to help them remember, so they would never forget how good he is.",
      "questions": [
        "How do you think the people felt walking through the middle of a river on dry ground?",
        "The stones helped them remember God's help. What helps you remember the good things God does?",
        "God took care of his people again and again. How has God taken care of you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["faith", "God's faithfulness", "remembering"],
    "quiz": [
      {"question": "What did the people need to cross to reach their new home?", "options": ["A big river", "A tall mountain", "A wide desert"], "answer": 0, "explanation": ""},
      {"question": "What happened when the priests stepped into the water?", "options": ["The river stopped flowing", "It started to rain", "They swam across"], "answer": 0, "explanation": ""},
      {"question": "Why did they pile up twelve stones?", "options": ["To help everyone remember", "To build a house", "To play a game"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "deborah", "era": "promised-land", "emoji": "🌴",
  "title": "Deborah the Judge", "date": "c. 1200 BC", "location": "The Hill Country of Ephraim",
  "connections": [
    {"title": "Three Hundred Men and Torches", "storyId": "gideon", "reference": "Judges 6:14",
     "why": "Like Gideon after her, Deborah is one of the judges God raised up to rescue his people whenever they cried out to him."},
    {"title": "Wherever You Go", "storyId": "ruth", "reference": "Ruth 1:1",
     "why": "Ruth's story takes place in these same days of the judges, when God was quietly at work through ordinary, faithful people."},
    {"title": "The Walls Come Down", "storyId": "jericho", "reference": "Judges 4:14",
     "why": "Just as God handed Jericho to Joshua, he hands Sisera's mighty army to a people who march out trusting his word."}
  ],
  "tier1": {
    "book": "Judges 4–5",
    "hook": "When God's people had no king and a cruel enemy with nine hundred iron chariots, God raised up a wise woman to lead them back to freedom.",
    "story": [
      "After Joshua died, the people of Israel kept forgetting God and falling into trouble. Again and again, when they cried out to him, God raised up rescuers called judges to save them. One of the greatest of all the judges was a wise woman named Deborah.",
      "Deborah was a prophet, and people came from all around to sit under her palm tree while she helped them settle their arguments and hear from God. In those days a cruel king and his army commander, a man named Sisera, had been crushing Israel for twenty years. Sisera had nine hundred iron chariots, and the people were afraid.",
      "Deborah sent for a soldier named Barak and gave him God's message. \"The Lord commands you: take ten thousand men to Mount Tabor. I will lead Sisera and his chariots and his army to the river, and I will hand him over to you.\"",
      "But Barak was afraid to go alone. \"If you go with me, I will go,\" he told Deborah. \"But if you do not go with me, I will not go.\" Deborah agreed to go. \"But because of the way you are doing this,\" she said, \"the honor of the victory will not be yours. The Lord will hand Sisera over to a woman.\"",
      "So Deborah went with Barak and the army to the mountain. When the time came, Deborah said, \"Go! This is the day the Lord has given you victory. Has the Lord not gone ahead of you?\" Barak charged down the mountain with his ten thousand men.",
      "And God threw Sisera's whole army into a panic. A great rainstorm turned the ground to thick mud, and the nine hundred iron chariots that everyone feared got stuck fast and useless. Barak's army won a complete victory, and not one of the enemy soldiers was left.",
      "Sisera himself jumped down from his chariot and ran away on foot. He hid in the tent of a woman named Jael, who gave him milk and covered him with a blanket. But while he slept, brave Jael made sure that Sisera would never harm Israel again. Just as Deborah had promised, a woman won the day.",
      "Then Deborah sang a song that people would remember for hundreds of years, praising the God who answers his people when they cry out. God does not need the strongest army or the most powerful person. He uses anyone, man or woman, young or old, who is willing to trust him and obey."
    ],
    "devotional": {
      "bigIdea": "God's people faced an enemy with nine hundred iron chariots, and God handed the victory to a wise woman, a willing soldier, and a sudden rainstorm. God is not impressed by chariots or armies. He uses whoever is willing to trust him and follow.",
      "questions": [
        "Barak would only go if Deborah came with him. When has having a friend beside you helped you do something brave?",
        "Everyone was afraid of the nine hundred iron chariots, but God used mud to stop them. What is something that looks too big to beat, that is small to God?",
        "God used Deborah, Barak, and Jael together to rescue his people. What might God want to use you for?"
      ]
    },
    "tags": ["courage", "leadership", "trust", "God's power", "the judges"],
    "quiz": [
      {"question": "What was Deborah's job among God's people?", "options": ["She was a judge and a prophet", "She was a queen", "She was a soldier"], "answer": 0, "explanation": "People came to her palm tree to settle arguments and hear from God."},
      {"question": "What was the enemy army famous for?", "options": ["Nine hundred iron chariots", "Flying machines", "Giant horses"], "answer": 0, "explanation": ""},
      {"question": "What did Barak say he needed in order to go?", "options": ["More gold", "Deborah to go with him", "A faster horse"], "answer": 1, "explanation": ""},
      {"question": "How did God stop the mighty iron chariots?", "options": ["A rainstorm turned the ground to mud", "An earthquake", "A fire"], "answer": 0, "explanation": ""},
      {"question": "What does this story show about who God uses?", "options": ["Only kings and soldiers", "Anyone willing to trust and obey him", "Only very strong people"], "answer": 1, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Judges 4-5",
    "hook": "God's people were in trouble and needed a brave leader. God chose a wise woman named Deborah to help save them.",
    "story": [
      "After Joshua died, God's people kept getting into trouble. So God sent special helpers called judges to rescue them.",
      "One of the best judges was a very wise woman named Deborah. She would sit under a big palm tree, and people came to her to solve their problems and hear from God.",
      "A mean king and his army had been hurting God's people for a long, long time. The army had nine hundred strong chariots, and the people were scared.",
      "So Deborah called for a soldier named Barak. \"God says to take an army to the mountain,\" she told him. \"God will help you win!\"",
      "But Barak was afraid. \"I will only go if you come with me,\" he said. So brave Deborah went with him.",
      "When it was time to fight, Deborah said, \"Go now! This is the day God will help you win!\"",
      "Then God sent a big rainstorm. The ground turned to thick, sticky mud, and all the enemy chariots got stuck and could not move.",
      "So God's people won the battle! God had saved them again.",
      "Then Deborah sang a happy song to thank God. God can use anyone who trusts him, to do brave and wonderful things."
    ],
    "devotional": {
      "bigIdea": "God used a wise woman named Deborah and a little rainstorm to save his people from a great big army. God can use anyone who is willing to trust him.",
      "questions": [
        "Barak was braver when Deborah went with him. Who helps you be brave?",
        "God used a rainstorm to stop the scary chariots. What is something big that is small to God?",
        "God used Deborah in a special way. What do you think God might use you for?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["courage", "leadership", "trust"],
    "quiz": [
      {"question": "What was Deborah?", "options": ["A wise judge who helped God's people", "A farmer", "A queen of Egypt"], "answer": 0, "explanation": ""},
      {"question": "How did God stop the enemy's chariots?", "options": ["With a rainstorm and mud", "With a big wind", "With fire"], "answer": 0, "explanation": ""},
      {"question": "What can God do with anyone who trusts him?", "options": ["Use them for brave and wonderful things", "Nothing much", "Make them a king"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "samson", "era": "promised-land", "emoji": "💪",
  "title": "Samson's Strength", "date": "c. 1100 BC", "location": "The Land of the Philistines",
  "connections": [
    {"title": "Three Hundred Men and Torches", "storyId": "gideon", "reference": "Judges 13:5",
     "why": "Like Gideon, Samson is one of the judges, but his story is a warning that God's gifts are wasted when we will not follow him."},
    {"title": "Deborah the Judge", "storyId": "deborah", "reference": "Judges 13:1",
     "why": "Samson comes in the same long age of the judges, when God kept rescuing a people who kept forgetting him."},
    {"title": "One Stone", "storyId": "david-goliath", "reference": "Judges 16:28",
     "why": "Like David against Goliath, Samson's victories were never really about human muscle. The power always belonged to God."}
  ],
  "tier1": {
    "book": "Judges 13–16",
    "hook": "God gave Samson strength so great he could fight a lion with his bare hands. But his greatest enemy was never the Philistines. It was his own foolish choices.",
    "story": [
      "God's people were suffering under the Philistines, and they cried out to God. So an angel came to a woman who had no children and promised her a son who would begin to rescue Israel. The boy must never cut his hair. It would be the sign that he belonged to God in a special way, set apart from birth.",
      "The boy was named Samson, and he grew up with strength like no one had ever seen. Once, when a lion roared and rushed at him, Samson tore it apart with his bare hands. Again and again he fought the Philistines and won, because the Spirit of the Lord was powerful on him.",
      "But Samson was reckless and proud. He broke his promises to God and did whatever he pleased, chasing after whatever he wanted. Yet as long as his hair stayed uncut, the sign of his promise, his great strength stayed with him.",
      "Then Samson fell in love with a woman named Delilah. The Philistine rulers offered her silver to discover the secret of his strength. Three times she begged him to tell her, three times he gave her a false answer, and three times the Philistines tried to capture him and failed.",
      "But Delilah nagged him day after day until Samson was tired to death of it, and at last he told her the truth. \"My hair has never been cut, because I have belonged to God since I was born. If my head were shaved, my strength would leave me, and I would be as weak as anyone else.\"",
      "That night, while Samson slept, his hair was shaved off. When the Philistines came, he woke and said, \"I will shake myself free as before.\" But he did not know the saddest thing of all: the Lord had left him. His strength was gone. The Philistines captured him, blinded him, and put him to work grinding grain in prison.",
      "But there in the prison, little by little, Samson's hair began to grow back again. One day the Philistine rulers held a giant feast in the temple of their false god, and they brought Samson out to laugh at him. Standing between the two great pillars that held up the temple, Samson prayed. \"Sovereign Lord, remember me. Please, God, give me strength just one more time.\"",
      "Then Samson pushed against the pillars with all his might, and the whole temple came crashing down. In that one last moment, God used him to defeat more of Israel's enemies than in his whole life before. Samson had wasted so much of God's gift, yet God still answered him at the end. The strength had never really been about Samson. It had always been about God."
    ],
    "devotional": {
      "bigIdea": "Samson had gifts most people only dream of, and he wasted most of them on foolish, selfish choices. Yet when he finally prayed and asked God for help, God answered. The strength was never really Samson's own. It belonged to God, and so does ours.",
      "questions": [
        "Samson was given amazing gifts but kept making foolish choices with them. What gifts has God given you, and how can you use them well?",
        "Samson did not even notice when God had left him. How can we stay close to God instead of drifting away little by little?",
        "Even after everything, Samson prayed and God answered. What does that tell you about how God responds when we finally turn to him?"
      ]
    },
    "tags": ["strength", "choices", "God's power", "second chances", "the judges"],
    "quiz": [
      {"question": "What was the sign that Samson belonged to God?", "options": ["His uncut hair", "A golden crown", "A special sword"], "answer": 0, "explanation": ""},
      {"question": "What amazing thing did Samson do with his bare hands?", "options": ["Lifted a mountain", "Tore apart a lion", "Stopped a river"], "answer": 1, "explanation": ""},
      {"question": "Who learned the secret of his strength?", "options": ["Delilah", "Deborah", "His mother"], "answer": 0, "explanation": ""},
      {"question": "What happened when his hair was cut off?", "options": ["His strength left him", "He got even stronger", "Nothing changed"], "answer": 0, "explanation": ""},
      {"question": "What did Samson do at the very end?", "options": ["He prayed, and God gave him strength one last time", "He ran away", "He became a king"], "answer": 0, "explanation": "The strength was always God's, and God answered when Samson finally asked."}
    ]
  },
  "tier2": {
    "book": "Judges 13-16",
    "hook": "God gave a man named Samson amazing strength. As long as he kept his special promise to God, no one could beat him.",
    "story": [
      "God's people were having a hard time. So God sent a special baby boy named Samson to help save them.",
      "An angel said that Samson must never cut his hair. It was a special sign that Samson belonged to God.",
      "When Samson grew up, God gave him amazing strength. He was the strongest man anyone had ever seen! As long as he did not cut his hair, no one could beat him.",
      "But Samson did not always make good choices, and he did not always listen to God.",
      "One day, a woman named Delilah kept asking Samson why he was so strong. Finally, he told her his secret: it was his long hair.",
      "While Samson was sleeping, his enemies came and cut off his hair. When he woke up, his great strength was gone, and his enemies caught him and put him in prison.",
      "But while Samson was in prison, his hair slowly started to grow back again.",
      "One day his enemies brought him to their big building to laugh at him. Samson prayed, \"God, please give me strength just one more time.\"",
      "And God did! Samson pushed against the big pillars, and the whole building came tumbling down. Even after all of Samson's mistakes, God still listened when he prayed. God is strong, and he loves to help us when we ask."
    ],
    "devotional": {
      "bigIdea": "God gave Samson amazing strength. Samson made many bad choices, but when he finally prayed, God still helped him. God loves to help us when we ask him.",
      "questions": [
        "God gave Samson special strength. What special things has God given you?",
        "Samson forgot to listen to God. What are some ways we can listen to God every day?",
        "When Samson prayed, God helped him. How does it feel to know God hears your prayers?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["strength", "choices", "second chances"],
    "quiz": [
      {"question": "What made Samson so strong?", "options": ["God gave him strength, shown by his uncut hair", "He ate lots of vegetables", "A magic ring"], "answer": 0, "explanation": ""},
      {"question": "What was the secret of Samson's strength?", "options": ["His long hair", "His big shoes", "His sword"], "answer": 0, "explanation": ""},
      {"question": "When Samson prayed at the end, did God help him?", "options": ["Yes, God gave him strength again", "No, it was too late", "God was asleep"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-02b.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-02b.json with {len(batch)} stories.")
