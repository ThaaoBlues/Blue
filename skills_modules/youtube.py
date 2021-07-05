from webbrowser import open as open_w
from youtubesearchpython import VideosSearch
from subprocess import Popen
from pyautogui import hotkey, click, size
from platform import system
import pafy
from time import sleep



def initialize(voice_command,sentences):

    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

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

    
    if results['result'][0]['duration'] != 0:
        time = results['result'][0]['duration']
        time = time.split(":")
        time = int(time[0])*60 + int(time[1])
        sleep(time)
        hotkey("alt","f4")
        
    else:
        
        sleep(20*60)
        hotkey("alt","f4")        
    
    
    
    return True, response



    
    
    
    