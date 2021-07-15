from platform import system

try:
    #windows
    from pyautogui import press
except ImportError:
    #linux (debian-based)
    from alsaaudio import Mixer


def initialize(voice_command,sentences):

    if system() == "Windows":
        press('volumedown',presses=5)
    else:
        m = Mixer()
        current_volume = m.getvolume() # Get the current Volume
        m.setvolume(current_volume-10) # Set the volume to -10%.

    return True, ""