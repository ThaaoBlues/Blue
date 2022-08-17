powershell -Command "Invoke-WebRequest https://github.com/ThaaoBlues/Blue/archive/refs/heads/main.zip -o main.zip"
powershell Expand-Archive main.zip -DestinationPath blue
cd blue
python -m pip install pipwin
pipwin install pyaudio
pipwin install psutil
python -m pip install -r windows_requirements.txt
python Blue.py
