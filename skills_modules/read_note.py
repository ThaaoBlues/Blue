

def initialize(voice_command,sentences):

    with open("config/notes.txt", "r",encoding="utf-8",errors="ignore") as f:
        response = "Voici le contenu de vos notes : "+f.read()


    return True, response