from googletrans import Translator


def translate(text,src,dest='fr'):
    translator = Translator()

    return translator.translate(text,src=src,dest=dest).text