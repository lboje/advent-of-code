"""
Reads from an input.txt file. Input.txt is integers separated by line breaks.
We create an array of the sums, in rolling groups of 3, of the values from the file.
ex: arr =  [(file[0] + file[1] + file[2]), (file[1], file[2], file[3]), ...]
Then, we determine how many times the values on that array increase as we iterate through it
ex: arr[1] > arr[0]

This is not the most efficient way of doing this, by any means.
Finished 12/13/2021
"""
import os


#For advent of code purposes, the file is always there and correctly formatted
#Read input file fileName within current directory, return input as array of integers
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    fileContents = []
    with open(filePath, "r") as file:
        for line in file:
            fileContents.append(int(line.strip()))
    return fileContents


#For an array of integers, return an array of the rolling sums of n items
def rollingSums(arr, n):
    sums = []
    for i in range(len(arr) - (n - 1)):
        nSum = sum(arr[i : (i + n)])
        sums.append(nSum)
    return sums 


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
    sums = rollingSums(fileContents, 3)  
    print(getIncrease(sums))


if __name__ == "__main__":
    main()