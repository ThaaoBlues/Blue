echo [+] Installing required packages via apt...
sudo apt install git python3 python3-pip python3-tk python3-dev python3-pyaudio python3-dbus python3-alsaaudio vlc
echo [v] Packages installed !
echo [+] Cloning Blue from github...
git clone https://www.github.com/ThaaoBlues/Blue
echo [v] Blue cloned !
echo [+] Cd into Blue folder
cd ./Blue
echo [+] Installing required python packages via pip... 
sudo python3 -m pip install -r linux_requirements.txt --no-cache-dir
echo [v] Python packages installed, starting Blue !
sudo python3 Blue.py