###WORKS IF YOU HAVE ONE TAB OPEN IN YOUR BROWSER
import pyautogui
import time
import pyperclip

#start the algo
time.sleep(3)

def hold_W(hold_time):
    start = time.time()  
    while time.time() - start < hold_time:
        pyautogui.press('space')

while True:
    #scroll down                      
    pyautogui.click(1000, 210)
    hold_W(60)

    #save backup
    pyautogui.click(1280, 210)
    pyautogui.hotkey('ctrl', 'c')
 
    s = pyperclip.paste() 
    with open(rf'C:\Users\ardit\Desktop\Projects\relevanceAI\_repos\datasets\220202_producthunt\marketing.txt','w') as f:
        f.write(s)

    #leave time to interrupt the algo
    time.sleep(6)