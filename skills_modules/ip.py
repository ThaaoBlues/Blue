from socket import gethostbyname_ex, gethostname, socket, AF_INET, SOCK_DGRAM
from requests import get

def get_private_ips():
    """
    :return: a list of all private IP addresses liked to your machine (may be vm) 
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_public_ip():
    """
    :return: a string containing your public ip
    """
    return get('https://api.ipify.org').text


def initialize(voice_command,sentences):
    
    response = "Votre adresse ip publique est : " + get_public_ip() + " , et votre adresse ip privée est : " + str(get_private_ips())

    return True, response



