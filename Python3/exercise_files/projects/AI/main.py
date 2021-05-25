from sr import takecommand
from wish_me import wishMe
from speak import speak

wishMe()
while(True):
    a = takecommand()

    if a in 'who are you?':
        speak("I'm Alexa, please tell me how may I help you?")
    elif a in "how old are you?":
        speak("I'm 18 years old now sir!")
    elif a in 'hello':
        speak("hi sir!")
    elif a in 'hi':
        speak("hello sir!")
    elif a in 'how are you?':
            speak("I'm fine sir")
    elif a in 'you can sleep now':
        print('Thank you sir')
        break