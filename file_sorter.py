import os
import shutil
import json

class Sorter:
    @staticmethod
    def start_sort():
        try:
            with open('C:/Users/63928/Desktop/File Sorter/config.json', 'r') as config_file:
                config = json.load(config_file)
                source = config["source-dir"]
                extensionConfig = config.get("file-extension")
                os.chdir(source)
                for file in os.listdir():
                    file_classifier = extensionConfig.get(os.path.splitext(file)[1])
                    folder = config.get("dest-folders").get(file_classifier)
                    source_path = os.path.join(source, file)
                    dest_path = os.path.join(folder, file)
                    if file_classifier is not None:
                        shutil.move(source_path, dest_path)
                    else:
                        print(f"{file} cannot be moved due to unspecified type")
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
        except Exception as e:
            print(f"An error occurred: {e}")
