from io import TextIOWrapper
import os

lengthBuckets = {
    2: ['1'],
    3: ['7'],
    4: ['4'],
    5: ['2', '3', '5'],
    6: ['0', '6', '9'],
    7: ['8']
}

segmentMap = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1010010',
    '8': '1111111',
    '9': '1111011'
}


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    patterns = []
    output = []
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            splitLine = [coord.strip() for coord in line.split("|")]
            patterns.append(splitLine[0])
            output.append(splitLine[1])
    return (patterns, output)

#determine whether or not "display" is a number we can already identify
#display is a string
def isIdentifiable(display):
    return len(lengthBuckets[len(display)]) == 1


#get count of already identifiable numbers
def getIdentifiableNumbers(outputs):
    identified = 0;
    for output in outputs:
        output = output.split()
        for display in output:
            print(display)
            if isIdentifiable(display):
                identified += 1
    return identified




def main():
    (patterns, outputs) = getFile("input.txt") 
    print(getIdentifiableNumbers(outputs))



if __name__ == "__main__":
    main()