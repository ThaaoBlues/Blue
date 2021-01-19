import socket
from multiprocessing import Process, freeze_support, Manager
import random
import sys
from threading import Thread
import socket
import subprocess
import signal
from multiprocessing import Process, freeze_support
import speech_recognition as sr
import pyaudio
import winanswer
import os
from gtts import gTTS
from requests import get


class blue_bot_server():
    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.accept_process = ""
        self.response = ""
        self.ans = winanswer.answer()
        self.hosts_number = Manager().Value('i',0)
    

        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)

        print("starting web config server on port 8080")
        subprocess.Popen(["python","blue_config_server.py"])
        self.start_listening()
        
        



    def start_listening(self):
        print("started")
        while True:
            print("\rlistening..",end="")
            voice_command = str(self.listen(5))
            print(voice_command)
            if voice_command == "merci":
                self.speak("Avec plaisir mec !")
            elif voice_command == "stop":
                p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
                out, err = p.communicate()
                for line in out.splitlines():
                    print(line)
                    if 'midori' in str(line).lower():
                        pid = int(line.split(None, 1)[0])
                        os.kill(pid, signal.SIGKILL)
            elif voice_command.startswith("blue"):
                self.ans.get_answer(voice_command.replace("blue","").strip(" "),client=None)


        

    def speak(self,text):
        try:
            tts = gTTS(text,lang="fr-FR")
            sn = str(randint(1,100000))+".mp3"
            tts.save(sn)
            playsound.playsound(sn)
            os.remove(sn)
        except:
            pass

    def listen(self,second):
        try:
            with sr.Microphone() as source:
                data = self.r.record(source,duration=second)
                voice_command = self.r.recognize_google(data,language='fr')
                return voice_command
        except:
            pass
        

    def check_files_integrity(self):
        if not os.path.isfile("custom_websites.blue"):
            subprocess.run(["python","setup.py"],shell=True)

        if not os.path.isfile("custom_servers.blue"):
            subprocess.run(["python","setup.py"],shell=True)

        if not os.path.isfile("irobot_cleaners.blue"):
            subprocess.run(["python","setup.py"],shell=True)

        if not os.path.isfile("skills.blue"):
            subprocess.run(["python","setup.py"],shell=True)


                
    #function to shutdown the server but this is useless you will always click on the red cross
    def shutdown_server(self):
        self.broadcast_process.terminate()
        self.accept_process.terminate()




if __name__ == "__main__":
    freeze_support()
    blue_bot_server1 = blue_bot_server()
