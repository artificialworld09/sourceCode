import os
from gtts import gTTS
from playsound import playsound

## basic code
# def speak(text):
#     tts = gTTS(text=text, lang='en-in')
#     filename = 'audios/'+text+'.mp3'
#     tts.save(filename)
#     playsound(filename)

def speak(text):
    tts = gTTS(text=text, lang='en-in')
    filename = 'audios/'+text+'.mp3'
    if os.path.exists(filename):
        playsound(filename)
    else:
        tts.save(filename)
        playsound(filename)
        
if(__name__=='__main__'):
    st = input("Type your words: ").lower()

    if st in 'who are you?':
        speak("I'm Alexa, please tell me how may I help you?")