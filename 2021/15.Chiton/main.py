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

Completed 12/24/21
"""
import os
import heapq
import numpy as np



#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    cave = np.genfromtxt(filePath, dtype=int, delimiter=1)
    return cave


def multiplyInput(inputArr, rowSize, colSize):
    newInput = inputArr.copy()
    
    base = newInput.copy()
    #first we complete the first row
    for _ in range(colSize - 1):
        base += 1
        base[base > 9] = 1
        newInput = np.concatenate((newInput, base), axis=1)
    
    base = newInput.copy()
    #then we expand it out
    for _ in range(rowSize - 1):
        base += 1
        base[base > 9] = 1
        newInput = np.concatenate((newInput, base), axis=0)

    return newInput




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
def getNeighborMap(arr):
    #Neighbors to an index
    neighborMap = {}
    for (x, y), _ in np.ndenumerate(arr):
        neighborMap[(x, y)] = getNeighbors((x, y), arr.shape)
    
    return neighborMap


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


def thanksDijkstra(riskArr, neighbors):
    (rowSize, colSize) = riskArr.shape
    #This is the bottom right location :)
    goal = (rowSize - 1, colSize - 1)

    #Gonna use heapq to speed things up a bit
    visiting = [(0,0)]
    #mapping the a location to the lowest risk to get there
    visited = {(0,0) : 0}
    
    #Do this until we can't
    while visiting: 
        closest = heapq.heappop(visiting)

        #we've found our
        if closest == goal:
            return visited[goal]

        for neighbor in neighbors[closest]:
            currRisk = visited[closest] + riskArr[neighbor]
            #short circuiting is important
            if neighbor not in visited or currRisk < visited[neighbor]:
                    heapq.heappush(visiting, neighbor)
                    visited[neighbor] = currRisk


def main():
    risk = getFile("input.txt")
    neighbors = getNeighborMap(risk) 
    partOne = thanksDijkstra(risk, neighbors)
    
    #Gotta make the input 25x bigger for part two :(
    bigRisk = multiplyInput(risk, 5, 5)
    neighbors = getNeighborMap(bigRisk) 
    partTwo = thanksDijkstra(bigRisk, neighbors)
    
    print("Part one answer: {0}\nPart two answer {1}".format(partOne, partTwo))
    

    


if __name__ == "__main__":
    main()