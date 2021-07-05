from webbrowser import open as display_website



def initialize(voice_command,sentences):
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    display_website("www.twitch.tv/"+voice_command.replace(" ",""))

    return True, "J'ai affiché le stream twitch de "+ voice_command