import re
val2bot = re.compile(r"value (\d+) goes to bot (\d+)")
# (?P<name>...) names a pattern
bot2bot = re.compile(r"bot (?P<bot1>\d+) gives low to (?P<lowtype>bot|output) \
(?P<low>\d+) and high to (?P<hightype>bot|output) (?P<high>\d+)")

class DynamicList(list):
    "Acts like a list but expands when you set an out of bounds index."
    def __getitem__(self, key):
        if key < len(self):
            super().__getitem__(key)
        else:
            return None

    def __setitem__(self, key, value):
        if key < len(self):
            super().__setitem__(key, value)
        else:
            self.extend([None]*(key-len(self)+1))
            self[key] = value

class Botnet:
    
