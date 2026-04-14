import cmath

inputNum = input()
complexNum = complex(inputNum)

numPhase = cmath.phase(complexNum)
numAbs = abs(complexNum)

print(numAbs)
print(numPhase)
