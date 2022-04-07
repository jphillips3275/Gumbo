from operator import invert
import numpy as np
# import pyautogui
import pytesseract
import cv2
import base64

from PIL import ImageGrab, Image

def readIncome(incomex,incomey,incomex2,incomey2,imageIncome):
    print("The income")
    for x in range(5):
        # getImage = cv2.imread(imageIncome)
        if (type(imageIncome) is np.ndarray):
            # getImage = cv2.imread(imageIncome)
            arr1 = imageIncome
        else:
            income = ImageGrab.grab(bbox= (incomex*2,incomey*2,incomex2*2,incomey2*2))
            arr1 = np.array(income)
            
        frame1 = cv2.cvtColor(arr1, cv2.COLOR_BGR2GRAY)
        incomeblur = cv2.GaussianBlur(frame1,(3,3),0)
        # thresh1= cv2.threshold(frame1,220,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        thresh1= cv2.threshold(incomeblur,220,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernelI = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        openingI = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernelI)
        invertI = 255 - openingI

        # psm 6, 10 or 13
        image = pytesseract.image_to_string(invertI,lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        print(image)
        # cv2.imshow("Opening",openingI)
        # cv2.waitKey(0)
    # Values are return as string
    return (image).strip()

    #Reads the income 
    #prints life value for 5 times
def readLife(xlife, ylife, lifex2, lifey2, imgLife):
    print("The life")
    for x in range(5):

        if (type(imgLife) is np.ndarray):
            # getImage = cv2.imread(imageIncome)
            arrL = imgLife
        else:
            life = ImageGrab.grab(bbox= (xlife*2,ylife*2,lifex2*2, lifey2*2))
            # Import the data into numpy array, because python reads the data as numpy array
            arrL = np.array(life)


        frame = cv2.cvtColor(arrL, cv2.COLOR_BGR2GRAY)
        lifeblur = cv2.GaussianBlur(frame,(3,3),0)
        thresh = cv2.threshold(lifeblur,220,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        invert = 255 - opening

        # psm 10 
        # For some maps works it better with invert(black background) or opening(solid black number, white background) image
        lifeText = pytesseract.image_to_string(opening,lang='eng',config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(lifeText)
        # Just shows the image that the computer is trying to read
        # cv2.imshow("InvertImage",invert)
        # cv2.imshow("Gray",frame)
        # cv2.imshow("kernel",frame)
        # cv2.imshow("Morp",opening)
        # cv2.waitKey()
        # or life.show() to show the original image
        # life.show()
       
    return (lifeText).strip()

def readRound(roundx, roundy, roundx2, roundy2, imgRound):
    #prints round value for 5 times
    #Image reading
    print("The round")
    for x in range(5):

        if (type(imgRound) is np.ndarray):
            # getImage = cv2.imread(imageIncome)
            arrR = imgRound
        else:
            round = ImageGrab.grab(bbox= (roundx*2,roundy*2,roundx2*2,roundy2*2))
            arrR = np.array(round)


        roundImage = cv2.cvtColor(arrR, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(roundImage,(3,3),0)
        # noiseImage = removeNoise(roundImage)
        roundThresh = cv2.threshold(blur,220,255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        
        kernelR = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        openingR = cv2.morphologyEx(roundThresh, cv2.MORPH_CLOSE, kernelR)
        invertR = 255 - openingR

        # Use --psm 8, because psm 13 doesn't work on number 4
        roundText = pytesseract.image_to_string(invertR,lang='eng',config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(roundText)
    
        # Shows the original image
        # round.show()
        # shows the image after inverted
        # cv2.imshow("test",invertR)
        # cv2.waitKey(0)
    return (roundText).strip()

def main():
    # Use python pyautogui.position() to get the coordinate or use built-in software to find coordinates
    # Top left coordinates of the life
    xlife = 61
    ylife = 81
    # Bottom right cooridinates of the life
    lifex2 = 115
    lifey2 = 121

    incomex = 211
    incomey = 77

    incomex2 = 275
    incomey2 = 135

    # For round coordinates 1/40: might be read as 140 or 1740 unless the coordinates only
    # captures the left most part
    roundx = 830
    roundy = 91

    roundx2 = 879
    roundy2 = 123

    # imgIncome = open('IncomeTest650.png')
    imgIncome = cv2.imread('')
    imgLife = cv2.imread('')
    imgRound = cv2.imread('')
    # imgIncome = 'IncomeTest650.png'
    # imgIncome.show()

    #This line is for window only
    #https://github.com/UB-Mannheim/tesseract/wiki Download from here
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    readIncome(incomex,incomey,incomex2,incomey2,imgIncome)
    readLife(xlife, ylife, lifex2, lifey2, imgLife)
    readRound(roundx, roundy, roundx2, roundy2, imgRound)

if __name__ == '__main__':
	main()

