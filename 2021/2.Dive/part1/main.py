"""
Reads from an input.txt file. Input.txt is lines of directions and integers
ex: forward 4
    up 3
    forward 1
    down 2

Starting from 0,0 we determine our endpoint using the directions from input.txt
"""
import os

vertical = ['up', 'down']

#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    fileContents = []
    with open(filePath, "r") as file:
        for line in file:
            splitLine = line.split()
            fileContents.append([splitLine[0], int(splitLine[1])])
    return fileContents

#Given commands, a list of directions and change in location, we calculate
#our final location in respect to the given origin (xPos, yPos)
def getLocation(xPos, yPos, commands):
    for command in commands:
        direction = command[0]
        delta = command[1] 

        if direction in vertical:
            invert = (-1 if direction == 'up' else 1)
            yPos += (delta * invert)
        else:
            xPos += delta

    return (xPos, yPos)



def main():
    fileContents = getFile("input.txt")    
    (xPos, yPos) = getLocation(0, 0, fileContents)
    print("{0} * {1} = {2}".format(xPos, yPos, (xPos * yPos)))


if __name__ == "__main__":
    main()