import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 1, phrase_time_limit= 5)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
    except Exception as e:
        # speak('Say that agian please...')
        print('Say that agian please...')
        return 'none'
    return query

if(__name__=='__main__'):

    a = takecommand()

    if "how are you" in a:
        print("I'm fine sir, thank you!")