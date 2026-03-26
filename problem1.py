greatestNum = None
smallestNum = None

inputNum = int(input("Input a Number (-1 to terminate): "))

while inputNum != -1:
    if greatestNum == None or greatestNum < inputNum:
        greatestNum = inputNum
    if smallestNum == None or smallestNum > inputNum: 
        smallestNum = inputNum
    
    inputNum = int(input("Input a Number (-1 to terminate): "))

print(f"Smallest number is: {smallestNum}")
print(f"Greatest number is: {greatestNum}")
    