#!/usr/bin/env python3
"""Authoring source for Batch 3b (Kingdom, part 2). Writes batch-03b.json."""
import json

batch = [
{
  "id": "mephibosheth", "era": "kingdom", "emoji": "🍽️",
  "title": "Kindness for Jonathan's Sake", "date": "c. 990 BC", "location": "Jerusalem",
  "connections": [
    {"title": "The Best of Friends", "storyId": "david-jonathan", "reference": "2 Samuel 9:1",
     "why": "David promised his friend Jonathan to be loyal to his family forever, and now, years later, he keeps that promise."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Luke 15:23",
     "why": "Like the father who welcomes his lost son to the feast, David welcomes a frightened, forgotten man to eat at the king's table."},
    {"title": "The Man in the Tree", "storyId": "zacchaeus", "reference": "Luke 19:5",
     "why": "Just as Jesus invited himself to the table of an outcast, David invites the last of Saul's family to share his own table."}
  ],
  "tier1": {
    "book": "2 Samuel 9",
    "hook": "Now that David was king, he could have wiped out the old king's family, as kings often did. Instead, he went looking for someone to be kind to.",
    "story": [
      "David was now the king, safe and strong on his throne. In those days, when a new king took over, he would often destroy every last person from the old king's family, so no one could ever challenge him. But David had something else on his mind.",
      "\"Is there anyone still left from the family of Saul,\" David asked, \"to whom I can show kindness for the sake of my friend Jonathan?\" David had never forgotten the promise he made to his beloved friend long ago.",
      "There was one. Jonathan had a son named Mephibosheth, who was now grown. When he was just a little boy, the day the bad news came about his father, his nurse had snatched him up to run, and in her hurry she dropped him, and from then on he could not walk. For years he had lived far away in hiding, sure that the king would want him gone.",
      "David sent for him. Imagine how Mephibosheth felt, carried into the throne room of the very king he feared, certain this was the end. He fell down before David, trembling. \"Mephibosheth,\" David said. \"Do not be afraid.\"",
      "\"I am going to show you kindness for the sake of your father Jonathan,\" David told him. \"I will give back to you all the land that belonged to your grandfather Saul. And from now on, you will always eat here, at my table, as one of my own sons.\"",
      "Mephibosheth could hardly believe it. \"Who am I,\" he said, \"that you would even notice someone like me?\" He had expected death, and instead he was given a home, land, and a permanent place at the king's table.",
      "And so it was. Mephibosheth, who could not walk, who had been hiding in fear, sat down to eat at the king's table every single day, treated like a prince. He had done nothing to earn it. It was all because of David's love for Jonathan. That is a picture of how God welcomes us, not because of anything we have done, but because of his great love."
    ],
    "devotional": {
      "bigIdea": "Mephibosheth expected the worst and received the best. He was given a seat at the king's table forever, not because of anything he did, but because of the king's love for someone else. That is exactly how God welcomes us to his table, because of his love, not because we have earned it.",
      "questions": [
        "Mephibosheth was sure the king wanted to harm him, but David wanted to bless him. Have you ever been afraid of something that turned out to be a gift?",
        "David showed kindness because of his promise to Jonathan. Who has been kind to you in a way you did not earn?",
        "God invites us to his table the way David invited Mephibosheth. How does it feel to be wanted like that?"
      ]
    },
    "tags": ["kindness", "grace", "promises", "welcome", "love"],
    "quiz": [
      {"question": "Why did David want to show kindness to Saul's family?", "options": ["Because of his promise to his friend Jonathan", "Because they paid him", "Because they were powerful"], "answer": 0, "explanation": ""},
      {"question": "Who was Mephibosheth?", "options": ["Jonathan's son, who could not walk", "A soldier", "A king of Egypt"], "answer": 0, "explanation": ""},
      {"question": "How did Mephibosheth feel when he was brought to the king?", "options": ["Afraid, expecting the worst", "Excited", "Angry"], "answer": 0, "explanation": ""},
      {"question": "What did David give Mephibosheth?", "options": ["Land and a place at the king's table forever", "A sword", "A long journey home"], "answer": 0, "explanation": ""},
      {"question": "What is this story a picture of?", "options": ["How God welcomes us out of love, not because we earned it", "How to win a battle", "How to become a king"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "2 Samuel 9",
    "hook": "King David made a promise to his best friend long ago. Now he kept that promise by being kind to someone everyone else had forgotten.",
    "story": [
      "David was now the king. He was safe and strong, sitting on his throne.",
      "One day David remembered his best friend, Jonathan, who had died. David had promised to always be kind to Jonathan's family.",
      "So David asked, \"Is anyone left from Jonathan's family that I can be kind to?\"",
      "There was one person. Jonathan had a son named Mephibosheth. When he was little, he had been hurt in his feet, and he could not walk.",
      "Mephibosheth had been hiding far away, because he was scared the new king would want to get rid of him.",
      "David sent for Mephibosheth. The poor man was shaking with fear as he was brought before the king.",
      "But David said gently, \"Do not be afraid! I am going to be kind to you, because I loved your father Jonathan.\"",
      "\"I am giving you back all your grandfather's land,\" said David. \"And you will eat at my table with me every day, like one of my own sons.\"",
      "Mephibosheth could hardly believe it! He thought he was in trouble, but instead he got a home and a special place at the king's table.",
      "He did nothing to earn it. It was all because of David's love. That is how God welcomes us too, because he loves us so much."
    ],
    "devotional": {
      "bigIdea": "Mephibosheth thought he was in trouble, but David gave him a place at the king's table because of love. That is how God welcomes us, because he loves us, not because we earned it.",
      "questions": [
        "Mephibosheth was scared, but David was kind. When has someone surprised you with kindness?",
        "David kept his promise to his friend. What is a promise you can keep?",
        "God gives us a special place with him because he loves us. How does that make you feel?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["kindness", "grace", "welcome"],
    "quiz": [
      {"question": "Why was David kind to Mephibosheth?", "options": ["Because he loved Jonathan, Mephibosheth's father", "Because he had to be", "Because Mephibosheth was rich"], "answer": 0, "explanation": ""},
      {"question": "What was special about Mephibosheth?", "options": ["He could not walk", "He was a giant", "He was a king"], "answer": 0, "explanation": ""},
      {"question": "What wonderful thing did David give him?", "options": ["A place at the king's table forever", "A horse", "A crown"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "david-bathsheba", "era": "kingdom", "emoji": "🕊️",
  "title": "David's Great Mistake", "date": "c. 990 BC", "location": "Jerusalem",
  "connections": [
    {"title": "God Looks at the Heart", "storyId": "david-anointed", "reference": "2 Samuel 12:13",
     "why": "God chose David for his heart, and even when that heart went badly wrong, God did not give up on him."},
    {"title": "The Lord Is My Shepherd", "storyId": "psalm23", "reference": "Psalm 51:1",
     "why": "After his sin, David poured out his sorrow in songs of repentance, some of the most honest prayers in the whole Bible."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Luke 15:21",
     "why": "Like the lost son who finally came home, David stopped hiding, admitted his sin, and found a Father ready to forgive."}
  ],
  "tier1": {
    "book": "2 Samuel 11–12",
    "hook": "David was a man after God's own heart. But even David did something terribly wrong, and then made it worse by trying to hide it. The question was what he would do when he was found out.",
    "story": [
      "David was the greatest king Israel had ever known, a man who loved God deeply. But the Bible never pretends its heroes are perfect. One day David made some very wrong and selfish choices. He took for himself something that was not his, and he badly hurt another person to do it.",
      "Then David did what people so often do after doing wrong. Instead of admitting it, he tried to cover it up. He arranged things so that no one would find out, and on the outside, it seemed to work. Life went on, and it looked like David had gotten away with it.",
      "But there was one who saw everything. God knew exactly what David had done, even the parts no person had seen. And because God loved David too much to leave him in his sin, he sent a brave prophet named Nathan to talk to the king.",
      "Nathan did not accuse David right away. Instead, he told him a story. \"There were two men in a city. One was rich and had huge flocks of sheep. The other was poor and had just one little lamb, which he loved like a member of his family. One day a traveler came to the rich man. But instead of taking a sheep from his own great flocks, the rich man stole the poor man's one little lamb.\"",
      "David was furious. \"As surely as the Lord lives,\" he burst out, \"the man who did this deserves to pay! He had no pity at all!\" Then Nathan looked the king straight in the eye and said four words David would never forget: \"You are that man.\"",
      "In that moment David saw himself clearly, and it broke him. He did not make excuses. He did not get angry at Nathan. He simply said, \"I have sinned against the Lord.\" And he meant it with all his heart.",
      "David was truly, deeply sorry, and he poured out his sorrow to God in honest prayers that people still pray today. \"Create in me a clean heart, O God. Wash me, and I will be clean.\" And God, who is full of mercy, forgave him. There were still sad consequences from what David had done, for our choices are real and they matter. But David was forgiven and restored.",
      "David's story is a hard one, but it holds wonderful news. Even the best of us do wrong. We cannot hide it from God, and we should not try. But when we stop hiding and tell God the truth, we find that he is ready to forgive."
    ],
    "devotional": {
      "bigIdea": "Even David, a man after God's own heart, sinned badly and then tried to hide it. But you cannot hide anything from God, and the wonderful truth is that you do not need to. When David finally stopped hiding and said, I have sinned, he found a God who was ready to forgive.",
      "questions": [
        "David tried to hide what he had done, but God saw it all. Why do you think we try to hide the wrong things we do?",
        "When Nathan said, you are that man, David did not make excuses. Why is it so hard, and so important, to admit when we are wrong?",
        "God forgave David completely. Is there something you need to stop hiding and tell God about, trusting that he will forgive you?"
      ]
    },
    "tags": ["confession", "forgiveness", "honesty", "repentance", "God's mercy"],
    "quiz": [
      {"question": "What did David do after he did something very wrong?", "options": ["He tried to hide it", "He told everyone right away", "He left the country"], "answer": 0, "explanation": ""},
      {"question": "Who saw what David had done, even though no person did?", "options": ["God", "The army", "Another king"], "answer": 0, "explanation": ""},
      {"question": "How did the prophet Nathan help David see his sin?", "options": ["He told him a story about a stolen lamb", "He shouted at him", "He wrote him a letter"], "answer": 0, "explanation": "When David got angry at the man in the story, Nathan said, you are that man."},
      {"question": "What did David say when he understood?", "options": ["I have sinned against the Lord", "It was not my fault", "Nothing at all"], "answer": 0, "explanation": ""},
      {"question": "What happened when David finally told God the truth?", "options": ["God forgave him", "God ignored him", "God made him stop being king that day"], "answer": 0, "explanation": "There were still sad results, but David was forgiven and restored."}
    ]
  },
  "tier2": {
    "book": "2 Samuel 11-12",
    "hook": "Even King David, who loved God, did something very wrong. Then he tried to hide it. But no one can hide from God.",
    "story": [
      "David was a great king who loved God very much. But one day, David made some very bad and selfish choices, and he hurt someone.",
      "After he did the wrong thing, David tried to keep it a secret. He hoped no one would ever find out.",
      "On the outside, it looked like nobody knew. But there was someone who saw everything David did.",
      "God knew. God sees all that we do, even the things we try to hide.",
      "But God loved David too much to leave him that way. So God sent a brave helper named Nathan to talk to David.",
      "Nathan told David a story about a rich man who stole a poor man's only little lamb. David got very angry. \"That is so unfair!\" he said.",
      "Then Nathan looked at David and said, \"You are that man.\" David suddenly saw what he had done.",
      "David did not make any excuses. He said, \"I have sinned against God.\" He was truly, deeply sorry.",
      "And God forgave David. God is always ready to forgive us when we are truly sorry.",
      "We cannot hide from God, and we do not need to. When we tell God we are sorry, he forgives us, just like he forgave David."
    ],
    "devotional": {
      "bigIdea": "Even David did something wrong and tried to hide it. But God sees everything. When David said he was sorry, God forgave him. God forgives us too when we tell him the truth.",
      "questions": [
        "Why do we sometimes try to hide it when we do something wrong?",
        "David said, I am sorry, and God forgave him. How does it feel to be forgiven?",
        "Is there something you can tell God you are sorry about, knowing he will forgive you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["confession", "forgiveness", "honesty"],
    "quiz": [
      {"question": "What did David try to do after he did wrong?", "options": ["Hide it", "Tell everyone", "Run away"], "answer": 0, "explanation": ""},
      {"question": "Who saw everything David did?", "options": ["God", "No one", "A lion"], "answer": 0, "explanation": ""},
      {"question": "What happened when David said he was sorry?", "options": ["God forgave him", "Nothing", "He had to leave"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "solomon-temple", "era": "kingdom", "emoji": "🏛️",
  "title": "Solomon Builds the Temple", "date": "c. 960 BC", "location": "Jerusalem",
  "connections": [
    {"title": "The Wisest Request", "storyId": "solomon-wisdom", "reference": "1 Kings 6:12",
     "why": "The same Solomon who asked God for wisdom now uses it to build the most beautiful house of worship the world had ever seen."},
    {"title": "Dancing Before the Lord", "storyId": "david-ark", "reference": "1 Kings 8:6",
     "why": "David brought the ark to Jerusalem in a tent, and now his son builds it a permanent home in the Temple's Most Holy Place."},
    {"title": "The Day Everything Changed", "storyId": "pentecost", "reference": "1 Corinthians 3:16",
     "why": "God's glory once filled the Temple, and at Pentecost his Spirit came to fill his people, who are now God's living temple."}
  ],
  "tier1": {
    "book": "1 Kings 5–8",
    "hook": "King David had dreamed of building a house for God. It was his son Solomon who finally built it, the most magnificent temple the world had ever seen.",
    "story": [
      "King David had always wanted to build a beautiful temple, a permanent house where God's people could come to worship. But God told David that his son would build it instead. So when David's son Solomon became king, he set out to build the most glorious temple the world had ever seen.",
      "It was an enormous task. Solomon gathered the finest cedar wood from the forests of Lebanon and the best stone from the quarries. Thousands and thousands of workers labored on it for seven long years.",
      "There was one beautiful detail. All the stones were cut and shaped far away, at the quarry, so that no hammer or chisel or any iron tool was ever heard at the temple site itself. The whole building rose up in perfect quiet, a house of worship built in peace.",
      "Inside, the temple glowed. The walls were lined with cedar carved with flowers and palm trees, and overlaid with pure gold. At the very center was the Most Holy Place, and there they brought the ark of the covenant, the golden chest that had traveled with God's people for so long. At last it had a permanent home.",
      "When everything was finished and the ark was set in place, a thick cloud filled the temple, the glory of the Lord, so bright and so powerful that the priests could not even stand up to do their work. God himself had come to fill his house.",
      "Then Solomon stood before all the people and prayed. He spread out his hands toward heaven and said something wonderfully humble. \"But will God really live here on earth? Look, the highest heavens cannot contain you, so how could this temple that I have built?\"",
      "Solomon understood that no building, no matter how golden and grand, could ever hold the God who made the universe. Yet in his kindness, God chose to meet his people there. And one day God would do something even greater. He would come to live not in a building of stone and gold, but inside his own people, making each of them a temple where his Spirit lives."
    ],
    "devotional": {
      "bigIdea": "Solomon built God the most beautiful temple imaginable, and yet he knew the whole universe could not contain God. The amazing thing is that this great God chooses to make his home with people. Today he lives not in a golden building, but in the hearts of those who love him.",
      "questions": [
        "The temple workers prepared everything so carefully and quietly. What does it look like to give God your very best?",
        "Solomon said even the highest heavens cannot contain God. What helps you remember how big and great God is?",
        "God now makes his home inside his people. What do you think it means that God wants to live with you?"
      ]
    },
    "tags": ["worship", "God's presence", "Solomon", "the Temple", "giving our best"],
    "quiz": [
      {"question": "Who built the great Temple in Jerusalem?", "options": ["Solomon", "David", "Moses"], "answer": 0, "explanation": "David wanted to, but God said his son Solomon would build it."},
      {"question": "How long did it take to build the Temple?", "options": ["Seven years", "Seven days", "One hundred years"], "answer": 0, "explanation": ""},
      {"question": "Why was no hammer or tool heard at the building site?", "options": ["The stones were shaped far away first", "Everyone was asleep", "They used no stone"], "answer": 0, "explanation": ""},
      {"question": "What filled the Temple when it was finished?", "options": ["A cloud of God's glory", "Rain", "Birds"], "answer": 0, "explanation": ""},
      {"question": "Where does God choose to live today?", "options": ["Inside his own people", "Only in golden buildings", "On a mountain"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "1 Kings 5-8",
    "hook": "King David dreamed of building a beautiful house for God. His son Solomon built it: the most amazing temple anyone had ever seen.",
    "story": [
      "King David had always wanted to build a special house for God, a place where everyone could come to worship.",
      "But God said that David's son would build it. So when Solomon became king, he started to build a wonderful temple for God.",
      "It was a huge job! Solomon used the best wood and the finest stone. Many, many workers helped, and it took seven whole years.",
      "Here is something amazing: the stones were all cut and shaped far away. So the temple was built without the sound of a single hammer at the site. It was quiet and peaceful.",
      "Inside, the temple was beautiful. The walls were covered with carvings of flowers and palm trees, and shining gold.",
      "In the very middle was the most special room. There they placed the ark, the golden chest. At last it had a forever home.",
      "When everything was done, a bright cloud filled the temple. It was the glory of God! God had come to fill his house.",
      "Then Solomon prayed, \"God, you are so big that even all of heaven cannot hold you. How wonderful that you would meet us here!\"",
      "Solomon knew that no building could ever hold the great big God who made everything.",
      "And here is the best part: today God comes to live right inside the hearts of people who love him. We get to be God's home!"
    ],
    "devotional": {
      "bigIdea": "Solomon built God a beautiful temple, but he knew nothing could hold our great big God. The wonderful news is that God now lives in the hearts of people who love him.",
      "questions": [
        "The workers gave their very best to build God's temple. How can you give God your best?",
        "God is bigger than all of heaven! What is something that helps you remember how great God is?",
        "God wants to live in our hearts. How does it feel that God wants to be close to you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["worship", "God's presence", "the Temple"],
    "quiz": [
      {"question": "Who built the great Temple?", "options": ["Solomon", "Noah", "Pharaoh"], "answer": 0, "explanation": ""},
      {"question": "What was special about how it was built?", "options": ["No hammer was heard at the site", "It was built in one day", "It was made of sand"], "answer": 0, "explanation": ""},
      {"question": "Where does God live today?", "options": ["In the hearts of people who love him", "Only in buildings", "On the moon"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "naboth", "era": "kingdom", "emoji": "⚖️",
  "title": "Naboth's Vineyard", "date": "c. 870 BC", "location": "Jezreel",
  "connections": [
    {"title": "Fire from Heaven", "storyId": "elijah", "reference": "1 Kings 21:17",
     "why": "It is the prophet Elijah whom God sends to stand up to wicked King Ahab and Queen Jezebel after they wrong Naboth."},
    {"title": "The Man Who Lost Everything", "storyId": "job", "reference": "Psalm 11:7",
     "why": "Like Job, Naboth is a good man treated unjustly, and the story reminds us that God sees and cares when people suffer wrongly."},
    {"title": "The Man Who Walked Away", "storyId": "rich-young-ruler", "reference": "1 Kings 21:4",
     "why": "King Ahab already had everything, yet he could not be happy without more, showing how wanting more and more can poison a heart."}
  ],
  "tier1": {
    "book": "1 Kings 21",
    "hook": "King Ahab had a whole kingdom, but he sulked like a child because of one thing he could not have: his neighbor's little vineyard. And his wicked queen was willing to do anything to get it for him.",
    "story": [
      "King Ahab of Israel had palaces and riches and power, but there was one small thing he wanted and did not have. Right next to his palace was a vineyard belonging to a man named Naboth, and Ahab wanted it for a vegetable garden.",
      "So Ahab offered to buy it or trade for it. But Naboth said no. \"This land has belonged to my family for generations,\" he explained. \"It is the inheritance God gave to my ancestors, and I cannot just sell it away.\" Naboth was not being stubborn. He was being faithful to what God had given his family.",
      "Ahab went home and sulked. He lay on his bed, turned his face to the wall, and refused to eat, all because he could not have one little vineyard. He had almost everything, and he was miserable over the one thing he could not get.",
      "His wife was the wicked Queen Jezebel, and she had no patience for this. \"Are you not the king?\" she sneered. \"Get up and eat. I will get you Naboth's vineyard myself.\"",
      "And Jezebel did a truly evil thing. She arranged for liars to falsely accuse Naboth of crimes he never committed, and because of those lies, innocent Naboth was put to death. Then Jezebel told Ahab the vineyard was his. Ahab asked no questions and went down to take it.",
      "But there was one who had seen the whole thing. God sent the prophet Elijah to meet Ahab right there in the stolen vineyard. \"This is what the Lord says,\" Elijah declared. \"Have you murdered a man and seized his land?\" Ahab's secret sin was dragged into the light, and God promised that such wickedness would not go unanswered.",
      "Naboth had no army and no power to defend himself. But he was never truly alone, because God saw everything, and God cared. Our God is a God of justice. He sees when the powerful hurt the weak, and he does not forget the ones the world tramples on."
    ],
    "devotional": {
      "bigIdea": "Ahab had nearly everything and was still unhappy because he wanted more. Poor Naboth had no power to protect himself. But God saw the whole thing, and God cared. Our God notices when people are treated unfairly, and he is always on the side of justice.",
      "questions": [
        "Ahab had so much, yet he was miserable over one thing he could not have. Why is wanting more and more such a hard trap to escape?",
        "Naboth had no one powerful to stand up for him, but God saw everything. How does it feel to know God sees when things are unfair?",
        "God cares deeply about justice. Is there someone being treated unfairly that you could stand up for or pray for?"
      ]
    },
    "tags": ["justice", "greed", "God sees", "courage", "fairness"],
    "quiz": [
      {"question": "What did King Ahab want that he could not have?", "options": ["Naboth's vineyard", "A bigger crown", "A faster horse"], "answer": 0, "explanation": ""},
      {"question": "Why would Naboth not sell his vineyard?", "options": ["It was his family's inheritance from God", "It was full of gold", "He did not like the king"], "answer": 0, "explanation": ""},
      {"question": "What did King Ahab do when he could not have it?", "options": ["He sulked and refused to eat", "He went on a trip", "He forgot about it"], "answer": 0, "explanation": ""},
      {"question": "Who did God send to confront Ahab?", "options": ["The prophet Elijah", "King David", "Samuel"], "answer": 0, "explanation": ""},
      {"question": "What does this story teach about God?", "options": ["He sees injustice and cares about the weak", "He does not notice what happens", "He only helps kings"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "1 Kings 21",
    "hook": "A king already had everything, but he wanted his neighbor's little garden too. When he could not have it, a very unfair thing happened. But God was watching.",
    "story": [
      "King Ahab had a big palace and lots of riches. But there was one little thing he wanted: a vineyard, like a garden, that belonged to his neighbor Naboth.",
      "Ahab said, \"Naboth, sell me your vineyard.\" But Naboth said, \"I am sorry, but this land belongs to my family. God gave it to us, so I cannot sell it.\"",
      "Ahab was so upset that he went to his room, lay on his bed, and would not even eat. He had almost everything, but he pouted about the one thing he could not have.",
      "Ahab's wife was a wicked queen named Jezebel. She said, \"You are the king! I will get you that vineyard.\"",
      "Then Jezebel did a very wicked thing. She told lies about Naboth, and because of those lies, poor Naboth was treated very unfairly and lost his life.",
      "Then Jezebel told Ahab, \"Now the vineyard is yours.\" So Ahab went to take it, as if nothing was wrong.",
      "But Someone had seen the whole thing. God saw everything that happened to Naboth.",
      "God sent the prophet Elijah to King Ahab. \"You did a very wicked thing,\" Elijah said. \"God saw it all.\"",
      "Naboth had no one strong to protect him. But God saw, and God cared about him.",
      "Our God always sees when people are treated unfairly, and he cares about everyone, especially those who need help."
    ],
    "devotional": {
      "bigIdea": "Ahab had so much but still wanted more. Naboth was treated unfairly, but God saw everything and cared. God always sees when things are unfair, and he cares about people who need help.",
      "questions": [
        "Ahab had so much but was sad about one thing. Why is it good to be thankful for what we have?",
        "God saw what happened to Naboth. How does it feel to know God sees when things are unfair?",
        "God cares about people who are treated unfairly. How can you be kind and fair to others?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["justice", "God sees", "fairness"],
    "quiz": [
      {"question": "What did King Ahab want from his neighbor?", "options": ["His vineyard", "His crown", "His horse"], "answer": 0, "explanation": ""},
      {"question": "Why would Naboth not sell it?", "options": ["It was his family's land from God", "It was haunted", "It was too small"], "answer": 0, "explanation": ""},
      {"question": "What did God do about the unfair thing?", "options": ["He saw it and sent Elijah to speak up", "He did nothing", "He gave Ahab more land"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "naaman", "era": "kingdom", "emoji": "🌊",
  "title": "Naaman and the Servant Girl", "date": "c. 850 BC", "location": "The Jordan River",
  "connections": [
    {"title": "The Bronze Snake", "storyId": "bronze-serpent", "reference": "2 Kings 5:14",
     "why": "Like the people who only had to look at the snake, Naaman only has to do something simple, wash in the river, and trust God to heal him."},
    {"title": "God Looks at the Heart", "storyId": "david-anointed", "reference": "2 Kings 5:3",
     "why": "God uses a young, captured servant girl that the world would overlook to point a great general to healing."},
    {"title": "Jesus Heals the Ten Lepers", "storyId": "ten-lepers", "reference": "Luke 4:27",
     "why": "Naaman is healed of the same disease Jesus would later heal, and like the one grateful leper, Naaman comes back to give thanks."}
  ],
  "tier1": {
    "book": "2 Kings 5",
    "hook": "Naaman was a mighty general, strong and respected, with one terrible problem he could not fix. And the person who pointed him to healing was the last person anyone would expect: a young slave girl.",
    "story": [
      "Naaman was the commander of the whole army of Aram, a powerful and respected man. But Naaman had a dreadful skin disease called leprosy, and all his power and money could not cure it.",
      "In Naaman's house was a young servant girl from Israel, captured in a raid and taken far from home. She could have stayed silent and bitter. Instead, she said kindly to Naaman's wife, \"I wish my master would go to the prophet who is in Israel. He could heal him.\" That little girl's words set everything in motion.",
      "So Naaman traveled all the way to Israel, to the house of the prophet Elisha, with horses and chariots and piles of treasure. He expected an important man like himself to be greeted with a grand ceremony. Instead, Elisha did not even come out. He just sent a messenger to the door with a simple instruction: \"Go, wash yourself seven times in the Jordan River, and you will be healed.\"",
      "Naaman was furious. \"I thought he would at least come out and wave his hand and call on his God! And the Jordan? It is a muddy little river. We have far better rivers back home. Why should I wash in that?\" He turned and stormed off in a rage.",
      "But Naaman's servants gently reasoned with him. \"Master,\" they said, \"if the prophet had told you to do some great and difficult thing, you would have done it gladly. So why not do this simple thing he asked, and just wash?\"",
      "Naaman swallowed his pride. He went down to the Jordan and dipped himself under the water once, twice, again and again, seven times, just as the prophet had said. And when he came up the seventh time, his skin was completely healed, fresh and new like the skin of a young child.",
      "Naaman went back to Elisha a changed man. \"Now I know,\" he declared, \"that there is no God in all the world except the God of Israel.\" The proud general had been humbled, healed, and best of all, he had come to know the one true God. And it all began because one little servant girl was brave and kind enough to speak."
    ],
    "devotional": {
      "bigIdea": "Naaman almost missed his healing because it was too simple and not grand enough for him. God often works through small, humble things: a simple act of obedience, a few words from a servant girl. We just have to be humble enough to trust him.",
      "questions": [
        "Naaman wanted something grand and was angry that the cure was so simple. Why is it sometimes hard to trust the simple thing God asks us to do?",
        "A young servant girl, far from home, started it all by speaking up kindly. How might God use you, even when you feel small or unimportant?",
        "Naaman had to let go of his pride to be healed. What is something pride sometimes keeps us from doing?"
      ]
    },
    "tags": ["humility", "healing", "obedience", "God uses the small", "pride"],
    "quiz": [
      {"question": "What was Naaman's big problem?", "options": ["A skin disease called leprosy", "He had no money", "He could not fight"], "answer": 0, "explanation": ""},
      {"question": "Who told Naaman about the prophet who could heal him?", "options": ["A young servant girl from Israel", "The king", "His army"], "answer": 0, "explanation": "God used someone small and overlooked to point him to healing."},
      {"question": "What did Elisha tell Naaman to do?", "options": ["Wash seven times in the Jordan River", "Pay a lot of gold", "Climb a mountain"], "answer": 0, "explanation": ""},
      {"question": "Why was Naaman angry at first?", "options": ["The cure seemed too simple and not grand enough", "It was too expensive", "It was too far"], "answer": 0, "explanation": ""},
      {"question": "What happened when Naaman finally obeyed?", "options": ["He was completely healed and believed in God", "Nothing happened", "He got worse"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "2 Kings 5",
    "hook": "Naaman was a strong, important general, but he was very sick. A kind servant girl knew just where he could find help.",
    "story": [
      "Naaman was the leader of a great big army. He was strong and important. But Naaman had a bad skin sickness that no one could fix.",
      "A young servant girl from Israel lived in Naaman's house. She was kind, and she said, \"There is a prophet in Israel who could make my master well!\"",
      "So Naaman traveled all the way to Israel to find the prophet Elisha. He brought horses and chariots and lots of treasure.",
      "But Elisha did not even come outside. He just sent a message: \"Go wash in the Jordan River seven times, and you will be all better.\"",
      "Naaman was angry! \"I thought he would do something big and fancy! And the Jordan is just a muddy little river!\" He started to stomp away.",
      "But his servants said kindly, \"Master, if he had asked you to do something hard, you would do it. So why not try this simple thing?\"",
      "So Naaman went to the river. He dipped under the water one, two, three times, all the way to seven times, just as Elisha said.",
      "When he came up the seventh time, his skin was all better! It was healthy and new, like a little child's skin.",
      "Naaman was so happy and thankful. \"Now I know that the God of Israel is the only true God!\" he said.",
      "And it all started because one little servant girl was brave and kind enough to speak up. God can use anyone, even you!"
    ],
    "devotional": {
      "bigIdea": "Naaman almost missed being healed because the cure seemed too simple. God used a little servant girl to help him. God can use anyone, even when they feel small, and he just wants us to trust him.",
      "questions": [
        "Naaman wanted something fancy, but God's way was simple. Why is it good to trust what God asks, even when it seems simple?",
        "A young servant girl helped a great general. How might God use you to help others?",
        "Naaman had to stop being proud. What is something it is good to ask for help with?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["humility", "healing", "God uses the small"],
    "quiz": [
      {"question": "What was wrong with Naaman?", "options": ["He had a skin sickness", "He was lost", "He was poor"], "answer": 0, "explanation": ""},
      {"question": "Who told him where to find help?", "options": ["A young servant girl", "A king", "A soldier"], "answer": 0, "explanation": ""},
      {"question": "What did Naaman have to do to be healed?", "options": ["Wash in the river seven times", "Pay gold", "Fight a battle"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-03b.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-03b.json with {len(batch)} stories.")
