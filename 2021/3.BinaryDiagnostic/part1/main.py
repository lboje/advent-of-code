"""
Reads from an input.txt file. Input.txt is binary - surprise!
Calculate the gamma (the most common value for each bit) and
the epsilon (inverse)
We then multiply them :)
"""
import os
from collections import Counter

#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    fileContents = []
    with open(filePath, "r") as file:
        for line in file:
            fileContents.append(line.strip())
    return fileContents

#gets most common element in array
#don't worry about equal appearance
def mostFrequent(arr):
    counter = Counter(arr)
    return counter.most_common(1)[0][0]


def getPowerConsumption(arr):
    bits = len(arr[0])
    gamma = ''

    for i in range(bits):
        bitPos = [number[i] for number in arr]
        commonBit = mostFrequent(bitPos)
        gamma += commonBit

    gamma = int(gamma, 2)
    #two things to think about here
    #1. integers are still binary in python...deep down
    #2. normal ^ will get us two's complement, but we want this unsigned
    epsilon = (gamma ^ (2 ** (bits) - 1))
    return gamma * epsilon


def main():
    fileContents = getFile("input.txt")    
    powerConsumption = getPowerConsumption(fileContents)
    print(powerConsumption)


if __name__ == "__main__":
    main()