from webbrowser import open as open_website
from googlesearch import search
from util.res import remove_useless_words


def initialize(voice_command,sentences):
    voice_command = remove_useless_words(voice_command.lower())
    
    if sentences != "":
        for sentence in sentences:
            for part in sentence.split("*"):
                voice_command = voice_command.replace(part,"",1)

    voice_command = voice_command.replace(" ","")
        
    if "." in voice_command:
        open_website("http://www."+voice_command)
        response = (f"j'ai affiché {voice_command} sur mon écran principal.")
    else:
        open_website(str(list(search(voice_command))[0]))
        response = (f"j'ai affiché {voice_command} sur mon écran principal.")
    
        
    return True, response
