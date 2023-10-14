import os
import time
from organizer import Organizer

class GUI:
    def sort_interface():
        os.system('cls')
        print("||========================== FILE SORTER ===========================||")
        print("||   [1] SORT ALL FILES                                             ||")
        print("||   [2] RETURN TO MAIN MENU                                        ||")
        choice = int(input("""||==================================================================||
    Enter your Choice: """))
        if choice == 1:
            Organizer.start_organize()
        elif choice == 2:
            os.system('cls')
            GUI.main_interface()
        else:
            os.system('cls')
            print("Invalid choice!")
            buffer = buffer = input("Press <ENTER> to continue...")
    
    def main_interface():
        os.system('cls')
        print("||========================== FILE SORTER ===========================||")
        print("||   [1] SORT FILES                                                 ||")
        print("||   [2] EXIT PROGRAM                                               ||")
        choice = int(input("""||==================================================================||
    Enter your Choice: """))
        if choice == 1:
            GUI.sort_interface()
        elif choice == 2:
            os.system('cls')
            exit()
        else:
            os.system('cls')
            print("Invalid choice!")
            buffer = buffer = input("Press <ENTER> to continue...")
            
class Main:
    def run():
        time.sleep(1)
        Organizer.start_organize()
        
if __name__ == "__main__":
    Main.run()