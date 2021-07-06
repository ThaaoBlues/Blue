import wikipedia
import locale
from util.res import remove_useless_words


def initialize(voice_command,sentences):
    voice_command = remove_useless_words(voice_command)
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)
        
    try:
        wikipedia.set_lang(locale.getlocale()[0][:2])
        response = str(wikipedia.summary(voice_command,sentences=2))

        return True, response
    except:
        response = "Auncun article sur wikipedia correspond à ce nom."
        return True, response