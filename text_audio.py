from cgitb import text
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('rate', 250) # speed control of voice
# engine.setProperty('voice',voices[1].id) # for femal voice input
text = "hello i am rupesh sigdel. i am from tarakeshwor,2-nuwakot"

engine.say(text)
engine.runAndWait()
