# -*- coding: utf-8 -*-
import os


def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)


    with open("config/notes.txt", "a",encoding="utf-8") as f:
        f.write(voice_command+"\n")


    return True, f"J'ai ajouté {voice_command} à vos notes."