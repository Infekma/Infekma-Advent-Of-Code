import aocd
from bitarray import bitarray
from bitarray.util import ba2int
from operator import xor

YEAR = 2021
DAY = 3

def solveAnswer(a, b):
    return a * b

def getMostCommonBitAtPosition(data, position) :
    bitArray = bitarray([int(val[position]) for val in data])
    return 1 if bitArray.count(1) >= bitArray.count(0) else 0
    
def flipBit(bit):
    return 1 - bit

def getGammaRating(data):
    gammaR = bitarray()
    for i in range(0, len(data[0])):
        gammaR.append(getMostCommonBitAtPosition(data, i))
    return gammaR

def getEpsilonRating(data):
    # epsilon rating is the inverse of gamma
    epsilonR = getGammaRating(data) 
    epsilonR = ~epsilonR
    return epsilonR

def part_a(data) -> int:
    return solveAnswer(ba2int(getGammaRating(data)), ba2int(getEpsilonRating(data)))

def getMostCommonBitArray(data, inverse):
    runningList = [bitarray(val) for val in data]
    for i in range(0, len(data[0])):
        commonBit = getMostCommonBitAtPosition(runningList, i)
        commonBit = flipBit(commonBit) if inverse else commonBit

        # stop once the list has been narrowed down to a single value
        if len(runningList) == 1:
            break
        
        # iterate over the running list and check whether any of them
        # does not have the correct common bit and add them to seperate list
        # to delete and subtract from the running list
        elemsToDelete = [val for val in runningList if val[i] != commonBit]

        # remove the list above from the running list since those do not match the criteria
        runningList = [val for val in runningList if val not in elemsToDelete]
        
    # at this stage the list should only have a single element, if it has multiple values
    # then they must be identical and duplicate values so its still "correct" to return first
    return runningList[0]

def getOxyGenRating(data):
    return getMostCommonBitArray(data, False)

def getCO2ScrubRating(data):
    # CO2 scrubber rating is the inverse of the oxygen rating - the least common as oppose to the most common
    return getMostCommonBitArray(data, True)

def part_b(data) -> int:
    return solveAnswer(ba2int(getOxyGenRating(data)), ba2int(getCO2ScrubRating(data)))

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