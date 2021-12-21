import aocd
from enum import Enum

YEAR = 2021
DAY = 2

class SubmarineActionType(Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

partA_actionMap = {
    SubmarineActionType.FORWARD: lambda horPos, depth, aim, val: (horPos + val, depth, aim),
    SubmarineActionType.DOWN:    lambda horPos, depth, aim, val: (horPos, depth + val, aim),
    SubmarineActionType.UP:      lambda horPos, depth, aim, val: (horPos, depth - val, aim),
}

# down/up actions were changed to instead modify the aim instead of depth
partB_actionMap = {
    SubmarineActionType.FORWARD: lambda horPos, depth, aim, val: (horPos + val, depth + (aim * val), aim),
    SubmarineActionType.DOWN:    lambda horPos, depth, aim, val: (horPos, depth, aim + val),
    SubmarineActionType.UP:      lambda horPos, depth, aim, val: (horPos, depth, aim - val),
}

def performAction(actionMap, action, val, horPos, depth, aim) -> int:
    # ensure the action is defined in the map
    if not action in actionMap:
        assert "action is not supported"
        return (horPos, depth, aim)
        
    return actionMap[action](horPos, depth, aim, val)

# <action> <value>, i.e. forward 8
def processLine(line):
    split = line.split()
    return SubmarineActionType(split[0]), int(split[1])

# solve all the actions for the given input and return the horizontal position and depth after every move has been completed
def solveActionsForInput(data, actionMap, useAim):
    horPos = 0
    depth = 0
    aim = 0

    # iterate through every line in the data, process the line to determine
    # action and value and then perform the action to move the submarine
    for line in data:
        action, val = processLine(line)
        horPos, depth, aim = performAction(actionMap, action, val, horPos, depth, aim if useAim else 0)

    return horPos, depth

def solveAnswer(horizontalPos, depth):
    return horizontalPos * depth

def part_a(data) -> int:
    results = solveActionsForInput(data, partA_actionMap, False)
    return solveAnswer(results[0], results[1])

def part_b(data) -> int:
    results = solveActionsForInput(data, partB_actionMap, True)
    return solveAnswer(results[0], results[1])

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