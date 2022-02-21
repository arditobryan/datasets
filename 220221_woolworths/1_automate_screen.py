###WORKS IF YOU HAVE ONE TAB OPEN IN YOUR BROWSER
from posixpath import dirname
import pyautogui
import time
import pyperclip
import os

base = 'https://www.woolworths.com.au/shop/recipes/collections/'
link_list = [
    'cooking-method-and-appliances',
    'category', 
    'seasons',
    'dietary-lifestyle',
    'fresh-ingredients',
    'everyday-cooking',
    'main-ingredient',
    'meal-type',
    'cuisine'
]

#start the algo
time.sleep(3)

def hold_W(hold_time, key):
    start = time.time()  
    while time.time() - start < hold_time:
        pyautogui.press(key)

for link in link_list:
    if link not in os.listdir(r'C:\Users\ardit\Desktop\Projects\relevanceAI\_repos\datasets\220221_woolworths\files'):
        counter = 0

        #change link
        full_link = base+link
        print(full_link)
        #change link
        pyautogui.click(600, 50)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(full_link)
        pyautogui.hotkey('Enter')
        time.sleep(3)  

        #given a path, create a folder and keep adding new files after that
        name = link
        path = r'C:\Users\ardit\Desktop\Projects\relevanceAI\_repos\datasets\220221_woolworths\files'
        path_files = path+'\\'+name

        if name not in os.listdir(path):
            os.mkdir(path_files)

        #while True cases a bunch of errors and dysinchronization
        while counter <= 8:
            #scroll down                        
            hold_W(2, 'space')
            hold_W(0.02, 'pageup')
                
            #WE NEED A PAUSE OF A FRACTION OF A SECOND AFTER A SCROLL
            #otherwise the image won't be recognized
            time.sleep(0.2)

            #locate show_more
            show_more_img = r'C:\Users\ardit\Desktop\Projects\relevanceAI\_repos\datasets\220221_woolworths\show_more.png'
            start = pyautogui.locateOnScreen(show_more_img, confidence=0.72) #If the file is not a png file it will not work
            print(start, counter)
            if start != None:
                pyautogui.click(start)
            else:
                counter += 1

            #scroll up
            time.sleep(2.6)

        #save backup       
        pyautogui.click(1710, 390)
        pyautogui.hotkey('ctrl', 'c')
        s = pyperclip.paste()
        highest = os.listdir(path_files)
        with open(path_files+'\\'+str(len(highest))+'.html', 'w') as f:
            f.write(s)