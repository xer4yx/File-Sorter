import os
import shutil
import json


class Sorter:
    @staticmethod
    def start_sort():
        with open('C:/Users/63928/Desktop/File Sorter/config.json', 'r') as config_file:
            config = json.load(config_file)
            source = config["source-dir"]
            extensionConfig = config.get("file-extension")
            os.chdir(source)
            for file in os.listdir():
                file_classifier = extensionConfig.get(os.path.splitext(file)[1])
                folder = config.get("dest-folders").get(file_classifier)
                if file_classifier is not None:
                    shutil.move(os.path.join(source, file), folder)
                else:
                    print(f"{file} cannot be moved due to unspecified type")
