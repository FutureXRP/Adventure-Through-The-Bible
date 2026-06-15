#!/usr/bin/env python3
"""Authoring source for Batch 5a (parables and miracles). Writes batch-05a.json."""
import json

batch = [
{
  "id": "mustard-seed", "era": "nt-life", "emoji": "🌳",
  "title": "The Tiny Mustard Seed", "date": "c. AD 28", "location": "Galilee",
  "connections": [
    {"title": "The Farmer and the Seeds", "storyId": "sower", "reference": "Matthew 13:31",
     "why": "Another of Jesus' seed parables, teaching that God's kingdom grows in ways we do not always see."},
    {"title": "Five Loaves and Two Fish", "storyId": "feeding-5000", "reference": "Matthew 13:33",
     "why": "Like a few loaves feeding thousands, the smallest beginning in God's hands becomes something far greater than we expect."},
    {"title": "The Day Everything Changed", "storyId": "pentecost", "reference": "Acts 1:8",
     "why": "Jesus' kingdom began with a tiny handful of followers and grew, just like the mustard seed, into something that filled the world."}
  ],
  "tier1": {
    "book": "Matthew 13",
    "hook": "Jesus said the kingdom of God is like the smallest seed a farmer could plant. It seems like nothing at all, until you see what it becomes.",
    "story": [
      "One day Jesus wanted to help people understand what God's kingdom is like. So he told them a very short story about a very small seed.",
      "\"The kingdom of heaven,\" Jesus said, \"is like a tiny mustard seed that a man planted in his field.\"",
      "Now a mustard seed is one of the smallest seeds of all. You could hold a hundred of them in the palm of your hand. If you dropped one on the ground, you might not even be able to find it again. It looks like nothing important at all.",
      "\"But when that little seed is planted and begins to grow,\" Jesus went on, \"it becomes the biggest plant in the garden. It grows into a tree so large that the birds of the air come and make their nests in its branches.\"",
      "The smallest seed imaginable becomes a tree big enough to shelter the birds. That is what God's kingdom is like.",
      "It often starts in ways that look tiny and unimportant. A baby born in a stable. Twelve ordinary followers. One small act of love. A quiet prayer. But God takes those small beginnings and grows them into something far bigger and more beautiful than anyone could imagine.",
      "So we never have to think that we are too small, or that what we do for God is too little to matter. In God's hands, even the tiniest seed of faith can grow into something wonderful."
    ],
    "devotional": {
      "bigIdea": "God loves to start with small things. A tiny seed becomes a great tree. Twelve followers became a worldwide family. We never have to feel too small or think our little acts of love do not matter, because in God's hands, small beginnings grow into amazing things.",
      "questions": [
        "The mustard seed looked too small to matter, but it grew into a tree. When have you seen something small grow into something big?",
        "Jesus said God's kingdom starts small and grows. What is one small thing you could do for God this week?",
        "Why do you think God so often chooses to start with small, humble things?"
      ]
    },
    "tags": ["the kingdom", "faith", "small beginnings", "parables", "growing"],
    "quiz": [
      {"question": "What did Jesus say the kingdom of heaven is like?", "options": ["A tiny mustard seed", "A big mountain", "A pile of gold"], "answer": 0, "explanation": ""},
      {"question": "How big is a mustard seed?", "options": ["One of the smallest seeds of all", "As big as an apple", "As big as a rock"], "answer": 0, "explanation": ""},
      {"question": "What does the tiny seed grow into?", "options": ["A tree big enough for birds to nest in", "A small weed", "Nothing"], "answer": 0, "explanation": ""},
      {"question": "What does this parable teach us?", "options": ["God grows small beginnings into something great", "Big seeds are best", "Gardening is hard"], "answer": 0, "explanation": ""},
      {"question": "How should this make us feel about small acts of love?", "options": ["They matter, because God can grow them", "They are a waste of time", "Only big things count"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Matthew 13",
    "hook": "Jesus said God's kingdom is like the smallest little seed. It looks like nothing, until you see what it grows into!",
    "story": [
      "One day Jesus told a very short story to help people understand what God's kingdom is like.",
      "\"God's kingdom is like a tiny mustard seed,\" Jesus said, \"that a man planted in his garden.\"",
      "A mustard seed is so small that you could hold a whole bunch of them in your hand. If you dropped one, you might not even find it again!",
      "\"But when that little seed grows,\" said Jesus, \"it becomes the biggest plant in the garden.\"",
      "It grows into a tree so big that birds come and build their nests in its branches!",
      "The teeny tiny seed becomes a great big tree. That is what God's kingdom is like.",
      "It often starts very small, like a baby born in a stable, or one little act of love.",
      "But God takes those small beginnings and grows them into something wonderful and big.",
      "So you are never too small for God to use. Even a little bit of love can grow into something amazing!"
    ],
    "devotional": {
      "bigIdea": "A tiny seed grows into a great big tree. God loves to take small things and grow them into something wonderful. You are never too small for God to use!",
      "questions": [
        "Have you ever seen something tiny grow into something big?",
        "What is one small, kind thing you could do for God?",
        "How does it feel to know God can use even little you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["the kingdom", "faith", "small beginnings"],
    "quiz": [
      {"question": "What did Jesus say the kingdom is like?", "options": ["A tiny mustard seed", "A big rock", "A river"], "answer": 0, "explanation": ""},
      {"question": "What does the tiny seed grow into?", "options": ["A big tree for birds", "A small weed", "A flower"], "answer": 0, "explanation": ""},
      {"question": "What does this teach us?", "options": ["God grows small things into big ones", "Only big things matter", "Seeds are boring"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "lost-sheep", "era": "nt-life", "emoji": "🐑",
  "title": "The Lost Sheep", "date": "c. AD 29", "location": "Galilee",
  "connections": [
    {"title": "The Lost Coin", "storyId": "lost-coin", "reference": "Luke 15:8",
     "why": "Jesus tells this story right alongside the lost coin, both about the joy of finding what was lost."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Luke 15:11",
     "why": "All three stories in a row, the lost sheep, the lost coin, and the lost son, show how much heaven rejoices when the lost are found."},
    {"title": "The Lord Is My Shepherd", "storyId": "psalm23", "reference": "Psalm 23:1",
     "why": "Jesus is the Good Shepherd who goes after the one lost sheep, just as the shepherd of Psalm 23 watches over his own."}
  ],
  "tier1": {
    "book": "Luke 15",
    "hook": "Some people grumbled that Jesus spent his time with the wrong sort of people. So Jesus told them a story about a shepherd who would leave ninety-nine sheep to go find just one.",
    "story": [
      "The religious leaders did not like that Jesus welcomed sinners and even ate meals with them. \"Why does this man spend time with people like that?\" they grumbled. So Jesus answered them with a story.",
      "\"Suppose one of you has a hundred sheep,\" Jesus said, \"and one of them wanders off and gets lost. What will you do? Won't you leave the ninety-nine safe in the open country and go after the one lost sheep until you find it?\"",
      "Every sheep mattered to the shepherd. He would not just shrug and say, well, I still have ninety-nine. That one lost sheep, alone and frightened and in danger, was worth going after.",
      "So the shepherd searches. He climbs the hills and looks through the valleys, calling and calling, until at last he finds his lost little sheep.",
      "And when he finds it, he is not angry. Jesus said the shepherd joyfully puts the sheep on his shoulders and carries it all the way home. Then he calls his friends and neighbors together and says, \"Rejoice with me! I have found my lost sheep!\"",
      "Then Jesus explained what the story meant. \"In the same way,\" he said, \"there is more rejoicing in heaven over one sinner who turns back to God than over ninety-nine who never wandered away.\"",
      "That is why Jesus spent time with lost and broken people. He is the Good Shepherd, and not one of his sheep is too lost or too far away for him to come looking. When even one person comes home to God, all of heaven throws a party."
    ],
    "devotional": {
      "bigIdea": "The shepherd did not give up on the one lost sheep, even though he still had ninety-nine. Jesus is that shepherd, and he comes looking for each one of us. To God, you are never just one in a crowd. You are the one he would leave everything to find, and heaven celebrates when you are found.",
      "questions": [
        "The shepherd went after just one lost sheep. How does it feel to know that God would come looking for you?",
        "When the sheep was found, the shepherd threw a party. Why do you think heaven celebrates so much when one person comes home to God?",
        "Jesus spent time with people others looked down on. Who is someone you could show God's love to this week?"
      ]
    },
    "tags": ["God seeks us", "the Good Shepherd", "joy", "parables", "being found"],
    "quiz": [
      {"question": "Why were the religious leaders grumbling about Jesus?", "options": ["He welcomed and ate with sinners", "He was too quiet", "He charged money"], "answer": 0, "explanation": ""},
      {"question": "How many sheep did the shepherd have, and how many got lost?", "options": ["A hundred, and one got lost", "Ten, and five got lost", "Two, and both got lost"], "answer": 0, "explanation": ""},
      {"question": "What did the shepherd do about the one lost sheep?", "options": ["Left the ninety-nine and went to find it", "Forgot about it", "Bought a new one"], "answer": 0, "explanation": ""},
      {"question": "What did the shepherd do when he found it?", "options": ["Carried it home with joy and celebrated", "Scolded it", "Sold it"], "answer": 0, "explanation": ""},
      {"question": "What happens in heaven when one person turns back to God?", "options": ["There is great rejoicing", "Nothing", "It gets quiet"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Luke 15",
    "hook": "Jesus told a story about a shepherd who had a hundred sheep. When just one got lost, he went to find it!",
    "story": [
      "Some people did not like that Jesus was kind to people who had done wrong. So Jesus told them a story.",
      "\"Imagine you have a hundred sheep,\" said Jesus, \"and one little sheep wanders off and gets lost.\"",
      "\"What would you do? Wouldn't you leave the ninety-nine and go look for the one lost sheep until you found it?\"",
      "Every single sheep was special to the shepherd. He did not want to lose even one.",
      "So the shepherd looked and looked, over the hills and through the valleys, until at last he found his lost little sheep!",
      "He was so happy! He gently lifted the sheep onto his shoulders and carried it all the way home.",
      "Then he called his friends and said, \"Be happy with me! I found my lost sheep!\"",
      "Jesus said that heaven is full of joy like that whenever even one person comes back to God.",
      "Jesus is like that good shepherd. He loves every one of us, and he comes looking for us. You are never too lost for Jesus to find!"
    ],
    "devotional": {
      "bigIdea": "The shepherd went to find his one lost sheep and was so happy when he found it. Jesus is that shepherd. He loves you so much that he would come looking just for you.",
      "questions": [
        "How does it feel to know Jesus would come looking just for you?",
        "The shepherd was so happy he had a party. Why is finding the lost sheep such good news?",
        "How can you show love to someone who feels lost or left out?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God seeks us", "the Good Shepherd", "joy"],
    "quiz": [
      {"question": "What did the shepherd do when one sheep got lost?", "options": ["Went to find it", "Ignored it", "Got a new one"], "answer": 0, "explanation": ""},
      {"question": "How did the shepherd feel when he found the sheep?", "options": ["So happy he had a party", "Angry", "Sad"], "answer": 0, "explanation": ""},
      {"question": "Who is like the good shepherd?", "options": ["Jesus", "A king", "A farmer"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "lost-coin", "era": "nt-life", "emoji": "🪙",
  "title": "The Lost Coin", "date": "c. AD 29", "location": "Galilee",
  "connections": [
    {"title": "The Lost Sheep", "storyId": "lost-sheep", "reference": "Luke 15:4",
     "why": "Jesus tells this story right after the lost sheep, making the very same point: God searches for what is lost."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Luke 15:11",
     "why": "The third in the trio of lost-and-found stories, all about the joy of heaven when one lost person comes home."},
    {"title": "The Man in the Tree", "storyId": "zacchaeus", "reference": "Luke 19:10",
     "why": "Jesus said he came to seek and to save the lost, which is exactly what the searching woman in this story does."}
  ],
  "tier1": {
    "book": "Luke 15",
    "hook": "A woman had ten silver coins, and she lost just one. So she turned her whole house upside down to find it, because that one coin mattered to her.",
    "story": [
      "Right after the story of the lost sheep, Jesus told another short story to make the very same point, this time about a woman and her coins.",
      "\"Suppose a woman has ten silver coins,\" Jesus said, \"and she loses one of them.\" These coins were precious to her, perhaps her savings, perhaps all the money she had. Losing even one was a real loss.",
      "\"What does she do?\" Jesus asked. \"She lights a lamp, sweeps the whole house, and searches carefully in every corner until she finds it.\" She does not just give up and say, well, I still have nine. She gets down on her hands and knees and searches every crack in the floor.",
      "She keeps looking and looking, refusing to stop until that one lost coin is back in her hand.",
      "And when she finally finds it, she is overjoyed. She runs to call her friends and neighbors together and says, \"Rejoice with me! I have found my lost coin!\" Her joy is so big she cannot keep it to herself.",
      "Then Jesus told them what it meant. \"In the same way,\" he said, \"there is rejoicing among the angels of God over one sinner who turns back to him.\"",
      "Like the shepherd with his sheep and the woman with her coin, God does not count us as just one of many. Each person is so precious to him that he searches, and when one lost person is found and comes home, all of heaven breaks into celebration."
    ],
    "devotional": {
      "bigIdea": "The woman searched her whole house for one lost coin because it was precious to her. That is how precious you are to God. He does not lose interest or give up. And when one lost person is found, the angels of heaven throw a celebration.",
      "questions": [
        "The woman searched everywhere for one coin. Have you ever looked and looked for something that really mattered to you?",
        "Jesus said the angels rejoice when one person comes back to God. How does it feel to be that valuable to God?",
        "Both the shepherd and the woman could not keep their joy to themselves. Who could you share the good news of God's love with?"
      ]
    },
    "tags": ["God seeks us", "being precious", "joy", "parables", "being found"],
    "quiz": [
      {"question": "How many coins did the woman have, and how many did she lose?", "options": ["Ten coins, and she lost one", "Five, and she lost two", "Two, and she lost both"], "answer": 0, "explanation": ""},
      {"question": "What did the woman do to find her lost coin?", "options": ["Lit a lamp and swept the whole house", "Bought a new coin", "Gave up"], "answer": 0, "explanation": ""},
      {"question": "How did she feel when she found it?", "options": ["Overjoyed, and she called her friends", "Annoyed", "Tired"], "answer": 0, "explanation": ""},
      {"question": "What does the lost coin stand for?", "options": ["A person who is precious to God", "Real money", "A toy"], "answer": 0, "explanation": ""},
      {"question": "What happens in heaven when one person turns back to God?", "options": ["The angels rejoice", "Nothing happens", "It gets quiet"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Luke 15",
    "hook": "A woman had ten special coins. When she lost just one, she searched her whole house until she found it!",
    "story": [
      "Right after the story of the lost sheep, Jesus told another little story that meant the same thing.",
      "\"Imagine a woman has ten silver coins,\" Jesus said, \"and she loses one of them.\"",
      "Those coins were very special to her. Losing even one made her sad.",
      "So what did she do? She lit a lamp and swept the whole house, looking in every corner.",
      "She got down low and searched and searched, and she would not stop until she found that one lost coin.",
      "And when she finally found it, she was so happy!",
      "She called all her friends and said, \"Be happy with me! I found my lost coin!\"",
      "Jesus said that the angels in heaven are happy like that whenever one person comes back to God.",
      "You are very, very precious to God, just like that special coin. God never gives up looking for the ones he loves."
    ],
    "devotional": {
      "bigIdea": "The woman searched everywhere for one special coin. That is how special you are to God. He never gives up, and heaven celebrates when one person comes home to him.",
      "questions": [
        "Have you ever looked really hard for something you lost?",
        "How does it feel to be so precious to God?",
        "The woman shared her happy news. Who could you tell about God's love?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God seeks us", "being precious", "joy"],
    "quiz": [
      {"question": "What did the woman lose?", "options": ["One of her special coins", "Her sheep", "Her shoes"], "answer": 0, "explanation": ""},
      {"question": "What did she do to find it?", "options": ["Swept the whole house and searched", "Took a nap", "Bought a new one"], "answer": 0, "explanation": ""},
      {"question": "How precious are you to God?", "options": ["Very precious, like the special coin", "Not very", "A little"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "paralytic", "era": "nt-life", "emoji": "🛏️",
  "title": "Through the Roof", "date": "c. AD 28", "location": "Capernaum",
  "connections": [
    {"title": "Jesus Heals Blind Bartimaeus", "storyId": "bartimaeus", "reference": "Mark 10:52",
     "why": "Another time Jesus heals someone whose faith would not be stopped, no matter what stood in the way."},
    {"title": "Jairus's Daughter", "storyId": "jairus", "reference": "Mark 5:23",
     "why": "Like Jairus, these friends are sure that if they can just get to Jesus, everything will change, and they are right."},
    {"title": "Jesus Calms the Storm", "storyId": "calm-storm", "reference": "Mark 2:10",
     "why": "Just as Jesus shows his power over the storm, here he shows his authority to do what only God can do, forgive sins."}
  ],
  "tier1": {
    "book": "Mark 2",
    "hook": "Four friends were determined to get their paralyzed friend to Jesus. When they found the house too packed to enter, they did the only thing they could think of: they went through the roof.",
    "story": [
      "Jesus was teaching inside a house in Capernaum, and so many people had crowded in that there was not an inch of room left, not even outside the door. People were packed in shoulder to shoulder to hear him.",
      "Now there was a man in that town who could not walk. He had four good friends who believed that if they could just get him to Jesus, Jesus could help. So they carried him on his mat all the way to the house, only to find they could not get anywhere near the door.",
      "But these friends would not give up. They carried their friend up the outside stairs to the flat roof. Then they began to dig, pulling apart the roof right above where Jesus was teaching, until they had made a hole big enough. And carefully, with ropes, they lowered their friend down on his mat, right in front of Jesus.",
      "When Jesus saw their faith, the bold, stubborn, loving faith of those four friends, he was pleased. He looked at the man on the mat and said something surprising. \"Son, your sins are forgiven.\"",
      "Some of the religious teachers sitting there were upset. \"Who does he think he is?\" they thought. \"Only God can forgive sins!\" And they were right that only God can forgive sins. They just did not understand who Jesus was.",
      "Jesus knew their thoughts. \"Which is easier,\" he asked, \"to say your sins are forgiven, or to say get up and walk? But so that you will know I have the authority to forgive sins...\" He turned to the man and said, \"Get up, take your mat, and go home.\"",
      "At once the man stood up, picked up the very mat he had been carried in on, and walked out through the amazed crowd. Everyone was stunned, praising God and saying, \"We have never seen anything like this!\" Jesus had shown that he could heal a body, and even more, that he had the power of God to forgive."
    ],
    "devotional": {
      "bigIdea": "Four friends would not let anything, not even a roof, keep their friend from Jesus. And Jesus gave the man something even greater than the ability to walk: he forgave his sins, showing that he has the very power of God. Good friends bring each other to Jesus, and Jesus heals us inside and out.",
      "questions": [
        "The four friends went to great lengths to get their friend to Jesus. How can you help bring your friends closer to Jesus?",
        "Jesus forgave the man's sins before he healed his legs. Why do you think Jesus cared about that even more?",
        "The man had to get up and walk when Jesus told him to. When has trusting Jesus meant actually doing something?"
      ]
    },
    "tags": ["friendship", "faith", "forgiveness", "healing", "Jesus"],
    "quiz": [
      {"question": "Why couldn't the friends get their friend to Jesus the normal way?", "options": ["The house was too crowded", "It was locked", "It was night"], "answer": 0, "explanation": ""},
      {"question": "How did the four friends get their friend to Jesus?", "options": ["They lowered him through the roof", "They waited a week", "They gave up"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus say to the man first?", "options": ["Your sins are forgiven", "Go away", "Pay me first"], "answer": 0, "explanation": ""},
      {"question": "Why were the teachers upset?", "options": ["They thought only God could forgive sins", "It was too loud", "The roof was broken"], "answer": 0, "explanation": "They did not understand that Jesus is God."},
      {"question": "What did the healed man do?", "options": ["Got up, took his mat, and walked home", "Stayed on his mat", "Ran and hid"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Mark 2",
    "hook": "Four friends wanted to bring their friend to Jesus. The house was so full that they had to lower him down through the roof!",
    "story": [
      "Jesus was teaching inside a house. So many people came that the house was packed full, with no room left at all.",
      "In that town was a man who could not walk. He had four good friends who knew Jesus could help him.",
      "They carried their friend on his mat all the way to the house. But they could not get inside, because it was too crowded.",
      "So the friends had a bold idea! They carried their friend up to the flat roof and made a hole in it.",
      "Then they carefully lowered their friend down on his mat, right in front of Jesus!",
      "When Jesus saw how much the friends believed, he was glad. He said to the man, \"Your sins are forgiven.\"",
      "Then Jesus said, \"Get up, pick up your mat, and go home.\"",
      "Right away, the man stood up! He picked up his mat and walked out, all better!",
      "Everyone was amazed and praised God. \"We have never seen anything like this!\" they said.",
      "Good friends bring each other to Jesus. And Jesus made the man well, both inside and out."
    ],
    "devotional": {
      "bigIdea": "Four friends would not let anything stop them from bringing their friend to Jesus. Jesus forgave him and made him walk. Good friends help each other get close to Jesus.",
      "questions": [
        "The friends worked so hard to bring their friend to Jesus. How can you help a friend?",
        "Jesus made the man well. What do you want to thank Jesus for?",
        "What was the most exciting part of this story?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["friendship", "faith", "healing"],
    "quiz": [
      {"question": "Why couldn't the friends get inside?", "options": ["The house was too crowded", "The door was locked", "It was raining"], "answer": 0, "explanation": ""},
      {"question": "How did they get their friend to Jesus?", "options": ["Through a hole in the roof", "Through a window", "They gave up"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus do for the man?", "options": ["Forgave him and made him walk", "Sent him away", "Nothing"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "calm-storm", "era": "nt-life", "emoji": "⛵",
  "title": "Jesus Calms the Storm", "date": "c. AD 28", "location": "The Sea of Galilee",
  "connections": [
    {"title": "Stepping Out", "storyId": "walk-on-water", "reference": "Matthew 14:25",
     "why": "Another night on the same lake where Jesus shows that the wind and waves are no match for him."},
    {"title": "Come, Follow Me", "storyId": "call-disciples", "reference": "Mark 1:17",
     "why": "The frightened men in the boat are the fishermen Jesus called, learning that the one they followed has power over creation itself."},
    {"title": "In the Beginning", "storyId": "creation", "reference": "Mark 4:41",
     "why": "The disciples ask, who is this that even the wind and waves obey him? The answer is the very One who made the sea in the beginning."}
  ],
  "tier1": {
    "book": "Mark 4",
    "hook": "A furious storm slammed into the little boat, and the disciples were sure they were going to drown. And there, in the back of the boat, Jesus was fast asleep.",
    "story": [
      "It had been a long day of teaching, and as evening came, Jesus said to his disciples, \"Let us cross over to the other side of the lake.\" So they set off in their boat across the Sea of Galilee, with Jesus among them.",
      "Jesus was so tired that he lay down in the back of the boat, put his head on a cushion, and fell fast asleep.",
      "Then, without warning, a fierce storm swept down on the lake. The wind howled, and the waves grew higher and higher, crashing over the sides of the boat. Water poured in, and the little boat began to fill up. Even the disciples, who were experienced fishermen, were terrified.",
      "But through all of it, Jesus kept sleeping peacefully in the back. The disciples could not believe it. They shook him awake, crying out, \"Teacher! Don't you care that we are about to drown?\"",
      "Jesus stood up in the rocking boat. He spoke to the wind, and he said to the raging waves, \"Quiet! Be still!\" And in an instant, the wind died down, and the water became completely calm. The storm was simply gone, as if it had never been there at all.",
      "Then Jesus turned to his friends. \"Why are you so afraid?\" he asked them gently. \"Do you still have no faith?\" He was not angry, but he wanted them to learn to trust him, even in the storm.",
      "The disciples were filled with awe, and they whispered to one another, \"Who is this? Even the wind and the waves obey him!\" They were beginning to understand the answer. The one asleep in their boat was the very One who made the wind and the sea in the beginning. And he was right there with them, in the storm, the whole time."
    ],
    "devotional": {
      "bigIdea": "The disciples thought they were all alone against the storm, but Jesus was in the boat the whole time, and the wind and waves obeyed his voice. When the storms of life crash over us, we are never alone. The One who made the sea is with us, and we can trust him.",
      "questions": [
        "The disciples were terrified, but Jesus was peacefully asleep. What do you think made the difference between his peace and their fear?",
        "Jesus was in the boat the whole time. When you feel scared, what helps you remember that God is with you?",
        "The wind and waves obeyed Jesus instantly. What does that show you about how powerful Jesus is?"
      ]
    },
    "tags": ["fear", "faith", "Jesus' power", "trust", "storms"],
    "quiz": [
      {"question": "What was Jesus doing when the storm hit?", "options": ["Sleeping in the back of the boat", "Fishing", "Swimming"], "answer": 0, "explanation": ""},
      {"question": "Why were the disciples so afraid?", "options": ["The storm was filling the boat with water", "It was dark", "They were lost"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus say to the wind and waves?", "options": ["Quiet! Be still!", "Go faster!", "Goodbye!"], "answer": 0, "explanation": ""},
      {"question": "What happened after Jesus spoke?", "options": ["The storm stopped and it was completely calm", "It got worse", "Nothing"], "answer": 0, "explanation": ""},
      {"question": "What did the disciples learn about Jesus?", "options": ["Even the wind and waves obey him", "He was a good sailor", "He liked storms"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Mark 4",
    "hook": "A scary storm shook the little boat, and the disciples were afraid. But Jesus was fast asleep in the back!",
    "story": [
      "After a long day, Jesus said to his friends, \"Let's go across the lake.\" So they all got into a boat together.",
      "Jesus was very tired. He lay down in the back of the boat, rested his head on a pillow, and fell fast asleep.",
      "Suddenly, a big storm came. The wind blew hard, and huge waves crashed over the sides of the boat.",
      "Water started filling up the boat! The disciples were so scared, even though many of them were fishermen.",
      "But Jesus was still sleeping peacefully. The friends woke him up and cried, \"Teacher! Don't you care that we might drown?\"",
      "Jesus stood up. He spoke to the wind and the waves and said, \"Quiet! Be still!\"",
      "And right away, the wind stopped and the water became calm and smooth. The storm was all gone!",
      "Jesus asked his friends gently, \"Why were you so afraid? Don't you trust me?\"",
      "The disciples were amazed. \"Who is this?\" they whispered. \"Even the wind and waves obey him!\"",
      "Jesus was with them the whole time. When we are scared, Jesus is with us too, and we can trust him."
    ],
    "devotional": {
      "bigIdea": "A big storm scared the disciples, but Jesus calmed it with just his words. Jesus was with them the whole time. When we are scared, Jesus is with us, and we can trust him.",
      "questions": [
        "The disciples were scared, but Jesus was calm. What helps you feel calm when you are afraid?",
        "Jesus was in the boat the whole time. How does it help to know Jesus is with you?",
        "What does it show you that the wind and waves obeyed Jesus?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["fear", "faith", "Jesus' power"],
    "quiz": [
      {"question": "What was Jesus doing when the storm came?", "options": ["Sleeping in the boat", "Swimming", "Fishing"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus say to the storm?", "options": ["Quiet! Be still!", "Hello!", "Faster!"], "answer": 0, "explanation": ""},
      {"question": "What happened after Jesus spoke?", "options": ["The storm stopped and it was calm", "It rained more", "The boat sank"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-05a.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-05a.json with {len(batch)} stories.")
