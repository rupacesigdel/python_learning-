import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

names = ["Rajan", "Sujan", "Bimal"]
for name in names:
 text = "Hello!!!"
 
 speak.Speak(text)

 speak.Speak(name)
 # 3 second sleep
 time.sleep(2) 

