import socket
from multiprocessing import Process, freeze_support, Manager
import random
import pyttsx3
import sys
from threading import Thread
import socket
import subprocess
import signal
from multiprocessing import Process, freeze_support
import speech_recognition as sr
import pyaudio
import answer
import os
from gtts import gTTS
from requests import get


class blue_bot_server():
    def __init__(self):
        
        if os.getuid() != 0:
            print("[!] Please run Blue as root.")
            exit(1)

        self.banner = """
__________.__                 
\______   \  |  __ __   ____  
 |    |  _/  | |  |  \_/ __ \ 
 |    |   \  |_|  |  /\  ___/ 
 |______  /____/____/  \___  >
        \/                 \/ 

"""





        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.accept_process = ""
        self.response = ""
        self.ans = answer.answer()

        #init offline text to speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 110)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty("voice", voices[26].id)
        
    

        #self.hosts_number = Manager().Value('i',0)
        self.lang = str(getdefaultlocale()[0])
        print("starting web config server on port 8080")
        subprocess.Popen(["python3","blue_config_server.py"])
        print("Starting BLUE server...")

        #litteraly starting the server like I said above
        self.start_server()
        try:
            self.r = sr.Recognizer()
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
                self.start_listening()
        except:
            print("[+] No microphone detected, please use the app on your phone !")
        
        
        



    def start_listening(self):
        print("started")
        while True:
            print("\rlistening..",end="")
            voice_command = str(self.listen(5))
            print(voice_command)
            if voice_command == "merci":
                print("BLUE : Avec plaisir mec ! ")
                self.speak("Avec plaisir mec !")
                
            elif voice_command.startswith("blue"):
                self.run_cmd("xset dpms force on")
                r = self.ans.get_answer(voice_command.replace("blue","").strip(" "),client=None)

            subprocess.run(["clear"],shell=True)
            print(self.banner+"\n"+r)


    def start_server(self):
        self.sock.bind(('', 8835))
        self.accept_process = Process(target = self.accept_hosts)
        self.accept_process.start()
        #subprocess.run(["clear"],shell=True)
        print("[+]Server is now online.")
        print("[+]Listening on : (Private IP) {} || (Public IP) {}".format(socket.gethostbyname_ex(socket.gethostname())[2],get('https://api.ipify.org').text))
        

    def speak(self,text):
        try:
            tts = gTTS(text,lang=self.lang[0]+self.lang[1])
            sn = str(randint(1,100000))+".mp3"
            tts.save(sn)
            playsound.playsound(sn)
            os.remove(sn)
        except:
            self.engine.say(text)
            self.engine.runAndWait()

    def listen(self,second):
        try:
            with sr.Microphone() as source:
                data = self.r.record(source,duration=second)
                voice_command = self.r.recognize_google(data,language=self.lang[0]+self.lang[1])
                return voice_command
        except:
            pass
        

    def check_files_integrity(self):
        if not os.path.isfile("custom_websites.blue"):
            subprocess.run(["python3","setup.py"],shell=True)

        if not os.path.isfile("custom_servers.blue"):
            subprocess.run(["python3","setup.py"],shell=True)

        if not os.path.isfile("irobot_cleaners.blue"):
            subprocess.run(["python3","setup.py"],shell=True)

        if not os.path.isfile("skills.blue"):
            subprocess.run(["python3","setup.py"],shell=True)


    

        
#funtion of the process accept_hosts_process to...yeah it's accepting hosts while the server is running
    def accept_hosts(self):
        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            #self.hosts_number.value += 1
            self.broadcast_process = Process(target = self.broadcast, args = (client,))
            self.broadcast_process.start()
            print("[+]user connected :: addr : {}".format(address[0]))
            #print("[!]Users are now {}".format(self.hosts_number.value))
            
            
    #recieve and send the messages
    def broadcast(self,client):
        while True:
            try:
                message = client.recv(1024)
                message = message.decode('utf-8')
                if message != "" and message != " " and message != "\n" and message != "\r" and message != "\r\n":
                    print(message)
                    self.run_cmd("xset dpms force on")
                    self.ans.get_answer(message,client)        
            except:
                #self.hosts_number.value -= 1
                pass
                
    #function to shutdown the server but this is useless you will always click on the red cross
    def shutdown_server(self):
        self.broadcast_process.terminate()
        self.accept_process.terminate()

    def run_cmd(self,sCommand):
        """
            run command line
            :sCommand: String parameter containing the command to run
            :returns: A string containing the stdout
        """
        return subprocess.run([sCommand],shell=True,capture_output=True).stdout.decode("utf-8")


if __name__ == "__main__":
    freeze_support()
    blue_bot_server1 = blue_bot_server()
