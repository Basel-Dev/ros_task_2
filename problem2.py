## Arithmetic Series, S_n = n/2 (a+l)
## n = (l-a / d) + 1 (Number of terms in the series)
## Even Numbers => d = 2 (Common Difference)
## Beginning from 1 && Even => a = 2 (1st Term)
## l = inputNum or inputNum-1 if odd (Last term)
## S_n => O(1), No Loops Required

inputNum = int(input("Input an Integer: "))

firstTerm = 2

if inputNum % 2 == 0:
    lastTerm = inputNum
else:
    lastTerm = inputNum-1     

commonDifference = 2
numberOfTerms = ((lastTerm - firstTerm) / commonDifference) + 1

sum = int((numberOfTerms/2) * (firstTerm+lastTerm))
print(f"The sum of even numbers from 1 to {lastTerm} is: {sum}")


