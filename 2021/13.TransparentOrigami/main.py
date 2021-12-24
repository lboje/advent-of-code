"""
Input file lines of coordinates, then directions
ex.
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

Plot them out, fold on the stated lines.

Finished 12/24/21
"""

from paper import Paper, foldDirection
import numpy as np
import os


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    coordinates = []
    commands = []

    paperCreated = False

    with open(os.path.join(os.path.dirname(__file__), fileName), "r") as file:
        for line in file:
            line = line.strip()
            #We are reading coordinates
            if not paperCreated:
                #There is a newline after creating listing coordinates 
                if len(line) == 0:
                    paper = Paper(coordinates)
                    paperCreated = True
                else:
                    coord = tuple(int(i) for i in line.split(','))
                    coordinates.append(coord)
            #We are creating commands
            else:
                command = tuple(line.split()[-1].split('='))
                commands.append(command)
       
    return (paper, commands)

def main():
    (paper, commands) = getFile("input.txt") 
    paper.fold(commands[0])
    print(paper.points)
    

if __name__ == "__main__":
    main()