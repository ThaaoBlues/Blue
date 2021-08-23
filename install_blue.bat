powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -o python-installer.exe"
start python-installer.exe
powershell -Command "Invoke-WebRequest https://github.com/ThaaoBlues/Blue/archive/refs/heads/main.zip -o main.zip"
powershell Expand-Archive main.zip -DestinationPath blue
cd blue
python -m pip install pipwin
pipwin install pyaudio
python -m pip install -r requirements.txt
python Blue.py
