with open('AdventOfCode2023_01.txt', 'r') as inputFile:
    p_input = inputFile.read()
print (p_input)

valueDictionary = {
    'o1ne': 'one',
    't2wo': 'two',
    'th3ree': 'three',
    'fo4ur': 'four',
    'fi5ve': 'five',
    's6ix': 'six',
    'se7ven': 'seven',
    'ei8ght': 'eight',
    'ni9ne': 'nine'
}


def ParseInput(puzzle):
    newPuzzle = []
    digitList = []
    for v in valueDictionary:
        if valueDictionary[v] in puzzle:
            puzzle = puzzle.replace(valueDictionary[v], v)
    print puzzle

    for p in puzzle:
        if p.isdigit():
            digitList.append(p)
        elif p == '\n':
            newPuzzle.append(digitList)
            digitList = []
    newPuzzle.append(digitList)
    return newPuzzle


def GetCalibrationValue(valueList):
    calibrationValue = valueList[0] + valueList[-1]
    calibrationValue = int(calibrationValue)
    return calibrationValue


data = ParseInput(p_input)
print (data)
total = 0
for d in data:
    total = total + GetCalibrationValue(d)
    print(GetCalibrationValue(d))
print (total)