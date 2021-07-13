# -*- coding: utf-8 -*-
from keyring import get_password
from json import loads
from util.res import get_assistant_name
import simplenote

def initialize(voice_command,sentences):


    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    ac_username = "null"
    with open("config/accounts.blue","r") as f:
        for line in f.read().splitlines():
            if loads(line)['service'] == "simplenote":
                ac_username = loads(line)['username']
                f.close()
                break
    if ac_username == "null":
        return False, "Vous n'avez pas encore enregistré votre compte simplenote.com"

    else:
        ac_password = get_password("simplenote",ac_username)

        #connecting to simplenote
        sn = simplenote.Simplenote('thaaoblues81@gmail.com', 'a88xme35v22v53emx88a')


        #trying to get assistant default note page
        found = False
        for note in sn.get_note_list():
            if note == 0:
                break
            if get_assistant_name() in note[0]['tags']:
                note_key = note[0]['key']
                content = note[0]['content']
                sn.update_note({'key':note_key,'tags':["test1"],'content':content+"\n"+"proutprout"}) 
                found = True
                break

        if not found:
            # note page of your assistant doesn't exists, creating one
            sn.add_note({'tags':get_assistant_name(),'content':voice_command})

        return True, f"J'ai ajouté {voice_command} à vos notes."