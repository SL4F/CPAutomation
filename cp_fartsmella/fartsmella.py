'''
fartsmella
'''
import pyautogui as pg
import time, random, os

def main():
    '''Creates and runs auto clicker.'''
    start = input("Run auto fart? (y/n): ")
    delay = random.randint(0, 1)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    if start.lower() == "y":
        print("Running... (Ctrl + C while this window is selected to end.)")
        print(start)
        while True:
            pg.press(keys=('e', 't'), interval=0.1)
            time.sleep(delay)
    else:
        input("Goodbye.")
        
while __name__ == "__main__":
    main()