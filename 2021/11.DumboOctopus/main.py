"""
Input file is to be interpreted as lines of single digit integers
ex.
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

Each integer represents the energy level of an octopus at that zone.
Given the rules for determining a flash
1: figure out how many flashed occur in 100 days 
2: figure out when the flashes synchronize

Finished 12/23/21
"""

import numpy as np
import os

#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    data = np.genfromtxt(filePath, dtype=int, delimiter=1)
    return data


#Create a list of the indexes of all neighbors to a given index
#Don't wrap around
def getNeighbors(idx, shape):
    neighbors = []

    #Create boundaries. We don't want to leave the grid
    #Range is exclusive, so our maxes are definitionally one off
    minX = idx[0] - 1 if idx[0] - 1 >= 0 else 0 
    maxX = idx[0] + 2 if idx[0] + 1 < shape[0] else shape[0]
    minY = idx[1] - 1 if idx[1] - 1 >= 0 else 0 
    maxY = idx[1] + 2 if idx[1] + 1 < shape[1] else shape[1]
    
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            #You don't neighbor yourself
            if (x,y) != idx:
                neighbors.append((x, y))
    
    return tuple(np.transpose(neighbors))


#Create a mapping of all indexes to their neighboring indexes
def getNeighborMap(arr):
    neighborMap = {}
    for idx, _ in np.ndenumerate(arr):
        neighborMap[idx] = getNeighbors(idx, arr.shape)
    return neighborMap


"""
Get through one day in the life of a neighborhood of octopuses
"""
def iterateDay(octopuses, neighborMap):
    flashes = 1
    #So far, nobody has flashed today. 
    hasFlashed = np.zeros_like(octopuses)

    #First, the energy level of each octopus increases by 1.
    octopuses += 1

    #An octopus will flash if its energy level is above 9
    flashing = [idx for idx, energyLevel in np.ndenumerate(octopuses) if energyLevel > 9]
    
    while len(flashing) != 0:
        """
        This octopus has enough energy to glow!
        I'm proud - and so are its neighbors, who are all so excited their energy increases. 
        """
        for octopus in flashing:
            neighbors = neighborMap[octopus]
            octopuses[neighbors] += 1
            hasFlashed[octopus] = True

        #Same as before, but now we also check if the octopus has already flashed this turn.
        flashing = [idx for idx, energyLevel in np.ndenumerate(octopuses) if energyLevel > 9 and not hasFlashed[idx]]


    octopuses[np.nonzero(hasFlashed)] = 0
    return np.count_nonzero(hasFlashed)

"""
Iterate a number of days (n) on the octopuses. 
"""
def iterateDays(octopuses, neighbors, n):
    totalFlashes = 0

    for i in range(n):
        totalFlashes += iterateDay(octopuses, neighbors)

    return totalFlashes

"""
Need to figure out when everything is the same.
We've already had 100 days
"""
def findSynchronizationPoint(octopuses, neighbors):
    day = 100
    synched = False

    while not synched:
        day += 1
        flashed = iterateDay(octopuses, neighbors)
        synched = (flashed == octopuses.size)
    return day 

def main():
    octopuses = getFile("input.txt") 
    neighborMap = getNeighborMap(octopuses)
    partOne = iterateDays(octopuses, neighborMap, 100)
    partTwo = findSynchronizationPoint(octopuses, neighborMap)
    
    print("Part one answer: {0}\nPart two answer: {1}".format(partOne, partTwo))
    


if __name__ == "__main__":
    main()