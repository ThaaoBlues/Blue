import feedparser
from difflib import SequenceMatcher
from json import loads

def initialize(voice_command,sentences):
    
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"")

    print(voice_command)

    with open("config/custom_rss_feed.blue","r",encoding="utf-8") as f:

        for line in f.read().splitlines():
            try:
                if line.strip("\n").strip("\r") != "":
                    line = loads(line)
                    if SequenceMatcher(None, voice_command, line['command']).ratio() >= 0.65:


                        feed = feedparser.parse(line['url'])
                        response = "Voici les deux derniers articles publiés :"
                        i=1
                        for entry in feed.entries[:2]:
                            response += "article 1 :" if i == 1 else "article 2 :"

                            response += entry.title + "."

                            response += "voici donc le contenu de l'article :"
                            response += entry.summary
                            i+=1

                        f.close()
                        return True, response

                else:
                    f.close()
                    response = "Vous n'avez pas encore enregistré de flux RSS"
                    return True, response

            except:
                f.close()
                return False,"Lecture de votre flux de nouvelles impossible , une erreur est survenue."

