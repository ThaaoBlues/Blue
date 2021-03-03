from jokeapi import Jokes
from locale import getlocale


def initialize(voice_command,sentences):
    j = Jokes()
    joke = j.get_joke(blacklist=['racist','nsfw'],lang=getlocale()[0][:2])
    
    try:
        if joke['error'] != "":
            joke = j.get_joke(blacklist=['racist','nsfw'],lang="en")

    except:
        pass

    if joke["type"] == "single":
        return True, joke["joke"]

    else:
        return True, joke["setup"] + "."+joke["delivery"]

    
