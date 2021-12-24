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