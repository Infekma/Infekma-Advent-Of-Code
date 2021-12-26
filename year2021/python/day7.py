import aocd
import numpy as np

YEAR = 2021
DAY = 7

# sums all numbers from start to end
def sumOfAllNums(start, end):
    n = abs(end - start)
    return n * (n+1) / 2

def calculateFuelCostToMoveToHorPos(datadict, destPos, incrementallyExpensive):
    fuelCostList = [0] * len(datadict)
    for i, val in enumerate(datadict):
        f = sumOfAllNums(val['pos'], destPos) if incrementallyExpensive else abs(destPos - val['pos'])
        fuelCostList[i] = f * val['occurrence']

    return sum(fuelCostList)

# the data is prepared by creating a dictionary that bundles up duplicates into a single entry
# instead a occurence counter is set
def prepareData(data):
    datadict = data.copy()
    datadict = [int(val) for val in datadict[0].split(',')]
    datadict.sort()

    datadict = [{'pos': i, 'occurrence': datadict.count(i)} for i in datadict]
    datadict = list({v['pos']:v for v in datadict}.values())
    return datadict

def part_a(data) -> int:
    datadict = prepareData(data)

    # only have to iterate between the min and max values
    maxVal = datadict[-1]['pos']
    minVal = datadict[0]['pos']

    # get largest supported int size for the system
    minFuelCost = np.iinfo(np.int).max
    for i in range(minVal, maxVal):
        minFuelCost = min(calculateFuelCostToMoveToHorPos(datadict, i, False), minFuelCost)

    return round(minFuelCost)
    
def part_b(data) -> int:
    datadict = prepareData(data)

    maxVal = datadict[-1]['pos']
    minVal = datadict[0]['pos']

    minFuelCost = np.iinfo(np.int).max # get largest supported int size for the system
    for i in range(minVal, maxVal):
        minFuelCost = min(calculateFuelCostToMoveToHorPos(datadict, i, True), minFuelCost)

    return round(minFuelCost)

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