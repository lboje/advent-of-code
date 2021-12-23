"""
Given a file in the format of integers with line breaks to separate rows
ex:
2199943210
3987894921
9856789892
8767896789
9899965678

Part 1: Find the local minimums. 
Part 2: Find the largest 3 basins - areas bounded by 9s
Completed 12/22/21
"""

import os
import math



#For advent of code purposes, the file is always there and correctly formatted
#We surround the area with a border of 9s - it'll never get bigger. This makes iterating
def getFile(fileName):
    patternOutputMap = []
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            row = []
            for digit in line.strip():
                row.append(int(digit))
            #Create left and right boundaries
            row.insert(0, 9)
            row.append(9)
            patternOutputMap.append(row)

    #Create top and bottom boundaries
    rowLength = len(patternOutputMap[0])
    border = [9] * rowLength
    patternOutputMap.insert(0, border)
    patternOutputMap.append(border)
    return patternOutputMap

"""
Recursive function that checks if its 9. If not, add to set, 
"""
def getBasin(x, y, depthArray, basinSet):
    if depthArray[x][y] == 9 or (x, y) in basinSet:
        return basinSet

    basinSet.add((x,y))
    
    up = getBasin(x, y + 1, depthArray, basinSet)
    down = getBasin(x, y - 1, depthArray, basinSet)
    left = getBasin(x - 1, y, depthArray, basinSet)
    right = getBasin(x + 1, y, depthArray, basinSet)

    return basinSet.union(up, down, left, right)


"""
A location is considered a "low point" if that location is lower
than the surrounding areas. The surrounding area is here defined as 
the items directly above, below, left, and right. Diagonals do not count,
and we do not wrap around to check.
"""
def getBasins(depthArray, lowPoints):
    basins = []
    for x, y in lowPoints:
        basinSet = set()
        basin = getBasin(x, y, depthArray, basinSet)
        #We only need the size of the basin, so thats what we add
        basins.append(len(basin))
        
    #Sort in descending order. It's more convenient to do it here
    return sorted(basins, reverse=True)


#Since risk level is just the lowPoint's height + 1, we can obtain the risk level by 
#summing the heights and adding the length (+1 for each item :)) 
def returnRiskLevel(lowPoints):
    return sum(lowPoints) + len(lowPoints)

"""
A location is considered a "low point" if that location is lower
than the surrounding areas. The surrounding area is here defined as 
the items directly above, below, left, and right. Diagonals do not count,
and we do not wrap around to check.
"""
def isLowPoint(row, col, depthArray):
    coordHeight = depthArray[row][col]
    #Check above
    if coordHeight >= depthArray[row][col + 1]:
        return False
    #Check below 
    if coordHeight >= depthArray[row][col - 1]:
        return False
    #Check left
    if coordHeight >= depthArray[row - 1][col]:
        return False
    #Check right
    if coordHeight >= depthArray[row + 1][col]:
        return False
    return True


#Get all low points within the 2d array of integers
#(technically depthArray is a list of lists of integers)
def getLowPoints(depthArray):
    lowVals = []
    lowPoints = []

    for row in range(1, len(depthArray) - 1):
        for col in range(1, len(depthArray[0]) - 1):
            if isLowPoint(row, col, depthArray):
                lowVals.append(depthArray[row][col])
                lowPoints.append((row, col))
    return (lowVals, lowPoints)


def main():
    depthArray = getFile("input.txt") 
    (lowVals, lowPoints) = getLowPoints(depthArray)
    basins = getBasins(depthArray, lowPoints)

    partOneSolution = returnRiskLevel(lowVals)
    partTwoSolution = math.prod((basins)[:3])
    print('Part one solution: {0}\nPart two solution: {1}'.format(partOneSolution, partTwoSolution))


if __name__ == "__main__":
    main()