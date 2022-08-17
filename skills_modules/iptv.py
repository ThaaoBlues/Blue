from platform import system
from requests import get


def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)
    
    
    # vlc not installed on windows        
    if system() == "Windows":
        
        win_vlc_install()
        
        
    
        
def win_vlc_install():
    pass