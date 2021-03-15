from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en-in')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)