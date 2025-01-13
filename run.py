from typing import List
import json
import random

DATA_FILE = ".data.json"

imgs = List[str]

class data{
    
}
    # def previousData(self):
    #     try:
    #         try:
    #             with open(DATA_FILE, "r") as file:
    #                 _data = json.load(file)
    #                 self.path = _data.get("path")
    #                 self.imgs = _data.get("imgs")
    #                 print("[DEBUG] previous images: ", self.imgs)
    #         except FileNotFoundError:
    #             try:
    #                 print('creating db file ".data.json"')
    #                 with open(DATA_FILE, "w") as file:
    #                     file.write("{}")
    #             except Exception as e:
    #                 print("file creation failed:")
    #                 print(e)
    #                 sys.exit(1)
    #     except Exception as e:
    #         print("Error found:")
    #         print(e)
    #         sys.exit(1)

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