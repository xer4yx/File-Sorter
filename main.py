import time

from organizer import Organizer


class Main:
    @staticmethod
    def run():
        time.sleep(1)
        Organizer.start_organize()


if __name__ == "__main__":
    Main.run()
