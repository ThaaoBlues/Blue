from jokeapi import Jokes
from locale import getlocale


def initialize(voice_command,sentences):
    j = Jokes()
    return True,j.get_joke(blacklist=['racist'],lang=getlocale()[0][:2])
    
