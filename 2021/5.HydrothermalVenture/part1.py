"""
Given a list of coordinates indicating line segments in input.txt, measure overlapping points

input.txt format: 

x1, y1 -> x2, y2
x3, y3 -> x4, y4
...

Finished 12/14/2021
"""
from io import TextIOWrapper
import os


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName, size):
    graph = [ [0]*size for _ in range(size)]
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            split = [coord.strip() for coord in line.split("->")]
            coords = getPoints(split[0], split[1])
            for (x, y) in coords:
                graph[x][y] += 1
    return graph

#Get all points on a line
def getPoints(pos1, pos2):
    coords = []
    (x1, y1) = tuple(int(i) for i in pos1.split(','))
    (x2, y2) = tuple(int(i) for i in pos2.split(','))
    #its simpler this way
    (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])

    #These are our horizontal or vertical lines. The easy ones
    if (x1 == x2) or (y1 == y2):
        (left, right)  = sorted([x1, x2])
        (up, down) = sorted([y1, y2])

        #don't forget - range /isn't/ inclusive
        for x in range(left, right + 1):
            for y in range(up, down + 1):
                coords.append((x, y))

    return coords
    
"""
For the given map (a 2d list of integers), return the number of points of overlap
"""
def getOverlap(map):
    overlap = 0
    for row in map:
        for col in row:
            if col > 1:
                overlap += 1
    return overlap

def main():
    ventMap = getFile("input.txt", 1000)  
    overlap = getOverlap(ventMap)
    print(overlap)


if __name__ == "__main__":
    main()