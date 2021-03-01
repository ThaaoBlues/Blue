from googlesearch.googlesearch import GoogleSearch



def initialize(voice_commaend,sentences):

    voice_command = voice_command.replace("recherche","",1).replace("cherche","",1)

    response = GoogleSearch().search(voice_command)
    result1 = response.results[0]
    self.speak(f"selon {result1.title}, {result1.getText()}")

    return True, response