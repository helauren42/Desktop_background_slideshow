import json
from typing import List, Dict, Optional
import sys

DATA_FILE = ".data.json"

class database:
    def __init__(self):
        self.path: Optional[str] = None
        self.imgs: Optional[List[str]] = None
        self.time: Optional[int] = 30
        self.pid: Optional[int]= None
        self.fetch()

    def fetch(self) -> Dict:
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.path = data.get("path")
                self.imgs = data.get("imgs")
                self.time = data.get("time")
                self.pid = data.get("pid")
                print("[DEBUG] previous images: ", self.imgs)
                return data
        except FileNotFoundError:
            return {}
        except Exception as e:
            print("file reading failed:")
            print(e)
            sys.exit(1)

    def write(self):
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
    
    def addPid(self, pid: int):
        self.pid = pid
        self.write()
