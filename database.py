import json
from typing import List, Dict, Optional
import sys
import os

HOME = os.path.expanduser("~")
DATA_FILE = os.path.join(HOME, ".local/appman/apps/bg-slideshow/", "data.json")

class database:
    def __init__(self):
        self.path: Optional[str] = None
        self.imgs: Optional[List[str]] = None
        self.time: Optional[int] = None
        self.fetch()
        if self.time is None:
            self.time = 30

    def fetch(self) -> Dict:
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.path = data.get("path")
                self.imgs = data.get("imgs")
                self.time = data.get("time")
                return data
        except FileNotFoundError:
            return {}
        except Exception as e:
            print("file reading failed:")
            print(e)
            try:
                print("rebuilding db")
                with open(DATA_FILE, "w") as file:
                    empty = {}
                    json.dump(empty, file, indent=4)
            except Exception as e:
                print("Failed rebuild db, exiting now")
                sys.exit(1)

    def write(self):
        data: Dict = {}
        if self.path:
            data["path"] = self.path
        if self.imgs:
            data["imgs"] = self.imgs
        if self.time:
            data["time"] = self.time
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
