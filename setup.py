from subprocess import Popen


password = input("type your password : ")
Popen(["echo",password,"|","sudo","apt","--assume-yes","install","espeak"]).wait()
Popen(["echo",password,"|","sudo","apt","--assume-yes","install","alsa"]).wait()
Popen(["echo",password,"|","sudo","apt","--assume-yes","install","libasound-dev"]).wait()
Popen(["echo",password,"|","sudo","apt","--assume-yes","install","alsa-utils"]).wait()
Popen(["echo",password,"|","sudo","apt","--assume-yes","install","python3-pyaudio"]).wait()

Popen(["python3","-m","pip","install","feedparser","youtube-dl","pafy","playsound","gTTS","GoogleNews","pywhatkit","SpeechRecognition","chatterbot==1.0.4","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot","pyttsx3"]).wait()

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
open("custom_rss_feed.blue","w")
open("skills.blue","w")
