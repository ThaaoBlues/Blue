from random import sample
from string import ascii_lowercase, digits
from pyautogui import screenshot

def initialize(voice_command,sentences):
    filename = "".join(sample(digits+ascii_lowercase,16))+".jpg"
    screenshot().save(f"images/{filename}")
    
    return True, "L'image issue de la capture est disponible dans l'onglet images de mon site web"