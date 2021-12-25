"""
Reads from input file individual integers representing risk level
ex. 
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

Entering a location has the weight of its risk level
Find the path with lowest weight from top left to bottom right

aw yeah its dijkstra time
coordinates will be the nodes, values are the edge/weight
"""
import os
import sys
import numpy as np


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    cave = np.genfromtxt(filePath, dtype=int, delimiter=1)
    return cave

#Create a list of the indexes of all neighbors to a given index
#No diags allowed :(
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
        #You aren't your own neighbor
        if (x,idx[1]) != idx:
            neighbors.append((x, idx[1]))
        
    for y in range(minY, maxY):
        #Ditto
        if (idx[0],y) != idx:
            neighbors.append((idx[0], y))
    return neighbors


#Create a mapping of all indexes to their neighboring indexes
#As well, we create a distance map that from the starting node to that node
def getMaps(arr):
    #Neighbors to an index
    neighborMap = {}
    #Distance map
    distanceMap = {}
    infinity = sys.maxsize
    for (x, y), _ in np.ndenumerate(arr):
        neighborMap[(x, y)] = getNeighbors((x, y), arr.shape)
        #This will be remedied later (as part of the algorithim - this isn't a "todo")
        distanceMap[(x,y)] = infinity
    
    #The distance from start to itself is 0, actually
    distanceMap[0,0] = 0
    return (neighborMap, distanceMap)


def searchPath(room, visited):
    global paths
    if room == "end":
        paths += 1
        return

    for adjacent in cave[room]:
        if canEnter(adjacent, visited): 
            visited.append(adjacent)
            searchPath(adjacent, visited)
            visited.pop()
    return


def thanksDijkstra(riskArr, neighbors, unvisited):
    (rowSize, colSize) = riskArr.shape
    #This is the bottom right location :)
    goal = (rowSize - 1, colSize - 1)

    visited = {}
    prev = {} #Mapping from space to the one before it

    #Do this until we visit all spots
    while unvisited: 
        closest = min(unvisited, key=unvisited.get)
        
        for neighbor in neighbors[closest]:
            if neighbor not in visited:
                currRisk = unvisited[closest] + riskArr[neighbor]
                if currRisk < unvisited[neighbor]:
                    unvisited[neighbor] = currRisk
                    prev[neighbor] = closest

        visited[closest] = unvisited.pop(closest)

    return visited[goal]


def main():
    risk = getFile("input.txt")
    (adjacent, shortest) = getMaps(risk) 
    lowestRisk = thanksDijkstra(risk, adjacent, shortest)
    print(lowestRisk)

    


if __name__ == "__main__":
    main()