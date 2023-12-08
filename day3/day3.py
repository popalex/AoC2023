from collections import defaultdict
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
file = open(f'{home}/inputday3.txt', 'r', encoding=encoding)
sumOfParts = 0
lines = file.readlines()
matrix = [[c for c in line.replace('\n','') ] for line in lines]

numbers = defaultdict(list)
noOfLines = len(matrix)
charsPerLine = len(matrix[0])
for row in range(noOfLines):
    gears = set()
    nr = 0
    isPart = False
    for char in range(len(matrix[row])+1):
        if char < charsPerLine and matrix[row][char].isdigit():
            if matrix[row][char].isdigit():
                nr = nr * 10 + int(matrix[row][char])
                print(f"Line {row}, Nr {nr}")
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if (row+i>=0) and (row+i<noOfLines) and (char+j>=0) and (char+j<charsPerLine):
                            currentChar = matrix[row+i][char+j]
                            if not currentChar.isdigit() and currentChar != '.':
                                isPart = True
                            if currentChar == '*':
                                gears.add((row+i, char+j))
        elif nr > 0:
            for gear in gears:
                numbers[gear].append(nr)
            if isPart:
                print(f"currentChar={currentChar}, isPart={isPart}")
                sumOfParts = sumOfParts + nr
            else:
                print(f"isPart={isPart}")
            nr = 0
            isPart = False
            gears = set()
    
print(f"Full sum is {sumOfParts}")

sumOfGeers = 0
for key, value in numbers.items():
  if len(value)==2:
    sumOfGeers += value[0]*value[1]
print(f"sumOfGeers = {sumOfGeers}")

# Closing files
file.close()