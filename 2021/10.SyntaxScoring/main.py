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
"""

import os


"""
Mapping of an unexpected character to its associated score
"""
scoreMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

"""
Mapping of an end character to its starting character
"""
closureMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


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
                return scoreMap[char]
    return 0


"""
Line by line, check whether or not a line is valid. 
Return the sum of the values of unexpected characters
"""
def parseFile(inputTxt):
    sum = 0
    for line in inputTxt:
        sum += parseLine(line)
    return sum


def main():
    inputTxt = getFile("input.txt") 
    partOneAnswer = parseFile(inputTxt)
    print(partOneAnswer)
    


if __name__ == "__main__":
    main()