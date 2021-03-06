from difflib import SequenceMatcher

def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

    with open("/config/notes.txt", "r") as f:
        ratio = 0
        match = ""
        ctt = f.read()
        for line in ctt.split("\n"):
            r = SequenceMatcher(line,voice_command).ratio()
            if r > ratio:
                ratio = r
                match = line

        ctt = ctt.replace(match+"\n","")
        f.close()

    with open("/config/notes.txt", "w") as f:
        f.write(ctt)
        f.close()


    return True, f"j'ai supprimé {match} de vos notes"

            
