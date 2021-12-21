"""
Given the signals and output of a seven segment display, determine what is on it.
You might think that's not worth a whole program, but there's a catch
The input values are randomized. 


Part one solved 12/17/21
Part two solved 12/20/21
"""


from io import TextIOWrapper
from bidict import bidict
import os

"""
Mapping of the number of segments to which
numbers contain that many segments. 
"""
lengthBuckets = {
    2: ['1'],
    3: ['7'],
    4: ['4'],
    5: ['2', '3', '5'],
    6: ['0', '6', '9'],
    7: ['8']
}

#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName):
    patternOutputMap = []
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    with open(filePath, "r") as file:
        for line in file:
            #splitLine[0] is pattern, splitLine[1] is output
            splitLine = [coord.strip() for coord in line.split("|")]
            """
            The pattern line is something like
            be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb
            we split on the space, put each item in alphabetical order, and then sort on size
            So the example above (line 34) would end up looking like
            ['be', 'bde', 'bceg', 'cdefg', 'bcdef', 'abcdf', 'bcdefg', 'acdefg', 'abdefg', 'abcdefg']
            This makes it easy to identify mappings later
            """
            pattern = sorted([''.join(sorted(pattern)) for pattern in splitLine[0].split()], key=len)
            #Same as above (almost - sorting on length would mess us up)
            output = [''.join(sorted(output)) for output in splitLine[1].split()]
            patternOutputMap.append((pattern, output))
    return patternOutputMap



#if there is only one number with that number of segments, its immediately identifiable
def immediatelyIdentifiable(display):
    return len(lengthBuckets[len(display)]) == 1


#get count of immediately identifiable numbers
def getIdentifiableNumbers(outputs):
    identified = 0;
    for pattern, output in outputs:
        for display in output:
            print(len(display))
            if immediatelyIdentifiable(display):
                identified += 1
    return identified


"""
Since there are 5 segments in the signal, we can narrow the signal
down to being 2, 3, or 5. Note that since we sorted the signals by length,
we can be certain that the decoderMap already contains the signals '1', '7', and '4'.

"""
def fiveSegCheck(signal, decoderMap):
    signalSet = set(signal)
    #Of '2', '3', and '5', only '3' contains all of the segments from '1'
    if signalSet.issuperset(decoderMap['1']):
        return '3'

    #The overlap in segments between '2' and '4' is 2.
    #For '5' and '4' it is 3
    segmentOverlap = len(signalSet.intersection(decoderMap['4']))
    return '2' if segmentOverlap == 2 else '5'


"""
Since there are 6 segments in the signal, we can narrow the signal
down to being '0', '6', or '9'. Note that since we sorted the signals by length,
we can be certain that the decoderMap already contains the signals
'1', '2', '3', '4', '5', and '7'
"""
def sixSegCheck(signal, decoderMap):
    signalSet = set(signal)
    #Once again, we can check against '4'. Only '9' contains all of '4'
    if signalSet.issuperset(decoderMap['4']):
        return '9'
    #Between '0' and '6', only '6' contains all of '5'
    if signalSet.issuperset(decoderMap['5']):
        return '6'
    return '0'

#Figure out the numeric identity of a signal
def identifySignal(signal, decoderMap):
    """
    There are /effectively/ 3 cases for the segment count
    Case 1: The signal has a unique length (1, 7, 4, or 8),
    Case 2: The signal has 5 segments (2, 3, or 5),
    Case 3: The signal has has 6 segments (0, 6, or 9)
    """
    segments = len(signal)

    #Case 1. Since there's only one item, we can just send it back
    if immediatelyIdentifiable(signal):
        return lengthBuckets[segments][0]
    #Case 2
    if segments == 5:
        return fiveSegCheck(signal, decoderMap)
    #And finally, Case 3
    return sixSegCheck(signal, decoderMap)


"""
For a list of signals that we know represent 0-9 on a 
seven segment display (though not in that order),
figure out which is which. Note that pattern has already
been sorted on length at this point, and each item within it is 
in alphabetical order.
"""
def mapPattern(pattern):
    #Having a bidirectional mapping of the signal to its value is helpful
    decoderMap = bidict()
    for signal in pattern:
        value = identifySignal(signal, decoderMap)
        decoderMap.put(value, signal)
    return decoderMap


"""
Use the mapping 
"""
def identifyOutput(output, decoderMap):
    outputVal = ''.join(decoderMap.inverse[digit] for digit in output)
    return outputVal


#Input text is a list of tuples
#Both items in the tuples are lists of strings
def decodeOutput(inputTxt):
    sum = 0 
    for pattern, output in inputTxt:
        decoderMap = mapPattern(pattern)
        outputVal = identifyOutput(output, decoderMap)
        sum += int(outputVal)
    return sum


def main():
    inputTxt = getFile("input.txt") 
    partOneAnswer = getIdentifiableNumbers(inputTxt)
    partTwoAnswer = decodeOutput(inputTxt)
    print('Part 1 answer: {0}\nPart 2 answer: {1}'.format(partOneAnswer, partTwoAnswer))


if __name__ == "__main__":
    main()