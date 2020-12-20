from subprocess import Popen
Popen(["sudo","apt","install","espeak"])
Popen(["sudo","apt","install","alsa"])
Popen(["sudo","apt","install","libasound-dev"])
Popen(["sudo","apt","install","alsa-utils"])
Popen(["sudo","apt","install","python3-pyaudio"])

Popen(["python3","-m","pip","install","playsound","gTTS","GoogleNews","pywhatkit","SpeechRecognition","chatterbot==1.0.4","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot","pyttsx3"])

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
