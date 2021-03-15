import speech_recognition as sr
from speak import speak
from wish_me import wishMe

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        said = ""
    try:
        print("Recognizing......")
        said = r.recognize_google(audio, language='en-in')
        print(f"You said: {said}.....")
    except Exception as e:
        print("Say that again please......")
    return said
wishMe()

a = get_audio()

if "how are you" in a:
    speak("I'm fine sir, thank you!")
if "s your name" in a:
    speak("My name is Alexa sir!")