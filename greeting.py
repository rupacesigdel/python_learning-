import time
Times = time.strftime("%H:%M:%S")
hour = int(time.strftime('%H'))
hour = int(input("Enter the time in hour:"))
print(hour)

if(hour >= 0 and hour < 12):
    print("good morning sir!")
elif (hour >= 12 and hour<17):
    print("good afternoon sir!")
elif(hour >=17 and hour<24):
    print("good night sir!")