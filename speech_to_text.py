import speech_recognition as sr
recognizer = sr.Recognizer()

# listining from user and set record to microphone or earphone.
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
# traslating to text from speech 
try:
    text = recognizer.recognize_google(audio)
    print("you said: ", text)
except:
    print("error")
