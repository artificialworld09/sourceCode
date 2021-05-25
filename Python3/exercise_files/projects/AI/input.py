from speak import speak

st = input("Type your words: ").lower()

if st in 'who are you?':
        speak("I'm Alexa, please tell me how may I help you?")
elif st in "how old are you?":
        speak("I'm 18 years old now sir!")
elif st in 'hello':
        speak("hi sir!")
elif st in 'hi':
        speak("hello sir!")
elif st in 'how are you?':
        speak("I'm fine sir")