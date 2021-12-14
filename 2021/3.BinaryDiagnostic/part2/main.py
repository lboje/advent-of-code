"""
Reads from an input.txt file. Input.txt is binary - surprise!
We can recursively filter on most common bit to find the oxygen generator rating.
Ditto but inverse for co2 scrubber rating.
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


#if co2 is true, gets least common val in array - '0' on tie
#if co2 is false, gets most common val in array - '1' on tie
def startVal(arr, co2):
    counter = Counter(arr)
    frequency = counter.most_common()
    #if there is only one value found
    if(len(frequency) == 1):
        return frequency[0][0]
    #if there is a tie
    elif frequency[0][1] == frequency[1][1]:
        return '0' if co2 else '1'
    return frequency[1][0] if co2 else frequency[0][0]


"""
Recursively: 
Gets the most significant bit for each binary value
Finds the most/least (as determined by co2) common value
Filters such that we only have items starting with that value from the second item on
"""
def getRating(arr, rating, co2 = False):
    #if we only have one item, we've found it
    if(len(arr) == 1):
        rating += arr[0]
        return rating

    bitPos = [number[0] for number in arr]
    commonBit = startVal(bitPos, co2)
    filteredArr = [number[1:] for number in arr if number[0] == commonBit]
    rating += commonBit
    return getRating(filteredArr, rating, co2)


"""
Helper for getRating.
Gets oxygen and co2 ratings, converts to int
By multiplying the two, we get the lifesupport value
"""
def getLifeSupportVal(arr): 
    oxygenRating = int(getRating(arr, ''),2)
    co2Rating = int(getRating(arr, '', True),2)

    return oxygenRating * co2Rating



def main():
    fileContents = getFile("input.txt")    
    lifeSupport = getLifeSupportVal(fileContents)
    print(lifeSupport)


if __name__ == "__main__":
    main()