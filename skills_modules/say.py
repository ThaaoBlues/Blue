



def initialize(voice_command,sentences):

    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    return True, voice_command