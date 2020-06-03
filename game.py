

def main():
    list = makeList()
    horizontalLine = drawLine(70)
    instrcutions = getInstructions()
    playersTurn = 1

    print("Tic-Tac-Toe")
    print()
    print(horizontalLine)
    print(instrcutions)
    print()
    start = input()
    drawTabel(list)
    render(playersTurn, list)

def checkVictory(list, simbol):
    for row in list:
        if row[0] == simbol and row[1] == simbol and row[2] == simbol:
            return True
    for i in range(3):
        if list[0][i] == simbol and list[1][i] == simbol and list[2][i] == simbol:
            return True
    if list[0][0] == simbol and list[1][1] == simbol and list[2][2] == simbol:
        return True
    if list[2][0] == simbol and list[1][1] == simbol and list[0][2] == simbol:
        return True
    return False

def checkTie(list):
    for row in list:
        for col in row:
            if col == ' ':
                return False
    return True


def render(playersTurn, list):
    position = getPosition(playersTurn, list)
    row = int(position[0])-1
    colm = int(position[1])-1
    simbol = getSimbol(playersTurn)
    list[row][colm] = simbol
    drawTabel(list)
    if checkVictory(list, simbol):
        print(f"Player {playersTurn} won!!!")
    elif checkTie(list):
        print(f"No one won the Game!!!")
    else:
        if playersTurn == 1:
            playersTurn = 2
        else:
            playersTurn = 1
        render(playersTurn, list)

def validPosition(pos, list):
    row = int(pos[0])-1
    colm = int(pos[1])-1
    if list[row][colm] == ' ':
        return True
    else:
        return False

def getPosition(playersTurn, list):
    pos = 0
    validPos = ['11','12','13','21','22','23','31','32','33']
    while pos not in validPos:
        simbol = getSimbol(playersTurn)
        pos = input(f"PLAYER {playersTurn}({simbol}): ")
        if not pos in validPos:
            print("Please fill in a valid position.")
        elif validPosition(pos, list) == False:
            print("Please choose a empty square.")
            pos = 0
    return pos

def getSimbol(player):
    if player == 1:
        return 'X'
    elif player == 2:
        return 'O'

def drawTabel(list):
    marginTabel = setMargin(5)
    print()
    print(f"{marginTabel} {list[0][0]} | {list[0][1]} | {list[0][2]}")
    print(f"{marginTabel}---+---+---")
    print(f"{marginTabel} {list[1][0]} | {list[1][1]} | {list[1][2]}")
    print(f"{marginTabel}---+---+---")
    print(f"{marginTabel} {list[2][0]} | {list[2][1]} | {list[2][2]}")
    print()

def makeList():
    arr = []
    for i in range(3):
        arr.append([])
        for j in range(3):
            arr[i].append(" ")
    return arr

def drawLine(n):
    line = ''
    for i in range(n):
        line += '-'
    return line

def setMargin(n):
    margin = ''
    for i in range(n):
        margin += ' '
    return margin

def getInstructions():
    return "\nThe rules for this game are very simple, each round a player chose a free place in the # to put his simbol.\n\nThe first player will have an 'O' as a simbol and the second player an 'X'.\n\nTo chose a position  the player have to write first de number of the line followed buy the number of the row.\n\nFor the top left square the player would type 11, where the first one is fore the first row and the second 1 is for the first column, 13 would be for the top right position and 31 for the bottom left position. You can only choose a free location.\n\nThe first player taht has three simbols in a row (horizontal, vertical or diagonal) wins the game.\n\nPress ENTER to start."

main();
