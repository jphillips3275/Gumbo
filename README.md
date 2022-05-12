# Gumbo: CS Capstone II Project
### Project Overview: 
The purpose of this project is to use artificial intelligence to create a bot in Python that can outperform the average human player in the strategic game, Bloons Tower Defense 6. Bloons Tower Defense is a strategic game that consists of a player buying and organizing defensive towers that fire upon a set deployment of enemies (balloons). The AI pulls health and income data from the game by taking a screenshot of the game each round and using OCR to convert that into usable data. The AI takes control of the mouse and hotkeys to play the game and uses the genetic algorithm to determine the best location to place towers and the order it should buy/upgrade towers.

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
6. Run AI on top of game using `python3 AI.py`

### Demo Video:
LINK
