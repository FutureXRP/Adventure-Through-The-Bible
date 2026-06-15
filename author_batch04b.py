#!/usr/bin/env python3
"""Authoring source for Batch 4b (the start of Jesus' ministry). Writes batch-04b.json."""
import json

batch = [
{
  "id": "baptism", "era": "nt-life", "emoji": "🕊️",
  "title": "Jesus Is Baptized", "date": "c. AD 27", "location": "The Jordan River",
  "connections": [
    {"title": "Impossible News", "storyId": "annunciation", "reference": "Matthew 3:17",
     "why": "The Father calls Jesus his beloved Son, the very child the angel had promised would be called the Son of God."},
    {"title": "Tested in the Wilderness", "storyId": "temptation", "reference": "Matthew 4:1",
     "why": "Right after his baptism, the same Spirit who came down like a dove leads Jesus into the wilderness to be tested."},
    {"title": "In the Beginning", "storyId": "creation", "reference": "Genesis 1:2",
     "why": "As at creation the Spirit hovered over the waters and God spoke, here the Spirit descends over the water and the Father's voice is heard."}
  ],
  "tier1": {
    "book": "Matthew 3",
    "hook": "Out in the wilderness, a wild-looking preacher named John was calling everyone to get ready for God. Then one day the very Son of God walked down to the river and asked to be baptized.",
    "story": [
      "In the wilderness near the Jordan River, a man named John was preaching. He wore rough clothes made of camel's hair and ate locusts and wild honey, and crowds came from everywhere to hear him. \"Turn back to God!\" he told them. \"Get your hearts ready, because someone far greater than I am is coming.\"",
      "People who were sorry for the wrong they had done came to John, and he baptized them in the river, dipping them under the water as a sign that God was washing them clean and they were starting fresh.",
      "Then one day Jesus himself came to the river and asked John to baptize him. John was shocked. \"It should be the other way around,\" he said. \"I need to be baptized by you! Why are you coming to me?\" Jesus had never done anything wrong, so he did not need to be washed clean like the others.",
      "But Jesus answered, \"Let it be this way for now. It is right for us to do this.\" Jesus wanted to stand together with the people he came to save, doing everything the right way. So John agreed and baptized him.",
      "The moment Jesus came up out of the water, something wonderful happened. The sky opened up, and the Spirit of God came down gently, like a dove, and rested on him.",
      "And a voice came from heaven, the voice of God the Father, saying, \"This is my Son, whom I love. With him I am very pleased.\"",
      "In that one amazing moment by the river, all three were there together: the Son coming up from the water, the Spirit resting on him like a dove, and the Father speaking from heaven. And the very first thing the Father said about his Son was how much he loved him and delighted in him, before Jesus had preached a single sermon or done a single miracle."
    ],
    "devotional": {
      "bigIdea": "Before Jesus had done any of his great works, the Father announced from heaven, This is my Son, whom I love, and with him I am well pleased. God's love came first, not as a reward for doing enough. That is how God loves his children: not because of what we do, but because we are his.",
      "questions": [
        "The Father said he loved his Son before Jesus had done any miracles. How does it feel to know God loves you not for what you do, but just because you are his?",
        "Jesus did not need to be baptized, but he did it to stand with us. What does that show you about Jesus?",
        "The Father, Son, and Spirit were all there at the river. What do you find amazing about that?"
      ]
    },
    "tags": ["Jesus", "the Father's love", "the Trinity", "new beginnings", "John the Baptist"],
    "quiz": [
      {"question": "Who was preaching in the wilderness and baptizing people?", "options": ["John the Baptist", "Moses", "Peter"], "answer": 0, "explanation": ""},
      {"question": "Why was John surprised that Jesus came to him?", "options": ["John felt Jesus should baptize him instead", "Jesus was late", "Jesus had no money"], "answer": 0, "explanation": "Jesus had never sinned, so he did not need washing like the others."},
      {"question": "What came down on Jesus like a dove?", "options": ["The Spirit of God", "A real bird", "Rain"], "answer": 0, "explanation": ""},
      {"question": "What did the voice from heaven say?", "options": ["This is my Son, whom I love", "Come back later", "Build a temple"], "answer": 0, "explanation": ""},
      {"question": "Who was present at the river?", "options": ["The Father, the Son, and the Spirit", "Only Jesus", "Only John"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Matthew 3",
    "hook": "A preacher named John was getting people ready for God. Then Jesus came to the river, and heaven opened up!",
    "story": [
      "Out in the wilderness, a man named John was preaching by the Jordan River. He wore clothes made of camel hair and ate locusts and wild honey.",
      "John told everyone, \"Turn back to God! Get your hearts ready, because someone much greater than me is coming.\"",
      "People who were sorry for the wrong things they had done came to John, and he baptized them in the river to show they were starting fresh with God.",
      "Then one day, Jesus came to the river and asked John to baptize him too.",
      "John was surprised. \"You should baptize me!\" he said. But Jesus said, \"It is right for us to do this.\" So John baptized Jesus.",
      "The moment Jesus came up out of the water, the sky opened up!",
      "The Spirit of God came down softly, like a gentle dove, and rested on Jesus.",
      "Then God the Father spoke from heaven. He said, \"This is my Son, whom I love. I am very pleased with him.\"",
      "God said he loved his Son before Jesus had done any miracles at all. God loves us that same way, just because we are his children."
    ],
    "devotional": {
      "bigIdea": "God the Father said he loved Jesus before Jesus had done anything. God loves us that way too, not for what we do, but just because we are his children.",
      "questions": [
        "God said he loved his Son right away. How does it feel that God loves you just because you are his?",
        "Jesus was baptized to stand with us. What does that tell you about Jesus?",
        "What do you think it was like to hear God's voice from heaven?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["Jesus", "the Father's love", "John the Baptist"],
    "quiz": [
      {"question": "Who baptized people in the river?", "options": ["John", "Pharaoh", "Goliath"], "answer": 0, "explanation": ""},
      {"question": "What came down on Jesus like a dove?", "options": ["The Spirit of God", "Snow", "A leaf"], "answer": 0, "explanation": ""},
      {"question": "What did God say from heaven?", "options": ["This is my Son, whom I love", "Go home", "Build a boat"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "temptation", "era": "nt-life", "emoji": "🏜️",
  "title": "Tested in the Wilderness", "date": "c. AD 27", "location": "The Wilderness",
  "connections": [
    {"title": "Jesus Is Baptized", "storyId": "baptism", "reference": "Matthew 4:1",
     "why": "Straight from the joy of his baptism, the Spirit leads Jesus into the desert to be tested before his ministry begins."},
    {"title": "The First Bad Choice", "storyId": "adam-eve", "reference": "Romans 5:19",
     "why": "Where Adam and Eve gave in to the tempter in a beautiful garden, Jesus stands firm against him in a barren desert."},
    {"title": "The Ten Commandments", "storyId": "ten-commandments", "reference": "Matthew 4:4",
     "why": "Jesus fights every temptation with God's own words, the Scriptures, showing how powerful and precious they are."}
  ],
  "tier1": {
    "book": "Matthew 4",
    "hook": "Right after his baptism, the Spirit led Jesus deep into the desert, where he went without food for forty days. Then, when he was at his weakest, the tempter came.",
    "story": [
      "After Jesus was baptized, the Spirit of God led him out into the lonely wilderness. There Jesus went without any food for forty days and forty nights, praying and preparing for the work ahead. By the end, he was very, very hungry.",
      "That was when the tempter, the devil, came to him. \"If you really are the Son of God,\" he sneered, \"then tell these stones to turn into bread.\" It would have been so easy, and Jesus was starving. But Jesus answered with God's own words: \"It is written: People do not live on bread alone, but on every word that comes from the mouth of God.\"",
      "Next the devil took Jesus to the highest point of the temple. \"If you are the Son of God, jump off! Doesn't the Bible say God's angels will catch you?\" He was twisting Scripture to dare Jesus into a foolish stunt. But Jesus answered, \"It also says: Do not put the Lord your God to the test.\"",
      "Then the devil showed Jesus all the kingdoms of the world in all their glory. \"I will give all of this to you,\" he promised, \"if you will just bow down and worship me.\" He offered Jesus the whole world for the price of his loyalty to God.",
      "But Jesus would not. \"Away from me, Satan!\" he said. \"For it is written: Worship the Lord your God, and serve only him.\" Three times the devil tempted him, and three times Jesus stood firm, holding tight to his Father and to the word of God.",
      "Then the devil left him, defeated. And angels came and took care of Jesus, bringing him what he needed after his long, hard test.",
      "Long ago, Adam and Eve had everything they could want in a beautiful garden, and still they gave in to the tempter. Now Jesus, with nothing at all in a barren desert, said no. He won the battle we could never win, and because he understands exactly what it feels like to be tempted, he is able to help us when we are tempted too."
    ],
    "devotional": {
      "bigIdea": "Jesus was tempted just like we are, but he never gave in. He fought back every time with the words of God. Because Jesus faced temptation and won, he understands our struggles and gives us his own strength to say no to what is wrong.",
      "questions": [
        "Jesus answered each temptation with words from the Bible. Why do you think knowing God's word helps us when we are tempted?",
        "The devil offered Jesus the whole world if he would just stop following God. What things sometimes tempt us to stop doing what is right?",
        "Jesus understands what it feels like to be tempted. How does it help to know that Jesus understands and can help you?"
      ]
    },
    "tags": ["temptation", "obedience", "God's Word", "Jesus", "victory"],
    "quiz": [
      {"question": "Where did the Spirit lead Jesus after his baptism?", "options": ["Into the wilderness", "To a palace", "Across the sea"], "answer": 0, "explanation": ""},
      {"question": "How long did Jesus go without food?", "options": ["Forty days and nights", "One day", "A week"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus use to answer every temptation?", "options": ["The words of God from the Scriptures", "A loud shout", "A sword"], "answer": 0, "explanation": ""},
      {"question": "What did the devil offer Jesus if he would bow down?", "options": ["All the kingdoms of the world", "A loaf of bread", "A long rest"], "answer": 0, "explanation": ""},
      {"question": "What happened after Jesus refused every temptation?", "options": ["The devil left, and angels cared for him", "Jesus gave up", "Nothing"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Matthew 4",
    "hook": "Right after Jesus was baptized, he went into the desert. He was very hungry when the devil came to tempt him to do wrong.",
    "story": [
      "After Jesus was baptized, God's Spirit led him out into the desert.",
      "Jesus stayed there for forty days and forty nights with no food at all. By the end, he was very, very hungry.",
      "Then the devil came to tempt Jesus, to try to get him to do wrong. \"If you are God's Son,\" he said, \"turn these stones into bread!\"",
      "But Jesus said no. He answered with God's words: \"People do not live on bread alone, but on every word from God.\"",
      "The devil tried again. He took Jesus up high and said, \"Jump off! God's angels will catch you.\" But Jesus said, \"Do not test God.\"",
      "Then the devil showed Jesus all the kingdoms of the world. \"I will give them all to you,\" he said, \"if you bow down to me.\"",
      "But Jesus said, \"Go away! We must worship and obey God alone.\"",
      "Three times the devil tried, and three times Jesus said no by trusting God and God's words.",
      "Finally the devil gave up and left. Then angels came and took care of Jesus.",
      "Jesus knows just what it feels like to be tempted. So he can help us say no to wrong things too."
    ],
    "devotional": {
      "bigIdea": "The devil tried three times to get Jesus to do wrong, but Jesus said no every time by trusting God and God's words. Jesus understands when we are tempted, and he helps us do what is right.",
      "questions": [
        "Jesus said no to wrong things by remembering God's words. How can knowing about God help you do right?",
        "What is something that sometimes tempts you to not do the right thing?",
        "Jesus understands when things are hard. How does it help to know Jesus can help you?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["temptation", "obedience", "Jesus"],
    "quiz": [
      {"question": "Where did Jesus go after his baptism?", "options": ["The desert", "A castle", "A boat"], "answer": 0, "explanation": ""},
      {"question": "How did Jesus answer the devil each time?", "options": ["With God's words", "By running", "By hiding"], "answer": 0, "explanation": ""},
      {"question": "How many times did Jesus say no to the devil?", "options": ["Three times", "Never", "One time"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "call-disciples", "era": "nt-life", "emoji": "🎣",
  "title": "Come, Follow Me", "date": "c. AD 27", "location": "The Sea of Galilee",
  "connections": [
    {"title": "Five Loaves and Two Fish", "storyId": "feeding-5000", "reference": "Matthew 4:19",
     "why": "These ordinary fishermen Jesus calls become the disciples who help him feed thousands and learn from him every day."},
    {"title": "Stepping Out", "storyId": "walk-on-water", "reference": "Matthew 14:29",
     "why": "Simon Peter, who drops his nets here to follow Jesus, will later step out of a boat to walk to him on the water."},
    {"title": "The Man Who Walked Away", "storyId": "rich-young-ruler", "reference": "Mark 10:22",
     "why": "The fishermen leave everything in a heartbeat to follow Jesus, unlike the rich young man who walks away sad, unwilling to let go."}
  ],
  "tier1": {
    "book": "Matthew 4",
    "hook": "Jesus did not start his work by choosing kings or scholars. He walked along a lake and called a few ordinary fishermen with three simple words: Come, follow me.",
    "story": [
      "Jesus began to travel around telling people the good news that God's kingdom was near. One day he was walking beside the Sea of Galilee, a large and beautiful lake where many people made their living by fishing.",
      "There he saw two brothers, Simon Peter and Andrew, throwing their net into the water, for they were fishermen. Jesus called out to them, \"Come, follow me, and I will make you fishers of people.\" And at once, right then and there, they left their nets and followed him.",
      "A little farther along, Jesus saw two more brothers, James and John, in a boat with their father, mending their fishing nets. Jesus called them too. Immediately they left the boat and their father and went with Jesus.",
      "Think about how amazing that is. Jesus did not go to the palace to find princes, or to the schools to find the smartest scholars. He walked along a lake and called rough, ordinary, hardworking fishermen, men who smelled of fish and knew nothing fancy.",
      "And when Jesus called, they did not say, \"Let us think about it,\" or \"Maybe next year.\" They dropped what they were doing and followed him right away. They left behind their boats, their nets, and the only work they had ever known, all to be with Jesus.",
      "Over time Jesus gathered twelve close followers, called disciples, an ordinary bunch including fishermen and even a tax collector that most people hated. These were the people Jesus would teach and love and send out to change the world.",
      "Jesus still calls ordinary people today. He does not wait for us to be important or perfect or to have it all figured out. He simply says, Come, follow me, and asks us to trust him enough to go."
    ],
    "devotional": {
      "bigIdea": "Jesus chose ordinary fishermen, not the rich or the famous or the experts. He called them with two simple words, follow me, and they left everything to go. Jesus calls ordinary people like us too. He is not looking for perfect people. He is looking for people who will trust him and come.",
      "questions": [
        "The fishermen left their nets right away to follow Jesus. Is there anything that might be hard for you to leave behind to follow Jesus?",
        "Jesus chose ordinary people, not famous or important ones. How does it feel to know Jesus wants you just as you are?",
        "Jesus said, follow me. What do you think it looks like to follow Jesus in your everyday life?"
      ]
    },
    "tags": ["following Jesus", "the disciples", "trust", "ordinary people", "calling"],
    "quiz": [
      {"question": "What were Simon Peter and Andrew doing when Jesus called them?", "options": ["Fishing", "Sleeping", "Building a house"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus say to them?", "options": ["Come, follow me", "Go away", "Bring me gold"], "answer": 0, "explanation": ""},
      {"question": "How quickly did they follow Jesus?", "options": ["At once, leaving their nets", "After a year", "They did not go"], "answer": 0, "explanation": ""},
      {"question": "What kind of people did Jesus choose as his disciples?", "options": ["Ordinary people like fishermen", "Only kings", "Only scholars"], "answer": 0, "explanation": ""},
      {"question": "What does Jesus still say to people today?", "options": ["Come, follow me", "Stay away", "Earn it first"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Matthew 4",
    "hook": "Jesus walked by a big lake and saw some fishermen. He said three simple words that changed their lives: Come, follow me.",
    "story": [
      "Jesus began to travel and tell people the good news about God.",
      "One day he was walking beside a big lake called the Sea of Galilee, where lots of people caught fish for their job.",
      "Jesus saw two brothers, Simon Peter and Andrew, throwing their fishing net into the water.",
      "Jesus called to them, \"Come, follow me, and I will make you fishers of people!\"",
      "Right away, they left their nets and went with Jesus!",
      "A little farther down, Jesus saw two more brothers, James and John, fixing their nets in a boat.",
      "Jesus called them too. And right away, they left their boat and followed him.",
      "Jesus did not pick kings or the smartest people. He picked ordinary, hardworking fishermen.",
      "And when Jesus called, they did not wait. They followed him right away.",
      "Jesus still calls ordinary people like us today. He says, Come, follow me!"
    ],
    "devotional": {
      "bigIdea": "Jesus called ordinary fishermen, and they followed him right away. Jesus calls ordinary people like us too. He just wants us to trust him and follow.",
      "questions": [
        "The fishermen followed Jesus right away. What do you think it means to follow Jesus?",
        "Jesus picked ordinary people. How does it feel that Jesus wants you?",
        "Is there something that would be hard to leave to follow Jesus?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["following Jesus", "the disciples", "trust"],
    "quiz": [
      {"question": "What job did Simon Peter and Andrew have?", "options": ["They were fishermen", "They were kings", "They were farmers"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus say to them?", "options": ["Come, follow me", "Go home", "Give me a fish"], "answer": 0, "explanation": ""},
      {"question": "How fast did they follow Jesus?", "options": ["Right away", "After many years", "They did not"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "cana", "era": "nt-life", "emoji": "🏺",
  "title": "Water into Wine", "date": "c. AD 27", "location": "Cana in Galilee",
  "connections": [
    {"title": "Impossible News", "storyId": "annunciation", "reference": "John 2:5",
     "why": "It is Mary, the mother who once said yes to God, who tells the servants here, do whatever he tells you."},
    {"title": "Five Loaves and Two Fish", "storyId": "feeding-5000", "reference": "John 2:11",
     "why": "Just as Jesus would make a little food feed thousands, here he makes ordinary water into the very best wine, with plenty to spare."},
    {"title": "The Night Before", "storyId": "last-supper", "reference": "John 2:11",
     "why": "Jesus' first sign uses cups of wine at a joyful feast, pointing ahead to the cup he shares with his friends the night before he dies."}
  ],
  "tier1": {
    "book": "John 2",
    "hook": "Jesus' very first miracle was not healing a sickness or calming a storm. It happened at a wedding party, when the host ran out of wine and the celebration was about to be ruined.",
    "story": [
      "Jesus, his mother Mary, and his disciples were all invited to a wedding in the town of Cana. In those days, a wedding was a huge celebration that could last for days, with feasting and joy for the whole village.",
      "But partway through, something went wrong. The wine ran out. This was a terrible embarrassment for the family hosting the wedding, the kind of thing people would talk about for years. Mary noticed, and she came to Jesus and said simply, \"They have no more wine.\"",
      "Jesus said, \"Dear woman, why come to me? My time has not yet come.\" But Mary trusted her son completely. She turned to the servants nearby and told them, \"Do whatever he tells you.\"",
      "Standing close by were six large stone jars, the kind used for washing. Each one could hold a huge amount of water. Jesus said to the servants, \"Fill the jars with water.\" So they filled them right up to the brim.",
      "Then Jesus said, \"Now dip some out and take it to the master in charge of the feast.\" The servants did, wondering what was happening. But when the master of the feast tasted it, the water had become wine, and not just any wine, the very best wine of all.",
      "The master did not know where it had come from, but he was amazed. He called the bridegroom over and said, \"Everyone serves the good wine first and saves the cheap wine for last. But you have saved the best wine until now!\"",
      "This was the first of Jesus' miraculous signs, and it showed his glory, and his disciples believed in him. It is a beautiful thing that Jesus chose a happy wedding for his first miracle. It shows that he cares about our joys and our celebrations, not only our troubles, and that whatever he touches, he makes wonderfully good."
    ],
    "devotional": {
      "bigIdea": "Jesus' first miracle was at a joyful wedding, saving the celebration and providing the very best. It shows that Jesus cares about every part of our lives, the happy times as well as the hard ones, and that whatever he touches, he makes good. And Mary's advice is still the best there is: do whatever he tells you.",
      "questions": [
        "Mary told the servants, do whatever he tells you. Why is that such good advice for us, too?",
        "Jesus made the very best wine, more than enough. What does that tell you about how generous God is?",
        "Jesus' first miracle was at a happy party, not a sad place. What does that show you about the things Jesus cares about?"
      ]
    },
    "tags": ["Jesus", "miracles", "joy", "trust", "generosity"],
    "quiz": [
      {"question": "Where did Jesus do his first miracle?", "options": ["At a wedding in Cana", "On a mountain", "In a boat"], "answer": 0, "explanation": ""},
      {"question": "What problem happened at the wedding?", "options": ["The wine ran out", "It started raining", "The food burned"], "answer": 0, "explanation": ""},
      {"question": "What did Mary tell the servants?", "options": ["Do whatever he tells you", "Go home", "Hide the jars"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus turn the water into?", "options": ["The very best wine", "Milk", "Gold"], "answer": 0, "explanation": ""},
      {"question": "What did this first miracle show?", "options": ["Jesus' glory, and his disciples believed in him", "That weddings are long", "That water is good"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "John 2",
    "hook": "Jesus' very first miracle happened at a wedding party, when the drinks ran out and everyone was worried.",
    "story": [
      "Jesus, his mother Mary, and his friends were all invited to a big wedding party in a town called Cana.",
      "Back then, a wedding was a huge celebration with lots of food and fun for many days.",
      "But in the middle of the party, something went wrong. They ran out of wine to drink! This was very embarrassing for the family.",
      "Mary went to Jesus and said, \"They have no more wine.\" Then she told the servants, \"Do whatever Jesus tells you.\"",
      "Nearby were six great big stone jars. Jesus said to the servants, \"Fill the jars all the way up with water.\" So they did.",
      "Then Jesus said, \"Now dip some out and take it to the man in charge of the party.\"",
      "When the man tasted it, the water had turned into wine! And it was the very best wine of all!",
      "\"Most people serve the best first,\" he said, \"but you saved the best for last!\" He could not believe how good it was.",
      "This was Jesus' very first miracle. It showed how amazing and powerful he is.",
      "Jesus did his first miracle at a happy party. That shows us Jesus cares about our happy times too, and he makes everything good."
    ],
    "devotional": {
      "bigIdea": "Jesus' first miracle was at a happy wedding, where he made the very best wine. Jesus cares about our happy times too, and whatever he touches, he makes good.",
      "questions": [
        "Mary said, do whatever Jesus tells you. Why is that good advice for us?",
        "Jesus made the best wine, more than enough. What does that show about God?",
        "Jesus' first miracle was at a happy party. What does that tell you about Jesus?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["Jesus", "miracles", "joy"],
    "quiz": [
      {"question": "Where did Jesus do his first miracle?", "options": ["At a wedding party", "On a boat", "In a cave"], "answer": 0, "explanation": ""},
      {"question": "What ran out at the party?", "options": ["The wine to drink", "The chairs", "The music"], "answer": 0, "explanation": ""},
      {"question": "What did Jesus turn the water into?", "options": ["The best wine", "Juice", "Ice"], "answer": 0, "explanation": ""}
    ]
  }
},
{
  "id": "sower", "era": "nt-life", "emoji": "🌱",
  "title": "The Farmer and the Seeds", "date": "c. AD 28", "location": "By the Sea of Galilee",
  "connections": [
    {"title": "The Tiny Mustard Seed", "storyId": "mustard-seed", "reference": "Mark 4:31",
     "why": "Another of Jesus' seed stories about God's kingdom, showing how something tiny can grow into something great."},
    {"title": "The Upside-Down Kingdom", "storyId": "sermon-mount", "reference": "Matthew 7:24",
     "why": "Like the wise builder who hears Jesus and obeys, the good soil stands for those who hear God's word and let it take root."},
    {"title": "The Boy Who Came Home", "storyId": "prodigal", "reference": "Luke 15:11",
     "why": "Jesus loved to teach with stories, and like the prodigal son, the parable of the sower reveals what our hearts are really like."}
  ],
  "tier1": {
    "book": "Matthew 13",
    "hook": "So many people crowded around Jesus that he climbed into a boat to teach them. And he told them a story about a farmer, some seeds, and four very different kinds of ground.",
    "story": [
      "Such huge crowds gathered to hear Jesus that one day he got into a boat and pushed out a little way from the shore, so everyone on the beach could see and hear him. Then he taught them using a story, the kind of story called a parable.",
      "\"A farmer went out to scatter his seed,\" Jesus began. \"As he scattered it, some seed fell on the hard path. The birds came along and quickly ate it all up.\"",
      "\"Other seed fell on rocky ground, where there was not much soil. It sprang up fast, but because the roots could not go deep, the hot sun scorched the little plants and they withered away.\"",
      "\"Other seed fell among thorns and weeds. The seed grew, but so did the thorns, and the thorns choked the young plants so they could not grow.\"",
      "\"But other seed fell on good, rich soil. There it grew strong and healthy and produced a wonderful crop, far more than was ever planted.\" Then Jesus said, \"Whoever has ears, let them listen.\"",
      "Later, Jesus explained the story to his disciples. The seed, he said, is God's message about his kingdom. The different kinds of ground are the different ways people's hearts receive it. The hard path is the person who hears but does not understand, and the message is snatched away. The rocky ground is the person who is excited at first, but gives up the moment trouble comes, because the message never took root.",
      "\"The thorny ground,\" Jesus went on, \"is the person who hears, but lets the worries of life and the love of money choke the message out. But the good soil is the person who hears the word, understands it, holds on to it, and lets it grow. That person's life produces a beautiful crop.\" The question Jesus leaves with each of us is simple: what kind of soil is my heart?"
    ],
    "devotional": {
      "bigIdea": "The same seed fell on every kind of ground, but only the good soil grew a crop. God's word comes to everyone, but it only changes the hearts that are ready to receive it and hold on to it. The question Jesus asks each of us is: what kind of soil is my heart?",
      "questions": [
        "The same seed was scattered everywhere, but only the good soil grew a crop. What do you think makes a heart like good soil?",
        "The thorns were worries and the love of money that choked out the plants. What things might crowd God's word out of our hearts?",
        "Jesus said, whoever has ears, let them listen. What is one thing you have heard from God that you want to hold on to and let grow?"
      ]
    },
    "tags": ["God's word", "the heart", "parables", "growing", "the kingdom"],
    "quiz": [
      {"question": "Why did Jesus get into a boat to teach?", "options": ["The crowd was so big everyone could see and hear", "He was going fishing", "It was raining"], "answer": 0, "explanation": ""},
      {"question": "What happened to the seed that fell on the hard path?", "options": ["Birds ate it up", "It grew the biggest", "It turned to gold"], "answer": 0, "explanation": ""},
      {"question": "Why did the seed on rocky ground wither?", "options": ["Its roots could not go deep", "Too much rain", "Birds took it"], "answer": 0, "explanation": ""},
      {"question": "What does the seed stand for?", "options": ["God's message about his kingdom", "Real food", "Money"], "answer": 0, "explanation": ""},
      {"question": "What is the good soil like?", "options": ["A heart that hears God's word, holds on to it, and grows", "A rich person", "A fast plant"], "answer": 0, "explanation": ""}
    ]
  },
  "tier2": {
    "book": "Matthew 13",
    "hook": "So many people came to hear Jesus that he taught from a boat. He told a story about a farmer who scattered seeds on four kinds of ground.",
    "story": [
      "One day, such a big crowd came to hear Jesus that he got into a boat. He pushed out a little, so everyone on the beach could see and hear him.",
      "Then Jesus told them a story. \"A farmer went out to plant his seeds,\" he said.",
      "\"Some seeds fell on the hard path. The birds flew down and gobbled them all up.\"",
      "\"Some seeds fell on rocky ground. They grew fast, but their roots could not go deep, so the hot sun made them dry up.\"",
      "\"Some seeds fell where there were thorny weeds. The weeds grew up and crowded out the little plants.\"",
      "\"But some seeds fell on good, soft soil. Those seeds grew strong and made lots and lots of new plants!\"",
      "Later, Jesus told his friends what the story meant. The seed is God's word, the good news about him.",
      "The different grounds are like different hearts. Some people hear God's word but forget it, or give up, or let other things crowd it out.",
      "But the good soil is a heart that hears God's word, holds it close, and lets it grow big and strong.",
      "Jesus wants us to have hearts like the good soil, ready to listen to God and let his word grow in us."
    ],
    "devotional": {
      "bigIdea": "The same seeds fell everywhere, but only the good soil grew a big crop. God's word grows best in a heart that listens and holds on to it. Jesus wants our hearts to be like good soil.",
      "questions": [
        "What do you think makes a heart like good soil?",
        "Some things crowded out the little plants. What things might keep us from listening to God?",
        "How can you keep your heart soft and ready to listen to God?"
      ]
    },
    "devotionalHeading": "Let's Talk About It",
    "tags": ["God's word", "the heart", "parables"],
    "quiz": [
      {"question": "Why did Jesus teach from a boat?", "options": ["The crowd was very big", "He was fishing", "He was tired"], "answer": 0, "explanation": ""},
      {"question": "What did the seed in the story stand for?", "options": ["God's word", "Real food", "Money"], "answer": 0, "explanation": ""},
      {"question": "What kind of heart does Jesus want us to have?", "options": ["A heart like good soil", "A hard path", "A thorny patch"], "answer": 0, "explanation": ""}
    ]
  }
}
]

with open("batch-04b.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print(f"Wrote batch-04b.json with {len(batch)} stories.")
