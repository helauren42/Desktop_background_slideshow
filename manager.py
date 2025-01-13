import argparse
from typing import List, Dict, Optional
import json
import subprocess
from abc import ABC
from database import database
import sys
import os

PID = os.getpid()

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
    def getImages(self):
        if not self.db.path:
            return
        try:
            files = subprocess.run("ls", stdout=subprocess.PIPE, text=True, cwd=self.db.path).stdout.splitlines()
            print("DB PATH: ", self.db.path)
            self.db.imgs = []
            for file in files:
                type = file.split(".")[-1]
                if type in VALID_TYPES:
                    self.db.imgs.append(file)

            if len(self.db.imgs) == 0:
                print("Warning: set images path contains no image")
        except Exception as e:
            print(f'Failed to cd and ls {self.db.path}:')
            print(e)

class Manager(Abstract_manager):
    def __init__(self):
        self.db: database = database()

    def newPath(self, args_path):
        self.db.path = args_path
        self.getImages()

    def setTime(self, args_time):
        self.db.time = args_time

    def start(self):
        try:
            process = subprocess.Popen(["python3", "run.py"], close_fds=True)
            print("launched run.py")
            sys.exit(0)
        except Exception as e:
            print(f"Could open process:\n{e}")

    def stop(self):
        if not self.db.pid or len(self.db.pid) <= 0:
            print("No running process to kill")
            return
        for pid in self.db.pid:
            try:
                subprocess.run(["kill", str(pid)], check=True)
                print("Killed process: ", pid)
            except Exception as e:
                print(f"Could not stop process:\n{e}")
            self.db.pid = None

    def refresh(self):
        self.stop()
        self.start()

    def executeArgs(self, args: argparse.ArgumentParser):
        if args.set_time:
            self.setTime(args_time=args.set_time)
        if args.path:
            self.newPath(args_path=args.path)
        if args.refresh:
            self.refresh()
        if args.start:
            self.start()
        if args.stop:
            self.stop()
        
        self.db.write()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--set-time", type=int, help="time between images in seconds, defaults to 30 seconds")
    parser.add_argument('path', type=str, nargs='?', help="Directory path containing images for the slideshow")

    parser.add_argument("-start", "--start", action="store_true", help="start the slideshow, requires path to be set")
    parser.add_argument("-stop", "--stop", action="store_true", help="stop the slideshow")
    parser.add_argument("-refresh", "--refresh", action="store_true", help="updates when the images directory has been modified")

    args = parser.parse_args()
    manager = Manager()
    manager.executeArgs(args)

main()
