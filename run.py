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
CWD = os.getcwd()

db: database = database()

if not db.imgs or len(db.imgs) <= 0:
    print("No images have been found, can not start")

def main():
    while(True):
        sleep(db.time)
        i = random.randint(0, len(db.imgs) -1)
        img = db.imgs[i]
        try:
            subprocess.run([ "sudo", "./change_wallpaper.sh", img], cwd=CWD, check=True)
            print("running: ", img)
        except Exception as e:
            print("changing wallpaper failed:")
            print(e)

if __name__ == "__main__":
    main()