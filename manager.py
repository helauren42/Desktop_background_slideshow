import argparse
from typing import List, Dict, Optional
import subprocess
from abc import ABC
from database import database
import os
import sys

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
    "raw",
    "avif"
]

HOME = os.path.expanduser("~")
WD = os.path.join(HOME, ".local/appman/apps/bg-slideshow")

class Abstract_manager(ABC):
    def getImages(self):
        if not self.db.path:
            return
        try:
            files = subprocess.run("ls", stdout=subprocess.PIPE, text=True, cwd=self.db.path).stdout.splitlines()
            self.db.imgs = []
            for file in files:
                type = file.split(".")[-1]
                if type in VALID_TYPES:
                    self.db.imgs.append(file)

            if len(self.db.imgs) == 0:
                print("Warning: set images path contains no image")
        except Exception as e:
            print(f'Fetching image file names failed')
            print(e)

class Manager(Abstract_manager):
    def __init__(self):
        self.db: database = database()

    def newPath(self, args_path):
        self.db.path = args_path
        self.getImages()

    def setTime(self, args_time, minutes=False):
        if args_time is None:
            return
        if minutes:
            self.db.time = args_time * 60
        else:
            self.db.time = args_time

    def activate(self):
        if self.db.imgs is None or len(self.db.imgs) <= 0:
            print("Error: no imgs directory set, failed to activate")
        try:
            self.deactivate()
        except Exception as e:
            pass
        try:
            process = subprocess.Popen(["python3", os.path.join(WD + "/bg-slideshow.py")], close_fds=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        except Exception as e:
            print(f"Failed to activate application:\n{e}")

    def deactivate(self):
        # if not self.db.pid or len(self.db.pid) <= 0:
        #     return
        # for pid in self.db.pid:
        #     try:
        #         subprocess.run(["kill", str(pid)], check=True, close_fds=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        #     except Exception as e:
        #         pass
        subprocess.run(["pkill", "-f", "/home/helauren/.local/appman/apps/bg-slideshow/bg-slideshow.py"], check=True, close_fds=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        self.db.pid = None

    def refresh(self):
        self.deactivate()
        self.activate()

    def executeArgs(self, args: argparse.ArgumentParser):
        if args.uninstall:
            subprocess.run([os.path.join(WD + "/uninstall.sh")])
            sys.exit(0)
        if args.set_time:
            self.setTime(args_time=args.set_time, minutes=False)
        if args.set_time_minutes:
            self.setTime(args_time=args.set_time, minutes=True)
        if args.path:
            self.newPath(args_path=args.path)
        if args.refresh:
            self.refresh()
        if args.activate:
            self.activate()
        if args.deactivate:
            self.deactivate()

        self.db.write()

def main():
    parser = argparse.ArgumentParser(prog="bg-slideshow", description="A command-line utility for managing background slideshows in gnome.")

    parser.add_argument("-s", "--set-time", type=int, help="time between images in seconds, defaults to 30 seconds")
    parser.add_argument("-sm", "--set-time-minutes", type=int, help="time between images in minutes")
    parser.add_argument('path', type=str, nargs='?', help="Directory path containing images for the slideshow")

    parser.add_argument("-activate", "--activate", action="store_true", help="activate the slideshow, requires path to be set")
    parser.add_argument("-deactivate", "--deactivate", action="store_true", help="deactivate the slideshow, will deactivate all instances of the \
                        application if multiple are running")
    parser.add_argument("-refresh", "--refresh", action="store_true", help="reactivates app to be updated with the current \
                        shell environment and images in the directory")
    parser.add_argument("--uninstall", action="store_true", help="uninstals the background slideshow application and all the application's components")

    if len (sys.argv) <= 1:
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    
    manager = Manager()
    manager.executeArgs(args)

main()
