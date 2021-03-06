import os


def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)


    with open("/config/notes.txt", "a") as f:
        f.write(voice_command)


    return True, f"J'ai ajouté {voice_command} à vos notes."