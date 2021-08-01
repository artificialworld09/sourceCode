import speech_recognition as sr
def takecommand():
    #it takes microphone input and string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
       print("listing......")
       r.pause_threshold=2
       audio = r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in") #for English
        # query=r.recognize_google(audio,language="hi-in") #for Hindi
        print(f'User said : {query} \n')
    except Exception as e:
        print("somthing wrong...say again...")
        return "None"
    return query  

if __name__ == "__main__":
    while True:
        query=takecommand().lower()
        print(query)
        if 'stop' in query:
            break