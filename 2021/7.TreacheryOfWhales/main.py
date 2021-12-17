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
import math


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


#get the total cost for all crabs to get aligned
def getTotalCost(crabs, alignedPos, constant):
    sum = 0
    for crab in crabs:
        sum += getGas(crab, alignedPos, constant)
    return int(sum)


#returns cost at best position crab alignment
#for part 1, its the median (average would be thrown off by statistical outliers)
def findCostConst(crabs):
    bestPos = int(statistics.median(crabs))

    cost = getTotalCost(crabs, bestPos, True)
    return cost

#returns cost at best position crab alignment
#for part 2, statistical outliers matter A LOT. 
def findCostTriangular(crabs):
    mean = statistics.mean(crabs)
    floor = math.floor(mean)
    ceil = math.ceil(mean)

    floorCost = getTotalCost(crabs, floor, False)
    ceilCost = getTotalCost(crabs, ceil, False)

    return min([floorCost, ceilCost])


"""
gets amount of gas to get from point a to b
for part 1, its a constant price and we can just do the absolute value of the difference 
for part 2, the price for each step is equal to its distance. e.x.: 1, 2, 3, 4, 5
So the sum at each distance would be 1, 3, 6, 10, 15, 21. 
We can solve the partial sum at f(n), where n is any integer, with the formula f(n) = n(n+1) / 2
This pattern is usually called "triangular numbers", its like....summative factorial
"""
def getGas(posA, posB, constant):
    difference = int(abs(posA - posB))
    if constant:
        return difference
    return (difference * (difference + 1)) / 2


def main():
    crabs = getFile("input.txt")    
    pt1Pos = findCostConst(crabs)
    pt2Pos = findCostTriangular(crabs)
    print("Cost for part 1: {0}\nCost for part 2: {1}".format(pt1Pos, pt2Pos));
    

if __name__ == "__main__":
    main()