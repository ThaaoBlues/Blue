from socket import gethostname, gethostbyname_ex,create_connection
from requests import get
from datetime import date
from random import randint
from os import listdir, remove,chdir,path,getcwd
from psutil import cpu_percent, virtual_memory
from platform import system, platform, python_version
from colorama import Fore, Back, Style
from colorama import init
from pathlib import Path
from socket import socket, AF_INET, SOCK_DGRAM
import logging
import click
from xml.etree import ElementTree
from xml.sax.saxutils import escape
from json import dumps, loads




def get_custom_websites_voice_commands():
    """
    return a list of json objects containing data from user registereed voice commands to open a website
    
    """

    with open("config/custom_websites.blue","r") as f:
        websites = f.read().splitlines()
        f.close()


    return [loads(i) for i in websites]


def get_registered_services():
    """
    return a list of services names, written in services.blue
    """

    with open("config/services.blue","r") as f:
        services = f.read().splitlines()
        f.close()

    return services

def is_service_registered(service_name):
    """
    return True if the service name is present in services.blue, else False
    
    """

    return True if service_name in get_available_services() else False


def register_service(service_name):
    """
    add a new service name in services.blue
    """

    with open("config/services.blue","a") as f:
        f.write(f"{service_name}\n")
        f.close()


def delete_registered_service(service_name):
    """
    delete an already registered service from services.blue
    return True if the service is deleted and False if the service doesn't exists
    """

    try:
        services = get_available_services()
        with open("config/services.blue","w") as f:
            services.pop(services.index(service_name))
            f.writelines(services)
            f.close()
        return True
    except:
        return False


def is_user_account_for_service(service_name):
    """
    return True if the user has already stored credentials for a service else False
    """

    ac_username = "null"
    with open("config/accounts.blue","r") as f:
        for line in f.read().splitlines():
            if loads(line)['service'] == service_name:
                f.close()
                return True
    if ac_username == "null":
        return False


def get_username_for_service(service_name):

    """
    get a username for the given external service
    return "null" if none is available
    """

    ac_username = "null"
    with open("config/accounts.blue","r") as f:
        for line in f.read().splitlines():
            if loads(line)['service'] == service_name:
                ac_username = loads(line)['username']
                f.close()


    return ac_username


def get_assistant_name():

    with open("config/assistant_name.blue","r")  as f:
        name = f.read()
        f.close()

    return name

def add_wake_up_alarm(days_left,time,url):

    et = ElementTree.parse("config/reminders.xml")
    root = et.getroot()

    new_ele = ElementTree.SubElement(root,"wakeup")
    new_ele.text = dumps({"days_left" : abs(int(days_left)-date.today().day),"time" : time, "url" : escape(url)})
    et.write("config/reminders.xml")
    
    from skills_modules import reminder

    reminder.start_wakeup_timer(abs(int(days_left)-date.today().day),time,url)


def add_reminder(date,time):
    pass

def get_reminders_list():
    pass

def get_wakeup_list():

    et = ElementTree.parse("config/reminders.xml")
    root = et.getroot()
    all_tags = [ele.tag for ele in root]
    all_times = [ele.attrib['time'] for ele in root]

    return {"tags" : all_tags,"times" : all_times}

def remove_useless_words(string):

    ws = open("config/unnecessary.blue","r").read().split(",")
    
    for w in ws:
        string = string.replace(" "+w+" "," ")

    return string

def disable_flask_logs():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    def secho(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    def echo(text, file=None, nl=None, err=None, color=None, **styles):
        pass

    click.echo = echo
    click.secho = secho


def check_internet():
    """
    a simple function to check if an internet connection is available
    :return: True if connected, else it returns false
    """
    try:
        create_connection(("1.1.1.1", 53),2)
        return True
    except:
        return False



def is_available(website, port = None):
    """
    a simple function to check if a website/server is available
    :param: website is a string where you put the website url/ip
    :param: port is an optionnal argument where you can specify a port
    :return: True if available, else it returns false
    """
    if port !=None:
        try:
            create_connection((website, port),2)
            return True
        except:
            return False
    else:
        try:
            create_connection((website, 80),2)
            return True
        except:
            return False



def get_os_name():
    """
    :return: the os name
    """
    return str(system())



def get_full_os_name():
    """
    :return: the full os name
    """
    return str(platform())



def get_python_version():
    """
    :return: the python version you are using
    """
    return str(python_version())



def get_file_number_of_lines(fname):
    """
    :param: fname is a string containing the path to the file you want to count the lines
    :return: the number of line of the file
    """
    with open(f"{getcwd()}/{fname}") as f:
        for i, l in enumerate(f):
            pass
    return i + 1



def get_file_size(fname):
    """
    :param: fname is a string containing the path to the file you want to get the size
    :return: a string containing the size of the file in Megabytes
    """
    byte = int(path.getsize(f"{getcwd()}/{fname}"))
    return f"{byte/1000000}"

def get_time():
    """
    :return: a string containing the time
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def perror(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a error-style custom and colored error message
    """
    init()
    if time:
        print(f"{Fore.RED}{get_time()} [x] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.RED}[x] {str} {Fore.WHITE}")



def pwarn(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a warning-style custom and colored warning message
    """
    init()
    if time:
        print(f"{Fore.YELLOW}{get_time()} [!] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.YELLOW}[!] {str} {Fore.WHITE}")




def pinfo(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a info-style custom and colored info message
    """
    init()
    if time:
        print(f"{Fore.BLUE}{get_time()} [+] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.BLUE}[+] {str} {Fore.WHITE}")




def psuccess(str,time=False):
    """
    :param: time is set to false by default, set to true it display the time with the message
    :param: str is just a string where you put your message
    This function display a success-style custom and colored success message
    """
    init()
    if time:
        print(f"{Fore.GREEN}{get_time()} [v] {str} {Fore.WHITE}")
    else:
        print(f"{Fore.GREEN}[v] {str} {Fore.WHITE}")




def get_private_ips():
    """
    :return: a list of all private IP addresses liked to your machine (may be vm) 
    """
    return gethostbyname_ex(gethostname())[:2]



def get_private_ip():
    """
    get the private ip linked to your machine
    :return: a string containing the private ip used on your machine

    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]




def get_public_ip():
    """
    :return: a string containing your public ip
    """
    return get('https://api.ipify.org').text




def get_hostname():
    """
    :return: a string containing the hostname
    """
    return gethostname()



def get_date():
    """
    :return: a string containing today's date
    """
    today = datetime.today()
    return today.strftime("%d/%m/%Y")




def write_temp_file(purpose,content,append=True):
    """
    :param: purpose is a string where you specify an idea of what you are putting in the temp file
    :param: content is a string where you put the content of the temp file
    :param: append is a boolean set to True by default to open the temp file in append mode or not
    write the specified string on a random named temp file
    """
    if append: mode = "a" 
    else: mode = "w"
    with open(str(randint(0,99999999999))+purpose+".res",mode) as f:
        f.write(content)
        f.close()



def read_temp_file(purpose):
    """
    :param: purpose is a string  where ypu specify an idea of what you have put in the temp file
    :return: a string containing the content of the temp file or False if the file for this purpose don't exist
    """
    found = False
    for file in listdir():
        if (purpose in file) and (".res" in file):
            found = True
            with open(file) as f:
                content = f.read()
                f.close()
    
    if not found:
        return False
    else:
        return content
            

def clear_temp_files():
    """
    delete all temporary files created by write_temp_file
    """
    for file in listdir():
        if (".res" in file):
            remove(file)

def get_ram_usage():
    """
    :return: a string containing the percentage of ram used
    """
    return str(virtual_memory().percent)

def get_cpu_usage():
    """
    :return: a string containing the percentage of cpu used
    """
    return str(cpu_percent())



def auto_chdir_to_file_root():
    """
    a function to make sure that the program is writing/reading at his root 
    (need to put res file in a folder)
    """
    chdir(path.abspath(__file__).replace("\\util\\res.py","").replace("/util/res.py",""))


def get_home_dir_path():
    """
    :return: a string containing the path to the home directory of the curent user
    """

    return str(Path.home())
