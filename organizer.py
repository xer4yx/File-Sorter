import os
import json
from pathlib import Path
from file_sorter import Sorter


class Organizer:
    @staticmethod
    def start_organize():
        with open('path/to/File Sorter/config.json', 'r') as config_file:
            config = json.load(config_file)
            target = config["target-dir"]
            os.chdir(target)
            Path("Audio").mkdir(exist_ok=True)
            Path("Compressed").mkdir(exist_ok=True)
            Path("Disc & Media").mkdir(exist_ok=True)
            Path("Data & Database").mkdir(exist_ok=True)
            Path("Executables").mkdir(exist_ok=True)
            Path("Fonts").mkdir(exist_ok=True)
            Path("Image").mkdir(exist_ok=True)
            Path("Powerpoint").mkdir(exist_ok=True)
            Path("Programming").mkdir(exist_ok=True)
            Path("Spreadsheet").mkdir(exist_ok=True)
            Path("System").mkdir(exist_ok=True)
            Path("Video").mkdir(exist_ok=True)
            Path("Text").mkdir(exist_ok=True)
            Path("Misc").mkdir(exist_ok=True)
            Sorter.start_sort()
