from subprocess import Popen
Popen(["sudo","apt","install","espeak"])
Popen(["python3","-m","pip","install","chatterbot==1.0.4","youtube_search","googletrans","colorama","speedtest-cli","wikipedia","google","googlesearch-python","flask","pyirobot"])

#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")