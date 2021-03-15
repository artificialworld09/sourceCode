import os
import pyttsx3
os.system('clear')

engine = pyttsx3.init()
engine.say("Hello world")
engine.runAndWait()