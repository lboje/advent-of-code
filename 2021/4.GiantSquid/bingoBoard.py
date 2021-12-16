
"""
A bingo board is a 5x5 board.
By filling any row or column, one may win
"""
class Board:

    """
    Call order is an mapping of strings to the round they're called
    board is a 5x5 array of strings
    """
    def __init__(self, callOrder, board, boardSize):
        self.callOrder = callOrder
        self.board = board
        self.boardSize = boardSize
        self.findWin()

    
    #Find the time of win, as well as the value of the board at that time
    def findWin(self):
        #Initialize a 5x5 array of 0s
        checkSum = [ [0]*self.boardSize for _ in range(self.boardSize)]
        order = self.mapBoard()

        #Iterate through, marking up checkSum appropriately
        for round, call in enumerate(self.callOrder): 
            if call in order:
                (row, col) = order[call]
                checkSum[row][col] = 1
                if self.hasWon(checkSum):
                    self.winRound = round
                    self.remaining = self.sumRemainder(checkSum)
                    self.winCall = int(call)
                    return
        

    #Map call order to the coordinates for that spot on the board
    def mapBoard(self):
        order = {}
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                order[col] = (i, j)
        return order


    #We've won if any row or column is equal to 5.
    def hasWon(self, board):
        for i in range(self.boardSize):
            #Check row
            if sum(board[i]) == self.boardSize:
                return True
            #Check column
            column = [row[i] for row in board]
            if sum(column) == self.boardSize:
                return True
        return False

    #Find non-called spaces on board, add them together
    def sumRemainder(self, board):
        sum = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if board[i][j] != 1:
                    sum += int(self.board[i][j])
        return sum

    #This is the first round where this board could win
    @property
    def round(self):
        return self.winRound

    #This is the score for the board
    @property
    def score(self):
        return 

    #We just want to print the winning score
    def __str__(self):
        return str(self.remaining * self.winCall)

    #For the purposes of winning, we only care who's done first
    #No ties in baseball
    def __eq__(self, other):
        return self.winRound == other.winRound

    #See __eq__
    def __lt__(self, other):
        return self.winRound < other.winRound


