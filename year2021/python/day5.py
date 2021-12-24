import aocd
import numpy as np

YEAR = 2021
DAY = 5

# returns as ints
def getLargestValuesBetweenArrays(array1, array2):
    return np.array([np.max([int(i1),int(i2)]) for i1,i2 in zip(array1, array2)])

class Grid:
    def __init__(self, size):
        self.grid = np.zeros(size+(1,1), dtype=int)
        self.size = size

    def processVentLines(self, ventLines):
        for ventLine in ventLines:
            for path in ventLine.linePath:
                self.grid[path[0], path[1]] += 1

    # most dangerous lines are defined by the threshold, effectively this is just a count for occurence of threshold
    def countMostDangerousLines(self, threshold):
        numOfDangerLines = 0
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                if self.grid[x,y] >= threshold:
                    numOfDangerLines += 1
        return numOfDangerLines

class HydroVentLine:
    def __init__(self, line, skipDiagonal=True):
        split = [val.split(',') for val in line.split('->')]
        self.start = np.array([split[0][0], split[0][1]], dtype=float)
        self.end = np.array([split[1][0], split[1][1]], dtype=float)
        self.linePath = []
        self.skipDiag = skipDiagonal
        self.calculateLinePath()

    def calculateLinePath(self):
        dir = self.end - self.start
        # the direction is rounded here, resulting in either axis-aligned movement or 45" diagonal movements (when [1,1] or [-1,-1])
        normDir = np.round(np.divide(np.linalg.norm(dir), dir, out=np.zeros_like(dir), where=dir!=0.0))

        # conditional for allowing part a to still give correct answer
        if self.skipDiag and not np.any(np.isclose(self.start, self.end)):
            return

        # move from self.start to self.end with the normalised direction
        curPos = self.start.copy()
        while not np.all(np.isclose(curPos, self.end)):
            # work with floats throughout the iteration but store as int
            self.linePath.append(curPos.copy().astype(int))
            curPos = curPos + normDir
        self.linePath.append(self.end.astype(int)) # also include the ending node

def getHydroVentLines(data, skipDiagonal):
    ventLinesList = []
    for line in data:
        ventLinesList.append(HydroVentLine(line, skipDiagonal))
    return ventLinesList

def getGridSizeFromVentLines(ventLines):
    gridSize = np.array([0,0])
    for ventLine in ventLines:
        largestVentLinePos = getLargestValuesBetweenArrays(ventLine.start, ventLine.end)
        gridSize = getLargestValuesBetweenArrays(largestVentLinePos, gridSize)
    return gridSize

def part_a(data) -> int:
    dangerThreshold = 2
    ventLines = getHydroVentLines(data, True)
    grid = Grid(getGridSizeFromVentLines(ventLines))
    grid.processVentLines(ventLines)
    return grid.countMostDangerousLines(dangerThreshold)

def part_b(data) -> int:
    dangerThreshold = 2
    ventLines = getHydroVentLines(data, False)
    grid = Grid(getGridSizeFromVentLines(ventLines))
    grid.processVentLines(ventLines)
    return grid.countMostDangerousLines(dangerThreshold)

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