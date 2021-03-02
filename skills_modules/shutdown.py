from subprocess import run
from platform import system


def initialize(voice_command,sentences):

    if system() == "Linux":
        
        run(["xset dpms force off"],shell=True)
    
    else:
        run(["%systemroot%\system32\scrnsave.scr /s"],shell=True)


    response = "bonne journée !"
    return True, response