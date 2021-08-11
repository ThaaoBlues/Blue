# Blue
## Blue is a vocal assistant that you can use and modify to add your own features.

Please read the whole readme file before doing anything !

## Language-related informations :
This assistant is designed for french language, it will use a translator if you aren't french but the result may not be accurate. If someone is able to traduct ``skills.blue`` and ``unnecessary.blue`` files with his own language I could get rid of the translator and let the user choose his language by the settings web server.

## installation :

- Linux (debian-based):
```bash
sudo apt install git python3 python3-pip python3-pyaudio python3-dbus python3-alsaaudio
git clone https://www.github.com/ThaaoBlues/Blue
cd ./Blue
sudo python3 -m pip install -r requirements.txt
sudo python3 Blue.py
```

- Windows :
    - Install python from [the official page](https://www.python.org)
    - Download the zip file of the source code and extract it or clone the git repo if you have git
    - open a command prompt on the Blue/ folder
    - type ``pip install pipwin`` then ``pipwin install pyaudio`` and ``pip install -r requirements.txt``
    - and finally launch Blue with ``python Blue.py``

### Don't forget to download the [android app](https://www.github.com/thaaoblues/blue_android_app) for a better experience.


## Blue can do a bunch of things like:

- wake you up with a video/music (program the day and the hour by the web page)


- add notes to your [Simplenote](https://simplenote.com) account


- read your [Simplenote](https://simplenote.com) notes


- delete a note from your [Simplenote](https://simplenote.com) account


- play/pause/skip/fullscreen music/video from youtube
(needs [this browser extension](https://chrome.google.com/webstore/detail/hotkey-music-controller-y/pohakmokiogdbhiocmacgalcmnfdbbne/related) to make keyboard shortcuts work on browser)

- volume up/volume down


- display the twitch stream of anyone


- talk with you and learn from your responses to be more accurate.(coming soon)


- play the top 100


- effectuate speedtest


- display a website by name or url


- make google searches


- make wikipedia searches and saying the result aloud


- reading your favorite news feed


- give you the time


- give you the date


- shutdown himself


- reboot himself


- display your IP configuration


- close/kill a process running on the machine just by name (coming soon)


- give you informations about the weather


A webserver is running on port 80 to access and config Blue easily.


### By the configuration page you can add:


- customs RSS feed


- customs messages to send to an ip


- add a voice command that open directly the desired website


- add new skills to Blue

- add a wake-up alarm the day and time you want

## YOU CAN NOW ADD YOUR OWN PYTHON-WRITTEN SKILLS FOR BLUE DIRECTLY FROM THE WEBSERVER !


### Blue skill script example :


file : ``skills_modules/add_note.py``
purpose : Add a note by voice command to a simplenote account with the simplenote api

```python


# -*- coding: utf-8 -*-
from util.res import *
import simplenote

def initialize(voice_command,sentences):
    """
    :voice_command: the sentence the user said
    :sentences: the sentences that you have specified while uploading the skill
    :returns: response is a string containing the sentence you want to say aloud
    """
    
    #use the following lines to strip voice_command and get only the main word(s)
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)
    
    # usefull if you don't want words like "the"
    voice_command = remove_useless_words(voice_command)


    #check if the external service "simplenote" has been registered
    if not is_service_registered("simplenote"):
        register_service("simplenote")


    #check if user has registered an simplenote account    
    if is_user_account_for_service("simplenote"):
       #an account has been registered, getting his username
        ac_username = get_username_for_service("simplenote")

    # no account available for this service, returning some sentences to guide him
    else:
        return False, "Vous n'avez pas encore enregistré votre compte simplenote.com"

    #getting password from secure keyring
    ac_password = get_password("simplenote",ac_username)

    #==================================================
    # simplenote api stuff/ not important for the demo
    #==================================================

    #connecting to simplenote
    sn = simplenote.Simplenote(ac_username,ac_password )

    #trying to get assistant default note page
    found = False
    for note in sn.get_note_list():
        if note == 0:
            break
        if get_assistant_name() in note[0]['tags']:
            note_key = note[0]['key']
            content = note[0]['content']
            sn.update_note({'key':note_key,'tags':[get_assistant_name()],'content':content+"\n"+voice_command}) 
            found = True
            break

    if not found:
        # note page of your assistant doesn't exists, creating one
        sn.add_note({'tags':[get_assistant_name()],'content':voice_command})

    #finally return a sentence to make Blue say something and True to mark processing as successfully terminated
    return True, f"J'ai ajouté {voice_command} à vos notes."


```

### list of useful functions :

they all needs to include util.res to work

- ``voice_command = get_user_response()`` to capture the next user command and exclude its usage on normal process

- ``speak('Hello World !')`` speak a sentence automatically traducted in the user language

- ``boolean = is_user_account_for_service('my_service')`` If you plan to use an online account, check if the user has registered his account into Blue

- ``boolean = is_service_registered("my_service")`` If you plan to use an online account, check if the service you use has been registred into blue configuration web-page so the user can link his account  

- ``register_service("my_service")`` Register an online service that needs an account so the user can register his credentials into the configuration page so you can use it later

- ``ac_username = get_username_for_service("my_service")`` Get the username which the user is using to connect to the service (please check if you have registered this service and if the user has registered an account before using this function)

- ``ac_password = get_password("my_service",ac_username)`` extract the password linked to the specified service and username from the secure keyring

### while uploading, the sentences to trigger your skill must follow these rules:

- being separated by the "/" character.

- if you want to take some random words in you trigger sentence, just add * at the word position. 

## Android app :
The android app (Blue-v2.apk) is designed to be used as a microphone if you don't have one or there is to many noises around (the app uses google-based speech to text engine and it is super mega over turbo powerfull). You need to enter the IP of the machine where Blue is running before speaking (don't worry, it will be prompted to you).


## Informations

If you are near the Blue base and a microphone is plugged in, you can talk without opening the app on your phone (Blue_v2.apk) by beginning your sentences by the hot word you have chossen at the setup.


All the commands are designed for french people, the script use a translator so you can talk in any languages but it may not translate in the right way to trigger some features.


If you are using Blue on a machine running 24/24, you need to desactivate the sleep mode of your os and the screen auto-lock to not have to retype your password when blue turn off the screen.
