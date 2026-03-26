## String -> List split by whitespace -> Reverse List -> Back To String

inputString = input("Enter a sentence: ")
strList = inputString.split()
strList.reverse()
reversedSentence = " ".join(strList)

print(reversedSentence)



