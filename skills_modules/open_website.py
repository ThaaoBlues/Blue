from webbrowser import open as open_website
from googlesearch import search



def initialize(voice_command,sentences):

    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)
    
    if "." in voice_command:
        open_website("http://www."+voice_command.strip("va sur").replace(' ','').replace('blue',"").lower())
        response = (f"j'ai affiché {voice_command.strip('va sur').replace(' ','').lower()} sur mon écran principal.")
    else:
        open_website(str(list(search(voice_command.strip('va sur').replace(' ','').lower()))[0]))
        response = (f"j'ai affiché {voice_command.strip('va sur').replace(' ','').lower()} sur mon écran principal.")
    
        
    return True, response
