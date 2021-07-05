from youtubesearchpython import VideosSearch
from subprocess import run, Popen
from multiprocessing import Process, freeze_support
import webbrowser
from platform import system
import pafy
from time import sleep



def initialize(voice_command,sentences):
    freeze_support()
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

    results = VideosSearch(voice_command, limit = 2).result()
    url = results['result'][1]['link']
    vid = pafy.new(url)
    best = vid.getbest()

    if system() == "Linux":

        p_video = Popen(["xdg-open",f"\"{best.url}\""])

    else:
        p_video = Popen(["start",url],shell=True)

    
    response = f"j'ai affiché {voice_command.lower()} sur mon écran principal."

    
    if results['result'][0]['duration'] != 0:
        time = results['result'][0]['duration']
        time = time.split(":")
        time = int(time[0])*60 + int(time[1])
        sleep(time)
        p_video.terminate()
        
    else:
        
        sleep(20*60)
        p_video.terminate()        
    
    
    
    return True, response



    
    
    
    