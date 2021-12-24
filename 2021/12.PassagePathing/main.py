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

part 1: find all paths
"""
import os
from collections import defaultdict

paths = 0
#adjacency list for rooms
cave = defaultdict(list)
#big rooms can be entered more than once
bigRooms = set()

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


def searchPath(room, visited):
    global paths
    if room == "end":
        paths += 1
        return

    for adjacent in cave[room]:
        if adjacent not in visited or adjacent in bigRooms: 
            visited.append(adjacent)
            searchPath(adjacent, visited)
            visited.pop()
    return


def main():
    getFile("input.txt") 
    searchPath("start", ["start"])
    print("Part one answer: {0}".format(paths))
    


if __name__ == "__main__":
    main()