import speech_recognition as sr

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
        #said = r.recognize_google(audio, language='hi-in')
        print(f"You said: {said}.....")
    except Exception as e:
        print("Say that again please......")
    return said

a = get_audio()
print(a)