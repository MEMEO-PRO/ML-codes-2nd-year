import random

def printString(string):
    for i in range(8):
        print(string[i], end="")
    print("")

def randomBin():
    string = []
    for i in range(8):
        string.append(random.randint(0, 1))
    return string

def fitness(string):
    fitness = 0
    for i in range(8):
        fitness += int(string[i]) * pow(2, 7 - i)
    return fitness

strings = [randomBin(), randomBin(), randomBin(), randomBin()]

for i in range(4):
    print(f"String {i}: ", end="")
    printString(strings[i])

fitnessList = []
for i in range(4):
    fitnessList.append(fitness(strings[i]))
print(fitnessList)

noOfIterations = int(input("Enter the number of iterations: "))

for i in range(noOfIterations):
    max = 0
    for j in range(4):
        if fitnessList[j] > max:
            max = fitnessList[j]
            maxStr = j
    min = 1000
    for k in range(4):
        if fitnessList[k] < min:
            min = fitnessList[k]
            minStr = k

    strings[k] = strings[j]

    mutationDivision = random.randint(2, 8)
    for x in range(mutationDivision):
        temp = strings[maxStr][x]
        strings[maxStr][x] = strings[max2Str][x]
        strings[max2Str][x] = temp

    fitnessList = []
    for l in range(4):
        fitnessList.append(fitness(strings[l]))

print(f"Final Fitness: {fitnessList}")

