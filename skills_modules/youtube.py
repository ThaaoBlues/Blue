from webbrowser import open as open_w
from youtubesearchpython import VideosSearch
from pyautogui import click, size
from util.res import remove_useless_words


def initialize(voice_command,sentences):

    voice_command = voice_command.lower()

    voice_command = remove_useless_words(voice_command)

    for sentence in sentences:
        for part in sentence.split("*"):
            if part in voice_command:
                voice_command = voice_command.replace(part,"")
            


    results = VideosSearch(voice_command, limit = 2).result()
    url = results['result'][1]['link']

    #open video
    open_w(url+"&autoplay=1")

    #youtube already autoplay ??
    """sleep(4)
    screenWidth, screenHeight = size()
    click(screenWidth//2,screenHeight//2)"""

    response = f"j'ai affiché {voice_command} sur mon écran principal."
   
    return True, response



    
    
    
    