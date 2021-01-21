from googletrans import Translator

gtl = Translator(service_urls=['translate.googleapis.com'])

print(gtl.translate("Hello",dest="fr").text)