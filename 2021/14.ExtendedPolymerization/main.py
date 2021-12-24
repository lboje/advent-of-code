"""
Given an initial polymer and rules for pair insertion, insert the pairs

ex.
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

Completed 12/24/21
"""
import os
from collections import defaultdict, Counter

#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    rules = {}

    with open(filePath, "r") as file:
        polymer = file.readline().strip()
        for line in file:
            rule = line.strip()
            if len(rule):
               (pair, insertion) = tuple(rule.split(' -> '))
               rules[pair] = insertion
    return polymer, rules

def setup(polymer, rules):
    #Nothing can come after this. Since we'll be adding to the count based on the first character,
    #we need to make sure we count this :)
    lastElement = polymer[-1]
    #This is a map of the number of times a pair shows up. We'll be having /fun/ with this one.
    occurenceMap = defaultdict(int)
    
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        occurenceMap[pair] += 1

    return (lastElement, occurenceMap)

#Just a helper for insertion
def insertAll(occurences, rules, n):
    for _ in range(n):
        occurences = insert(occurences, rules)
    return occurences

def insert(occurences, rules):
    newOccurences = defaultdict(int)
    #Make a new dict. We don't want pairs to influence others
    for pair in occurences:
        newOccurences[pair[0] + rules[pair]] += occurences[pair]
        newOccurences[rules[pair] + pair[1]] += occurences[pair]
        #Rip pair, but they've all been split up
        occurences[pair] -= occurences[pair]

    #join them back in
    for pair in newOccurences:
        occurences[pair] = newOccurences[pair]

    return occurences


def getElementRange(pairCount, lastElement):
    elementCount = defaultdict(int)

    for pair in pairCount:
        elementCount[pair[0]] += pairCount[pair]
    
    #Since we only count the first of each pair, we need the last element
    #It literally will not be counted otherwise :(
    elementCount[lastElement] += 1

    values = elementCount.values()
    return max(values) - min(values)


def main():
    (polymer, rules) = getFile("input.txt")
    (last, pairCount) = setup(polymer, rules)
    #Only difference between part 1 and 2 is 10 vs 40
    finalPairs = insertAll(pairCount, rules, 40)
    elementRange = getElementRange(pairCount, last)
    print(elementRange)



if __name__ == "__main__":
    main()