import platform
import re
from os.path import expanduser


home = expanduser("~")

if platform.system() == 'OS/390':
    encoding='cp1047'
    print("Running on z/OS!")
else:
    encoding='UTF-8'

# encoding='cp1047' needed of z/OS
file = open(f'{home}/inputday2.txt', 'r', encoding=encoding)
sumOfGames = 0
sumOfFewCubes = 0

games = []
maxCubes = { 'red': 12, 'green': 13 , 'blue': 14}
cubes = ['red','green','blue']

for line in file:
    if (line.startswith("Game ")):
        line = line.replace('Game ','')
    currentGameNumber = int(line[0:line.find(':')])
    currentGame = {}
    currentfewCubs = {'red': -1, 'green': -1 , 'blue': -1}

    line = line[line.find(':') + 1:]
    print(f"Current Game {currentGameNumber}, line: {line.strip()}")
    
    sets = line.strip().split(';')
    isGameOverMax = False
    for set in sets:
        set = set.strip()
        currentGame = {}
        
        for cube in cubes:
            # not needed
            # pos = set.find(cube)
            noOfCubes = re.findall(r"(\d+)\ "+cube, set)
            noOfCubesInt = [int(x) for x in noOfCubes]
            currentGame[cube] = sum(noOfCubesInt)
            if currentfewCubs[cube] < sum(noOfCubesInt):
                currentfewCubs[cube] = sum(noOfCubesInt)

        print(f"Current set game {currentGame}, currentfewCubs {currentfewCubs} ")

        isSetOverMax = False
        for cube in maxCubes.keys():
            if (currentGame[cube] > maxCubes[cube]) and (not isGameOverMax):
                isSetOverMax = True
                isGameOverMax = True
                break
        print(f"Current Game {currentGameNumber} set {set} is over max {isSetOverMax}")
    
    currentPower = currentfewCubs['red']*currentfewCubs['green']*currentfewCubs['blue']

    print(f"Current Game {currentGameNumber} is over max {isGameOverMax}")
    sumOfFewCubes = sumOfFewCubes + currentPower

    if not isGameOverMax:
        sumOfGames = sumOfGames + currentGameNumber

    print(f"Current game {currentGameNumber}, Full sum is {sumOfGames}, sumOfFewCubes {sumOfFewCubes}\n")
 
print(f"Full sum is {sumOfGames}, sumOfFewCubes {sumOfFewCubes}")
# Closing files
file.close()