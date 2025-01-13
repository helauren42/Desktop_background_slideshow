from typing import List
import json
import random
import os
import sys
from database import database
from time import sleep
import subprocess

DATA_FILE = ".data.json"
PID = os.getpid()

COLOR_SCHEME = subprocess.run(["gsettings get org.gnome.desktop.interface color-scheme"], shell=True, 
                              stdout=subprocess.PIPE, text=True).stdout.strip()
COLOR_SCHEME = "dark" if COLOR_SCHEME.find("dark") != -1 else "light"

print(f'color scheme: "{COLOR_SCHEME}"')
print("color scheme: ", COLOR_SCHEME)

db: database = database()

if not db.imgs or len(db.imgs) <= 0:
    print("No images have been found, can not start")
    sys.exit()

db.addPid(PID)

def main():
    while(True):
        sleep(db.time)
        i = random.randint(0, len(db.imgs) -1)
        img = db.imgs[i]
        img_path = db.path + "/" + img
        try:
            if COLOR_SCHEME == "dark":
                subprocess.run([f'gsettings set org.gnome.desktop.background picture-uri-dark {img_path}'], shell=True)
            else:
                subprocess.run([f'gsettings set org.gnome.desktop.background picture-uri {img_path}'], shell=True)
        except Exception as e:
            print("changing wallpaper failed:")
            print(e)

if __name__ == "__main__":
    main()
