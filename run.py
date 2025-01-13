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

SCRIPT_WD = CWD + "/" + "change_wallpaper.sh"

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
            # print("ls: ", subprocess.run(["ls"], cwd=CWD, check=True, stdout=subprocess.PIPE, text=True).stdout)
            subprocess.run([SCRIPT_WD, img_path],  check=True)
            print("CWD: ", CWD)
            print("running: ", img_path)
        except Exception as e:
            print("changing wallpaper failed:")
            print(e)

if __name__ == "__main__":
    main()