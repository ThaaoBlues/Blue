from webbrowser import open as display_website

def initialize(voice_command,sentences):
    
    for sentence in sentences:
        for part in sentence.split("*"):
            voice_command = voice_command.replace(part,"",1)

    display_website(f"https://www.google.com/search?q={voice_command}")


    response = "J'ai ouvert les résultats de ta recherche dans ton navigateur"

    return True, response