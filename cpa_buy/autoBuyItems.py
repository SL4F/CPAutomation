import time
import keyboard
from pynput.mouse import Button, Controller
import os

mouse = Controller()
times_bought = 0
start = input("Run auto buy? (y/n): ")
if start.lower() == "y":
    print('Hover your mouse over the "ok" button\nSaving spot in 3 seconds...')
    time.sleep(3)
    buy_button = mouse.position
    print('Saved')
    os.system('cls')
    print('Hover your mouse over the "ok" button\nSaving spot in 3 seconds...')
    time.sleep(3)
    yes_button = mouse.position
    print('Saved')
    os.system('cls')
    print('Hover your mouse over the "ok" button\nSaving spot in 3 seconds...')
    time.sleep(3)
    ok_button = mouse.position
    print('Saved')

while start.lower() == "y":
    os.system('cls')
    print(f'times bought: {str(times_bought)}\npress b to buy')
    keyboard.wait('b')
    # Clicks on the item and opens buy menu
    mouse.position = buy_button
    mouse.click(Button.left,1)
    print('clicked item')
    time.sleep(0.5)
    # Buys item
    mouse.position = yes_button
    mouse.click(Button.left,1)
    print('clicked yes')
    time.sleep(1)
    # clicks ok
    mouse.position = ok_button
    mouse.click(Button.left,1)
    print('clicked ok')
    times_bought += 1