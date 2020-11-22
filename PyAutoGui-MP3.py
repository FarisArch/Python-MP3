 # 
import webbrowser
import time
import pyautogui
import sys
webbrowser.open("https://www.mp3juices.cc/") #Opens any webbrowser available
time.sleep(3)
search =pyautogui.prompt("What to search?:") # Prompts a GUI 
if search == None:
    sys.exit()
else:
    pyautogui.click(671, 376) # Clicks on searchbar
    pyautogui.typewrite(search)
    pyautogui.click(951, 374) #Clicks on search icon
    time.sleep(5)
    pyautogui.click(556,161) # Clicks on first choice in list
    time.sleep(5)
    pyautogui.click(654,428) # Clicks the download
    time.sleep(5)
    pyautogui.click(583,557) #Downloads
    time.sleep(5)
    pyautogui.click(475,427) # Save file
    time.sleep(3)
    pyautogui.click(879,525) # Confirm
    sys.exit()
