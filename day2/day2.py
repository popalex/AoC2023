import re
from os.path import expanduser


home = expanduser("~")

file = open(f'{home}/inputday2.txt', 'r')
sumOfGames = 0

games = []
maxCubes = { 'red': 12, 'green': 13 , 'blue': 14}
cubes = ['red','green','blue']


for line in file:
    #replace Game 
    if (line.startswith("Game ")):
        line = line.replace('Game ','')
    currentGameNumber = int(line[0:line.find(':')])
    currentGame = {}

    # line is the line after : char
    line = line[line.find(':') + 1:]
    print(f"Current Game {currentGameNumber}, line: {line.strip()}")
    
    sets = line.strip().split(';')
    isGameOverMax = False
    for set in sets:
        set = set.strip()
        currentGame = {}
        
        for cube in cubes:
            pos = set.find(cube)
            noOfCubes = re.findall(r"(\d+)\ "+cube, set)
            noOfCubesInt = [int(x) for x in noOfCubes]
            currentGame[cube] = sum(noOfCubesInt)

        print(f"Current set game {currentGame}")
        isSetOverMax = False
        for cube in maxCubes.keys():
            if (currentGame[cube] > maxCubes[cube]) and (not isGameOverMax):
                isSetOverMax = True
                isGameOverMax = True
                break
        print(f"Current Game {currentGameNumber} set {set} is over max {isSetOverMax}")
    
    print(f"Current Game {currentGameNumber} is over max {isGameOverMax}")

    if not isGameOverMax:
        sumOfGames = sumOfGames + currentGameNumber

    print(f"Current game {currentGameNumber}, Full sum is {sumOfGames}\n")
 
print(f"Full sum is {sumOfGames}")
# Closing files
file.close()