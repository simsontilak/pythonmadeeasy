import random

def generateRandomNumber(howMany):

    numbersToBeSorted = []

    for count in range(1, howMany + 1):
        randomNumber = random.randint(0, howMany)
        numbersToBeSorted.append(randomNumber)

    return numbersToBeSorted

def sortNumbers(givenNumbers):
    for i in range(0,len(givenNumbers)):
        for j in range(i+1,len(givenNumbers)):
            if(givenNumbers[i] > givenNumbers[j]):
                temp = givenNumbers[i]
                givenNumbers[i] = givenNumbers[j]
                givenNumbers[j] = temp
    return givenNumbers

def printNumbers(givenNumbers):
    count = 0
    noOfDigits = len(str(len(givenNumbers))) + 1
    for givenNumber in givenNumbers:
        count = count + 1
        numberFormat = "{:" + str(noOfDigits) + "d}"
        print(numberFormat.format(givenNumber), end="")
        if (count % 10 == 0):
            print()



givenNumbers = generateRandomNumber(10000)
print("Random set of numbers")
printNumbers(givenNumbers)

sortedNumbers = sortNumbers(givenNumbers)
print("Sorted set of numbers")
printNumbers(sortedNumbers)


