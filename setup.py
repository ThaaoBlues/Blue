from subprocess import Popen
from os import system
banner = """
__________.__                 
\______   \  |  __ __   ____  
 |    |  _/  | |  |  \_/ __ \ 
 |    |   \  |_|  |  /\  ___/ 
 |______  /____/____/  \___  >
        \/                 \/ 

"""

print(banner)

password = input("type your password : ")
system(f"echo {password} | sudo apt --assume-yes install espeak libasound2-dev python3-pyaudio python3-tk python3-dev & echo kali | sudo apt --assume-yes install alsa-utils")

Popen(["python3","-m","pip","install","feedparser","youtube-dl","pafy","playsound","gTTS","GoogleNews","pywhatkit","SpeechRecognition","chatterbot==1.0.4","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot","pyttsx3"]).wait()

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
open("custom_rss_feed.blue","w")
open("skills.blue","w")

print(banner+"\n\n[+] All is set up ! you can now use Blue by typing \"python3 Blue.py\"")
