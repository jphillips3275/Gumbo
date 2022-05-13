# Gumbo: CS Capstone II Project
### Project Overview: 
The purpose of this project is to use artificial intelligence to create a bot in Python that can outperform the average human player in the strategic game, Bloons Tower Defense 6. Bloons Tower Defense is a strategic game that consists of a player buying and organizing defensive towers that fire upon a set deployment of enemies (balloons). The AI pulls health and income values from the game by taking a screenshot of the game each round and converts that into usable data through OCR. The AI takes control of the mouse and hotkeys to play the game and uses the genetic algorithm to determine the best location to place towers and the order it should buy/upgrade towers.

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

=======
Project Documentation: https://drive.google.com/drive/folders/1nx5NhjpqwfuoiZjwGuZzL7UeC2b44zds?usp=sharing

### Team Members
- Jackson Phillips (AI)
- Jim Yang (OCR)
- Yilong Yuan (Interfacing with game)
- Xin Zhang (Interfacing with game)

### Requirements:
- Bloons Tower Defense 6
- pyautogui library `pip install pyautogui` (on Windows) or `pip3 install pyautogui` (on MacOS and Linux)
- tesseract
  -  [Installation instructions](https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md)
      -  NOTE: Windows requires downloading Tesseract Installer; see Installation instructions for more details
  -  Check tesseract installed correctly by typing command `tesseract --version`
- pytesseract, OpenCV, numpy library  (OCR Requirements)
  - tesseract is not a Python library so need to install the python wrapper, pytesseract, as well as openCV and numpy for manipulating images
    ```
    pip install pytesseract
    pip install opencv-python
    pip install numpy
    ```
- pynput library `pip install pynput`

### How to run code:
1. Clone github repository `git clone https://github.com/jphillips3275/Gumbo.git`
2. Create virtual environment `virtualenv env`
3. Activate virtual environment `source env/bin/activate`
4. Install all requirements
5. Start a Bloons TD game 
6. Run AI using `python3 AI.py`. We recommend two monitors to ensure you're not blocking the AI from interacting with the game.

### Demo Video:
https://youtu.be/Y5P86a5NryM
