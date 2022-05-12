###WORKS IF YOU HAVE ONE TAB OPEN IN YOUR BROWSER
import pyautogui
import pyperclip
import os
import time
import random

#give time to start the algo
time.sleep(3)

#it keep going from the latest downloaded file
path = r'D:\_Projects\relevanceAI\_repos\datasets\220429_glassdoor\files'
#highest_page_n = len(os.listdir(path))
highest_page_n = 1

for page_n in range(highest_page_n, 5000):
    #change url    
    pyautogui.click(875, 55)
    #pyautogui.write(f'https://www.glassdoor.com.au/Reviews/Uber-Reviews-E575263_P{page_n}.htm?filter.iso3Language=eng') 
    pyautogui.write(f'https://www.glassdoor.com.au/Reviews/Lyft-Reviews-E700614_P{page_n}.htm?filter.iso3Language=eng')
    pyautogui.press('Enter') 

    time.sleep(14)
    #save backup in html
    pyautogui.click(1700, 245)
    pyautogui.hotkey('ctrl', 'c')

    s = pyperclip.paste()
    
    # highest = os.listdir(path)
    # with open(path+'\\'+str(len(highest))+'.html', 'w') as f:
    #     f.write(s)

    with open(path+'\\'+'Lyft_'+str(page_n)+'.html', 'w') as f:
        f.write(s)

    time.sleep(10+random.randint(2, 10))