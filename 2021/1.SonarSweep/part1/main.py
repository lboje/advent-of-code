"""
Reads from an input.txt file. Input.txt is integers separated by line breaks.
We keep track of how many times the input value increased from its previous value
"""
import os


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    fileContents = []
    with open(filePath, "r") as file:
        for line in file:
            fileContents.append(int(line.strip()))
    return fileContents


#For a given array, iterate through and return number of times a value 
#was greater than the one immediately preceding it
def getIncrease(arr): 
    increasing = 0
    for i in range(len(arr)):
        if i:
            increasing += (1 if arr[i] > arr[i - 1] else 0)
    return increasing


def main():
    fileContents = getFile("input.txt")    
    print(getIncrease(fileContents))


if __name__ == "__main__":
    main()