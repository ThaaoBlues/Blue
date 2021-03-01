import datetime

def initialize(voice_command,sentences):
    date = datetime.datetime.now()
    response = (str(date.hour) + ':' + str(date.minute) +" et "+ str(date.second) + " secondes")
    return True, response