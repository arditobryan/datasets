###WORKS IF YOU HAVE ONE TAB OPEN IN YOUR BROWSER
from posixpath import dirname
import pyautogui
import time
import pyperclip
import os
                  
#given a path, create a folder and keep adding new files after that
name = 'mix3'
path = r'D:\_Projects\relevanceAI\_repos\datasets\220216_opensea\files'
path_files = path+'\\'+name

if name not in os.listdir(path):
    os.mkdir(path_files)

#start the algo
time.sleep(3)

def hold_W(hold_time):
    start = time.time()  
    while time.time() - start < hold_time:
        pyautogui.press('space')

while True:
    #scroll down                      
    pyautogui.click(1635, 210)
    hold_W(0.25)
    time.sleep(2.6)

    #save backup
    pyautogui.click(1700, 195)
    pyautogui.hotkey('ctrl', 'c')
 
    s = pyperclip.paste()
    highest = os.listdir(path_files)
    with open(path_files+'\\'+str(len(highest))+'.html', 'w') as f:
        f.write(s)

    #leave time to interrupt the algo
    time.sleep(0.6)

