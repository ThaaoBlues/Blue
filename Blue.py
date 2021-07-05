from util.res import *
import speech_recognition as sr
from time import sleep
import locale
from skills import check_skills
from util import setup
from config_server import start_webserver
from util.translator import translate
from multiprocessing import Process,freeze_support
import app_server


def listen():
    print("listening...")
    try:
        with sr.Microphone() as source:
            data = r.record(source,duration=5)
            voice_command = r.recognize_google(data,language=locale.getlocale()[0][:2])
            return voice_command
    except:
        pass





if __name__ == '__main__':

    auto_chdir_to_file_root()

    #make sure the user have choosen a hot word
    setup.check_files_integrity()
    
    hot_word = setup.get_hot_word()


    #start configuration server
    freeze_support()
    Process(target=start_webserver).start()

    #start app handling server
    app_server.initialize()

    #init voice recognizer
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            
        while True:
            voice_command = listen()
            if voice_command != None:
                print(voice_command)
                #translate to french so the modules can be triggered if you are not french
                if locale.getlocale()[0][:2] != 'fr':
                    voice_command = translate(voice_command,locale.getlocale()[0][:2],True)

                if(hot_word in voice_command):
                    voice_command = voice_command.replace(hot_word,"")

                    if not check_skills(voice_command):
                        print("Je ne sais pas encore faire cela")

    except:
        perror("No desktop microphone found, you must use the android app.")

    



