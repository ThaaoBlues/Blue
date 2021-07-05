


def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)


    open("config/notes.txt", "w",encoding="utf-8")

    return True, "J'ai vidé votre liste de notes !"
