#!/bin/bash

sudo apt-get install python3-pip -y
sudo apt-get install tor
sudo apt-get install figlet
sudo apt-get install vlc
sudo apt-get install libreoffice
# Install Pyaudio
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip install pyaudio
# Install Visual Studio Code
sudo apt-get install software-properties-common apt-transport-https wget -y
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
apt-get update
apt-get install code



#Install Anonsurf
git clone https://github.com/Und3rf10w/kali-anonsurf.git
chmod 777 -R kali-anonsurf
cd kali-anonsurf
./installer.sh
sudo anonsurf start

#Install tor Browser
sudo apt install tor torbrowser-launcher
sudo torbrowser-launcher
