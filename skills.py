from utils.res import *
import importlib
import Levenshtein
from locale import getlocale
from gtts import gTTS
from random import randint
from os import remove
import playsound
from difflib import SequenceMatcher
from utils.translator import translate
from multiprocessing import Process

def check_skills(voice_command):
    with open("config/skills.blue","r",encoding="utf-8") as f:
        for line in f.read().splitlines():
            module = line.split(":")[0]
            sentences = line.split(":")[1]

            for sentence in sentences.split("/"):

                if sentence.split(" ")[0] == "startswith":
                    if(sentence.replace("startswith","",1).replace(" ","") in voice_command.replace(" ","")[:len(voice_command)//2]):
                        print(f"module : {module} | confidence : startswith keyword")
                        Process(target=call_skill,args=(module,voice_command,sentences.split("/"),)).start()
                        return True
                else:
                    ratio = SequenceMatcher(None, voice_command, sentence).ratio()

                    if (ratio>=0.65):
                        ratio = round(ratio,4)
                        print(f"module : {module} | confidence : {ratio*100}%")
                        Process(target=call_skill,args=(module,voice_command,sentences.split("/"),)).start()
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


def call_skill(module,voice_command,sentences):
    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace("startswith","",1)
        
    skill = importlib.import_module(f"skills_modules.{module}")

    ret, response = skill.initialize(voice_command,sentences)
    response = translate(response,'fr',False,dest=getlocale()[0][:2])
    print(response)
    if response != "":
        speak(response)
    