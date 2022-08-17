from calendar import c
from platform import system
from requests import get
from locale import getlocale 
from os import startfile

def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)
    
    
    
    # vlc not installed on windows
    if system() == "Windows":
        
        win_vlc_install()
        
    country_code = getlocale()[0][3:]
    
    with open("iptv.m3u","wb") as f:
        f.write(get(f"https://iptv-org.github.io/iptv/countries/{country_code}.m3u"))
        
    startfile("iptv.m3u")
            
        
    
        
def win_vlc_install():
    pass