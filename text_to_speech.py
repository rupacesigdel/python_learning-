import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speaker = wincom.Dispatch("SAPI.SpVoice")

names = ["Rajan", "Sujan", "Bimal"]

for i in names:
 print("shoutout to "+i)

for name in names:
 list = name.split()
 shoutout = f"Shoutout to {list[0]}"
 speaker.Speak(shoutout)
 
print("Shoutout of all for you")


#  OR,

#  text = f"Hello!!! {name}"
#  speaker.Speak(text)
# # 2 second sleep
#  time.sleep(2) 
