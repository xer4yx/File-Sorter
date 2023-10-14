import os
import time
from organizer import Organizer
            
class Main:
    def run():
        time.sleep(1)
        Organizer.start_organize()
        
if __name__ == "__main__":
    Main.run()