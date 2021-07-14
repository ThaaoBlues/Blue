<<<<<<< HEAD
=======
import simplenote

from util.res import get_assistant_name

found = False
for note in sn.get_note_list():
    if note == 0:
        break
    if "test1" in note[0]['tags']:
        note_key = note[0]['key']
        content = note[0]['content']
        sn.update_note({'key':note_key,'tags':["test1"],'content':content+"\n"+"proutprout"})
        found = True
        break
    
if not found:
    sn.add_note({"tags":["test1"], "content":"test1"})


>>>>>>> 4aa30461399406132c07ac5fd22ab642f218c9a5
