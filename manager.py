import argparse
from typing import List, Dict, Optional
import json
import sys
import subprocess
from abc import ABC

CWD = subprocess.run(["pwd"], stdout=subprocess.PIPE, text=True).stdout
print("CWD: ", CWD)

DATA_FILE = ".data.json"
VALID_TYPES = [
    "jpeg", "jpg",
    "png",
    "gif",
    "bmp",
    "tiff", "tif",
    "webp",
    "ico",
    "heif", "heic",
    "raw"
]

class Abstract_manager(ABC):

    def previousData(self):
            try:
                with open(DATA_FILE, "r") as file:
                    _data = json.load(file)
                    self.path = _data.get("path")
                    self.imgs = _data.get("imgs")
                    print("[DEBUG] previous images: ", self.imgs)
            except FileNotFoundError:
                pass
            except Exception as e:
                    print("file reading failed:")
                    print(e)
                    sys.exit(1)

    def getImages(self):
        if not self.path:
            return
        try:
            files = subprocess.run("ls", stdout=subprocess.PIPE, text=True, cwd=self.path).stdout.splitlines()
            self.imgs = []
            for file in files:
                type = file.split(".")[-1]
                if type in VALID_TYPES:
                    self.imgs.append(file)

            print("\n\n[DEBUG] files: ", files)

            if len(self.imgs) == 0:
                print("Warning: set images path contains no image")
        except Exception as e:
            print(f'Failed to cd and ls {self.path}:')
            print(e)

    def writeToDatabase(self):
        data: Dict = {}
        if self.path:
            data["path"] = self.path
        if self.imgs:
            data["imgs"] = self.imgs
        if self.time:
            data["time"] = self.time
        if self.pid:
            data["pid"] = self.pid

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

class Manager(Abstract_manager):
    path: Optional[str] = None
    imgs: Optional[List[str]] = None
    time: Optional[int] = 30
    pid: Optional[int]= None

    def __init__(self):
        pass

    def newPath(self, args_path):
        self.path = args_path
        self.getImages()
    
    def setTime(self, args_time):
        self.time = args_time

    def start(self):
        process = subprocess.Popen(["python3", "run.py"])
        self.pid = process.pid()
            
    # def refresh(self):
    #     with 

    def executeArgs(self, args: argparse.ArgumentParser):
        self.previousData()
        if args.set_time:
            self.setTime()
        if args.path:
            self.newPath(args_path=args.path)
        if args.refresh:
            self.refresh()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--set-time", type=int, help="time between images")
    parser.add_argument('path', type=str, nargs='?', help="Directory path containing images for the slideshow")

    parser.add_argument("-start", "--start", action="store_true", help="start the slideshow")
    parser.add_argument("-stop", "--stop", action="store_true", help="stop the slideshow")
    parser.add_argument("-refresh", "--refresh", action="store_true", help="updates when the images directory has been modified")

    args = parser.parse_args()
    manager = Manager()
    manager.executeArgs(args)

main()
