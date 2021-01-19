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
Popen(["python","-m","pip","install","pipwin"]).wait()
Popen(["python","-m","pipwin","install","pyaudio"]).wait()
Popen(["python","-m","pipwin","install","spacy"]).wait()
Popen(["python","-m","pip","install","--no-cache-dir","feedparser","youtube-dl","pafy","playsound","gTTS","GoogleNews","pywhatkit","SpeechRecognition","mathparse","chatterbot","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot"]).wait()

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
open("custom_rss_feed.blue","w")
open("skills.blue","w")

print(banner+"\n\n[+] All is set up ! you can now use Blue by typing \"python winblue.py\"")