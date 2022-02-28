import numpy as np
import pyautogui
import pytesseract
import cv2
import random

from PIL import ImageGrab


def main():
    #Read BTD6 screen based on screen 1152 x 720, with screen on top left
    
    #coordinate for the life
    x = 11
    y = 68
    lifex2 = 121
    lifey2 = 135
    
    #coordinates for the income
    incomex = 200
    incomey = 70
    incomex2 = 280
    incomey2 = 135

    #coordinates for the round
    roundx = 823
    roundy = 85
    roundx2 = 930
    roundy2 = 125

    
    #Reads the income 
    #Has errors
    #EX: $411 can't be read because the number are too close based on the font used
    #EX: $ sign can be read as 3
    for x in range(5):
        income = ImageGrab.grab(bbox= (incomex*2,incomey*2,incomex2*2,incomey2*2))
        #cconfig = r'--oem 3 --psm 6 outputbase digits'
        #top = cv2.cvtColor(np.array(top), cv2.COLOR_BGR2GRAY)
        # income = cv2.resize(np.array(income), None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        # income = cv2.medianBlur(np.array(income),5)
        image = pytesseract.image_to_string(cv2.cvtColor(np.array(income), cv2.COLOR_BGR2RGB),config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(image)

        if(image == ""):
            incomeTotal = 0
        else:
            incomeTotal = int(image)
        
        #Use mouse control to place dart monkeys randomly
        # print(incomeTotal)
        # if(incomeTotal > 170):
        #     x = random.randrange(140,s800)
        #     y = random.randrange(200,600)
        #     pyautogui.click(956,150)
        #     pyautogui.typewrite("q")
        #     pyautogui.moveTo(x,y, duration=1)
        #     pyautogui.click()

    #prints life value for 5 times
    #Life result from reading image: 180, 9180(9 could be from the heart)
    for x in range(5):
        life = ImageGrab.grab(bbox= (x*2,y*2,lifex2*2, lifey2*2))
        #life.show() Shows an image that was crop with imageGRab
        life = cv2.resize(np.array(life), None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        life = cv2.medianBlur(np.array(life),5)

        lifeText = pytesseract.image_to_string(cv2.cvtColor(np.array(life), cv2.COLOR_BGR2RGB),config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print((lifeText))
        
    #prints round value for 5 times
    #Image reading result: 240, 0, 2740(/ is read as 7)
    for x in range(5):
        round = ImageGrab.grab(bbox= (roundx*2,roundy*2,roundx2*2,roundy2*2))
        round = cv2.resize(np.array(round), None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        round = cv2.medianBlur(np.array(round),5)
        
        roundText = pytesseract.image_to_string(cv2.cvtColor(np.array(round), cv2.COLOR_BGR2GRAY),config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print((roundText))

main()
