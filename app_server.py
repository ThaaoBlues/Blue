from util.res import *
from util.translator import translate
import socket
from multiprocessing import Process, freeze_support
from locale import getlocale
from skills import check_skills




def initialize():
    Process(target=start_server).start()
    psuccess("App server started.")


def start_server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",8835))
    s.listen(10)
    while True:
        cli,addr = s.accept()
        print(addr[0])
        Process(target=handle_client,args=(cli,)).start()


def handle_client(cli):
    while True:
        voice_command = cli.recv(2048)
        print(voice_command)

        if voice_command != b"":
            voice_command = voice_command.decode('utf-8')

            if getlocale()[0][:2] != 'fr':
                    voice_command = translate(voice_command,getlocale()[0][:2],True)

            if not check_skills(voice_command):
                print("Je ne sais pas encore faire cela")

        else:
            break


if __name__ == '__main__':

    freeze_support()

    initialize()