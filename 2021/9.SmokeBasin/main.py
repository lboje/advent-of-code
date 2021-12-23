"""
Given a file in the format of integers with line breaks to separate rows
ex:
2199943210
3987894921
9856789892
8767896789
9899965678

Find the local minimums. 
Part 1 finishe 12/22/21
"""

import os



#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    patternOutputMap = []
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            row = []
            for digit in line.strip():
                row.append(int(digit))
            patternOutputMap.append(row)
    return patternOutputMap

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
def isLowPoint(row, col, height, width, depthArray):
    coordHeight = depthArray[row][col]
    #Check above (if possble)
    if col < width - 1 and coordHeight >= depthArray[row][col + 1]:
        return False
    #Check below (if possible)
    if col > 0 and coordHeight >= depthArray[row][col - 1]:
        return False
    #Check left
    if row > 0 and (coordHeight >= depthArray[row - 1][col]):
        return False
    #Check right
    if row < height - 1 and coordHeight >= depthArray[row + 1][col]:
        return False
    return True


#Get all low points within the 2d array of integers
#(technically depthArray a list of lists of integers)
def getLowPoints(depthArray):
    height = len(depthArray)
    width = len(depthArray[0])
    lowPoints = []

    for row in range(height):
        for col in range(width):
            if isLowPoint(row, col, height, width, depthArray):
                lowPoints.append(depthArray[row][col])
    return lowPoints


def main():
    depthArray = getFile("input.txt") 
    lowPoints = getLowPoints(depthArray)
    print(returnRiskLevel(lowPoints))


if __name__ == "__main__":
    main()