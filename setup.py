from subprocess import run
banner = """
__________.__                 
\______   \  |  __ __   ____  
 |    |  _/  | |  |  \_/ __ \ 
 |    |   \  |_|  |  /\  ___/ 
 |______  /____/____/  \___  >
        \/                 \/ 

"""

print(banner)

def run_cmd(sCommand):
        """
            run command line
            :sCommand: String parameter containing the command to run
            :returns: A string containing the stdout
        """
        return subprocess.run([sCommand],shell=True,capture_output=True).stdout.decode("utf-8")


password = input("type your password : ")

print("[+] installing requiered debian packages")
try:
        run_cmd(f"echo {password} | sudo apt --assume-yes install espeak libasound2-dev python3-pyaudio python3-tk python3-dev & echo kali | sudo apt --assume-yes install alsa-utils")
except:
        print("[x] An error occurred")


print("[+] Installing requiered python modules...")
try:
        run_cmd("python -m pip install feedparser youtube-dl pafy playsound gTTS GoogleNews pywhatkit SpeechRecognition mathparsechatterbot youtube_search googletrans colorama speedtest-cli wikipedia google googlesearch-python flask pyirobot pyttsx3")
except:
        print("[x] An error occurred")



#custom files, can be modified by user on [blue IP]:8080
open("custom_websites.blue","w")
open("custom_servers.blue","w")
open("irobot_cleaners.blue","w")
open("custom_rss_feed.blue","w")
open("skills.blue","w")

print(banner+"\n\n[+] All is set up ! you can now use Blue by typing \"python3 Blue.py\"")
