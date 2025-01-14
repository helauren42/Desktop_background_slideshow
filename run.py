import random
import os
import sys
from database import database
from time import sleep
import subprocess
from collections import deque

# GLOBAL VARIABLES
imgs_history = deque()
db: database = database()

# CONST GLOBAL
LENGTH = len(db.imgs)
DATA_FILE = ".data.json"
PID = os.getpid()
COLOR_SCHEME = subprocess.run(["gsettings get org.gnome.desktop.interface color-scheme"], shell=True,
                              stdout=subprocess.PIPE, text=True).stdout.strip()
COLOR_SCHEME = "dark" if COLOR_SCHEME.find("dark") != -1 else "light"

if not db.imgs or len(db.imgs) <= 0:
    print("No images have been found, can not start")
    sys.exit()

db.addPid(PID)

def getImage():
    while len(imgs_history) > LENGTH // 2:
        imgs_history.popleft()
    img = None
    while img is None or img in imgs_history:
        i = random.randint(0, LENGTH -1)
        img = db.imgs[i]
    imgs_history.append(img)
    return img

def main():
    while(True):
        img = getImage()
        img_path = db.path + "/" + img
        try:
            if COLOR_SCHEME == "dark":
                subprocess.run([f'gsettings set org.gnome.desktop.background picture-uri-dark {img_path}'], shell=True)
            else:
                subprocess.run([f'gsettings set org.gnome.desktop.background picture-uri {img_path}'], shell=True)
        except Exception as e:
            print("changing wallpaper failed:")
            print(e)
        sleep(db.time)

if __name__ == "__main__":
    main()
