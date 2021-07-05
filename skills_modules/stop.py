import pyautogui



def initialize(voice_command,sentences):
    """
    :voice_command: the sentence the user said
    :sentences: the sentences that you have specified while uploading the skill
    :returns: response is a string containing the sentence you want to say aloud
    """
    pyautogui.press('q')
    pyautogui.hotkey("alt","f4")
    response=""
    return True, responseq