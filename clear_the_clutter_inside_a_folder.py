import os
files = os.listdir("clutterfolders")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutterfolders/{file}", f"clutterfolders/{i}.png")
        print(file)
        i = i + 1

# os.rename(f"clutterfolders/clutter.txt", f"clutterfolders/xyz.txt") #here to change the file name in folder.