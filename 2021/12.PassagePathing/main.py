"""
Reads from input file that is structured as node - node
ex. 
start-A
start-b
A-c
A-b
b-d
A-end
b-end

This represents an undirected graph. 
find all paths
Completed 12/23/21
"""
import os
from collections import defaultdict, Counter

paths = 0
#adjacency list for rooms
cave = defaultdict(list)

#big rooms can be entered however many times you want
bigRooms = set()
#goal rooms can be entered exactly once
goalRooms = {'start', 'end'}



#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    with open(os.path.join(os.path.dirname(__file__), fileName), "r") as file:
        for line in file:
            (start, end) = line.strip().split('-')
            #Since its bidirectional, we add it both ways
            cave[start].append(end)
            cave[end].append(start)

            #a room is "big" if its all capitalized
            if start.isupper(): bigRooms.add(start)
            if end.isupper(): bigRooms.add(end)
    return

"""
You can enter a big room however many times you want
You can enter goal rooms only once

"""
def canEnter(room, visited):
    if room in bigRooms:
        return True
    if room in goalRooms:
        return room not in visited
    
    #We only want to count small rooms
    locationCount = Counter([location for location in visited if location not in bigRooms])
    #If we have more than one of any small room, we don't want /more/
    maxVal = 1 if locationCount.most_common(1)[0][1] > 1 else 2
    return locationCount[room] < maxVal



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


def main():
    getFile("input.txt") 
    searchPath("start", ["start"])
    print(paths)
    


if __name__ == "__main__":
    main()