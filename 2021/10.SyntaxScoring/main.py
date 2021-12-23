"""
Given a file with lines of chunks
ex.
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]

parse the syntax

Completed 12/22/21
"""

import os
from bidict import bidict
import statistics



"""
Mapping of an unexpected character to its associated score
"""
unexpectedScore = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


"""
Mapping of autocompleted character to its associated score
"""
autocompleteScore = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4 
}

"""
Mapping of an end character to its starting character
"""

closureMap = bidict({
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
})


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    inputTxt = []
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            inputTxt.append(line.strip())
    return inputTxt

"""
Iterate through the line, exiting out upon identification of an unexpected character
An unexpected character is here defined as a closure that either has no match, or 
would be blocking other chunks from closure
"""
def parseLine(line):
    startList = ['(', '[', '{', '<']
    openExpr = []
    
    for char in line:
        if char in startList:
            openExpr.append(char)
        else:
            #This indicates an unexpected expression
            if not openExpr or openExpr.pop() != closureMap[char]:
                return (unexpectedScore[char], False)
    return ([closureMap.inverse[char] for char in reversed(openExpr)], True)


"""
Calculate the completion score for completion phrase
Start with 0. Then, for each character, multiply sum by 5, then add 
the associated value for that character
"""
def completionScore(completionList):
    sum = 0
    for char in completionList:
        sum = (sum * 5) + autocompleteScore[char]
    return sum

"""
Line by line, check whether or not a line is valid. 
Return the sum of the values of unexpected characters,
as well as the median value of autocomplete values
"""
def parseFile(inputTxt):
    unexpectedSum = 0
    autocompleteSum = []
    for line in inputTxt:
        (value, valid) = parseLine(line)
        if valid:
            autocompleteSum.append(completionScore(value))
        else:
            unexpectedSum += value
    return (unexpectedSum, statistics.median(autocompleteSum))


def main():
    inputTxt = getFile("input.txt") 
    (partOne, partTwo) = parseFile(inputTxt)
    print("Part one answer: {0}\nPart two answer: {1}".format(partOne, partTwo))
    


if __name__ == "__main__":
    main()