from googletrans import Translator


def translate(text,src):
    translator = Translator()

    return translator.translate(text,src=src,dest='fr').text