from chatterbot import ChatBot, filters
from chatterbot.trainers import ChatterBotCorpusTrainer
import socket
from requests import get
from multiprocessing import Process, freeze_support, Manager
from youtube_search import YoutubeSearch
import webbrowser
import platform
import os
import locale
import time
import datetime
import random
from googlesearch import search
import sys
import webbrowser
from threading import Thread
import socket
import string
import googletrans
from colorama import *
import speedtest
import subprocess
import signal
from multiprocessing import Process, freeze_support
import wikipedia



class blue_bot_server():
    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.accept_process = ""
        self.accept_process = ""
        self.response = ""
        self.chatbot = ""
        self.hosts_number = Manager().Value('i',0)
        self.lang = locale.getdefaultlocale()[2:]
        print(self.lang)
        wikipedia.set_lang("fr")

        # Create a new chat bot named  Blue
        self.chatbot = ChatBot('Blue',
        filters=[filters.get_recent_repeated_responses],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='sqlite:///db.sqlite3')


        #ONLY USE IT THE FIRST TIME DUMBASS
        """self.trainer = ChatterBotCorpusTrainer(self.chatbot,
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='sqlite:\\\db.sqlite3')
        self.trainer.train("chatterbot.corpus.french")"""

        print("starting web config server on port 8080")
        subprocess.Popen(["python3","blue_config_server.py"])
        print("Starting BLUE server...")
        #litteraly starting the server like I said above
        self.start_server()

    def start_server(self):
        self.sock.bind(('', 8835))
        self.accept_process = Process(target = self.accept_hosts)
        self.accept_process.start()
        print("[+]Server is now online.")
        print("[+]Listening on : (Private IP) {} || (Public IP) {}".format(socket.gethostbyname_ex(socket.gethostname())[2],get('https://api.ipify.org').text))
        self.accept_process.join()
        

    def speak(self,text):
        print(text)
        os.system(f"espeak -v fr -s 6 \"{text}\"")
        
        
#funtion of the process accept_hosts_process to...yeah it's accepting hosts while the server is running
    def accept_hosts(self):
        self.sock.listen(10)
        while True:
            client, address = self.sock.accept()
            self.hosts_number.value += 1
            self.broadcast_process = Process(target = self.broadcast, args = (client,))
            self.broadcast_process.start()
            print("[+]user connected :: addr : {}".format(address[0]))
            print("[!]Users are now {}".format(self.hosts_number.value))
            
            
    #recieve and send the messages
    def broadcast(self,client):
        while True:
            try:
                message = client.recv(1024)
                message = message.decode('utf-8')
                if message != "" and message != " " and message != "\n" and message != "\r" and message != "\r\n":
                    print(message)
                    if not self.check_commands(message,client):
                        print(message)
                        response = str(self.chatbot.get_response(message))
                        print(f"BLUE:{response}")
                        client.send(bytes(response,'utf-8'))
                    
            except:
                pass
                
    #function to shutdown the server but this is useless you will always click on the red cross
    def shutdown_server(self):
        self.broadcast_process.terminate()
        self.accept_process.terminate()

    def display_website(self,ws):
        subprocess.run(["python3","websearch.py",ws])


    def check_commands(self,message,client):

        if "va sur" in message:
            if "." in message:
                self.display_website("http://www."+message.strip('va sur').replace(' ','').lower())
                client.send(bytes(f"j'ai affiché {message.strip('va sur').replace(' ','').lower()} sur la base BLUE","utf-8"))
                self.speak(f"j'ai affiché {message.strip('va sur').replace(' ','').lower()} sur la base BLUE")
            else:
                self.display_website(str(list(search(message.strip('va sur').replace(' ','').lower(),num=1,start=0,stop=1))[0]))
                client.send(bytes(f"j'ai affiché {message.strip('va sur').replace(' ','').lower()} sur la base BLUE","utf-8"))
                self.speak(f"j'ai affiché {message.strip('va sur').replace(' ','').lower()} sur la base BLUE")
            return True



        if "cherche" in message:
            response = GoogleSearch().search(message.strip("cherche"))
            result1 = response.results[0]
            self.speak(f"selon {result1.title}, {result1.getText()}")

            return True

        
            

        elif "mets" in message or "met" in message:
            message = message.strip("mets").strip("met").strip("la video de").strip("la chanson de").strip("la musique de").strip("une video de").strip("une chanson de").strip("une musique de")
            results = YoutubeSearch(message,max_results=10).to_dict()
            Self.display_website("https://www.youtube.com/embed/"+results[0]["url_suffix"]+"?autoplay=1")
            print(f"j'ai affiché {message.lower()} sur la base BLUE")
            client.send(bytes(f"j'ai affiché {message.lower()} sur la base BLUE","utf-8"))
            return True

        elif message in "quelle heure est-il quelle heure il est donne moi l'heure s'il te plais":
            date = datetime.datetime.now()
            client.send(bytes(str(date.hour) + ':' + str(date.minute) +"et"+ str(date.second) + " secondes","utf-8"))
            return True

        elif message in "quel jour sommes-nous quel jour on est quel jour est-on donne moi le jour":
            d = datetime.date.today().strftime("%d %B %Y")
            client.send(bytes(str(d),"utf-8"))
            return True

        elif message in "adieu goodbye exit aurevoir au revoir tais toi shut-up au-revoir ta gueule ferme-la chut":
            client.send(bytes("bonne journée !","utf-8"))
            return True

    
        elif message.startswith("dis"):
            client.send(bytes(message[3:],"utf-8"))
            self.speak(message[3:])
            return True

        elif message in "ouvre youtube":
            self.display_website("https://www.youtube.com")
            client.send("j'ai ouvert youtube dans votre navigateur")
            return True

        elif message in "ouvre google":
            self.display_website("https://www.google.com")
            client.send("j'ai ouvert google dans votre navigateur")
            return True

        elif message in "ouvre drive ouvre le drive ouvre google drive ouvre mon drive":
            self.display_website("https://drive.google.com/drive/my-drive")            
            client.send("j'ai ouvert google drive dans votre navigateur")
            return True

        elif message in "ouvre classroom ouvre google classroom":
            self.display_website("https://classroom.google.com/u/0/h")            
            client.send("j'ai ouvert google classroom dans votre navigateur")
            return True

        elif message in "ouvre Gmail ouvre gmail ouvre mes mails ouvre mail ouvre ma boite mail ouvre ma boite gmail":
            self.display_website("https://mail.google.com/mail/u/0/#inbox")
            client.send("j'ai ouvert votre boite mail dans votre navigateur")
            return True

        elif message in "effectue  un speedtest effectue un test de vitesse fais un speedtest s'il te plaît fais un test de vitesse s'il te plaît c'est un speedtest s'il te plaît":
            client.send("Mise en route d'un speedtest..")
            s = speedtest.Speedtest()
            s.get_servers()
            s.get_best_server()
            s.download()
            s.upload()
            res = s.results.dict()
            d = (float(res["download"]) / 1024)/1000
            u = (float(res["upload"]) / 1024)/1000
            p = float(res["ping"])
            d = round(d,3)
            u = round(u,3)
            p = round(p,3)
            d = str(d)
            u = str(u)
            p = str(p)
            d = d.replace(".",",")
            u = u.replace(".",",")
            p = p.replace(".",",")
            client.send("Vous êtes actuellement à {} Mb/s download et {} Mb/s upload, avec un ping de {} millisecondes".format(d,u,p))
            return True

        elif message in "éteins toi éteins-toi extinction shutdown":
            try:
                if platform.system() == "Windows":
                    os.system("shutdown -f")
                else:
                    os.system("shutdown -h now")
            except:
                client.send("Désolé, l'exécution de la commande a foirée")
            return True
    
        elif message in "redémarre toi redémarre-toi redémarrage reboot":
            try:
                if platform.system() == "Windows":
                    os.system("shutdown /r")
                else:
                    os.system("reboot")
            except:
                client.send("Désolé, l'exécution de la commande a foirée")
            return True


        elif message in "joue de la musique mets de la musique" or "top 50" in message or "top 100" in message:
            self.display_website("https://www.youtube.com/watch?v=TmKh7lAwnBI&list=PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM")
            
            return True

        elif message in "ifconfig ipconfig quelle est mon adresse IP locale mon IP locale":
            if platform.system() == "Windows":
                print(os.system("ipconfig"))
            else:
                print(os.system("ifconfig"))
            self.speak("Voici votre configuration IP")
            client.send(bytes("Voici votre configuration IP","utf-8"))
            return True
            
        elif "ferme" in message:
            message = message.split(sep= " ")
            if platform.system() == "Windows":
                try:
                    print(message[1:])
                    process_name = " ".join(message[1:])
                    print(process_name)
                    os.system("taskkill /f /im  \"{}.exe\" ".format(process_name))
                    self.speak("j'ai fermé {}".format(process_name))
                    client.send(bytes("j'ai fermé {}".format(process_name),"utf-8"))
                except:
                    print("ya une couille dans le pâté")
                    
            else:
                process_name = " ".join(message[1:])
                os.system(f"killall {process_name}")
                self.speak("j'ai fermé {}".format(process_name))
                client.send(bytes("j'ai fermé {}".format(process_name),"utf-8"))

            return True

        elif message in "quelle est mon adresse IP routeur mon IP routeur":
            self.speak("voici votre IP routeur " + socket.gethostbyname(socket.gethostname()))
            client.send(bytes("Voici votre IP routeur" + socket.gethostbyname(socket.gethostname()),"utf-8"))
            return True

        elif message in "quel temps fait-il dehors donnes moi la météo":
            self.display_website("https://www.google.com/search?q=meteo")         
            client.send("j'ai ouvert la météo dans votre navigateur")
            return True
        
        elif "wikipédia" in message:
            message = message.split()
            message = message[-1]
            self.display_website("https://fr.wikipedia.org/wiki/{}".format(message))            
            client.send("voici la page wikipédia de {}".format(message))
            return True

        elif "comment" in message and "faire" in message or "how to" in message:
            message = message.split()
            
            if len(message[-2]) <= 2:
                message = message[-2] + message[-1]
            else:
                message = message[-1]

            self.display_website("https://fr.wikipedia.org/wiki/{}".format(message))    
            client.send(bytes("voici la page wikipédia de {}".format(message),"utf-8"))
            return True



        elif "définition" in message or "qui est" in message or "qui etait" in message or "c'est quoi" in message or "qu'est-ce qu":
            message = message.split()
            message = message[-1]
            res = wikipedia.summary(message,sentences=1)
            client.send(bytes(res,"utf-8"))
            self.speak(res)
            return True

        elif message in "fait un compte à rebours":
            #pas finis
            return True
        


        #custom app mode (edit file in App.data file)
        elif "ouvre" in message or "open" in message:
            #split by space
            message = message.split(sep = " ")
            #important to define with a spaces so the join will separate elements with space
            voice_list = " ".join(message[1:])
            print(voice_list)
            found = False
            if platform.system() == "Windows":
                with open("res/dictionary/App_Windows.data.Blue","r",encoding = "utf-8") as f:
                    for line in f:
                        if voice_list.lower() in line.lower():
                            client.send(bytes("ouverture de : {}".format(voice_list),"utf-8"))
                            found = True
                            path = f.readline().strip("\n")
                            subprocess.call([path])
                            return True
                    f.close()
                    if found == False:
                        client.send(bytes("Je n'ai pas trouvé ton application, modifie le fichier App.data pour l'ajouter.","utf-8"))
                        return True
            
            if platform.system() == "Linux":
                with open("res/dictionary/App_Linux.data.Blue","r",encoding = "utf-8") as f:
                    for line in f:
                        if voice_list.lower() in line.lower():
                            client.send(bytes("Okay, j'ouvre : {}".format(voice_list),"utf-8"))
                            found = True
                            path = f.readline().strip("\n")
                            subprocess.call([path])
                            return True
                    f.close()
                    if found == False:
                        client.send(bytes("Je n'ai pas trouvé ton application, modifie le fichier App.data pour l'ajouter.","utf-8"))
                        return True

        elif message == "test":
            self.display_website("www.google.com")

        else:
            return False
            



if __name__ == "__main__":
    freeze_support()
    blue_bot_server1 = blue_bot_server()


    
    
    
    
    
    
    


    
    
    

    
    
    