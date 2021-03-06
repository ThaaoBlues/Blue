

def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)


    with open("/config/notes.txt", "r") as f:
        response = "Voici le contenu de vos notes : "+f.read()


    return True, response