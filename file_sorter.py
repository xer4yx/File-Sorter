import os
import shutil
import json


class Sorter:
    @staticmethod
    def start_sort():
        try:
            with open('C:/Users/63928/Desktop/File Sorter/config.json', 'r') as config_file:
                config = json.load(config_file)

                source = config.get("source-dir")
                if not source:
                    print("Source directory not specified in config.")
                    return

                extension_config = config.get("file-extension")
                os.chdir(source)
                dest_folders = config.get("dest-folders", {})

                for file in os.listdir():
                    file_classifier = extension_config.get(os.path.splitext(file)[1])
                    folder = dest_folders.get(file_classifier)

                    if file_classifier is None:
                        print(f"{file} cannot be moved due to unspecified type")
                        continue

                    if folder is None:
                        print(f"No destination folder specified for {file_classifier} files.")
                        continue

                    source_path = os.path.join(source, file)
                    dest_path = os.path.join(folder, file)
                    shutil.move(source_path, dest_path)

        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Program has been executed")
