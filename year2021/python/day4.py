import aocd
import csv
from numpy import matrixlib

YEAR = 2021
DAY = 4

# simple class representation for single value on the bingo board
class BingoEntry:
    def __init__(self, value):
        self.value = int(value)
        self.isMarked = False

    # checks if this entry matches the provided value
    # if the entry matches the value it will be marked
    def check(self, value):
        if self.isMarked:
            return

        self.isMarked = True if self.value == value else False
        return self.isMarked
        
class BingoBoard:
    def __init__(self, rows):
        self.board = []

        # populate board with rows of bingo entry
        for row in rows:
            self.board.append([BingoEntry(val) for val in row.split()])

    def check(self, value):
        for row in self.board:
            for entry in row:
                # the bingo board assumes that there are no duplicates
                # return early if the value was found on the board
                if entry.check(value):
                    break
        
    def bingo(self):
        return self.checkForBingoInRows() or self.checkForBingoInColumns()

    def checkForBingoInRows(self):
        # iterate through each row and check for bingo
        for row in self.board:
            if all([val.isMarked for val in row]):
                return True
        return False

    def checkForBingoInColumns(self):
        numOfColumns = len(self.board[0])
        numOfRows = len(self.board)
        # iterate through each column and check for bingo
        for i in range(0, numOfColumns):
            if all([self.board[y][i].isMarked for y in range(0, numOfRows)]):
                return True
        return False

    def getAllUnMarkedEntries(self):
        listOfUnMarkedEntries = []
        for row in self.board:
            for entry in row:
                if not entry.isMarked:
                    listOfUnMarkedEntries.append(entry.value)
        return listOfUnMarkedEntries

    # visualises the bingo board by writing row by row
    # if the board has bingo it'll stand out from non-bingo boards
    # entries that are marked are also indicated
    def visualise(self):
        for row in self.board:
            for i in range(0, len(row)):
                printVal = f" {row[i].value} " if not row[i].isMarked else f"|{row[i].value}| "
                print(printVal, end='')
            print()
            
def getSequence(data):
    sequence = data[0].split(',')
    return [int(val) for val in sequence]

def getBingoBoards(data):
    numOfBoardRows = 5 # hard coded

    boardList = []
    # process each board 1 at a time by processing the numOfBoardRows
    # the data also has a newline between each board that needs to be skipped
    # hence the additional 1
    for x in range(2, len(data)-numOfBoardRows, numOfBoardRows+1):
        boardRows = [data[row] for row in range(x, x+numOfBoardRows)]
        boardList.append(BingoBoard(boardRows))

    return boardList

def checkBingoBoardsAgainstSequence(sequence, boards):
    winningBoards = []
    for value in sequence:
        for board in boards:
            if board.bingo(): # early continue if board is already bingo
                continue

            # check if the current value in the sequence is in the board
            board.check(value)
            if board.bingo(): # is the board a bingo due to the value that was just checked?
                winningBoards.append([board, value])
    return winningBoards

def visualiseBingoBoards(boards):
    for board in boards:
        if board.bingo():
            print("========= BINGO ============")
            board.visualise()
            print("========= BINGO ============")
            print()
        else:
            board.visualise()
            print()

def solveAnswer(a, b):
    return a * b

def part_a(data) -> int:
    boards = getBingoBoards(data)
    results = checkBingoBoardsAgainstSequence(getSequence(data), boards)

    firstResults = results[0]
    unmarkedEntries = firstResults[0].getAllUnMarkedEntries()

    return solveAnswer(sum(unmarkedEntries), firstResults[1])

def part_b(data) -> int:
    boards = getBingoBoards(data)
    results = checkBingoBoardsAgainstSequence(getSequence(data), boards)

    lastResults = results[-1]
    unmarkedEntries = lastResults[0].getAllUnMarkedEntries()
 
    return solveAnswer(sum(unmarkedEntries), lastResults[1])

if __name__ == "__main__": 
    # session token is derived from AOC_SESSION environmental variable
    dayPuzzle = aocd.models.Puzzle(year=YEAR, day=DAY)
    dayData = aocd.transforms.lines(dayPuzzle.input_data)

    partA = part_a(dayData)
    partB = part_b(dayData)

    print(f"part a: {partA}")
    print(f"part b: {partB}")

    submitResults = True
    if submitResults:
        aocd.submit(partA, part="a", day=DAY, year=YEAR)
        aocd.submit(partB, part="b", day=DAY, year=YEAR)