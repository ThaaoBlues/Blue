from pyautogui import size, click



def initialize(voice_command,sentences):

    
    screenWidth, screenHeight = size()
    click(screenWidth//2,screenHeight//2)


    return True, "J'ai mis ton contenu en pause"