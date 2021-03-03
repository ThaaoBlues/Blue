from webbrowser import open as display_website



def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

    display_website("www.twitch.tv/"+voice_command.replace(" ",""))

    return True, "J'ai affiché le stream twitch de "+ voice_command