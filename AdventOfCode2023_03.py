from collections import Counter

with open('AdventOfCode2023_03.txt', 'r') as inputFile:
    p_input = inputFile.read()
print (p_input)


def ParseInput(puzzle):
    newPuzzle = []
    puzzleLine = []
    for p in puzzle:
        if p == '\n':
            newPuzzle.append(puzzleLine)
            puzzleLine = []
        else:
            puzzleLine.append(p)
    newPuzzle.append(puzzleLine)
    return newPuzzle


def PartLocation(currentLocation, data):
    alreadyCounted = False
    row = currentLocation[0]
    column = currentLocation[1]
    columnMax = len(data[row])
    # check to the left
    if data[row][column - 1].isdigit():
        alreadyCounted = True
        partLocation = currentLocation
    # check to the right
    else:
        columnCheck = column
        while columnCheck < columnMax:
            columnCheck = columnCheck + 1
            if columnCheck == columnMax:
                break
            if data[row][columnCheck].isdigit() is False:
                break
        partLocation = [row, columnCheck - 1]
    return partLocation, alreadyCounted


# # Part One
# def SearchForValidity(startLocation, stopLocation, data):
#     valid = False
#     row = startLocation[0]
#     columnMin = startLocation[1]
#     columnMax = stopLocation[1]
#     # check left
#     if columnMin > 0:
#         if data[row][columnMin - 1] != '.':
#             valid = True
#     else:
#         columnMin = 1
#     # check right
#     if columnMax < len(data[row]) - 1:
#         if data[row][columnMax + 1] != '.':
#             valid = True
#     else:
#         columnMax = len(data[row]) - 2
#     # check above
#     if row > 0:
#         c = columnMin - 1
#         while c <= columnMax + 1:
#             if data[row - 1][c] != '.':
#                 valid = True
#                 break
#             else:
#                 c = c + 1
#     # check below
#     if row < (len(data) - 1):
#         c = columnMin - 1
#         while c <= columnMax + 1:
#             if data[row + 1][c] != '.':
#                 valid = True
#                 break
#             else:
#                 c = c + 1
#     value = GiveValue(startLocation, stopLocation, data)
#     print value
#     return valid, value


# Part Two
def SearchForValidity(startLocation, stopLocation, data):
    Gears = []
    row = startLocation[0]
    columnMin = startLocation[1]
    columnMax = stopLocation[1]
    # check left
    if columnMin > 0:
        if data[row][columnMin - 1] == '*':
            Gears.append('(' + str(row) + ', ' + str(columnMin - 1) + ')')
    else:
        columnMin = 1
    # check right
    if columnMax < len(data[row]) - 1:
        if data[row][columnMax + 1] == '*':
            Gears.append('(' + str(row) + ', ' + str(columnMax + 1) + ')')
    else:
        columnMax = len(data[row]) - 2
    # check above
    if row > 0:
        c = columnMin - 1
        while c <= columnMax + 1:
            if data[row - 1][c] == '*':
                Gears.append('(' + str(row - 1) + ', ' + str(c) + ')')
            c = c + 1
    # check below
    if row < (len(data) - 1):
        c = columnMin - 1
        while c <= columnMax + 1:
            if data[row + 1][c] == '*':
                Gears.append('(' + str(row + 1) + ', ' + str(c) + ')')
            c = c + 1
    if Gears:
        value = [GiveValue(startLocation, stopLocation, data)]
    else:
        value = []
    return Gears, value


def GiveValue(startLocation, stopLocation, data):
    row = startLocation[0]
    columnStart = startLocation[1]
    columnStop = stopLocation[1]
    value = ''
    while columnStart <= columnStop:
        value = value + data[row][columnStart]
        columnStart = columnStart + 1
    return int(value)


def FindValidParts(data):
    ValidPartsList = []
    allGears = []
    allValues = []
    for row in range(len(data)):
        for item in range(len(data[row])):
            currentLocation = [row, item]
            if data[row][item].isdigit():
                endLocation = PartLocation(currentLocation, data)
                if endLocation[1] is False:
                    isValid = SearchForValidity(currentLocation, endLocation[0], data)
                    # # Part One
                    # if isValid[0] is True:
                    #     ValidPartsList.append(isValid[1])
                    # Part Two
                    allGears = allGears + isValid[0]
                    allValues = allValues + isValid[1]
    print allGears
    print allValues

    cogCounter = Counter(allGears)

    for cog in cogCounter:
        if cogCounter[cog] == 2:
            gearPairs = []
            while cog in allGears:
                print cog
                gearIndex = allGears.index(cog)
                gearPairs.append(allValues[gearIndex])
                del allGears[gearIndex]
                del allValues[gearIndex]
            ValidPartsList.append(gearPairs)
    print ValidPartsList
    return ValidPartsList


parsed_data = ParseInput(p_input)
parts = FindValidParts(parsed_data)
total = 0
for p in parts:
    print p
    # Part One
    # total = total + p
    # Part Two
    total = total + (p[0] * p[1])
print('TOTAL: ' + str(total))
