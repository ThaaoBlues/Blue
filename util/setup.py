from os import path,mkdir
from util.res import *
from locale import getlocale


def init_reminders_file():

    with open("config/reminders.xml","w") as f:

        f.write("<reminders_root>\n</reminders_root>")

        f.close()




def get_hot_word():

    if not path.exists("config/general_config.blue"):
        hot_word = input("\nplease select a word/sentence to trigger your assistant\n-->")
        psuccess(f"Congratulations ! Your assistant is now called {hot_word} !")
        
        with open("config/general_config.blue","w") as f:
            f.write(dumps({"assistant_name" : hot_word, "is_waiting_user_command" : False}))
            f.close()

        return hot_word
    else:
        with open("config/general_config.blue","r") as f:
            config = loads(f.read())
            f.close()

        return config['assistant_name']


def check_files_integrity():
    
    if not path.exists("config/"):
        mkdir("config")
        hot_word = input("\nplease select a word/sentence to trigger your assistant\n-->")
        psuccess(f"Congratulations ! Your assistant is now called {hot_word} !")
        with open("config/general_config.blue","w") as f:
            f.write(dumps({"assistant_name" : hot_word, "is_waiting_user_command" : False}))
            f.close()


    if not path.exists("skills_modules/"):
        mkdir("skills_modules")
    
    
    if not path.exists("config/custom_websites.blue"):
        open("config/custom_websites.blue","w")
    
    
    if not path.exists("config/custom_servers.blue"):
        open("config/custom_servers.blue","w")

    if not path.exists("config/accounts.blue"):
        open("config/accounts.blue","w")
    
    if not path.exists("config/custom_rss_feed.blue"):
        open("config/custom_rss_feed.blue","w")

    if not path.exists("config/reminders.xml"):
        init_reminders_file()

    if not path.exists("config/services.blue"):
        open("config/services.blue","w")


    locale = getlocale()[0][2:]
    if locale not in get("https://raw.githubusercontent.com/ThaaoBlues/Blue/main/language-files/supported_languages.txt").text:
        locale = "fr"


    if not path.exists("config/skills.blue"):
        with open("config/skills.blue","w",encoding="utf-8") as f:
            f.write(get(f"https://raw.githubusercontent.com/ThaaoBlues/Blue/main/language-files/{locale}/skills.blue").text)
            f.close()

    if not path.exists("config/unnecessary.blue"):
        with open("config/unnecessary.blue","w",encoding="utf-8") as f:
            f.write(get(f"https://raw.githubusercontent.com/ThaaoBlues/Blue/main/language-files/{locale}/unnecessary.blue").text)
            f.close()
