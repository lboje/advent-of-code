"""
Reads from an input.txt file. Input.txt a csv of integers
Calculate the number of lanternfish given specific rules.
Finished 12/14/2021
"""
import os
import csv


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    initFish = {i: 0 for i in range(9)}

    with open(filePath, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                initFish[int(value)] += 1
    return initFish

"""
To iterate a day, we take all the fish from bucket n and move them to bucket n - 1
For the amount of fish (f) in bucket 0, we can add that value to bucket 6 (cycle starts again)
as well as bucket 8 (new fish!)
"""
def iterateDay(fish):
    newFish = {
        0: fish[1],
        1: fish[2],
        2: fish[3],
        3: fish[4],
        4: fish[5],
        5: fish[6],
        6: fish[7] + fish[0],
        7: fish[8],
        8: fish[0]
    }
    
    return newFish


"""
Modify the fish dictionary by iterating it through a number (n) of days
We then return the sum
"""
def iterateDays(fish, n):
    for _ in range(n):
        fish = iterateDay(fish)

    return sum(fish.values())


def main():
    initFish = getFile("input.txt")    
    #difference between part 1 and part 2 is just the number passed in here
    fishNum = iterateDays(initFish, 256)
    print(fishNum)


if __name__ == "__main__":
    main()