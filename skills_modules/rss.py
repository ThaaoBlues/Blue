import feedparser
from difflib import SequenceMatcher


def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)

    with open("../config/custom_rss_feed.blue","r") as f:
            while(True):
                try:
                    l = f.readline().lower()

                    if SequenceMatcher(None, voice_command, l).ratio() >= 0.65:

                        url = f.readline()
                        feed = feedparser.parse(url)
                        response = "Voici les deux derniers articles publiés :"
                        for entry in feed.entries[:2]:
                            response += entry.title + "."

                            response += "voici donc le contenu de l'article :"
                            response += entry.summary

                        f.close()
                        return True, response
                        break
                    
                    elif l.strip("\n").strip("\r") == "":
                        response = "You don't have registered any rss stream"
                        return True, response
                except:
                    print(e)
                    f.close()
                    return False,response
                    break

