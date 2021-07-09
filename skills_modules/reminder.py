from util.res import *
from datetime import datetime
from threading import Timer
from calendar import monthrange
from functools import partial
from webbrowser import open as open_url
from skills import speak



def initialize(voice_command,sentences):

    open_url("http://127.0.0.1/action/[ADD REMINDER]")

    return True, "J'ai ouvert la page de configuration de tes alarmes et réveils sur ton navigateur !"


def alarm(url):
    speak("Comme prévu, je viens te réveiller !")
    open_url(url)

def start_wakeup_timer(days_left,time,url):

    x=datetime.today()
    days_left = int(days_left)
    r = monthrange(x.year,x.month)[1]
    if r < x.day+days_left:    
        #number of days is on next month
        y=x.replace(month= x.month+1 if x.month != 12 else 1,day= days_left - (r - x.day), hour=int(time.split(":")[0]), minute=int(time.split(":")[1]), second=0, microsecond=0)

    else:
        y=x.replace(day=x.day+days_left, hour=int(time.split(":")[0]), minute=int(time.split(":")[1]), second=0, microsecond=0)
    
    delta_t=y-x

    secs=delta_t.seconds+1

    t = Timer(secs, partial(alarm,url))
    t.start()

