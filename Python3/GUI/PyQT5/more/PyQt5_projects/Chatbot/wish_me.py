import datetime
from speak import speak

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<17:
        speak("good afternoon sir!")
    elif hour>=18 and hour<19:
        speak("good evening sir!")
    else:
        speak("good night sir!")
    speak("I'm Alexa, please tell me how may I help you?")

if(__name__=='__main__'):
    wishMe()