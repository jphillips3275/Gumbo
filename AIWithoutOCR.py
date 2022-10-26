import copy
import pyautogui
import random
import time
from pynput.keyboard import Controller
chanceMutation = 8 #higher number out of 10 means less likely
chanceUpgrade = 4
difficulty = 3 #0 = easy, 1 = normal, 2 = hard, 3 = CHIMPS
if difficulty == 0:
    from towerPrice import towerPrice
elif difficulty == 1:
    from towerPriceNormal import towerPrice
else:
    from towerPriceHard import towerPrice
topScore = 0
topMonkeySet = []
topCoordSet = []

pyautogui.FAILSAFE = False
keyboard = Controller()
instructionSize = 150

def randomCoord():
    xCoord = random.randrange(leftBorder, rightBorder)
    yCoord = random.randrange(topBorder, bottomBorder)
    return [xCoord, yCoord]

def randomTowers(monkeys):
    towers = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "iceMonkey", "glueGunner", "sniperMonkey", "monkeyAce",
    "heliPilot", "mortarMonkey", "dartlingGunner", "wizardMonkey", "superMonkey", "ninjaMonkey", "alchemist", "druid", "spikeFactory", "engineerMonkey"]
    towersLimited = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "sniperMonkey", "wizardMonkey", "ninjaMonkey",
     "alchemist", "druid", "engineerMonkey"]

    i=1
    while i < instructionSize:  #this is stupid but for some reason doing 2 loops isn't working for me and I hate it
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
        x = random.randrange(0, len(towers))
        monkeys[5].append(towers[x])
        x = random.randrange(0, len(towers))
        monkeys[6].append(towers[x])
        i+=1
    x = random.randrange(0, len(towersLimited)) #some small bugs when you can't buy a tower round 1 so I just limited the towers possible
    monkeys[0][0] = towersLimited[x]                #makes it more likely to complete too so whatever
    x = random.randrange(0, len(towersLimited))
    monkeys[1][0] = towersLimited[x]  
    x = random.randrange(0, len(towersLimited))
    monkeys[2][0] = towersLimited[x]  
    x = random.randrange(0, len(towersLimited))
    monkeys[3][0] = towersLimited[x]  
    x = random.randrange(0, len(towersLimited))
    monkeys[4][0] = towersLimited[x] 
    x = random.randrange(0, len(towersLimited))
    monkeys[5][0] = towersLimited[x] 
    x = random.randrange(0, len(towersLimited))
    monkeys[6][0] = towersLimited[x] 
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
    # pyautogui.click(100, 100)
    # time.sleep(.3)
    # pyautogui.click(100,100)
    # time.sleep(.3)
    # uncomment this if you're having prolems with monkey knowledge stopping the program

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
    timer = time.time() #hopefully should fix the problem of it sometimes not catching the end of the round
    while check != px or time.time() >= timer + 300:
        im = pyautogui.screenshot()
        x = pyautogui.position(1810, 1024)
        check = im.getpixel(x)
        if checkDeath() == True:
            print("death")
            break
    print("round ended")

def buyMonkey(monkeys, coord, money):
    money = money - towerPrice[monkeys]["baseCost"]
    i = 0
    while i < 50:
        print(coord)
        pyautogui.moveTo(1800, 100)
        key = towerPrice[monkeys]["hotkey"]
        pyautogui.moveTo(coord)
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(.3)
        pyautogui.click(coord)
        print("Monkey:", monkeys)
        time.sleep(.3)
        if checkPlaceable() == True:
            return money, coord
        coord = randomCoord()
        i+=1

def getUpgradeCost(path, targetIndex, monkeysList, coordsList):
    target = monkeysList[targetIndex]
    location = coordsList[targetIndex]

    cost = 0
    x = 0
    while x < int(path[0]):
        cost = cost + towerPrice[target]["path1"][x]
        x+=1
    x = 0
    while x < int(path[1]):
        cost = cost + towerPrice[target]["path2"][x]
        x+=1
    x = 0
    while x < int(path[2]):
        cost = cost + towerPrice[target]["path3"][x]
        x+=1
    x = 0
    print("buy a", path, "upgrade on a", target, "at location", location, "for price", cost)
    return cost

def buyUpgrade(path, targetIndex, coordsList):
    location = coordsList[targetIndex]
    pyautogui.click(location)
    x = 0
    while x < int(path[0]):
        keyboard.press(",")
        keyboard.release(",")
        time.sleep(.3)
        x+=1
    x = 0
    while x < int(path[1]):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.3)
        x+=1
    x = 0
    while x < int(path[2]):
        keyboard.press("/")
        keyboard.release("/")
        time.sleep(.3)
        x+=1
    x = 0
    pyautogui.click(1420, 40)

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
    print("checking win")
    if px == (241, 60, 11):
        print("win!")
        quit()

def playGame(monkeys, coords, income):
    money = income[0]
    if income[1] == 121:
        rounds = 0
        dif = 1
    elif income[1] == 138:
        rounds = 3
        dif = 2
    elif income[1] == 163:
        rounds = 6
        dif = 3

    if money - towerPrice[monkeys[0]]["baseCost"] > 0:
        money, coords[0] = buyMonkey(monkeys[0],coords[0], money)
    else:
        print(towerPrice[monkeys[0]]["baseCost"],"too expensive")
    startRound(False)
    rounds+=1
    money = money + income[1]

    coordPlace = 1
    while rounds < 100:
        time.sleep(.5)
        checkWin()
        if checkDeath() == True:
            return rounds
        print("moneys is", money)

        try:
            while money-towerPrice[monkeys[coordPlace]]["baseCost"] > 0:
                money, coords[coordPlace] = buyMonkey(monkeys[coordPlace],coords[coordPlace], money)
                print("monkey bought, remaning money is", money)
                coordPlace+=1
            else:
                print(monkeys[coordPlace], "too expensive, cost is:", towerPrice[monkeys[coordPlace]]["baseCost"], "money is:", money,)
        except:
            try:
                if money-getUpgradeCost(monkeys[coordPlace], coords[coordPlace], monkeys, coords) > 0:
                    print("buying upgrade, money is", money)
                    money = money - getUpgradeCost(monkeys[coordPlace], coords[coordPlace], monkeys, coords)
                    buyUpgrade(monkeys[coordPlace], coords[coordPlace], coords)
                    coordPlace+=1
                else:
                    print("upgrade too expensive, current money is:",money)
            except Exception as e:
                print("upgrade failed, upgrade attempted to be placed on an upgrade instruction")
                print(e)
                coordPlace+=1
        if checkDeath() == True:
            return rounds
        startRound(True)
        print("income is", income[rounds])
        if dif == 3:
            money = money + income[rounds-5]
        elif dif == 2:
            money = money + income[rounds-2]
        else:
            money = money + income[rounds]
        rounds+=1
        print("rounds =", rounds)
        if checkDeath() == True:
            return rounds

    print("round = ", rounds, "money = ", money)

def createChildren(monkeys, coords, score):
    sortedScore = []
    sortedScore.append(score[0]) #this is stupid but I have to do it like this because sorted = score passes it by value and sorts score which I don't want
    sortedScore.append(score[1])
    sortedScore.append(score[2])
    sortedScore.append(score[3])
    sortedScore.append(score[4])
    sortedScore.append(score[5])
    sortedScore.append(score[6])
    sortedScore.sort(reverse=True)
    parent1 = score.index(sortedScore[0])  #parent 1 and 2 should contain the indexes of the top 2 performing monkey arrays
    parent2 = score.index(sortedScore[1])
    if parent1 == parent2:
        x = 0
        while x < len(score):
            if score[x] == score[parent1] and x != int(parent1):
                parent2 = x
            x+=1

    print("score =",score)
    print("parent1 =",parent1)
    print("parent2 =",parent2)
    
    global topScore
    global topMonkeySet
    global topCoordSet
    print("comparing", sortedScore[0], "vs", topScore)
    if sortedScore[0] >= topScore:
        print("sortedScore[0] is better")
        topScore = sortedScore[0]
        topMonkeySet = copy.deepcopy(monkeys[parent1])
        topCoordSet = copy.deepcopy(coords[parent1])
    else:
        print("topScore is better")
        monkeys[parent1] = copy.deepcopy(topMonkeySet)
        coords[parent1] = copy.deepcopy(topCoordSet)

    file = open("troubleshooting.txt", "a")
    for scores in score:
        file.write(str(scores))
        file.write(" ")
    file.write("\n\t")
    tsparent1 = "parent1 = "+str(parent1)
    tsparent2 = "parent2 = "+str(parent2)
    file.write(tsparent1)
    file.write(" ")
    file.write(tsparent2)
    file.write(" topScore = ")
    file.write(str(topScore))
    file.write("\n")
    file.close()

    child1 = []
    cCoord1 = []
    child2 = []
    cCoord2 = []
    child3 = []
    cCoord3 = []
    child4 = []
    cCoord4 = []
    child5 = []
    cCoord5 = []
    child6 = []
    cCoord6 = []
    child7 = []
    cCoord7 = []
    children = [child1, child2, child3, child4, child5, child6, child7]
    cCoords = [cCoord1, cCoord2, cCoord3, cCoord4, cCoord5, cCoord6, cCoord7]

    x = 0
    y = 0
    while x < len(monkeys[0]):
        if x%2 == 0:
            children[0].append(monkeys[parent1][x])
            cCoords[0].append(coords[parent1][x])
            children[1].append(monkeys[parent2][x])
            cCoords[1].append(coords[parent2][x])
        else:
            children[0].append(monkeys[parent2][x])
            cCoords[0].append(coords[parent2][x])
            children[1].append(monkeys[parent1][x])
            cCoords[1].append(coords[parent1][x])
        if y < 2:
            children[2].append(monkeys[parent1][x])
            cCoords[2].append(coords[parent1][x])
            children[3].append(monkeys[parent2][x])
            cCoords[3].append(coords[parent2][x])
            y+=1
        else:
            children[2].append(monkeys[parent2][x])
            cCoords[2].append(coords[parent2][x])
            children[3].append(monkeys[parent1][x])
            cCoords[3].append(coords[parent1][x])
            y+=1

        towers = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "iceMonkey", "glueGunner", "sniperMonkey", "monkeyAce",
    "heliPilot", "mortarMonkey","dartlingGunner", "wizardMonkey", "superMonkey", "ninjaMonkey", "alchemist", "druid", "spikeFactory", "engineerMonkey"]
        towersLimited = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "sniperMonkey", "wizardMonkey", "ninjaMonkey",
     "alchemist", "druid", "engineerMonkey"]
        children[4].append(towers[random.randrange(len(towers))])
        children[4][0] = towersLimited[random.randrange(len(towersLimited))]
        cCoords[4].append(randomCoord())
        x+=1
    i = 0
    while i < len(monkeys):
        children[i], cCoords[i] = mutate(children[i], cCoords[i])
        i+=1

    children[6] = copy.deepcopy(topMonkeySet) #should make sure the top scorer gets recorded and mutated
    cCoords[6] = copy.deepcopy(topCoordSet)
    i = 0
    while i < 6:
        cCoords[i] = verifyChild(children[i], cCoords[i])
        i+=1
    children[5] = copy.deepcopy(topMonkeySet)  #should make sure the top scorer gets recorded
    cCoords[5] = copy.deepcopy(topCoordSet)

    return children, cCoords

def mutate(children, cCoords):
    #I coded the random towers in a stupid way and I don't want to change it now so this is what we've got
    towers = ["dartMonkey", "boomerangMonkey", "bombShooter", "tackShooter", "iceMonkey", "glueGunner", "sniperMonkey", "monkeyAce",
    "heliPilot", "mortarMonkey", "dartlingGunner", "wizardMonkey", "superMonkey", "ninjaMonkey", "alchemist", "druid", "spikeFactory", "engineerMonkey"]
    newTowers = []
    newCoords = []
    i = 0
    while i < instructionSize:
        newTowers.append(towers[random.randrange(len(towers))])
        newCoords.append(randomCoord())
        i+=1
    newTowers, newCoords = addUpgrades(newTowers, newCoords)

    i = 1
    while i < len(children):
        rng = random.randrange(10)
        if rng > chanceMutation: #change this value to effect how often mutations happen
            children[i] = newTowers[i]
            cCoords[i] = newCoords[i]
        i+=1
    return children, cCoords

def verifyChild(monkeys, coords):   #likeliest place for bugs
    upgradeIndexes = [] #the indexes of every upgrade we do
    usedIndexes = [] #the indexes of every location that an upgrade points to
    usableIndexes = [] #the indexes that are still usable
    x = 0
    while x < len(monkeys):
        if len(monkeys[x]) == 3:
            upgradeIndexes.append(x)
        x+=1
    x = 0
    while x < len(coords):
        if coords[x] not in usedIndexes and isinstance(coords[x], int):
            usedIndexes.append(coords[x])
        x+=1
    x = 0
    while x < len(monkeys):
        if x not in usedIndexes and x not in upgradeIndexes:
            usableIndexes.append(x)
        x+=1

    x = 0
    while x < len(upgradeIndexes): #this loop fixes errors where an upgrade is placed on another upgrade instruction (or at least should)
        if len(monkeys[coords[upgradeIndexes[x]]]) == 3:
            try:
                coords[upgradeIndexes[x]] = usableIndexes.pop(0)
            except:
                pass
        x+=1

    coords = fixDuplicates(monkeys, coords)
    coords = fixSorting(coords)

    return(coords)

def fixSorting(coords):
    allTargets = []
    upgradeIndexes = []
    x = 0
    while x < len(coords):
        if isinstance(coords[x], int):
            allTargets.append(coords[x])
            upgradeIndexes.append(x)
        x+=1
    
    x = 0
    while x < len(upgradeIndexes):
        y = 0
        while y < len(allTargets):
            if allTargets[y] < upgradeIndexes[x]:
                try:
                    coords[upgradeIndexes[x]] = allTargets.pop(y)
                except:
                    pass
                break
            y+=1
        x+=1
        

    return(coords)

def fixDuplicates(monkeys, coords):
    upgradeIndexes = []
    usedIndexes = []
    usableIndexes = []
    duplicateIndexes = []
    x = 0
    while x < len(monkeys):
        if len(monkeys[x]) == 3:
            upgradeIndexes.append(x)
        x+=1
    x = 0
    while x < len(coords):
        if coords[x] not in usedIndexes and isinstance(coords[x], int):
            usedIndexes.append(coords[x])
        x+=1
    x = 0
    while x < len(monkeys):
        if x not in usedIndexes and x not in upgradeIndexes:
            usableIndexes.append(x)
        x+=1

    noDups = []
    x = 0
    while x < len(coords):
        if coords[x] not in noDups:
            noDups.append(coords[x])
        else:
            duplicateIndexes.append(x)
        x+=1
    x = 0
    usableIndexes.sort()
    while x < len(duplicateIndexes):
        if isinstance(coords[duplicateIndexes[x]], int):
            try:
                coords[duplicateIndexes[x]] = usableIndexes.pop(0)
            except:
                pass
        x+=1

    return coords

def generateUpgradePath():
    digit1 = 0
    digit2 = 0
    digit3 = 0

    rng = random.randrange(3)
    if rng == 0:
        x = random.randrange(100)
        if x <= 17:
            digit1 = 0
        elif 17 < x <= 34:
            digit1 = 1
        elif 34 < x <= 51:
            digit1 = 2
        elif 51 < x <= 68:
            digit1 = 3
        elif 68 < x <= 85:
            digit1 = 4
        elif x > 85:
            digit1 = 5

        if digit1 > 1:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if y <= 33:
                    digit2 = 0
                elif 33 < y <= 66:
                    digit2 = 1
                elif y > 66:
                    digit2 = 2
                digit3 = 0
            else:
                digit2 = 0
                if y <= 33:
                    digit3 = 0
                elif 33 < y <= 66:
                    digit3 = 1
                elif y > 66:
                    digit3 = 2
        else:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if x <= 17:
                    digit2 = 0
                elif 17 < x <= 34:
                    digit2 = 1
                elif 34 < x <= 51:
                    digit2 = 2
                elif 51 < x <= 68:
                    digit2 = 3
                elif 68 < x <= 85:
                    digit2 = 4
                elif x > 85:
                    digit2 = 5

                digit3 = 0
            else:
                if x <= 17:
                    digit3 = 0
                elif 17 < x <= 34:
                    digit3 = 1
                elif 34 < x <= 51:
                    digit3 = 2
                elif 51 < x <= 68:
                    digit3 = 3
                elif 68 < x < 85:
                    digit3 = 4
                elif x > 85:
                    digit3 = 5

                digit2 = 0

    elif rng == 2:
        x = random.randrange(100)
        if x <= 17:
            digit2 = 0
        elif 17 < x <= 34:
            digit2 = 1
        elif 34 < x <= 51:
            digit2 = 2
        elif 51 < x <= 68:
            digit2 = 3
        elif 68 < x <= 85:
            digit2 = 4
        elif x > 85:
            digit2 = 5

        if digit1 > 2:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if y <= 33:
                    digit3 = 0
                elif 33 < y <= 66:
                    digit3 = 1
                elif y > 66:
                    digit3 = 2
                digit1 = 0
            else:
                digit3 = 0
                if y <= 33:
                    digit1 = 0
                elif 33 < y <= 66:
                    digit1 = 1
                elif y > 66:
                    digit1 = 2
        else:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if x <= 17:
                    digit3 = 0
                elif 17 < x <= 34:
                    digit3 = 1
                elif 34 < x <= 51:
                    digit3 = 2
                elif 51 < x <= 68:
                    digit3 = 3
                elif 68 < x <= 85:
                    digit3 = 4
                elif x > 85:
                    digit3 = 5

                digit1 = 0
            else:
                if x <= 17:
                    digit1 = 0
                elif 17 < x <= 34:
                    digit1 = 1
                elif 34 < x <= 51:
                    digit1 = 2
                elif 51 < x <= 68:
                    digit1 = 3
                elif 68 < x < 85:
                    digit1 = 4
                elif x > 85:
                    digit1 = 5

                digit3 = 0

    else:
        x = random.randrange(100)
        if x <= 17:
            digit3 = 0
        elif 17 < x <= 34:
            digit3 = 1
        elif 34 < x <= 51:
            digit3 = 2
        elif 51 < x <= 68:
            digit3 = 3
        elif 68 < x <= 85:
            digit3 = 4
        elif x > 85:
            digit3 = 5

        if digit3 > 2:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if y <= 33:
                    digit1 = 0
                elif 33 < y <= 66:
                    digit1 = 1
                elif y > 66:
                    digit1 = 2
                digit2 = 0
            else:
                digit1 = 0
                if y <= 33:
                    digit2 = 0
                elif 33 < y <= 66:
                    digit2 = 1
                elif y > 66:
                    digit2 = 2
        else:
            x = random.randrange(2)
            y = random.randrange(100)
            if x == 0:
                if x <= 17:
                    digit1 = 0
                elif 17 < x <= 34:
                    digit1 = 1
                elif 34 < x <= 51:
                    digit1 = 2
                elif 51 < x <= 68:
                    digit1 = 3
                elif 68 < x <= 85:
                    digit1 = 4
                elif x > 85:
                    digit1 = 5

                digit2 = 0
            else:
                if x <= 17:
                    digit2 = 0
                elif 17 < x <= 34:
                    digit2 = 1
                elif 34 < x <= 51:
                    digit2 = 2
                elif 51 < x <= 68:
                    digit2 = 3
                elif 68 < x < 85:
                    digit2 = 4
                elif x > 85:
                    digit2 = 5

                digit1 = 0
    if digit1 == 0 and digit2 == 0 and digit3 == 0:
        return generateUpgradePath()
    return str(digit1) + str(digit2) + str(digit3)

    

def addUpgrades(monkeys, coords):
    x = 3 #number of towers bought before we start generating upgrades
    usedCoords = []
    while x < len(monkeys):
        r = random.randrange(10)
        if r > chanceUpgrade: #change this to change the rate of upgrades
            monkeys[x] = generateUpgradePath()
            upgradeTarget = random.randrange(x)
            emergencyBreak = 0
            while (upgradeTarget in usedCoords) or len(monkeys[upgradeTarget]) == 3:
                upgradeTarget = random.randrange(x)
                if emergencyBreak == instructionSize:
                    break
                emergencyBreak+=1
            usedCoords.append(upgradeTarget)
            coords[x] = upgradeTarget
        x+=1
    return monkeys, coords

leftBorder = 144
rightBorder = 1436
topBorder = 185
bottomBorder = 992


#monkey arrays, this is stupid I should just make 2 2d arrays
test1 = []
coord1 = []
test2 = []
coord2 = []
test3 = []
coord3 = []
test4 = []
coord4 = []
test5 = []
coord5 = []
test6 = []
coord6 = []
test7 = []
coord7 = []
monkeys = [test1, test2, test3, test4, test5, test6, test7]
coords = [coord1, coord2, coord3, coord4, coord5, coord6, coord7]
score = [0, 0, 0, 0, 0, 0, 0]

monkeys = randomTowers(monkeys)
i=0
while i < instructionSize:
    coords[0].append(randomCoord())
    coords[1].append(randomCoord())
    coords[2].append(randomCoord())
    coords[3].append(randomCoord())
    coords[4].append(randomCoord())
    coords[5].append(randomCoord())
    coords[6].append(randomCoord())
    i+=1
i = 0
income = [650, 121, 137, 138, 175, 164, 163, 182, 200, 199, 314, 189, 192, 282, 259, 266, 268, 165, 358, 260, 186, 351, 298, 277, 167, 335, 333, 662, 266, 389, 337, 537, 627, 205, 912, 1150, 896, 1339, 1277, 1759, 521, 2181, 659, 1278, 1294, 2422, 716, 1637, 2843, 4758, 3016, 1091.5, 1595.5, 1595.5, 924.5, 2197.5, 2483, 1286.5, 1859, 2298, 2159, 922.5, 1232, 1386.4, 2826, 849.8, 3071.6, 1004.2, 1023.6, 777.8, 1391, 2618.8, 1503, 1504, 1392.6, 3044, 2667.4, 1316, 2540.2, 4862, 6709, 1400.2, 5366, 4757, 4749, 7044, 2625.4, 948.5, 2627.4, 3314, 2171, 339.3, 4191, 4537.4, 1946.6, 7667.1, 3718, 9955.6, 1417.2, 9653.8, 2827.9, 1534.6]
incomeHard = [650, 138, 175, 164, 163, 182, 200, 199, 314, 189, 192, 282, 259, 266, 268, 165, 358, 260, 186, 351, 298, 277, 167, 335, 333, 662, 266, 389, 337, 537, 627, 205, 912, 1150, 896, 1339, 1277, 1759, 521, 2181, 659, 1278, 1294, 2422, 716, 1637, 2843, 4758, 3016, 1091.5, 1595.5, 1595.5, 924.5, 2197.5, 2483, 1286.5, 1859, 2298, 2159, 922.5, 1232, 1386.4, 2826, 849.8, 3071.6, 1004.2, 1023.6, 777.8, 1391, 2618.8, 1503, 1504, 1392.6, 3044, 2667.4, 1316, 2540.2, 4862, 6709, 1400.2, 5366, 4757, 4749, 7044, 2625.4, 948.5, 2627.4, 3314, 2171, 339.3, 4191, 4537.4, 1946.6, 7667.1, 3718, 9955.6, 1417.2, 9653.8, 2827.9, 1534.6]
incomeCHIMPS = [650, 163, 182, 200, 199, 314, 189, 192, 282, 259, 266, 268, 165, 358, 260, 186, 351, 298, 277, 167, 335, 333, 662, 266, 389, 337, 537, 627, 205, 912, 1150, 896, 1339, 1277, 1759, 521, 2181, 659, 1278, 1294, 2422, 716, 1637, 2843, 4758, 3016, 1091.5, 1595.5, 1595.5, 924.5, 2197.5, 2483, 1286.5, 1859, 2298, 2159, 922.5, 1232, 1386.4, 2826, 849.8, 3071.6, 1004.2, 1023.6, 777.8, 1391, 2618.8, 1503, 1504, 1392.6, 3044, 2667.4, 1316, 2540.2, 4862, 6709, 1400.2, 5366, 4757, 4749, 7044, 2625.4, 948.5, 2627.4, 3314, 2171, 339.3, 4191, 4537.4, 1946.6, 7667.1, 3718, 9955.6, 1417.2, 9653.8, 2827.9, 1534.6, 426.2, 1101.68, 2589.96, 3159, 1883.5]
while i < 7:
    monkeys[i], coords[i] = addUpgrades(monkeys[i], coords[i])
    i+=1
a = 0
#uncomment sleep for single screen computers so you have time to tab back over
time.sleep(10)


pyautogui.click(500,500)
numTrials = 1
file = open("scores.txt", "w")
for scores in score:
    file.write(str(scores))
    file.write(" ")
file.write("\n")
file.close()
file = open("troubleshooting.txt", "w")
file.write(" ")
file.close()
while 1:
    p = 0
    while p <= 6:
        print("new testing round:",p)
        print("number of trials:", numTrials)
        if difficulty == 2:
            score[p] = playGame(monkeys[p], coords[p], incomeHard)
        elif difficulty == 3:
            score[p] = playGame(monkeys[p], coords[p], incomeCHIMPS)
        else:
            score[p] = playGame(monkeys[p], coords[p], income)
        pyautogui.click(982,817)
        time.sleep(.3)
        pyautogui.click(1146, 728)
        p+=1
        numTrials+=1
    file = open("scores.txt", "a")
    for scores in score:
        file.write(str(scores))
        file.write(" ")
    file.write("\n")
    file.close()
    topScore = topScore -1
    monkeys, coords = createChildren(monkeys, coords, score)