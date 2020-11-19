import webbrowser
import time
import pyautogui
import sys
webbrowser.open("https://www.mp3juices.cc/")
time.sleep(3)
search =pyautogui.prompt("What to search?:")
if search == None:
    sys.exit()
else:
    pyautogui.click(671, 376)
    pyautogui.typewrite(search)
    pyautogui.click(951, 374)
    time.sleep(5)
    pyautogui.click(556,161)
    time.sleep(5)
    pyautogui.click(654,428)
    time.sleep(5)
    pyautogui.click(583,557)
    time.sleep(5)
    pyautogui.click(475,427)
    time.sleep(3)
    pyautogui.click(879,525)
    sys.exit()
