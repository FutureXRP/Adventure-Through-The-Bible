#!/usr/bin/env python3
"""Authoring source for Batch 1 (the Jacob trilogy). Writes batch-01.json."""
import json

batch = [
{
  "id": "jacob-esau", "era": "patriarchs", "emoji": "🍲",
  "title": "The Stolen Blessing", "date": "c. 1900 BC", "location": "Canaan",
  "connections": [
    {"title": "A Promise as Big as the Stars", "storyId": "abraham", "reference": "Genesis 28:13",
     "why": "The blessing Jacob fought for was the very promise God first made to his grandfather Abraham, handed down through the family."},
    {"title": "Jacob's Ladder", "storyId": "jacob-ladder", "reference": "Genesis 28:15",
     "why": "Running for his life, Jacob meets God in the wilderness, who promises to stay with the very schemer who just lied to his father."},
    {"title": "The Dreamer's Long Road", "storyId": "joseph", "reference": "Genesis 37:3",
     "why": "Jacob grew up in a home with a favorite son, and sadly he repeated it with his own boys, loving Joseph best of all."}
  ],
  "tier1": {
    "book": "Genesis 25, 27",
    "hook": "Two brothers, one blessing, and a bowl of stew. Jacob wanted what belonged to Esau so badly that he was willing to lie to his own blind father to get it.",
    "story": [
      "Isaac married Rebekah, and for a long time they had no children. Isaac prayed, and at last Rebekah learned she was going to have a baby. But inside her there were two, and the babies struggled so hard against each other that she cried out to God. The Lord told her, \"There are two nations inside you. Two peoples will come from you, and one will be stronger than the other. And here is the surprising part: the older will serve the younger.\"",
      "The first baby came out red and covered with hair, and they named him Esau. Then his brother came out gripping Esau's heel, as if he were trying to pull his way to the front, and they named him Jacob, which means grabber. The boys grew up very different. Esau loved the open country and became a skillful hunter, and his father Isaac loved him best. Jacob was quiet and stayed near the tents, and his mother Rebekah loved him best.",
      "One day Esau came in from the fields starving, and Jacob was cooking a pot of thick red stew. \"Quick, let me have some of that red stew,\" Esau said. \"I am about to die of hunger.\" Jacob saw his chance. \"First sell me your birthright,\" he said, meaning the special double share and blessing that belonged to the oldest son. \"What good is a birthright if I starve to death?\" said Esau, and he swore it away for a single bowl of soup. He ate, got up, and walked off, and just like that he threw away the greatest gift he had.",
      "Years passed. Isaac grew old, and his eyes became so weak that he could no longer see. He called Esau and said, \"I am old now. Take your bow, hunt some wild game, and make me the tasty food I love. Then I will give you my blessing before I die.\" Rebekah was listening. The moment Esau left to hunt, she ran to Jacob. \"Do exactly what I say,\" she told him. \"Bring me two young goats, and I will cook the food your father loves. You will carry it to him, and he will bless you instead of your brother.\"",
      "\"But Esau is hairy and I am smooth,\" Jacob said. \"If father touches me, he will know I am tricking him, and I will get a curse instead of a blessing.\" So Rebekah covered his arms and his neck with the goat skins, dressed him in Esau's best clothes, and put the food in his hands. Jacob went in to his father. \"Who are you, my son?\" Isaac asked. \"I am Esau,\" Jacob lied. Isaac was puzzled. \"The voice is the voice of Jacob,\" he said, \"but the hands are the hands of Esau.\" He touched the skins, he smelled the clothes, and at last he was fooled, and he gave Jacob the great blessing: \"May God give you the dew of heaven and the riches of the earth. May nations bow down to you, and may everyone who blesses you be blessed.\"",
      "Jacob had barely stepped out when Esau came back from the hunt with his father's favorite food. \"Father, sit up and eat,\" he said. Isaac began to tremble. \"Then who was it that already came and brought me food? I have blessed him, and the blessing will stand.\" Esau let out a loud and bitter cry. \"Bless me too, father, me also!\" But the blessing was already gone. Esau hated his brother for stealing it, and he said in his heart, \"When our father has died, I am going to kill Jacob.\"",
      "When Rebekah heard what Esau was planning, she sent for Jacob at once. \"Your brother is comforting himself with the thought of killing you,\" she warned. \"Run away to my brother Laban, far away in Haran, and stay there until your brother's anger cools down.\" So Jacob, who had grabbed and schemed and lied his way to the blessing, left home with almost nothing, running for his life into a strange and faraway land.",
      "Jacob had wanted that blessing more than anything in the world, and now he had it. But it had cost him his brother, his home, and every comfort he had ever known. The promise God had made to his grandfather Abraham would still come true through Jacob one day, not because Jacob earned it or deserved it, but because God is faithful even to people who are not."
    ],
    "devotional": {
      "bigIdea": "Jacob wanted God's blessing so badly that he lied and cheated to get it. He won the blessing, but it cost him his home and his brother. Here is the wonder of the story: God still kept his promise to Jacob anyway, not because Jacob was good, but because God is faithful even to people who are not.",
      "questions": [
        "Esau gave away something precious for a single meal because he wanted it right now. When is it hard for you to wait for something good?",
        "Jacob got what he wanted by lying, but it hurt the people he loved most. Can you think of a time when getting your way did not feel as good as you thought it would?",
        "God kept his promise to Jacob even though Jacob did wrong. What does that tell you about the way God loves you?"
      ]
    },
    "tags": ["family", "choices", "God's promises", "consequences", "grace"],
    "quiz": [
      {"question": "What did Esau trade away for a bowl of stew?", "options": ["His birthright", "His bow and arrows", "His father's tent"], "answer": 0, "explanation": "The birthright was the oldest son's special gift, and Esau gave it away for one meal."},
      {"question": "Why could Isaac not tell that Jacob was tricking him?", "options": ["It was dark outside", "He was old and could not see", "Jacob was wearing a mask"], "answer": 1, "explanation": ""},
      {"question": "How did Jacob make his smooth arms feel like Esau's?", "options": ["He rubbed them with mud", "He covered them with goat skins", "He wore long gloves"], "answer": 1, "explanation": ""},
      {"question": "What did Jacob have to do after he stole the blessing?", "options": ["Give it back to Esau", "Run far away from home", "Become a hunter"], "answer": 1, "explanation": ""},
      {"question": "The great blessing was really the promise God first made to whom?", "options": ["Abraham", "Moses", "Noah"], "answer": 0, "explanation": "God's promise passed from Abraham to Isaac, and now it came to Jacob."}
    ]
  },
  "tier2": {
    "book": "Genesis 25, 27",
    "hook": "Esau was born first, so the big blessing belonged to him. But his brother Jacob wanted it, and he came up with a sneaky plan to get it.",
    "story": [
      "Isaac and Rebekah had twin boys. The first one came out red and hairy, and they named him Esau. The second one came out holding on to his brother's heel, and they named him Jacob. Esau loved to hunt outside. Jacob liked to stay near home. They were brothers, but they were very different.",
      "Because Esau was born first, he had something special called the birthright. It meant that one day he would get the biggest gift and the special blessing from his father.",
      "One day Esau came home very hungry. Jacob was cooking a pot of red stew. \"Please give me some!\" said Esau. Jacob said, \"First give me your birthright.\" Esau was so hungry that he said yes, just for a bowl of soup. He gave away his special gift without even thinking about it.",
      "Many years later, their father Isaac was very old, and he could not see anymore. He wanted to give his big blessing to Esau. But Rebekah wanted Jacob to have it instead. So she made a plan.",
      "She cooked Isaac's favorite food. She put goat skins on Jacob's smooth arms so they would feel hairy like Esau's. Then Jacob went to his father and said, \"I am Esau.\" Isaac could not see, so he believed him, and he gave Jacob the big blessing.",
      "When Esau found out what had happened, he was very sad and very angry. He was so angry that Jacob had to run far away to keep safe.",
      "Jacob did a wrong thing when he tricked his father, and it made his whole family sad. But God was not finished with Jacob. Even when we make a mess, God still keeps his promises and never gives up on us."
    ],
    "devotional": {
      "bigIdea": "Jacob tricked his father to get the blessing, and it made his family very sad. But God did not give up on Jacob. God keeps his promises even when we make mistakes.",
      "questions": [
        "Esau gave away something special just because he was hungry right now. What is something good that is worth waiting for?",
        "How do you think Esau felt when he found out about the trick?",
        "Even when we do something wrong, God still loves us. How does that make you feel?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["family", "choices", "God's promises"],
    "quiz": [
      {"question": "Esau traded his special birthright for what?", "options": ["A bowl of stew", "A new bow", "A baby goat"], "answer": 0, "explanation": ""},
      {"question": "Isaac could not see Jacob's trick because he was?", "options": ["Sleeping", "Old and could not see", "Too busy eating"], "answer": 1, "explanation": ""},
      {"question": "After he tricked his father, Jacob had to do what?", "options": ["Say he was sorry", "Run far away", "Go hunting"], "answer": 1, "explanation": ""}
    ]
  }
},
{
  "id": "jacob-ladder", "era": "patriarchs", "emoji": "🪜",
  "title": "Jacob's Ladder", "date": "c. 1900 BC", "location": "Bethel",
  "connections": [
    {"title": "The Stolen Blessing", "storyId": "jacob-esau", "reference": "Genesis 28:10",
     "why": "Jacob is on the run because of the blessing he stole, and God meets him anyway with grace he never earned."},
    {"title": "A New Name", "storyId": "jacob-wrestles", "reference": "Genesis 32:24",
     "why": "Twenty years later God meets Jacob again, this time face to face, and gives the schemer a brand new name."},
    {"title": "A Promise as Big as the Stars", "storyId": "abraham", "reference": "Genesis 28:14",
     "why": "God repeats to Jacob the very promise he made to Abraham, that through this family every nation on earth would be blessed."}
  ],
  "tier1": {
    "book": "Genesis 28",
    "hook": "Jacob ran from home with nothing, a thief carrying a stolen blessing and a brother who wanted him dead. That night, in the middle of nowhere, heaven opened right above his head.",
    "story": [
      "Jacob ran. He had stolen his brother's blessing, and now Esau wanted him dead, so Jacob left everything behind and set out alone across the wilderness toward a far country where his uncle lived. He had no servants, no tent, and no comfort, nothing but the long road and the wide open sky.",
      "When the sun went down, Jacob stopped in an empty place. There was no bed and no pillow, so he took a stone, rested his head on it, and lay down to sleep under the stars. He was a runaway with a guilty heart, as alone as a person can be.",
      "And then he dreamed. He saw a great stairway resting on the earth, with its top reaching all the way up into heaven. On the stairway the angels of God were going up and coming down, up and down between heaven and earth. And there at the very top stood the Lord himself.",
      "God spoke to him. \"I am the Lord, the God of your grandfather Abraham and the God of your father Isaac. The ground you are lying on, I will give to you and to your children. Your family will spread out like the dust of the earth, and through you every family on earth will be blessed.\"",
      "Then God said the very thing Jacob needed most to hear. \"Look, I am with you. I will watch over you wherever you go, and I will bring you back to this land. I will not leave you until I have done everything I have promised you.\" A guilty runaway lay in the dirt, and God promised never to leave his side.",
      "Jacob woke up with his heart pounding. \"The Lord is in this place,\" he said, \"and I did not even know it.\" He was filled with wonder and a little fear. \"How awesome this place is. This is none other than the house of God. This is the very gate of heaven.\"",
      "Early in the morning Jacob took the stone he had slept on, stood it up like a marker, and poured oil over the top to set it apart for God. He named the place Bethel, which means house of God. And he made a promise of his own: \"If God will be with me and watch over me and bring me safely home, then the Lord will be my God.\"",
      "Jacob had done nothing to deserve a visit from heaven. He was running away from the mess he had made of his family. But God came to him anyway, in the loneliest place, on the worst night of his life, and promised to stay with him. That is the kind of God he is."
    ],
    "devotional": {
      "bigIdea": "Jacob was a runaway who had cheated his own family, and he had every reason to think God was finished with him. Instead God came down to him in the loneliest place and promised, I am with you, and I will never leave you. God does not wait for us to be good enough. He comes to us right in the middle of our mess.",
      "questions": [
        "Jacob felt completely alone, but God was right there with him. When do you feel alone, and what would it mean to remember that God is with you?",
        "God came to Jacob even though Jacob had done something wrong. Why do you think God did that?",
        "Jacob set up a stone to help him remember the night he met God. What helps you remember the good things God has done?"
      ]
    },
    "tags": ["God's presence", "loneliness", "grace", "God's promises", "worship"],
    "quiz": [
      {"question": "Why was Jacob running away from home?", "options": ["He wanted to see the world", "His brother Esau was angry enough to kill him", "He was searching for treasure"], "answer": 1, "explanation": ""},
      {"question": "What did Jacob use for a pillow?", "options": ["A bag of clothes", "A stone", "A bundle of grass"], "answer": 1, "explanation": ""},
      {"question": "What did Jacob see in his dream?", "options": ["A burning bush", "A stairway between earth and heaven", "A great flood"], "answer": 1, "explanation": ""},
      {"question": "What did God promise Jacob?", "options": ["That he would be rich", "That he was with him and would bring him home", "That he would become a king"], "answer": 1, "explanation": "God said, I am with you, and I will not leave you until I have done all I have promised."},
      {"question": "What did Jacob name the place?", "options": ["Bethel, the house of God", "Eden", "Jerusalem"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Genesis 28",
    "hook": "Jacob was all alone, far from home, with a stone for a pillow. Then he had a dream that showed him heaven was closer than he ever imagined.",
    "story": [
      "Jacob was running away from home because his brother was very angry with him. He walked a long, long way, all by himself, until the sun went down.",
      "There was no bed out in the wild country. So Jacob found a stone, put his head on it like a pillow, and went to sleep under the stars. He felt very alone.",
      "That night Jacob had an amazing dream. He saw a giant stairway that went all the way from the ground up into heaven. Angels were going up and coming down on it.",
      "At the very top stood God. And God said, \"I am with you. I will take care of you everywhere you go, and I will bring you back home. I will never leave you.\"",
      "When Jacob woke up, he was amazed. \"God is in this place,\" he said, \"and I did not even know it!\"",
      "Jacob took his stone pillow and stood it up tall to help him remember. He named the place Bethel, which means the house of God.",
      "Jacob had thought he was all alone. But God was right there with him the whole time. Even when you feel alone, God is closer than you know."
    ],
    "devotional": {
      "bigIdea": "Jacob felt all alone, but God was right there with him, and God promised to never leave him. God is with you too, even when you cannot see him.",
      "questions": [
        "When is a time you have felt alone? How does it help to know that God is with you?",
        "What was the most amazing part of Jacob's dream to you?",
        "Jacob set up a stone to remember God. What is something that helps you remember God loves you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God's presence", "loneliness", "God's promises"],
    "quiz": [
      {"question": "What did Jacob use for a pillow?", "options": ["A stone", "A pillow of feathers", "His shoes"], "answer": 0, "explanation": ""},
      {"question": "In his dream, Jacob saw a stairway going up to where?", "options": ["A mountain", "Heaven", "A castle"], "answer": 1, "explanation": ""},
      {"question": "What did God promise Jacob?", "options": ["He would be rich", "He would always be with him", "He would win every race"], "answer": 1, "explanation": ""}
    ]
  }
},
{
  "id": "jacob-wrestles", "era": "patriarchs", "emoji": "🌅",
  "title": "A New Name", "date": "c. 1880 BC", "location": "Peniel, by the Jabbok River",
  "connections": [
    {"title": "Jacob's Ladder", "storyId": "jacob-ladder", "reference": "Genesis 32:9",
     "why": "Years earlier God promised at Bethel to bring Jacob home safely, and now Jacob holds God to that very promise on the way back."},
    {"title": "The Stolen Blessing", "storyId": "jacob-esau", "reference": "Genesis 32:11",
     "why": "The brother Jacob cheated is finally right in front of him, and the cheater has to face the past he ran away from."},
    {"title": "The Dreamer's Long Road", "storyId": "joseph", "reference": "Genesis 35:10",
     "why": "Jacob, now named Israel, becomes the father of the sons whose families grow into the twelve tribes of Israel."}
  ],
  "tier1": {
    "book": "Genesis 32",
    "hook": "After twenty years away, Jacob was finally going home, straight toward the brother he had cheated. The night before they met, a stranger stepped out of the dark and wrestled him until dawn.",
    "story": [
      "Twenty years had passed. Jacob had married, raised a big family, and grown rich with flocks and herds. But now God had told him to go home, and going home meant one terrifying thing. It meant facing Esau, the brother he had cheated, the brother who had once promised to kill him.",
      "Jacob sent messengers ahead, and they came back with news that made his heart sink. \"Esau is coming to meet you, and he has four hundred men with him.\" Jacob was terrified. He split his family into two groups, so that if Esau attacked one, the other might escape. Then he sent ahead a huge gift of hundreds of animals, hoping somehow to soften his brother's anger.",
      "That night Jacob sent everyone across the river, and he stayed behind all alone. And in the dark, a man came and began to wrestle with him. They struggled all night long, neither one giving up, straining against each other hour after hour until the sky began to turn gray.",
      "When the man saw that he could not win, he reached out and simply touched Jacob's hip, and with that one touch he wrenched it out of joint. Still Jacob would not let go. \"Let me go,\" the man said, \"for the sun is coming up.\" But Jacob held on with everything he had left. \"I will not let you go,\" he gasped, \"unless you bless me.\"",
      "\"What is your name?\" the man asked. \"Jacob,\" he answered. And the name meant grabber, cheater, the one who takes what is not his. Saying it out loud was a kind of confession. For the first time in his life, Jacob told the plain truth about who he had been.",
      "\"Your name will no longer be Jacob,\" the man said. \"From now on you will be called Israel, which means he struggles with God, because you have struggled with God and with people, and you have not given up.\" And Jacob suddenly understood who he had been wrestling all night long. \"Please, tell me your name,\" he begged. But the man only blessed him there and was gone.",
      "Jacob named the place Peniel, which means the face of God. \"I have seen God face to face,\" he said, \"and yet my life was spared.\" As the sun rose over the river, Jacob walked on toward his brother. And he was limping.",
      "Jacob had spent his whole life grabbing, for the birthright, for the blessing, for anything he could get his hands on. But that night he finally stopped grabbing and held on to God instead, begging to be blessed. God gave him a new name and a limp he would feel forever, so that he would never forget the night the cheater met God and was changed."
    ],
    "devotional": {
      "bigIdea": "Jacob spent his whole life grabbing for things that were not his. But on his most frightening night, he finally stopped grabbing and held on to God instead, refusing to let go until God blessed him. God gave him a new name and a limp to remember it by. Sometimes God lets us struggle, not to hurt us, but to change us.",
      "questions": [
        "Jacob held on to God and would not let go. What does it look like to hold on to God when life is hard?",
        "God gave Jacob a limp he would feel forever so he would always remember that night. Why might a reminder like that be a gift and not just a hard thing?",
        "God gave Jacob a brand new name and a fresh start. If God gave you a name that told the truth about who he is making you to be, what do you hope it would say?"
      ]
    },
    "tags": ["transformation", "prayer", "perseverance", "identity", "God's presence"],
    "quiz": [
      {"question": "Why was Jacob so afraid to go home?", "options": ["He had forgotten the way", "He had to face Esau, the brother he had cheated", "He owed someone money"], "answer": 1, "explanation": ""},
      {"question": "Who wrestled with Jacob in the dark?", "options": ["Esau", "A robber", "A man who was really God"], "answer": 2, "explanation": ""},
      {"question": "What happened to Jacob's hip during the struggle?", "options": ["Nothing at all", "It was wrenched out of joint", "It was healed"], "answer": 1, "explanation": ""},
      {"question": "What did Jacob ask for before he would let go?", "options": ["A blessing", "A pile of gold", "A new home"], "answer": 0, "explanation": ""},
      {"question": "What new name did God give Jacob?", "options": ["Abraham", "Israel", "Peter"], "answer": 1, "explanation": "Israel means he struggles with God, and the whole nation would be named after him."}
    ]
  },
  "tier2": {
    "book": "Genesis 32",
    "hook": "Jacob was going home at last, but he was scared to see his brother Esau. Alone in the dark, a mysterious man began to wrestle with him all night long.",
    "story": [
      "Jacob was finally going back home after many years away. But he was very scared, because he had to see his brother Esau, and the last time, Esau had been so very angry.",
      "The night before they would meet, Jacob sent his family across the river. He stayed behind all by himself in the dark.",
      "Then a man came and started to wrestle with Jacob. They wrestled and wrestled, all night long, and neither one would give up.",
      "When morning was almost there, the man said, \"Let me go.\" But Jacob held on tight. \"I will not let go,\" he said, \"until you bless me.\"",
      "The man asked, \"What is your name?\" \"Jacob,\" he said. Then the man said, \"Your new name is Israel, because you have struggled with God and you kept holding on.\"",
      "Then Jacob knew something amazing. He had been wrestling with God! He named that place Peniel, and he said, \"I have seen God face to face.\"",
      "When the sun came up, Jacob walked toward his brother, and he was limping. Jacob had stopped grabbing for things, and now he held on tight to God instead."
    ],
    "devotional": {
      "bigIdea": "Jacob held on to God all night and would not let go until God blessed him. God gave him a new name and a new start. God can change us, even when life is a struggle.",
      "questions": [
        "Jacob held on tight to God. What are some ways you can hold on to God when you are scared?",
        "How do you think Jacob felt when God gave him a brand new name?",
        "God gave Jacob a fresh start. Is there something you would like a fresh start with?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["transformation", "perseverance", "identity"],
    "quiz": [
      {"question": "Jacob was scared to go home because he had to see whom?", "options": ["A lion", "His brother Esau", "A king"], "answer": 1, "explanation": ""},
      {"question": "Who did Jacob wrestle with all night?", "options": ["A man who was really God", "His brother", "A friend"], "answer": 0, "explanation": ""},
      {"question": "What new name did God give him?", "options": ["Israel", "Adam", "David"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-01.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-01.json with {len(batch)} stories.")
