import feedparser
from difflib import SequenceMatcher


def initialize(voice_command,sentences):
    for sentence in sentences:
        voice_command = voice_command.replace(sentence,"",1)


    with open("config/custom_rss_feed.blue","r",encoding="utf-8") as f:
            while(True):
                try:
                    l = f.readline().lower()
                    if SequenceMatcher(None, voice_command, l.strip("\n")).ratio() >= 0.65:

                        url = f.readline()
                        feed = feedparser.parse(url)
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
                        break
                    
                    elif l.strip("\n").strip("\r") == "":
                        response = "You don't have registered any rss stream"
                        return True, response
                except:
                    f.close()
                    return False,response
                    break

