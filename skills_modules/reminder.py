from util.res import *
from threading import Timer
from functools import partial
from webbrowser import open as open_url
from skills import speak



def initialize(voice_command,sentences):

    open_url("http://127.0.0.1/action/[ADD REMINDER]")

    return True, "J'ai ouvert la page de configuration de tes alarmes et réveils sur ton navigateur !"


def alarm(json:dict):
    
    if check_reminder(json):
        speak("Comme prévu, je viens te réveiller !")
        open_url(json['url'])
        
        r = get_all_reminders()
        r.pop(int(json['id']))
        rewrite_reminders_file(r)



def reminder(json:dict):

    if check_reminder(json):
        speak(json['content'])
        
        r = get_all_reminders()
        r.pop(int(json['id']))
        rewrite_reminders_file(r)



def start_wakeup_timer(days_left:int,hours_left:int,minutes_left:int,json:dict):

    sec = abs(3600*24*days_left + hours_left*3600 + minutes_left*60)
    print("wakeup : ",sec)
    t = Timer(sec, partial(alarm,json))
    t.start()



def start_reminder_timer(days_left:int,hours_left:int,minutes_left:int,json:dict) -> None:


    sec = abs(3600*24*days_left + hours_left*3600 + minutes_left*60)
    print(f"started for {sec} seconds.")
    
    t = Timer(sec, partial(reminder,json))
    t.start()


