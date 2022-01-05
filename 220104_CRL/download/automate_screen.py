###WORKS IF YOU HAVE ONE TAB OPEN IN YOUR BROWSER
import pyautogui
import time

with open('relevanceAI/_repos/datasets/220104_CRL/tag_list.txt') as file:
    str1 = file.read()
tag_list = [x[2:] for x in str1.split("',\n")][1:-1]
print(tag_list)

#start the algo
time.sleep(2)

for tag in tag_list:
    #click on the url and go to the new tag
    pyautogui.click(600, 50)
    pyautogui.write(f'https://royaleapi.com/player/{tag}/battles')
    pyautogui.hotkey('enter')

    #wait for the page to load
    time.sleep(5)
    pyautogui.click(1450, 460)
    time.sleep(1)