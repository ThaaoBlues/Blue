from webbrowser import open as open_w
from youtubesearchpython import VideosSearch
from pyautogui import click, size
import pafy
from time import sleep



def initialize(voice_command,sentences):

    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    results = VideosSearch(voice_command, limit = 2).result()
    url = results['result'][1]['link']
    vid = pafy.new(url)
    best = vid.getbest()

    #open video
    open_w(best.url)
    sleep(4)
    screenWidth, screenHeight = size()
    click(screenWidth//2,screenHeight//2)

    response = f"j'ai affiché {voice_command.lower()} sur mon écran principal."
   
    return True, response



    
    
    
    