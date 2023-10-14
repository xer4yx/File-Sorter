import os
import json
from pathlib import Path
from file_sorter import Sorter


class Organizer:
    @staticmethod
    def start_organize():
        """
            A method that creates or reads folders in a target directory. It also includes method from 
            another module that sorts out files and moves them from a different folder depending
            on their extension type.
        """
        with open('C:/Users/63928/Desktop/File Sorter/config.json', 'r') as config_file:
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
