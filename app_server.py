from util.res import *
from util.translator import translate
import socket
from multiprocessing import Process, freeze_support
from skills import check_skills
from json import loads
from webbrowser import open as display_website
from pyautogui import *


def initialize():
    p = Process(target=start_server)
    p.start()
    
    psuccess("App server started. IP : {}".format(get_private_ip()))
    
    return p

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 8835))
    s.listen(10)
    while True:
        try:
            cli, addr = s.accept()
            print(addr[0])
            Process(target=handle_client, args=(cli,)).start()
        except:
            pass


def handle_client(cli):
    
    asf = AndroidSpecialFeatures()
    
    while True:

        try:
            voice_command = cli.recv(4048)

            #make sure json is rightly formated and bytes are decoded
            voice_command = voice_command.decode(
                "utf-8").strip("\n")

            if voice_command != "":
                json = loads(voice_command)
            else:
                # get out of here if receiving empty packets (java is sending a lot of it at end of communication)
                break

            # process additional phone-related data
            if json["type"] == "voice_command":

                voice_command = json['voice_command']
                del json['voice_command']
                asf.process_data(json)

            else:
                asf.process_data(json)
                return

            # now get to the real work
            pinfo(f"IN-APP VOICE COMMAND : {voice_command}")

            if not check_skills(voice_command):
                print("Je ne sais pas encore faire cela")

        except Exception as e:
            print(e)





class AndroidSpecialFeatures():
    
    
    """'voice_command': 'user voice command'

CLASS USED TO PROCESS ADDITIONAL DATA SENT BY THE PHONE
NO DATA WILL BE STORED, NO DATA WILL BE SENT ANYWHERE


"""

    def process_data(self, json: dict):
        """
        process the json dict additional of data sent by the phone
        """

        self.check_battery(json['battery'], json['is_charging'])

        if json["type"] == "website":
            Process(target=display_website, args=(json["url"],)).start()
        


    def check_battery(self, battery: float, is_charging: bool):
        """

        simple low battery reminder

        """

        if not is_charging and battery < 25.0:
            battery_warn = "Votre battery est faible, vous devriez recharger votre téléphone portable."
            if get_locale() != 'fr':
                battery_warn = translate(
                    battery_warn, get_locale(), True)

            speak(battery_warn)

