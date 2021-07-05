# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    with open("config/notes.txt", "r",encoding="utf-8",errors="ignore") as f:
        ratio = 0
        ctt = f.read().split("\n")
        i = 0
        j = 0
        for line in ctt:
            r = SequenceMatcher(line,voice_command).ratio()
            if r > ratio:
                j = i
                ratio = r

            i += 1

        response = f"j'ai supprimé {ctt[j]} de vos notes"

        ctt.pop(j)
        f.close()

    with open("config/notes.txt", "w") as f:
        f.write("\n".join(ctt))
        f.close()


    return True, response

            
