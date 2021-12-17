"""
Reads from an input.txt file. Input.txt is a csv of integers
ex: 16,1,2,0,4,2,7,1,2,14
Each represents a crab submarine, which can only move on one axis. 
Align the crabs with minimal cost.
Cost, here, is gas. That stuffs expensive.
Finished 12/16/2021
"""
import os
import csv
import statistics


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    crabs = []

    with open(filePath, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                crabs.append(int(value))
    return crabs

#returns best position for all crabs
#it should be the median (average would be thrown off by statistical outliers)
def findBest(crabs):
    bestPos = int(statistics.median(crabs))
    return bestPos

#gets amount of gas to get from point a to b
#since its a flat cost, we can just do the absolute value of the difference 
def getGas(posA, posB):
    return abs(posA - posB)

#get the total cost for all crabs to get aligned
def getTotalCost(crabs, alignedPos):
    sum = 0
    for crab in crabs:
        sum += getGas(crab, alignedPos)
    return sum


def main():
    crabs = getFile("input.txt")    
    bestPos = findBest(crabs)
    cost = getTotalCost(crabs, bestPos)
    print(cost)



if __name__ == "__main__":
    main()