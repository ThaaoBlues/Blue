from util.res import *
import importlib
from locale import getlocale
from gtts import gTTS
from random import randint
from os import remove
import playsound
from difflib import SequenceMatcher
from util.translator import translate
from multiprocessing import Process

def check_skills(voice_command):
    
    
    with open("config/skills.blue","r",encoding="utf-8") as f:
        ratio = 0
        module = ""
        final_sentences = ""
        for line in f.read().splitlines():
            
            sentences = line.split(":")[1]

            for sentence in sentences.split("/"):

                if sentence.split(" ")[0] == "startswith":
                    if(sentence.replace("startswith","",1).replace(" ","") in voice_command.replace(" ","")[:len(voice_command)//2]):
                        final_sentences = sentences
                        module = line.split(":")[0]
                        print(f"module : {module} | confidence : startswith keyword")
                        Process(target=call_skill,args=(module,voice_command,sentences.split("/"),)).start()
                        return True
                else:
                   
                    r = SequenceMatcher(None, voice_command, sentence).ratio()

                    if r > ratio:
                        final_sentences = sentences
                        ratio = r
                        module = line.split(":")[0]

                    
        ratio = round(ratio,4)
        print(f"module : {module} | confidence : {ratio*100}%")

        Process(target=call_skill,args=(module,voice_command,final_sentences.split("/"),)).start()
        return True




def speak(text):
    try:
        tts = gTTS(text,lang=getlocale()[0][:2])
        sn = str(randint(1,100000))+".mp3"
        tts.save(sn)
        playsound.playsound(sn)
        remove(sn)
    except Exception as e:
        print(e)
        pass


def call_skill(module,voice_command,sentences):


    for i in range(len(sentences)):
        sentences[i] = sentences[i].replace("startswith","",1)
    
    try:
        skill = importlib.import_module(f"skills_modules.{module}")
    except Exception as e:
        perror(f"Error while importing skill module : {e}")
        return

    ret, response = skill.initialize(voice_command,sentences)

    try:
        if getlocale()[0][:2] != 'fr':
            response = translate(response,'fr',dest=getlocale()[0][:2])

    except Exception as e:
        perror(f"Error while translating Blue response to your language : {e}")
        return

    print(response)

    try:
        if response != "":
            speak(response)
    except Exception as e:
        perror(f"Error while trying to speak : {e}")
        return
    