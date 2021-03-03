import ast

def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

    response = eval(voice_command)

    return True, response