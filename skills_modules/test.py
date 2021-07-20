from util.res import *


def initialize(voice_command,sentences):
    """
    :voice_command: the sentence the user said
    :sentences: the sentences that you have specified while uploading the skill
    :returns: response is a string containing the sentence you want to say aloud
    """

    speak("parlez maintenant !")
    response= get_user_response()
    return True, response