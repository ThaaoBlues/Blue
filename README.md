# Blue
## Blue is a vocal assistant that you can use and modify to add your own features.


Use the requirements.txt file with pip before running Blue the first time. If you are on windows, pip will not be able to install pyaudio. To install it you must install pipwin with ``pip install pipwin`` then install pyaudio with pipwin ``pipwin install pyaudio``

## Language-related informations :
This assistant is designed for french language, it will use a translator if you aren't french but the result may not be accurate. If someone is able to traduct skills.blue and unnecessary.blue with his own language I could get rid of the translator and let the user choose his language by the settings web server.


## Blue can do a bunch of things like:

- add notes

- read your notes

- delete a note

- play music/video from youtube

- display the twitch stream of anyone

- talk with you and learn from your responses to be more accurate.


- play the top 100


- effectuate speedtest


- display a website by name or url


- make google searches


- make wikipedia searches and saying the result aloud


- reading your favorite news feed


- give you the time


- give you the date


- open your google drive/Classroom/gmail


- shutdown himself


- reboot himself


- display your IP configuration


- close/kill a process running on the machine just by name


- give you informations about the weather


A webserver is running on port 80 to access and config Blue easily.


### By the configuration page you can add:


-customs RSS feed


-customs messages to send to an ip


-add a voice command that open directly the desired website


-add new skills to Blue



## YOU CAN NOW ADD YOUR OWN PYTHON-WRITTEN SKILLS FOR BLUE DIRECTLY FROM THE WEBSERVER !


### the python script must follow this pattern:

```python



def initialize(voice_command,sentences):
    """
    :voice_command: the sentence the user said
    :sentences: the sentences that you have specified while uploading the skill
    :returns: response is a string containing the sentence you want to say aloud
    """
    #use the following lines to strip voice_command and get only the main word(s)
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"")
        
    voice_command = remove_useless_words(voice_command)

    return True, response


```


### while uploading, the sentences to trigger your skill must follow these rules:

- being separated by the "/" character.

- if you want to take some random words in you trigger sentence, just add * at the word position. 


## Informations

If you are near the Blue base and a microphone is plugged in, you can talk without opening the app on your phone by beginning your sentences by the hot word you have chossen at the setup.


All the commands are designed for french people, the script use a translator so you can talk in any languages but it may not translate in the right way to trigger some features.


If you are using Blue on a machine running 24/24, you need to desactivate the sleep mode of your os and the screen auto-lock to not have to retype your password when blue turn off the screen.
