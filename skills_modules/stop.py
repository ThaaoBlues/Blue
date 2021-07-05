from pyautogui import press, hotkey
from pywinauto import *


def initialize(voice_command,sentences):
    """
    :voice_command: the sentence the user said
    :sentences: the sentences that you have specified while uploading the skill
    :returns: response is a string containing the sentence you want to say aloud
    """
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    if voice_command != "":
        app = application.Application()
        #find window by name
        for w in Desktop(backend="uia").windows(visible_only=False):
            if voice_command in w.window_text().lower():
                app.connect(title_re = w.window_text())
                app_dialog = app.top_window()
                app_dialog.restore().set_focus()
                press('q')
                hotkey("alt","f4")
                response=""
    else:
        press('q')
        hotkey("alt","f4")
        response=""


    return True, response