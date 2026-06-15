#!/usr/bin/env python3
"""Authoring source for Batch 3a (Kingdom, part 1). Writes batch-03a.json."""
import json

batch = [
{
  "id": "hannah", "era": "kingdom", "emoji": "🙏",
  "title": "Hannah's Prayer", "date": "c. 1100 BC", "location": "Shiloh",
  "connections": [
    {"title": "Speak, Lord", "storyId": "samuel", "reference": "1 Samuel 1:20",
     "why": "The son God gives Hannah is Samuel, who grows up to hear God's voice and anoint Israel's first kings."},
    {"title": "Impossible News", "storyId": "annunciation", "reference": "Luke 1:46",
     "why": "Hannah's song of praise, that God lifts up the lowly and fills the hungry, is echoed centuries later in Mary's song."},
    {"title": "The Upside-Down Kingdom", "storyId": "sermon-mount", "reference": "1 Samuel 2:8",
     "why": "Hannah sings that God raises the poor from the dust, the same upside-down kingdom Jesus would teach about on the mountain."}
  ],
  "tier1": {
    "book": "1 Samuel 1–2",
    "hook": "Year after year, Hannah longed for a child and had none. So she went to God's house and poured out her heart in a prayer so quiet that only God could hear it.",
    "story": [
      "There was a woman named Hannah who loved God and wanted, more than anything in the world, to have a child. But year after year went by, and Hannah had no children, and it made her deeply sad. To make it worse, another woman in her household teased her about it and would not let her forget.",
      "Every year Hannah's family traveled to the house of God at Shiloh to worship. One year Hannah was so full of sorrow that she could not even eat. Her husband loved her dearly, but he could not fill the empty place in her heart. So Hannah went to the house of God by herself.",
      "There she wept and prayed from the very bottom of her heart. \"Lord,\" she promised, \"if you will give me a son, I will give him right back to you. He will belong to you and serve you his whole life long.\" She prayed silently, her lips moving but no sound coming out, pouring out all her pain to God.",
      "Eli the priest was watching, and he thought she had had too much wine. \"How long will you keep on like this?\" he said. \"No,\" Hannah answered, \"I have not been drinking. I am a woman who is deeply troubled, and I am pouring out my soul to the Lord.\" Eli's face softened. \"Go in peace,\" he said, \"and may God give you what you have asked of him.\"",
      "Hannah went home, and this time she ate, and her sadness lifted. She did not yet have anything in her arms, but she had given her heavy load to God, and she trusted him with it.",
      "And God remembered Hannah. In time she had a baby boy, and she named him Samuel, which sounds like the words, I asked the Lord for him. She was overjoyed.",
      "But Hannah did not forget her promise. When Samuel was still very young, she brought him to the house of God and gave him to Eli to be raised in God's service. \"I prayed for this child,\" she said, \"and now I give him to the Lord for his whole life.\" It must have been so hard, yet she trusted God with the very gift she had begged for.",
      "Then Hannah sang a song that bubbled up out of her joy. \"My heart rejoices in the Lord! There is no one holy like him.\" She sang that God lifts up the poor and fills the hungry and remembers the forgotten. Many years later, a young woman named Mary would sing almost the very same song when God chose her to be the mother of Jesus."
    ],
    "devotional": {
      "bigIdea": "Hannah did not hide her sadness or pretend she was fine. She poured out her whole heart to God, and then she trusted him with it. And when God gave her the gift she had longed for, she gave it right back to him. God loves it when we bring him our deepest hopes and hurts.",
      "questions": [
        "Hannah told God exactly how sad she was. Why do you think it helps to tell God how we really feel?",
        "Hannah promised to give her son back to God, and she kept her promise even though it was hard. What is something hard you could trust God with?",
        "When God answered her prayer, Hannah sang for joy. What is something God has done that makes you want to thank him?"
      ]
    },
    "tags": ["prayer", "trust", "God listens", "thankfulness", "hope"],
    "quiz": [
      {"question": "What did Hannah want more than anything?", "options": ["A child", "A big house", "A crown"], "answer": 0, "explanation": ""},
      {"question": "How did Hannah pray in the house of God?", "options": ["Very loudly", "Silently, with her lips moving", "In a song"], "answer": 1, "explanation": "Eli even thought she had been drinking because her prayer was so quiet."},
      {"question": "What did Hannah name her son?", "options": ["Samuel", "David", "Saul"], "answer": 0, "explanation": "It sounds like, I asked the Lord for him."},
      {"question": "What did Hannah do after Samuel was born?", "options": ["She kept her promise and gave him to serve God", "She hid him away", "She made him a king"], "answer": 0, "explanation": ""},
      {"question": "Whose later song sounds almost exactly like Hannah's?", "options": ["Mary, the mother of Jesus", "King David", "Moses"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "1 Samuel 1-2",
    "hook": "Hannah wanted a baby more than anything. So she went to God's house and prayed a quiet prayer that only God could hear.",
    "story": [
      "There was a woman named Hannah who loved God very much. More than anything in the world, she wanted to have a baby of her own.",
      "But year after year went by, and Hannah had no children. It made her very, very sad.",
      "One day Hannah went to God's house all by herself. She cried and prayed from deep in her heart.",
      "\"Dear God,\" she prayed quietly, \"if you give me a son, I will give him right back to you to serve you his whole life.\"",
      "Hannah prayed so quietly that her lips moved but no sound came out. Only God could hear her prayer.",
      "The priest, named Eli, told her, \"Go in peace, and may God give you what you have asked for.\"",
      "And God did! After a while, Hannah had a baby boy. She named him Samuel, and she was so happy.",
      "Hannah did not forget her promise. When Samuel was still little, she brought him to God's house to serve God, just like she had promised.",
      "Then Hannah sang a happy song to thank God. God had heard her quiet prayer, and God hears our prayers too."
    ],
    "devotional": {
      "bigIdea": "Hannah told God exactly how she felt and trusted him with her biggest wish. God heard her quiet prayer. God hears our prayers too, even the quiet ones.",
      "questions": [
        "Hannah told God how sad she was. How does it help to tell God how you feel?",
        "Hannah kept her promise to God even though it was hard. What is a promise you can keep?",
        "God heard Hannah's quiet prayer. How does it feel to know God always hears you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["prayer", "trust", "God listens"],
    "quiz": [
      {"question": "What did Hannah want most of all?", "options": ["A baby", "Gold", "A castle"], "answer": 0, "explanation": ""},
      {"question": "How quietly did Hannah pray?", "options": ["So quietly only God could hear", "Very loudly", "In a shout"], "answer": 0, "explanation": ""},
      {"question": "What did Hannah do after her son was born?", "options": ["Kept her promise and gave him to serve God", "Hid him", "Forgot her promise"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "saul-king", "era": "kingdom", "emoji": "👑",
  "title": "Israel's First King", "date": "c. 1050 BC", "location": "Israel",
  "connections": [
    {"title": "Speak, Lord", "storyId": "samuel", "reference": "1 Samuel 8:7",
     "why": "Samuel, the boy who once heard God's voice, is now the old prophet who warns the people and anoints their first king."},
    {"title": "God Looks at the Heart", "storyId": "david-anointed", "reference": "1 Samuel 16:7",
     "why": "Saul looked exactly like a king should look, but God would soon choose David instead, looking past the outside to the heart."},
    {"title": "The Cave and the King", "storyId": "david-saul", "reference": "1 Samuel 18:9",
     "why": "Saul began so humbly, but jealousy of David would grow in him until he was chasing the very man God had chosen."}
  ],
  "tier1": {
    "book": "1 Samuel 8–10",
    "hook": "God himself was Israel's king. But the people looked at the nations around them and decided they wanted a king they could see, like everyone else.",
    "story": [
      "For a long time, God had led his people through judges and prophets. God himself was their true king. But the people looked at all the nations around them, with their crowns and their thrones, and they came to the prophet Samuel with a demand. \"Give us a king to rule over us, like all the other nations have.\"",
      "This made Samuel sad, so he prayed about it. And God told him something surprising. \"Listen to the people. It is not you they are rejecting. They are rejecting me as their king. They want to be like everyone else instead of trusting me.\"",
      "God told Samuel to warn the people what a king would really be like. \"A king will take your sons for his armies and your daughters for his servants. He will take the best of your fields and your flocks, and you will become his servants. One day you will cry out because of the king you chose.\"",
      "But the people would not listen. \"No!\" they said. \"We want a king over us. Then we will be like all the other nations, and our king will lead us and fight our battles.\" So God told Samuel to give them what they asked for.",
      "God chose a young man named Saul. He was tall, a head taller than everyone else, and very handsome. He certainly looked the part of a king. And at first, Saul was humble. When the time came to present him to the people, he was so shy that he went and hid among the baggage, and they had to go and find him.",
      "Samuel poured oil on Saul's head to set him apart as king, and the people shouted, \"Long live the king!\" Saul had a good and humble beginning, and the Spirit of God came on him.",
      "But getting what they wanted would not make the people happy the way they thought. They had wanted a king they could see instead of trusting the God they could not see. God let them have their king, and he would still work out his good plan, but the people would learn that no human king could ever take the place of God."
    ],
    "devotional": {
      "bigIdea": "The people wanted to be like everyone else. They wanted a king they could see instead of trusting the God they could not see. God gave them what they asked for, but only God can truly be the King our hearts need.",
      "questions": [
        "The people wanted to be just like the nations around them. When do you feel like you want to be just like everyone else?",
        "God warned them what a king would cost, but they insisted anyway. Has wanting something so badly ever kept you from listening to good advice?",
        "Saul started out humble, even hiding among the baggage. Why do you think it is good to stay humble even when you are given something important?"
      ]
    },
    "tags": ["kingship", "trust", "following the crowd", "humility", "Samuel"],
    "quiz": [
      {"question": "Who was Israel's true king before they asked for a human one?", "options": ["God himself", "Samuel", "Moses"], "answer": 0, "explanation": ""},
      {"question": "Why did the people want a king?", "options": ["To be like all the other nations", "Because God told them to", "To stop a war"], "answer": 0, "explanation": ""},
      {"question": "What did Samuel warn a king would do?", "options": ["Take their sons, daughters, and best fields", "Give them lots of gold", "Make everyone happy"], "answer": 0, "explanation": ""},
      {"question": "Who did God choose as the first king?", "options": ["Saul", "David", "Jonathan"], "answer": 0, "explanation": ""},
      {"question": "Where was Saul when it was time to present him as king?", "options": ["Hiding among the baggage", "On a throne", "Leading an army"], "answer": 0, "explanation": "He started out humble and shy."}
    ]
  },
  "tier2": {
    "book": "1 Samuel 8-10",
    "hook": "God was already Israel's king. But the people wanted a king they could see, like all the other nations had.",
    "story": [
      "For a long time, God himself was the king of his people. He led them and took care of them.",
      "But the people looked at the other nations, who all had kings with crowns. They went to the prophet Samuel and said, \"We want a king too, like everyone else!\"",
      "This made Samuel sad. So he prayed, and God said, \"They are not really saying no to you. They are saying no to me as their king.\"",
      "Samuel warned the people. \"A king will take your sons and your best things, and one day you will be sorry.\"",
      "But the people still said, \"We want a king!\" So God let them have one.",
      "God chose a young man named Saul. He was very tall and looked just like a king should look.",
      "At first, Saul was humble. When it was time to make him king, he was so shy that he hid behind the bags, and the people had to go find him!",
      "Samuel made Saul the king, and everyone shouted, \"Long live the king!\"",
      "But the people learned something important. No king they could see could ever take the place of God, their real King."
    ],
    "devotional": {
      "bigIdea": "The people wanted to be like everyone else and have a king they could see. But only God can truly be the King our hearts need.",
      "questions": [
        "When do you want to be just like everyone else?",
        "Saul was humble and even hid behind the bags. Why is it good to be humble?",
        "God is the best King of all. What do you love about God being your King?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["kingship", "trust", "humility"],
    "quiz": [
      {"question": "Who was Israel's king before they asked for one?", "options": ["God himself", "A giant", "Samuel"], "answer": 0, "explanation": ""},
      {"question": "Why did the people want a king?", "options": ["To be like the other nations", "To win a game", "God told them to"], "answer": 0, "explanation": ""},
      {"question": "Where did Saul hide when it was time to be king?", "options": ["Among the baggage", "In a cave", "Up a tree"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "david-anointed", "era": "kingdom", "emoji": "🫒",
  "title": "God Looks at the Heart", "date": "c. 1025 BC", "location": "Bethlehem",
  "connections": [
    {"title": "Israel's First King", "storyId": "saul-king", "reference": "1 Samuel 16:1",
     "why": "Saul looked like a king on the outside, but God now sends Samuel to find a king after his own heart instead."},
    {"title": "One Stone", "storyId": "david-goliath", "reference": "1 Samuel 16:13",
     "why": "The shepherd boy anointed here is the same David who will soon face the giant Goliath with nothing but a sling and trust in God."},
    {"title": "The Lord Is My Shepherd", "storyId": "psalm23", "reference": "1 Samuel 16:11",
     "why": "David was out watching the sheep when God chose him, and the shepherd boy would grow up to write the most famous shepherd song of all."}
  ],
  "tier1": {
    "book": "1 Samuel 16",
    "hook": "God sent Samuel to find Israel's next king among eight brothers. Seven tall, strong sons walked by, but God was waiting for the one nobody had even bothered to call in from the fields.",
    "story": [
      "King Saul had turned away from following God, so God had a new king in mind. He sent the prophet Samuel to the little town of Bethlehem, to the house of a man named Jesse. \"One of Jesse's sons will be the next king,\" God told him. \"I will show you which one.\"",
      "When Samuel arrived, Jesse lined up his sons. The oldest, Eliab, stepped forward first. He was tall and strong and handsome, and Samuel thought, \"Surely this is the one God has chosen!\"",
      "But God said to Samuel, \"Do not look at how tall he is or how he looks on the outside. I have not chosen him. People look at the outside, but the Lord looks at the heart.\" Samuel was learning that God sees what people cannot see.",
      "So Jesse called his next son, and the next, and the next. Seven strong sons passed by Samuel, and each time God said no. Samuel was puzzled. \"The Lord has not chosen any of these,\" he told Jesse. \"Are these all the sons you have?\"",
      "\"There is still the youngest,\" Jesse said, \"but he is out in the fields watching the sheep.\" No one had even thought to call him in. \"Send for him,\" Samuel said. \"We will not sit down until he arrives.\"",
      "So they brought in the youngest boy, David. He had been out caring for the sheep, and he came in with the wind and the sun on his face. And God said to Samuel, \"This is the one. Rise and anoint him.\"",
      "Samuel poured oil over David's head right there in front of all his brothers, and from that day on, the Spirit of the Lord came powerfully on David. The boy everyone had overlooked, the one left out in the fields, was the one God had chosen all along, because God had looked straight at his heart."
    ],
    "devotional": {
      "bigIdea": "Everyone was impressed by the tall, strong, older brothers. But God was not looking at the outside at all. He was looking at David's heart. God does not care how we look or how impressive we seem. He sees who we really are on the inside.",
      "questions": [
        "Samuel was sure the tall, handsome brother was the one. Why do you think we are so quick to judge people by how they look?",
        "God said he looks at the heart. If God looked at your heart today, what do you think he would see?",
        "David was overlooked by everyone, even his own family, but not by God. How does it feel to know God never overlooks you?"
      ]
    },
    "tags": ["the heart", "being chosen", "humility", "God sees", "David"],
    "quiz": [
      {"question": "Where did God send Samuel to find the new king?", "options": ["To Jesse's house in Bethlehem", "To Egypt", "To the palace"], "answer": 0, "explanation": ""},
      {"question": "Why did God say no to the tall, handsome oldest brother?", "options": ["God looks at the heart, not the outside", "He was too old", "He was a shepherd"], "answer": 0, "explanation": ""},
      {"question": "Where was David when Samuel arrived?", "options": ["Out in the fields watching the sheep", "Asleep in bed", "At the market"], "answer": 0, "explanation": "No one had even thought to call him in."},
      {"question": "What did Samuel do when David came in?", "options": ["Anointed him with oil as the chosen one", "Sent him back to the sheep", "Made him a soldier"], "answer": 0, "explanation": ""},
      {"question": "What is the big lesson of this story?", "options": ["God looks at the heart, not the outside", "Tall people are best", "Always be first in line"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "1 Samuel 16",
    "hook": "Samuel went to pick the next king. Seven strong brothers walked by, but God was waiting for the youngest one, who was still out with the sheep.",
    "story": [
      "King Saul had stopped following God. So God sent the prophet Samuel to a town called Bethlehem to find a new king.",
      "God sent him to the house of a man named Jesse, who had many sons. \"One of them will be the new king,\" God said.",
      "The oldest son came first. He was tall and strong and handsome. Samuel thought, \"This must be the one!\"",
      "But God said, \"No. People look at the outside, but I look at the heart.\"",
      "So one by one, seven big, strong sons walked past Samuel. And each time, God said, \"Not this one.\"",
      "\"Are these all your sons?\" Samuel asked. \"There is one more,\" said Jesse. \"My youngest, David. He is out watching the sheep.\"",
      "Nobody had even thought to call him in! So they ran to get David from the fields.",
      "When David came in, God said, \"This is the one!\" So Samuel poured oil on David's head to show he was God's chosen king.",
      "God did not pick David because he was the biggest or strongest. God picked him because of his heart. God always sees what is inside us."
    ],
    "devotional": {
      "bigIdea": "Everyone looked at the big strong brothers, but God looked at David's heart. God does not care how we look on the outside. He sees who we really are inside.",
      "questions": [
        "Why do we often look at how people look on the outside?",
        "God looks at our hearts. What do you think God sees when he looks at your heart?",
        "Everyone forgot about David, but God did not. How does it feel that God never forgets you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["the heart", "being chosen", "God sees"],
    "quiz": [
      {"question": "What does God look at when he chooses someone?", "options": ["The heart", "How tall they are", "Their clothes"], "answer": 0, "explanation": ""},
      {"question": "Where was David when Samuel came?", "options": ["Watching the sheep", "Sleeping", "Eating dinner"], "answer": 0, "explanation": ""},
      {"question": "Why did God choose David?", "options": ["Because of his heart", "Because he was the biggest", "Because he was the oldest"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "david-jonathan", "era": "kingdom", "emoji": "🏹",
  "title": "The Best of Friends", "date": "c. 1015 BC", "location": "Gibeah",
  "connections": [
    {"title": "One Stone", "storyId": "david-goliath", "reference": "1 Samuel 18:1",
     "why": "It was right after David defeated Goliath that Prince Jonathan's heart was knit to David's in friendship."},
    {"title": "The Cave and the King", "storyId": "david-saul", "reference": "1 Samuel 19:1",
     "why": "Jonathan's own father, King Saul, grows so jealous of David that Jonathan must risk his life to protect his friend."},
    {"title": "Kindness for Jonathan's Sake", "storyId": "mephibosheth", "reference": "1 Samuel 20:42",
     "why": "David and Jonathan promise to be loyal forever, and years later David keeps that promise to Jonathan's son."}
  ],
  "tier1": {
    "book": "1 Samuel 18–20",
    "hook": "Jonathan was the prince, the one in line to be king. David was the shepherd boy who would take his place. By every rule, they should have been rivals. Instead, they became the truest of friends.",
    "story": [
      "After David defeated the giant Goliath, he was brought to live in the palace of King Saul. There he met the king's son, Prince Jonathan. From the very first day, Jonathan loved David like his own brother, and the two of them became the closest of friends.",
      "Jonathan made a promise of friendship with David, a covenant to be loyal to each other always. Then Jonathan did something amazing. He took off his own royal robe and gave it to David, along with his sword, his bow, and his belt. Jonathan was the prince, the next in line for the throne, and yet he gladly gave his place to his friend.",
      "But all was not well. The people loved David and sang songs about him, and King Saul grew bitterly jealous. The jealousy festered until Saul wanted David dead. He even told Jonathan and his servants to kill him.",
      "Jonathan was caught between his father and his friend. He chose to do what was right. He warned David, and he spoke up for him to Saul. \"David has never done anything to harm you,\" he told his father. \"He risked his life to save us all.\" For a while, Saul listened.",
      "But Saul's jealousy returned, worse than before. So David and Jonathan made a secret plan. David would hide in a field, and Jonathan would find out his father's true feelings. If David was in danger, Jonathan would shoot three arrows and tell the boy fetching them that they were far away. That would be the signal to run.",
      "When Jonathan saw that his father truly meant to kill David, his heart broke. He went to the field and shot the arrows far out beyond the boy. \"Hurry, the arrows are beyond you!\" he called, and David knew he had to flee for his life.",
      "When they were finally alone, the two friends held each other and wept, because they knew they might never meet again. \"Go in peace,\" Jonathan said. \"We have promised in the Lord's name to be friends forever, you and I and our children after us.\" And that is a promise David would never forget."
    ],
    "devotional": {
      "bigIdea": "Jonathan had every reason to see David as a rival, since David would take the throne that should have been Jonathan's. Instead, Jonathan loved David, protected him, and gladly gave up his own place for him. That is what real friendship looks like: wanting what is best for someone else, even when it costs you.",
      "questions": [
        "Jonathan gave up his own crown for his friend. What is something you could give up to be a good friend to someone?",
        "Jonathan had to choose between his father and his friend. Have you ever had to do the right thing even when it was really hard?",
        "What do you think makes someone a true friend, the kind David and Jonathan were to each other?"
      ]
    },
    "tags": ["friendship", "loyalty", "love", "courage", "sacrifice"],
    "quiz": [
      {"question": "Who was Jonathan?", "options": ["King Saul's son, the prince", "David's brother", "A giant"], "answer": 0, "explanation": ""},
      {"question": "What did Jonathan give David to show his friendship?", "options": ["His royal robe, sword, and bow", "A bag of gold", "A horse"], "answer": 0, "explanation": "He gladly gave up his own royal things for his friend."},
      {"question": "Why did King Saul want to hurt David?", "options": ["He was jealous of him", "David had stolen from him", "David was lazy"], "answer": 0, "explanation": ""},
      {"question": "How did Jonathan warn David to run?", "options": ["With a signal using arrows", "By sending a letter", "By ringing a bell"], "answer": 0, "explanation": ""},
      {"question": "What promise did the two friends make?", "options": ["To be loyal friends forever", "To never speak again", "To fight each other"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "1 Samuel 18-20",
    "hook": "Jonathan was a prince, and David would one day be king in his place. But instead of being rivals, they became the very best of friends.",
    "story": [
      "After David beat the giant Goliath, he came to live at the palace of King Saul.",
      "There he met the king's son, Prince Jonathan. Right away, Jonathan loved David like a brother, and they became the very best of friends.",
      "Jonathan even gave David his own royal robe and his sword. He was the prince, but he gladly shared everything with his friend.",
      "But King Saul became very jealous of David, because everyone loved him. Saul wanted to hurt David.",
      "Jonathan was sad and worried for his friend. He bravely warned David that he was in danger.",
      "They made a secret plan with arrows. If Jonathan shot the arrows far away, it meant David must run to stay safe.",
      "When Jonathan saw David really was in danger, he shot the arrows far out into the field. That was the signal.",
      "The two friends hugged and cried, because David had to run far away. \"Go in peace,\" said Jonathan. \"We will be friends forever.\"",
      "David and Jonathan loved each other and helped each other. That is what good friends do."
    ],
    "devotional": {
      "bigIdea": "Jonathan and David were the best of friends. Jonathan even gave up his own things and kept his friend safe. Real friends want what is best for each other.",
      "questions": [
        "Jonathan shared his special things with David. How can you be a good friend by sharing?",
        "Jonathan kept David safe. Who are the friends who help you?",
        "What do you think makes someone a really good friend?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["friendship", "loyalty", "love"],
    "quiz": [
      {"question": "Who was David's best friend?", "options": ["Jonathan", "Goliath", "Pharaoh"], "answer": 0, "explanation": ""},
      {"question": "What did Jonathan give David?", "options": ["His royal robe and sword", "A bowl of soup", "A boat"], "answer": 0, "explanation": ""},
      {"question": "How did Jonathan warn David to run away?", "options": ["With a signal using arrows", "With a letter", "With a song"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "david-ark", "era": "kingdom", "emoji": "🎶",
  "title": "Dancing Before the Lord", "date": "c. 1000 BC", "location": "Jerusalem",
  "connections": [
    {"title": "God Looks at the Heart", "storyId": "david-anointed", "reference": "2 Samuel 6:14",
     "why": "The shepherd boy God chose for his heart grows into a king whose heart overflows with joyful worship."},
    {"title": "The Lord Is My Shepherd", "storyId": "psalm23", "reference": "Psalm 30:11",
     "why": "David, who danced before the Lord with all his might, was also the singer and poet who gave us the Psalms."},
    {"title": "The Wisest Request", "storyId": "solomon-wisdom", "reference": "1 Kings 8:1",
     "why": "David brings the ark to Jerusalem, and his son Solomon would later build the great Temple to be its permanent home."}
  ],
  "tier1": {
    "book": "2 Samuel 6",
    "hook": "When King David brought the ark of God home to Jerusalem, he was so full of joy that he danced through the streets with all his might, and he did not care one bit who was watching.",
    "story": [
      "David was now the king of all Israel, and there was one thing he wanted more than anything for his new capital city, Jerusalem. He wanted to bring home the ark of the covenant, the special golden chest that was the sign of God's presence with his people. It had been away for a long time, and David longed to put God right at the center of the kingdom.",
      "The people had once tried to move the ark the wrong way, carelessly, and it had gone badly, because God is holy and is not to be treated lightly. So this time David made sure they did it God's way, carried carefully by the priests, just as God had commanded long ago.",
      "And what a celebration it was! As the ark made its way into the city, there were trumpets and harps and tambourines and shouting. All of Israel came out to bring the ark of the Lord home with songs of joy.",
      "King David led the whole parade, and he was so overjoyed that he danced before the Lord with all his might. He had taken off his royal robes and wore a simple linen garment like an ordinary priest, leaping and dancing down the street, worshiping God with his whole body and his whole heart.",
      "But David's wife Michal watched from a window, and when she saw the king leaping and dancing, she was embarrassed by him. She thought a king should be more dignified, more proper, and she looked down on him in her heart.",
      "When David came home, she scolded him. \"How the great king made a fool of himself today, dancing around in front of everyone!\" But David did not back down. \"I was dancing before the Lord, who chose me. I will celebrate before him, and I will become even more undignified than this. I do not care if I look foolish, as long as I am honoring God.\"",
      "David knew something important. Worship is not about looking proper or impressing people. It is about loving God so much that you cannot hold it in. The king of Israel was not ashamed to look a little silly, because his heart was bursting with joy over his God."
    ],
    "devotional": {
      "bigIdea": "David was the king, but he did not care about looking dignified when it came to worshiping God. He danced with all his might because he loved God with all his heart. Real worship is not about looking proper. It is about loving God so much that your joy spills out.",
      "questions": [
        "David danced with all his might and did not care who was watching. What are some ways you can worship God with your whole self?",
        "Michal thought David should be more proper. Have you ever felt embarrassed to show how much you love God? What helped?",
        "David put God right at the center of his city and his life. What would it look like to put God at the center of your day?"
      ]
    },
    "tags": ["worship", "joy", "wholehearted", "David", "celebration"],
    "quiz": [
      {"question": "What did David want to bring home to Jerusalem?", "options": ["The ark of the covenant", "A golden statue", "A new throne"], "answer": 0, "explanation": "The ark was the sign of God's presence with his people."},
      {"question": "How did David celebrate as the ark came into the city?", "options": ["He danced with all his might", "He sat quietly", "He hid inside"], "answer": 0, "explanation": ""},
      {"question": "How did David's wife Michal feel when she saw him dancing?", "options": ["She was embarrassed by him", "She danced too", "She was proud"], "answer": 0, "explanation": ""},
      {"question": "What did David say about his dancing?", "options": ["He was celebrating before the Lord and did not care if he looked foolish", "He was sorry", "He would never do it again"], "answer": 0, "explanation": ""},
      {"question": "What does this story teach about worship?", "options": ["It is about loving God with your whole heart, not looking proper", "It must always be quiet", "Only kings can worship"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "2 Samuel 6",
    "hook": "When King David brought God's special golden chest home to the city, he was so happy that he danced with all his might, and he did not care who was watching!",
    "story": [
      "David was now the king of all God's people. He wanted to bring something very special home to his city, Jerusalem.",
      "It was the ark of the covenant, a golden chest that showed that God was with his people. David wanted God right at the center of everything.",
      "So they carried the ark carefully into the city, just the way God said to. And there was a huge, happy celebration!",
      "There were trumpets and harps and tambourines. Everyone sang and shouted for joy as the ark came home.",
      "King David was so full of joy that he danced and danced with all his might, right down the middle of the street!",
      "But David's wife, Michal, watched from a window. She thought a king should not dance like that. She felt embarrassed.",
      "She told David, \"You looked silly today!\" But David said, \"I was dancing for God! I do not care if I look silly. I just want to honor him.\"",
      "David loved God so much that his joy spilled right out of him.",
      "Worshiping God is not about looking proper. It is about loving God with your whole heart, just like David did."
    ],
    "devotional": {
      "bigIdea": "King David danced with all his might because he loved God so much. Worshiping God is about loving him with your whole heart, not about looking proper.",
      "questions": [
        "David danced to show his love for God. What are fun ways you can worship God?",
        "David did not care if he looked silly. Why do you think he was so happy?",
        "How can you put God at the center of your day, like David did?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["worship", "joy", "celebration"],
    "quiz": [
      {"question": "What did David bring home to the city?", "options": ["God's special golden chest, the ark", "A new crown", "A big drum"], "answer": 0, "explanation": ""},
      {"question": "What did David do because he was so happy?", "options": ["He danced with all his might", "He took a nap", "He hid"], "answer": 0, "explanation": ""},
      {"question": "What did David care about most?", "options": ["Honoring God, not looking proper", "Looking like a fancy king", "Winning a dance contest"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-03a.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-03a.json with {len(batch)} stories.")
