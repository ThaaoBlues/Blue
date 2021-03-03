# Blue
## Blue is a vocal assistant that you can use and modify to add your own features.


Use the requirements.txt and the setup.py files before running Blue the first time. (If you are on windows, download the .exe release)


## Blue can do a bunch of things like:


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

    return True, response


```


### while uploading, the sentences to trigger your skill must follow these rules:

- being separated by the "/" character.

- if you want to just check if the uer sentence begin by one word, type startswith followed by a space and the word you want. 


## Informations

If you are near the Blue base and a microphone is plugged in, you can talk without opening the app on your phone by beginning your sentences by the hot word you have chossen at the setup.


All the commands are designed for french people, the script use a translator so you can talk in any languages but it may not translate in the right way to trigger some features.


If you are using Blue on a machine running 24/24, you need to desactivate the sleep mode of your os and the screen auto-lock to not have to retype your password when blue turn off the screen.
