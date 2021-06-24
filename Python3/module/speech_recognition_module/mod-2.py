# import speech_recognition as sr

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening......")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=5, phrase_time_limit=5)
#     try:
#         print("Recognizing......")
#         query = r.recognize_google(audio, language = 'en-in')
#         print(f"user said: {query}")
#     except Exception as e:
#         # speak('Say that agian please...')
#         print('Say that agian please...')
#         return 'none'
#     return query

# if(__name__=='__main__'):

#     a = takecommand()
#     print(a)


import speech_recognition as sr
def takequery():
    #it takes microphone input and string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
       print("listing......")
       r.pause_threshold=2
       audio = r.listen(source,timeout=2,phrase_time_limit=10)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f'User said : {query} \n')
    except Exception as e:
        print(e)
        print("somthing wrong...say again...")
        return "None"
    return query   

########## 
if __name__ == "__main__":
    while True:
        query=takequery().lower()
        print(query)
        if 'stop' in query:
            break