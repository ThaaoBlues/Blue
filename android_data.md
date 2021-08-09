## General info
    
    - Blue listen phone voice command on port 8835 


___


## Data syntax :

    - a json dict is sent by the socket, here is the full list of parameters:

    1. 'type', can only be 'voice_command' or 'website' yet

    2. 'voice_command': 'user voice command'

    3. 'battery': float containing battery percentage

    4. 'is_charging': boolean. True is the phone is charging, else False

