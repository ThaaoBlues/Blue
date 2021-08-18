import re
from util.translator import translate
from util.res import *
from time import sleep
from multiprocessing import Process

def initialize(voice_command,sentences):

    match = re.findall("\d+",voice_command)

    if match == []:
        return True,"Vous n'avez pas précisé de temps. Je ne peut pas compter sans instruction claire !"

    translated_string = translate(voice_command,src=get_locale(),dest="fr")

    if "minute" in translated_string:
        #minutes
        sec = int(match[0])*60

    elif "heure" in translated_string:
        #hours
        sec = int(match[0])*3600

    else:
        #seconds
        sec = int(match[0])

    Process(target=countdown, args=(sec,)).start()

    return True, ""


def countdown(i:int):

    while i >= 0:
        
        if i <= 10:
            speak(str(i))

        sleep(1)

        i -= 1