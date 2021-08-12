from googletrans import Translator


def translate(text,src,dest):
    """
    sorry, this module is giving some errors,
    using it is to unstable
    """
    
    translator = Translator()

    return translator.translate(text,src=src,dest=dest).text

