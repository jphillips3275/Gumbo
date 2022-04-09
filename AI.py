import pyautogui
import random
import time
from pynput.keyboard import Key, Controller
from towerPrice import towerPrice

pyautogui.FAILSAFE = False
keyboard = Controller()

def randomCoord():
    xCoord = random.randrange(leftBorder, rightBorder)
    yCoord = random.randrange(topBorder, bottomBorder)
    return [xCoord, yCoord]

def randomTowers(monkeys):
    towers = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "iceMonkey", "glueGunner", "sniperMonkey", "monkeyAce",
    "heliPilot", "mortarMonkey", "wizardMonkey", "superMonkey", "ninjaMonkey", "alchemist", "druid", "spikeFactory", "engineerMonkey"]
    towersLimited = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "iceMonkey", "glueGunner", "sniperMonkey", "monkeyAce",
    "mortarMonkey", "wizardMonkey", "ninjaMonkey", "alchemist", "druid", "engineerMonkey"]

    i=1
    while i < 100:  #this is stupid but for some reason doing 2 loops isn't working for me and I hate it
        x = random.randrange(0, len(towers))
        monkeys[0].append(towers[x])
        x = random.randrange(0, len(towers))
        monkeys[1].append(towers[x])
        x = random.randrange(0, len(towers))
        monkeys[2].append(towers[x])
        x = random.randrange(0, len(towers))
        monkeys[3].append(towers[x])
        x = random.randrange(0, len(towers))
        monkeys[4].append(towers[x])
        i+=1
    x = random.randrange(0, len(towersLimited)) #some small bugs when you can't buy a tower round 1 so I just limited the towers possible
    monkeys[0][0] = towers[x]                   #makes it more likely to complete too so whatever
    x = random.randrange(0, len(towersLimited))
    monkeys[1][0] = towers[x]
    x = random.randrange(0, len(towersLimited))
    monkeys[2][0] = towers[x]
    x = random.randrange(0, len(towersLimited))
    monkeys[3][0] = towers[x]
    x = random.randrange(0, len(towersLimited))
    monkeys[4][0] = towers[x]
    return monkeys

def checkPlaceable():
    im = pyautogui.screenshot()
    x = pyautogui.position(1596, 123)
    px = im.getpixel(x)
    if px != (255, 255, 255):
        print("placeable")
        return True
    else:
        print("not placeable")
        return False

def startRound(started):
    im = pyautogui.screenshot()
    x = pyautogui.position(1810, 1024)
    px = im.getpixel(x)
    check = im.getpixel(pyautogui.position(0,0))

    pyautogui.click(1810, 1024)
    time.sleep(1)
    if started == False:
        pyautogui.click(1810, 1024)
        started = True
    pyautogui.moveTo(0,0)
    print("round started")
    while check != px:
        im = pyautogui.screenshot()
        x = pyautogui.position(1810, 1024)
        check = im.getpixel(x)
        if checkDeath() == True:
            print("death")
            break
    print("round ended")

def buyMonkey(monkeys, coord, money):
    x = 0
    money = money - towerPrice[monkeys]["baseCost"]
    while 1:
        print(coord)
        pyautogui.moveTo(1800, 100)
        key = towerPrice[monkeys]["hotkey"]
        pyautogui.moveTo(coord)
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(.3)
        pyautogui.click(coord)
        if checkPlaceable() == True:
            return money, coord
        coord = randomCoord()

def checkDeath():
    im = pyautogui.screenshot()
    x = pyautogui.position(564, 456)
    px = im.getpixel(x)
    if px == (96, 148, 215):
        return True
def checkWin():
    im = pyautogui.screenshot()
    x = pyautogui.position(687, 217)
    px = im.getpixel(x)
    if px == (241, 60, 11):
        print("win!")
        quit()

def playGame(monkeys, coords):
    moneyEasy = [650, 121, 137, 138, 175, 164, 163, 182, 200, 199, 314, 189, 192, 282, 259, 266, 268, 165, 358, 260, 186, 351, 298, 277, 167, 335, 333, 662, 266, 389, 337, 537, 627, 205, 912, 1150, 896, 1339, 1277, 1759, 521]
    money = moneyEasy[0]
    rounds = 0

    tempMoney = money
    if money - towerPrice[monkeys[0]]["baseCost"] > 0:
        money, coords[0] = buyMonkey(monkeys[0],coords[0], money)
    else:
        print(towerPrice[monkeys[0]]["baseCost"],"too expensive")
    startRound(False)
    rounds+=1
    money = money + moneyEasy[1]

    coordPlace = 1
    while rounds < 40:
        checkWin()
        while money-towerPrice[monkeys[coordPlace]]["baseCost"] > 0:
            money, coords[coordPlace] = buyMonkey(monkeys[coordPlace],coords[coordPlace], money)
            coordPlace+=1
        else:
            print(towerPrice[monkeys[coordPlace]]["baseCost"], "too expensive")
        startRound(True)
        rounds+=1
        money = money + moneyEasy[rounds]
        if checkDeath() == True:
            return rounds
            break

    print("round = ", rounds, "money = ", money)

def createChildren(monkeys, coords, score):
    sorted = []
    sorted.append(score[0]) #this is stupid but I have to do it like this because sorted = score passes it by value and sorts score which I don't want
    sorted.append(score[1])
    sorted.append(score[2])
    sorted.append(score[3])
    sorted.append(score[4])
    sorted.sort(reverse=True)
    parent1 = sorted[0]
    parent1 = score.index(first)  #parent 1 and 2 should contain the indexes of the top 2 performing monkey arrays
    parent2 = sorted[1]
    parent2 = score.index(second)

    child1 = []
    cCoords1 = []
    child2 = []
    cCoords2 = []
    child3 = []
    cCoords3 = []
    child4 = []
    cCoords4 = []
    child5 = []
    cCoords5 = []
    children = [child1, child2, child3, child4, child5]
    cCoords = [cCoord1, cCoord2, cCoord3, cCoord4, cCoord5]

    while x < len(monkeys):
        if num%2 == 0:
            children[0][x] = monkeys[parent1][x]
            cCoords[0][x] = coords[parent1][x]
            children[1][x] = monkeys[parent2][x]
            cCoords[1][x] = coords[parent2][x]
        else:
            children[0][x] = monkeys[parent2][x]
            cCoords[0][x] = coords[parent2][x]
            children[1][x] = monkeys[parent1][x]
            cCoords[1][x] = coords[parent1][x]
        y = 0
        if y < 2:
            children[2][x] = monkeys[parent1][x]
            cCoords[2][x] = coords[parent1][x]
            children[3][x] = monkeys[parent2][x]
            cCoords[3][x] = coords[parent2][x]
        else:
            children[2][x] = monkeys[parent2][x]
            cCoords[2][x] = coords[parent2][x]
            children[3][x] = monkeys[parent1][x]
            cCoords[3][x] = coords[parent1][x]
        children[4][x] = monkeys[parent1][x]
        cCoords[4][x] = coords[parent1][x]

    children, cCoords = mutate(children, cCoords)

    return children, cCoords

def mutate(children, cCoords):
    replace1 = []
    cReplace1 = []
    replace2 = []
    cReplace2 = []
    replace3 = []
    cReplace3 = []
    replace4 = []
    cReplace4 = []
    replace5 = []
    cReplace5 = []
    replacements = [replace1, replace2, replace3, replace4, replace5]
    cReplacements = [cReplace1, cReplace2, cReplace3, cReplace4, cReplace5]
    replacements = randomTowers(replacements)
    i=0
    while i < 100:
        cReplacements[0].append(randomCoord())
        cReplacements[1].append(randomCoord())
        cReplacements[2].append(randomCoord())
        cReplacements[3].append(randomCoord())
        cReplacements[4].append(randomCoord())
        i+=1

    x = 0
    while x < len(children):
        y = random.randrange(1, 10)
        if y == 10:
            children[0][x] = replacements[0][x]
            cCoords[0][x] = cReplacements[0][x]
            children[1][x] = replacements[1][x]
            cCoords[1][x] = cReplacements[1][x]
            children[2][x] = replacements[2][x]
            cCoords[2][x] = cReplacements[2][x]
            children[3][x] = replacements[3][x]
            cCoords[3][x] = cReplacements[3][x]
            children[4][x] = replacements[4][x]
            cCoords[4][x] = cReplacements[4][x]
    return children, cCoords

leftBorder = 144
rightBorder = 1436
topBorder = 185
bottomBorder = 992


#monkey arrays, this is stupid I should just make 2 2d arrays
test1 = []
coord1 = []
score1 = []
test2 = []
coord2 = []
score2 = []
test3 = []
coord3 = []
score3 = []
test4 = []
coord4 = []
score4 = []
test5 = []
coord5 = []
score5 = []
monkeys = [test1, test2, test3, test4, test5]
coords = [coord1, coord2, coord3, coord4, coord5]
score = [score1, score2, score3, score4, score5]

monkeys = randomTowers(monkeys)
i=0
while i < 100:
    coords[0].append(randomCoord())
    coords[1].append(randomCoord())
    coords[2].append(randomCoord())
    coords[3].append(randomCoord())
    coords[4].append(randomCoord())
    i+=1

pyautogui.click(500,500)
while 1:
    p = 0
    while p <= 4:
        score[p] = playGame(monkeys[p], coords[p])
        pyautogui.click(853,817)
        time.sleep(.3)
        pyautogui.click(1146, 728)
        p+=1
    print(score)
    monkeys, coords = createChildren(monkeys, coords, score)