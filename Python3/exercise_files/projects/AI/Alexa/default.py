import os
from gtts import gTTS
from playsound import playsound

def speak2(text):
   data = text.lower()
   tts = gTTS(text=data, lang='hi')
   filename = 'audios/default.mp3'
   tts.save(filename)
   playsound(filename)
       
if(__name__=='__main__'):
   data='we have very low power, please connect to charging the system will shutdown very soon'
   speak2(data)