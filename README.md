# Python-Oscilloscope

An oscilloscope made in python to analyze the frequency spectrum of a signal collected by the audio card.

![alt text](/demo.png)

## ALSA LIB

    sudo apt-get install build-essential libasound2-dev -y

## Python 3 Libs

    sudo apt-get install python3-pyaudio python3-dev portaudio19-dev python3-setuptools python3-scipy python3-pip -y

## Setup Audio Board

sudo nano /etc/asound.conf

    pcm.!default {
            type hw
            card 1
    }
    ctl.!default {
            type hw
            card 1
    }

## Useful commands:

Install Libs:

    pip3 install -r requirements.txt

Update libs list:

    pip3 freeze > requirements.txt