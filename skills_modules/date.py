import datetime

def initialize(voice_command,sentences):
    d = datetime.date.today().strftime("%d %B %Y")
    response = (str(d))
    return True, response