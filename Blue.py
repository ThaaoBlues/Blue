from utils.res import *
import pyautogui
import speech_recognition as sr
from time import sleep
import locale
from skills import check_skills
from utils import setup
from skills_modules import heure
from config_server import start_webserver
from utils.translator import translate
from multiprocessing import Process,freeze_support




def listen():
    print("listening...")
    try:
        with sr.Microphone() as source:
            data = r.listen(source)
            voice_command = r.recognize_google(data,language=locale.getlocale()[0][:2])
            return voice_command
    except:
        pass





if __name__ == '__main__':

    #auto_chdir_to_file_root()

    #make sure the user have choosen a hot word
    hot_word = setup.get_hot_word()


    #start configuration server
    freeze_support()
    Process(target=start_webserver).start()

    #init voice recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)


    while True:
        voice_command = listen()
        if voice_command != None:
            print(voice_command)
            #translate to french so the modules can be triggered if you are not french
            if locale.getlocale()[0][:2] != 'fr':
                voice_command = translate(voice_command,locale.getlocale()[0][:2])

            if(hot_word in voice_command):
                voice_command = voice_command.replace(hot_word,"")

                if not check_skills(voice_command):
                    print("Je ne sais pas encore faire cela")



