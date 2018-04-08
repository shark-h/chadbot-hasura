import re
import random
from flask import Flask, render_template


pronounswitch = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

bot = [
    [r'hi(.*)',
     ["Hello",
      "Greetings",
      "Hi",
      "Sup!"
      ]],

    [r'hello(.*)',
     ["Hello",
      "Greetings",
      "Hi",
      "Sup!"
      ]],

    [r'(.*)bye(.*)',
     ["Cya",
      "Goodbye",
      "YEET, amirite?",
      "you\'ll see me in your dreams'",
    ]],

    [r'(.*)your name(.*)',
     ["Name\'s Chad, Chad the Chadbot!",
      "Hey, I\'m Chad!",
      "Aye, it\'s ya boi, Chad."
    ]],

    [r'(.*)favorite food(.*)',
     ["I eat anything from Chipotle, mah dude",
      "I can't get enough of Taco Bell, forreal forreal",
      "I eat salad, I\'ve been trying to get this summer bod ready, ya know wat I meaaaaaaaaaaaan ;)"
    ]],

    [r'(.*)favorite color(.*)',
     ["My favorite color is red...you know, I rock that Supreme brand all day."
    ]],

    [r'(.*)fave(.*)',
     ["Can you not use \'fave\' and actually type out \'favorite\'? k thx.",
      "uhh, \'fave'\?"
    ]],

    [r'(.*)hobby(.*)',
     ["Been on the Lax team since \'08 B)",
      "I'm always hittin/' the gym, bet you can tell.",
    ]],

    [r'(.*)hobbies(.*)',
     ["Been on the Lax team since \'08 B)",
      "I'm always hittin/' the gym, bet you can tell.",
      "I've been playin\' hella Fortnite"
    ]],
]

defaultresponse = ['Sorry, either I can\'t understand that, or you just don\'t know how chatbots work.',
                       'Sorry, I can\'t seem to understand you.']


def reflect(frag):
    tokens = frag.lower().split()
    for i, token in enumerate(tokens):
        if token in pronounswitch:
            tokens[i] = pronounswitch[token]
    return ' '.join(tokens)


def findMatch(messages):
    for pattern, responses in bot:
        match = re.match(pattern, messages.rstrip(".!"))
        if match is not None:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
        else:
            response = random.choice(defaultresponse)
            return response

def Chad():
    statement = "hello."
    message = statement.lower()
    return findMatch(message)
msg = Chad()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", msg=msg)

@app.route('/index.html')
def index():
    return render_template("index.html", msg=msg)
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/chat.html')
def chat():
    return render_template("chat.html")
if __name__ == "__main__":
    app.run()