# Blue
vocal assistant that you can use and modify to add your own features.


Use the setup.py file before running Blue the first time. (If you are on windows, run winsetup.py and winblue.py)


Blue can do a bunch of things like:


-playing music/video from youtube


-playing the top 100


-effectuate speedtest


-display a website by name or url


-make google searches


-make wikipedia searches and saying the result aloud


-reading your favorite news feed


-give you the time


-give you the date


-open your google drive/Classroom/gmail


-shutdown himself


-reboot himself


-display your IP configuration


-close/kill a process running on the machine just by name


-give you informations about the weather


-interract with some irobots cleaners (very buggy)



A webserver is running on port 8080 to access and config Blue easily.


By the configuration page you can add:


-customs RSS feed


-customs messages to send to an ip


-add a voice command that open directly the desired website


-add new skills to Blue



YOU CAN NOW ADD YOUR OWN PYTHON-WRITTEN SKILLS FOR BLUE DIRECTLY FROM THE WEBSERVER !


If you are near the Blue base and a microphone is plugged in, you can talk without opening the app on your phone by beginning your sentences by "blue".


This assistant is designed for linux so some features may not work on windows.
All the commands are designed for french people, the script use a translator so you can talk in any languages but it may not translate in the right way to trigger some features.

If you are willing to write your own skill, please make sure that your script takes one argument. Blue will run it and pass the user voice command in argument.

If you are using Blue on a machine running 24/24, you need to desactivate the sleep mode of your os and the screen auto-lock to not have to retype your password when blue turn off the screen.
