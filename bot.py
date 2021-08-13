import datetime
import random

def bot_answer(req):
    req = req.lower()

    if 'hi' in req or 'hello' in req:
        return "Hello! Wish you had a good day :>"
    elif 'name' in req:
        return "You can call me Valrhona."
    elif 'who' in req:
        return "I'm a bot who you just created."
    elif 'what' in req and 'time' in req:
        now = datetime.datetime.now()
        return "It's %s %s" % (now.hour, now.minute)
    elif 'how' in req and 'you' in req:
        return "I'm very fine!"
    elif 'weather' in req:
        return "Aw, it's rainy today:( We shouldn't go outside!"
    elif 'temperature' in req:
        return "It's about 23 degrees."
    elif 'color' in req:
        return "I love red."
    elif 'song' in req:
        return "'What makes you beautiful' by One Direction."
    elif 'movie' in req:
        return "Ratatouille."
    elif 'university' in req or 'itmo' in req:
        return "ITMO university!"
    elif 'goodbye' in req or 'bye' in req or 'see you' in req:
        return "Goodbye! Nice to talk to you. Seeya!"
    else:
        return "Oh sorry, I am not programmed to answer you this sentence:<"

sentences = ["How are you doing?",
            "Are you still there?",
            "I'm still waiting for you!",
            "Hi?",
            "Please ask me something!",
            "How was your day?",
            "Are you good?",
            "I am listening...",
            "You are a good man, aren't you?"]

def chatting():
    return random.choice(sentences)