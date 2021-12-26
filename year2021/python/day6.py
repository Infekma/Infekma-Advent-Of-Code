import aocd

YEAR = 2021
DAY = 6

# credit to my brother for this solution!

def getData(data):
    data = data[0].split(',')
    data = [int(i) for i in data]
    return data

def prepareData(data):
    # creating a dictionary of counts
    # key = [0, 1, 2, 3, ..., 8]
    # value = count of key in data
    data_dict = {}
    for i in range(9):
        data_dict[i] = data.count(i)
    return data_dict

REPRODUCTION_RATE = 6
NEWBORN_READY_RATE = 2

def simulate(data, time_length):
    # initializing loop counter
    day = 1
    
    while day <= time_length:
        births = data[0]
        
        # counting down all timers
        for i in range(8):
            data[i] = data[i+1]
            
        # births and resets    
        data[REPRODUCTION_RATE + NEWBORN_READY_RATE] = births
        data[REPRODUCTION_RATE] += births
        
        # increment loop counter
        day += 1
    
    return sum(data.values())

def part_a(data) -> int:
    return simulate(prepareData(getData(data)), 80)
    
def part_b(data) -> int:
    return simulate(prepareData(getData(data)), 256)

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