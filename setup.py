from subprocess import run
banner = """
__________.__                 
\______   \  |  __ __   ____  
 |    |  _/  | |  |  \_/ __ \ 
 |    |   \  |_|  |  /\  ___/ 
 |______  /____/____/  \___  >
        \/                 \/ 

"""

print(banner)

def run_cmd(sCommand):
        """
            run command line
            :sCommand: String parameter containing the command to run
            :returns: A string containing the stdout
        """
        return run([sCommand],shell=True,capture_output=True).stdout.decode("utf-8")


password = input("type your password : ")

print("[+] installing requiered debian packages")
try:
        run_cmd(f"echo {password} | sudo apt --assume-yes install espeak libasound2-dev python3-pyaudio python3-tk python3-dev & echo kali | sudo apt --assume-yes install alsa-utils")
except:
        print("[x] An error occurred")

print("\n\n[+] All is set up ! you can now use Blue by typing \"python3 Blue.py\"")
