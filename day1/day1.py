from collections import OrderedDict
from os.path import expanduser
home = expanduser("~")

file = open(f'{home}/inputday1.txt', 'r')
sumOfNumbers = 0
numbers = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']
# numberAsStrings = []

for line in file:
    found = False
    firstNumber = -1
    lastNumber = 1
    currentPos = -1
    firstPos = -1
    lastPos = -1
    pos = {}
    currentNumber = -1
    for idx, number in enumerate(numbers):
        # Last first of number
        currentPos = line.strip().find(number)
        # found it !!!
        if (currentPos > -1):
            pos[currentPos] = (idx % 9) + 1

        # Last index of number
        currentPos = line.strip().rfind(number)
        # found it !!!
        if (currentPos > -1):
            pos[currentPos] = (idx % 9) + 1
    
    pos_sorted = OrderedDict(sorted(pos.items()))
    # get the first item that is (pos, number) and then get the number from it
    firstNumber = list(pos_sorted.items())[0][1]
    lastNumber = list(pos_sorted.items())[len(pos_sorted) - 1][1]
    
    currentNumber = (firstNumber * 10) + lastNumber
    sumOfNumbers = sumOfNumbers + currentNumber
    print(f"Line{idx}: {line.strip()}")
    print(f"Current Number is {currentNumber}, Full sum is {sumOfNumbers}")
 
print(f"Full sum is {sumOfNumbers}")
# Closing files
file.close()