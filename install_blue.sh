echo [!] Commands outputs will be stored in ./blue_install.log
echo [+] Installing required packages via apt...
sudo apt install git python3 python3-pip python3-tk python3-dev python3-pyaudio python3-dbus python3-alsaaudio vlc &> ./blue_install.log
echo [v] Packages installed !
echo [+] Cloning Blue from github...
git clone https://www.github.com/ThaaoBlues/Blue &> ./blue_install.log
echo [v] Blue cloned !
echo [+] Cd into Blue folder
cd ./Blue &> ./blue_install.log
echo [+] Installing required python packages via pip... 
python3 -m pip install -r linux_requirements.txt --no-cache-dir &> ./blue_install.log
echo [v] Python packages installed, starting Blue !
echo [!] Please enter the name of your assistant, it will be used to trigger him -->
read hot_word
echo $hot_word | python3 Blue.py
wait