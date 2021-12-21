import aocd

YEAR = 2021
DAY = 1

def part_a(data) -> int:
    depthIncreased = 0
    last = data[0]
    for i in range(1, len(data)):
        cur = data[i]
        if cur > last:
            depthIncreased +=1  
        last = cur
    return depthIncreased

def part_b(data) -> int:
    sumSize = 3
    lastSumTotal = sum([data[x] for x in range(0, sumSize)])
    depthIncreased = 0
    # offset the iteration by 1 so that we start on the 2nd sum
    # lastSumTotal is initialised to the first sum
    for i in range(1, len(data)-(sumSize-1)):
        # calculcate the sum total for sumSize elements
        sumTotal = sum([data[x] for x in range(i, i+sumSize)])

        # check if the sum increased and its not the first depth
        if sumTotal > lastSumTotal:
            depthIncreased += 1

        # store for next comparison
        lastSumTotal = sumTotal

    return depthIncreased

if __name__ == "__main__": 
    # session token is derived from AOC_SESSION environmental variable
    dayPuzzle = aocd.models.Puzzle(year=YEAR, day=DAY)
    dayData = aocd.transforms.numbers(dayPuzzle.input_data)

    partA = part_a(dayData)
    partB = part_b(dayData)

    print(f"part a: {partA}")
    print(f"part b: {partB}")

    submitResults = True
    if submitResults:
        aocd.submit(partA, part="a", day=DAY, year=YEAR)
        aocd.submit(partB, part="b", day=DAY, year=YEAR)