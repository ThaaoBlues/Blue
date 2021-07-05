from platform import system
from subprocess import run, Popen

def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    url = "www.maps.google.com/maps/dir/" + voice_command

     if system() == "Linux":

        p_video = Popen(["xdg-open",f"\"{url}\""])

    else:
        p_video = Popen(["start",url],shell=True)


    response = "J'ai affiché la selecction d'itinéraires vers " + voice_command
    return True, response