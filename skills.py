from utils.res import *
import importlib
import Levenshtein
from locale import getlocale
from gtts import gTTS
from random import randint
from os import remove
import playsound
from difflib import SequenceMatcher



def check_skills(voice_command):
    with open("config/skills.blue","r") as f:
        for line in f.read().splitlines():
            module = line.split(":")[0]
            sentences = line.split(":")[1]

            for sentence in sentences.split("/"):

                if sentence.split(" ")[0] == "startswith":
                    if(voice_command.split(" ")[0] == sentence.split(" ")[0].replace("startswith","",1)):
                        print(f"module : {module} | confidence : startswith keyword")
                        skill = importlib.import_module(f"skills_modules.{module}")

                        ret, response = skill.initialize(voice_command,sentences.split("/"))
                        print(response)
                        speak(response)
                        return True

                else:


                    ratio = SequenceMatcher(None, voice_command, sentence).ratio()

                    if (ratio>=0.6):
                        ratio = round(ratio,4)
                        print(f"module : {module} | confidence : {ratio*100}%")
                        skill = importlib.import_module(f"skills_modules.{module}")

                        ret, response = skill.initialize(voice_command,sentences.split("/"))
                        print(response)
                        speak(response)
                        return True



def speak(text):
    try:
        tts = gTTS(text,lang=getlocale()[0][:2])
        sn = str(randint(1,100000))+".mp3"
        tts.save(sn)
        playsound.playsound(sn)
        remove(sn)
    except:
        print(e)
        pass