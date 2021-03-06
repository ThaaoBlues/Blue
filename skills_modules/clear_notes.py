


def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)


    open("/config/notes.txt", "w")

    return True, "J'ai vidé votre liste de notes !"
