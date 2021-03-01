import wikipedia
import locale


def initialize(voice_command,sentences):

    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)
        
    try:
        wikipedia.set_lang(locale.getlocale()[0][:2])
        response = str(wikipedia.summary(voice_command,sentences=2))

        return True, response
    except:
        print(e)
        response = "Auncun article sur wikipedia correspond à ce nom."
        return True, response