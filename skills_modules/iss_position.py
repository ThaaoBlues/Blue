from requests import get
from json import loads
from platform import system
from subprocess import Popen,run
import webbrowser

def initialize(voice_command,sentences):

            
    json_dict =  loads(get("http://api.open-notify.org/iss-now.json").text)
    
    coords = (json_dict["iss_position"]["latitude"],json_dict["iss_position"]["longitude"])
    
    
    url = f"https://www.google.com/maps/search/?api=1&query={coords[0]}%2C{coords[1]}&zoom=0"
    
    if system() == "Linux":

        proc = Popen(["xdg-open",f"\"{url}\""])

    else:
        run(f"start msedge \"{url}\"",shell=True)

    
    
            
