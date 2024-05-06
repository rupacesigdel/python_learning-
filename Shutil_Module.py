import shutil
import os

shutil.copy("Shuilt_Module.py", "Shuilt_Module2.py")
shutil.copy2("Shuilt_Module.py", "Shuilt_Module2.py")
shutil.copytree(".tutorial", "mytutorial")   # for files not folder
shutil.move(".tutorial/file.file", "file.file")
os.remove("file.file")