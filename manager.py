import argparse
from typing import List, Dict, Optional
import subprocess
from abc import ABC
from database import database
import os
import sys
import logging

USER_DIR = os.path.expanduser('~') + "/"
PROJECT_DIR = USER_DIR + ".local/appman/apps/bg-slideshow/"

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler(PROJECT_DIR + "manager.log", mode="w")],
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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

class Abstract_manager(ABC):
    def getImages(self):
        if not self.db.path:
            logging.warning("No image path set, skipping getImages()")
            return
        try:
            logging.info(f"Fetching image files from: {self.db.path}")
            files = subprocess.run("ls", stdout=subprocess.PIPE, text=True, cwd=self.db.path).stdout.splitlines()
            self.db.imgs = []
            for file in files:
                type = file.split(".")[-1]
                if type in VALID_TYPES:
                    self.db.imgs.append(file)
            
            if len(self.db.imgs) == 0:
                logging.warning("Set images path contains no valid images")
        except Exception as e:
            logging.error("Fetching image file names failed", exc_info=True)

class Manager(Abstract_manager):
    def __init__(self):
        logging.info("Initializing Manager")
        self.db: database = database()

    def newPath(self, args_path):
        logging.info(f"Setting new image path: {args_path}")
        self.db.path = args_path
        self.getImages()

    def setTime(self, args_time, minutes=False):
        if args_time is None:
            logging.warning("setTime() called with None value")
            return
        self.db.time = args_time * 60 if minutes else args_time
        logging.info(f"Set time interval: {self.db.time} seconds")

    def activate(self):
        if not self.db.imgs or len(self.db.imgs) <= 0:
            logging.error("No images directory set, activation failed")
            print("Error: no imgs directory set, failed to activate")
            return
        try:
            logging.info("Activating slideshow application")
            process = subprocess.run(["python3", os.path.join(PROJECT_DIR + "bg-slideshow.py")], close_fds=True, capture_output=True)
            logging.debug(f"Activation output: {process.stdout}, errors: {process.stderr}")
        except Exception as e:
            logging.error("Failed to activate application", exc_info=True)
            print(f"Failed to activate application:\n{e}")

    def deactivate(self):
        try:
            logging.info("Deactivating slideshow application")
            subprocess.run(["pkill", "-f", f"bg-slideshow.py"], check=True, close_fds=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except Exception as e:
            logging.warning("No process to terminate", exc_info=True)
            print("Warning: No process to terminate")

    def refresh(self):
        logging.info("Refreshing application")
        self.deactivate()
        self.activate()

    def executeArgs(self, args: argparse.ArgumentParser):
        logging.info("Executing command-line arguments")
        if args.uninstall:
            logging.info("Uninstalling application")
            subprocess.run([os.path.join(PROJECT_DIR + "uninstall.sh")])
            sys.exit(0)
        if args.set_time:
            self.setTime(args_time=args.set_time, minutes=False)
        if args.set_time_minutes:
            self.setTime(args_time=args.set_time_minutes, minutes=True)
        if args.path:
            self.newPath(args_path=args.path)
        if args.refresh:
            self.refresh()
        if args.activate:
            self.activate()
        if args.deactivate:
            self.deactivate()
        
        self.db.write()
        logging.info("Command execution completed")

def main():
    parser = argparse.ArgumentParser(prog="bg-slideshow", description="A command-line utility for managing background slideshows in GNOME.")

    parser.add_argument("-s", "--set-time", type=int, help="Time between images in seconds, defaults to 30 seconds")
    parser.add_argument("-sm", "--set-time-minutes", type=int, help="Time between images in minutes")
    parser.add_argument('path', type=str, nargs='?', help="Directory path containing images for the slideshow")

    parser.add_argument("-a", "--activate", action="store_true", help="Activate the slideshow, requires path to be set")
    parser.add_argument("-d", "--deactivate", action="store_true", help="Deactivate the slideshow, will terminate all instances if multiple are running")
    parser.add_argument("-r", "--refresh", action="store_true", help="Reactivates app to be updated with the current shell environment and images in the directory")
    parser.add_argument("--uninstall", action="store_true", help="Uninstalls the background slideshow application and all its components")

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    
    manager = Manager()
    manager.executeArgs(args)

if __name__ == "__main__":
    main()
