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

    if (x1 == x2) != (y1 == y2):
        coords.append((x1, y1))
        coords.append((x2, y2))

        #add horizontal points
        if y1 == y2:
            (left, right) = sorted([x1, x2])
            for i in range((right - left) - 1): 
                coords.append(((left + i) + 1, y1))
                
        #add vertical points
        elif x1 == x2:
            (up, down) = sorted([y1, y2])
            for i in range((down - up) - 1): 
                coords.append((x1, (up + i) + 1))

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