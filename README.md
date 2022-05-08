# Gumbo
CS Capstone II Project

## **About**
An AI that plays Bloons tower defense 6 (BTD6) by placing down towers. Currently AI does not upgrade the tower and only places them down.


## Issues 
Orginally plan to use CheatEngine to get the data from the game, but the application does not work on MACOS unless the SIP is disable.

## Implementations
The AI is implemented using genetic algorithm. Switch to use an OCR that would instead read the data on the game screen such as the current round and health. Pytesseract is able to read an image from the game by taking two coordinates points to form a box around the text.

## Language
Python

## Dependency
Install these if error occur with imported libraries<br>
pip install opencv-python<br>
pip install pytesseract<br>
pip install numpy<br>

#This line is for window only<br>
#https://github.com/UB-Mannheim/tesseract/wiki Download from here<br>

