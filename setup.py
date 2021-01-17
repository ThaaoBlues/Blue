from subprocess import run


password = input("type your password : ")
run(["echo",password,"|","sudo","apt","install","espeak"],shell=True)
run(["echo",password,"|","sudo","apt","install","alsa"],shell=True)
run(["echo",password,"|","sudo","apt","install","libasound-dev"],shell=True)
run(["echo",password,"|","sudo","apt","install","alsa-utils"],shell=True)
run(["echo",password,"|","sudo","apt","install","python3-pyaudio"],shell=True)

run(["python3","-m","pip","install","feedparser","youtube-dl","pafy","playsound","gTTS","GoogleNews","pywhatkit","SpeechRecognition","chatterbot==1.0.4","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot","pyttsx3"],shell=True)

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
open("custom_rss_feed.blue","w")
open("skills.blue","w")
