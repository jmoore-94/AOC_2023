with open('AdventOfCode2023_02.txt', 'r') as inputFile:
    p_input = inputFile.read()
print (p_input)


def ParseInput(puzzle):
    newPuzzle = []
    puzzleLine = ''
    for p in puzzle:
        if p == '\n':
            newPuzzle.append(puzzleLine)
            puzzleLine = ''
        else:
            puzzleLine = puzzleLine + p
    newPuzzle.append(puzzleLine)
    return newPuzzle


def CollectGameData(data):
    gameData = []
    for d in data:
        game = d.split(': ')
        game[0] = int(game[0].replace('Game ', ''))
        game[1] = game[1].replace(',', '')
        game[1] = game[1].replace(' ', '')
        game[1] = game[1].split(';')
        print game[1]
        collectAll = []
        for g in game[1]:
            collect = []
            for i in range(len(g)):
                if g[i].isdigit():
                    if g[i + 1].isdigit():
                        pass
                    elif g[i - 1].isdigit():
                        collect.append((int(g[i - 1] + g[i]), str(g[i + 1])))
                    else:
                        collect.append((int(g[i]), str(g[i + 1])))
            collectAll.append(collect)
        game[1] = collectAll
        gameData.append(game)
    return gameData


parsed_data = ParseInput(p_input)
total_games = CollectGameData(parsed_data)
tally = 0

# # part one
# # total cubes
# red = 12
# green = 13
# blue = 14
# for eachGame in total_games:
#     valid = True
#     # print(eachGame[0])
#     for each in eachGame[1]:
#         # print(each)
#         for e in each:
#             if e[1] == 'r':
#                 if e[0] > red:
#                     valid = False
#                     break
#             elif e[1] == 'g':
#                 if e[0] > green:
#                     valid = False
#                     break
#             elif e[1] == 'b':
#                 if e[0] > blue:
#                     valid = False
#                     break
#     if valid is True:
#         tally = tally + eachGame[0]

# part two
for eachGame in total_games:
    valid = 1
    red = 0
    green = 0
    blue = 0
    # print(eachGame[0])
    for each in eachGame[1]:
        for e in each:
            if e[1] == 'r':
                if e[0] > red:
                    red = e[0]
            elif e[1] == 'g':
                if e[0] > green:
                    green = e[0]
            elif e[1] == 'b':
                if e[0] > blue:
                    blue = e[0]
        # print(each, red, green, blue)
    valid = valid * red * green * blue
    tally = tally + valid
print tally


