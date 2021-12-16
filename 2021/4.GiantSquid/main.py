"""
Literally squid game, i can't believe this
Finished 12/14/2021
"""
from io import TextIOWrapper
import os
from bingoBoard import Board


#For advent of code purposes, the file is always there and correctly formatted
def getFile(fileName, boardSize):
    filePath = os.path.join(os.path.dirname(__file__), fileName)
    callOrder = []
    boards = []

    with open(filePath, "r") as file:
        callOrder = file.readline().strip().split(',')
        board = []
        for line in file:
            cleaned = line.strip()
            if len(cleaned):
                board.append(cleaned.split())
            if len(board) == boardSize:
                boards.append(Board(callOrder, board, boardSize))
                board = []
    return boards




def main():
    boards = getFile("input.txt", 5)  
    #This is part 1
    print("Score of first winner: {0}".format(min(boards)))
    #This is part 2
    print("Score of last winner: {0}".format(max(boards)))


if __name__ == "__main__":
    main()