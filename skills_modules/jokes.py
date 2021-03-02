from jokeapi import Jokes
from locale import getlocale


def initialize(voice_command,sentences):
    j = Jokes()
    joke = j.get_joke(blacklist=['racist'],lang=getlocale()[0][:2])

    if joke["type"] == "single":
        return True, joke["joke"]

    else:
        return True, joke["setup"] + "."+joke["delivery"]

    
