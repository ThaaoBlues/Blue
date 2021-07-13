# -*- coding: utf-8 -*-
from keyring import get_password
from json import loads
import gkeepapi
from util.res import get_assistant_name

def initialize(voice_command,sentences):


    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    ac_username = "null"
    with open("config/accounts.blue","r") as f:
        for line in f.read().splitlines():
            if loads(line)['service'] == "Google Keep note":
                ac_username = loads(line)['username']
                f.close()
                break
    if ac_username == "null":
        return False, "Vous n'avez pas encore enregistré votre compte google keep notes."

    else:
        ac_password = get_password("Google Keep note",ac_username)
        keep = gkeepapi.Keep()
        keep.login(ac_username, ac_password)

        #trying to get assistant default note page
        try:
            note = keep.get(get_assistant_name())
            note.text = note.text + voice_command
        except:
            # note page of your assistant doesn't exists, creating one
            keep.createNote(get_assistant_name(),voice_command)

        return True, f"J'ai ajouté {voice_command} à vos notes."