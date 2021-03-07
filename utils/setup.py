from os import path,mkdir
from utils.res import *



def get_hot_word():

    if not path.exists("config/assistant_name.blue"):
        hot_word = input("\nplease select a word/sentence to trigger your assistant\n-->")
        psuccess(f"Congratulations ! Your assistant is now called {hot_word} !")
        with open("config/assistant_name.blue","w") as f:
            f.write(hot_word)

        return hot_word
    else:
        with open("config/assistant_name.blue","r") as f:
            return f.read()


def check_files_integrity():
    
    if not path.exists("config/"):
        mkdir("config")
        hot_word = input("\nplease select a word/sentence to trigger your assistant\n-->")
        psuccess(f"Congratulations ! Your assistant is now called {hot_word} !")
        with open("config/assistant_name.blue","w") as f:
            f.write(hot_word)
    
    if not path.exists("skills_modules/"):
        mkdir("skills_modules")
    
    
    if not path.exists("config/custom_websites.blue"):
        open("config/custom_websites.blue","w")
    
    
    if not path.exists("config/custom_servers.blue"):
        open("config/custom_servers.blue","w")
    
    if not path.exists("config/irobot_cleaners.blue"):
        open("config/irobot_cleaners.blue","w")
    
    
    if not path.exists("config/custom_rss_feed.blue"):
        open("config/custom_rss_feed.blue","w")
    
    if not path.exists("config/skills.blue"):
        open("config/skills.blue","w")
