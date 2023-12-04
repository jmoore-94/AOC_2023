from collections import Counter

with open('AdventOfCode2023_04.txt', 'r') as inputFile:
    p_input = inputFile.read()
print (p_input)


def ParseInput(puzzle):
    newPuzzle = []
    puzzleLine = ''
    for p in puzzle:
        if p == '\n':
            puzzleLine = puzzleLine.split(' ')
            newPuzzle.append(puzzleLine)
            puzzleLine = ''
        else:
            puzzleLine = puzzleLine + p
    puzzleLine = puzzleLine.split(' ')
    newPuzzle.append(puzzleLine)
    return newPuzzle


def OrganizeData(data):
    cardList = []
    for card in data:
        cardInfo = []
        cardValues = []
        for c in card:
            if ':' in c:
                cardNumber = c[:-1]
                cardInfo.append(cardNumber)
            elif c.isdigit():
                cardValues.append(int(c))
            elif '|' in c:
                cardInfo.append(cardValues)
                cardValues = []
        cardInfo.append(cardValues)
        cardInfo.append(1)
        cardList.append(cardInfo)
    return cardList


# # Part One
# def FindWinningNumbers(dataA, dataB):
#     winningNumbers = Counter(dataA + dataB)
#     count = 0
#     for w in winningNumbers:
#         if winningNumbers[w] == 2:
#             if count == 0:
#                 count = count + 1
#             else:
#                 count = count * 2
#     return count


# Part Two
def FindWinningNumbers(dataA, dataB):
    winningNumbers = Counter(dataA + dataB)
    count = 0
    for w in winningNumbers:
        if winningNumbers[w] == 2:
            count = count + 1
    return count


CardData = ParseInput(p_input)
OrganizedCardData = OrganizeData(CardData)
tally = 0
for o in range(len(OrganizedCardData)):
    # print('Card Number: ' + str(OrganizedCardData[o][0]))
    # # Part One
    # temp = FindWinningNumbers(OrganizedCardData[o][1], OrganizedCardData[o][2])
    # tally = tally + temp

    # Part Two
    temp = FindWinningNumbers(OrganizedCardData[o][1], OrganizedCardData[o][2])
    for t in range(temp):
        OrganizedCardData[o + (t + 1)][3] = OrganizedCardData[o + (t + 1)][-1] + (1 * OrganizedCardData[o][-1])

# Part Two
for o in OrganizedCardData:
    tally = tally + o[-1]
print('TOTAL: ' + str(tally))
