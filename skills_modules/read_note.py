from keyring import get_password
from json import loads
import simplenote
from util.res import get_assistant_name



def initialize(voice_command,sentences):

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
        sn = simplenote.Simplenote(ac_username, ac_password)

        #trying to get assistant default note page
        found = False
        for note in sn.get_note_list():
            if note == 0:
                break
            if get_assistant_name() in note[0]['tags']:
                response = note[0]['content']
                found = True
                break

        if not found:
            # note page of your assistant doesn't exists
            response = "Vous n'avez pas encore pris de notes."
            

        return True, response