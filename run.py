import sys
from typing import List
import json
import random

DATA_FILE = ".data.json"

imgs = List[str]

def getImages():
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        imgs = data.get("imgs")
        # imgs = data["imgs"]

def main():
    getImages()
    while(True):
        i = random.randint(0, len(imgs) -1)
        img = imgs[i]
        

if __name__ == "__main__":
    main()