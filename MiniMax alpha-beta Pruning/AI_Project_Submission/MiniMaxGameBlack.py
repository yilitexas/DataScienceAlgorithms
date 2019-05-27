import math
import sys

if(len(sys.argv) != 4) :
    print("takes 3 arguments. Not ")
    sys.exit()

input_name = sys.argv[1]
output_name = sys.argv[2]
d = int(sys.argv[3])

input1 = open(input_name, "r")
lines = input1.readlines()
board1 = lines[0]
input1.close()

def SwitchWhiteBlack(board):
    new_board = ""
    for i in range(21):
        if (board[i] == "W"):
            new_board += "B"
        elif (board[i] == "B"):
            new_board += "W"
        else:
            new_board += "x"

    return new_board


def GenerateMoveWhite(board):
    L = []
    for location in range(21):
        if (board[location] == "W"):
            n = Neighbors(location)
            for newLocation in n:
                if (board[newLocation] == "x"):
                    b1 = board[: location] + "x" + board[(location + 1) : ]
                    b2 = b1[: newLocation] + "W" + b1[(newLocation + 1) : ]
                    if (closeMill(newLocation, b2)):
                        L = GenerateRemoveBlack(b2, L)
                    else:
                        L.append(b2)

    return L

def GenerateHoppingWhite(board):
    L = []
    for location in range(21):
        if (board[location] == "W"):
            for newLocation in range(21):
                if (board[newLocation] == "x"):
                    b1 = board[: location] + "x" + board[(location + 1) : ]
                    b2 = b1[: newLocation] + "W" + b1[(newLocation + 1) : ]
                    if (closeMill(newLocation, b2)):
                        L = GenerateRemoveBlack(b2, L)
                    else:
                        L.append(b2)

    return L

def GenerateHoppingBlack(board):
    L = []
    for location in range(21):
        if (board[location] == "B"):
            for newLocation in range(21):
                if (board[newLocation] == "x"):
                    b1 = board[: location] + "x" + board[(location + 1) : ]
                    b2 = b1[: newLocation] + "B" + b1[(newLocation + 1) : ]
                    if (closeMill(newLocation, b2)):
                        L = GenerateRemoveWhite(b2, L)
                    else:
                        L.append(b2)

    return L


def GenerateMoveBlack(board):
    L = []
    for location in range(21):
        if (board[location] == "B"):
            n = Neighbors(location)
            for newLocation in n:
                if (board[newLocation] == "x"):
                    b1 = board[: location] + "x" + board[(location + 1):]
                    b2 = b1[: newLocation] + "B" + b1[(newLocation + 1):]
                    if (closeMill(newLocation, b2)):
                        L = GenerateRemoveWhite(b2, L)
                    else:
                        L.append(b2)

    return L

def GenerateRemoveBlack(board, L):
    flag1 = True

    for location in range(21):
        if (board[location] == "B"):
            if (not closeMill(location, board)):
                b = board[: location] + "x" + board[(location + 1) : ]
                L.append(b)
                flag1 = False

    if (flag1):
        L.append(board)

    return L

def GenerateRemoveWhite(board, L):
    flag1 = True

    for location in range(21):
        if (board[location] == "W"):
            if (not closeMill(location, board)):
                b = board[: location] + "x" + board[(location + 1) : ]
                L.append(b)
                flag1 = False

    if (flag1):
        L.append(board)

    return L


def Neighbors(location):
    if (location == 0):
        return [1, 2, 6]
    elif (location == 1):
        return [0, 11]
    elif (location == 2):
        return [0, 3, 4, 7]
    elif (location == 3):
        return [2, 10]
    elif (location == 4):
        return [2, 5, 8]
    elif (location == 5):
        return [4, 9]
    elif (location == 6):
        return [0, 7, 18]
    elif (location == 7):
        return [2, 6, 8, 15]
    elif (location == 8):
        return [4, 7, 12]
    elif (location == 9):
        return [5, 10, 14]
    elif (location == 10):
        return [3, 9, 11, 17]
    elif (location == 11):
        return [1, 10, 20]
    elif (location == 12):
        return [8, 13]
    elif (location == 13):
        return [12, 14, 16]
    elif (location == 14):
        return [9, 13]
    elif (location == 15):
        return [7, 16]
    elif (location == 16):
        return [13, 15, 17, 19]
    elif (location == 17):
        return [10, 16]
    elif (location == 18):
        return [6, 19]
    elif (location == 19):
        return [16, 18, 20]
    else:
        return [11, 19]


def closeMill(location, board):
    flag1 = False

    if (board[location] == "W"):
        if (location == 0):
            if (((board[6] == "W") and (board[18] == "W")) or ((board[2] == "W") and (board[4] == "W"))):
                flag1 = True
        elif (location == 1):
            if ((board[11] == "W") and (board[20] == "W")):
                flag1 = True
        if (location == 2):
            if (((board[0] == "W") and (board[4] == "W")) or ((board[7] == "W") and (board[15] == "W"))):
                flag1 = True
        elif (location == 3):
            if ((board[10] == "W") and (board[17] == "W")):
                flag1 = True
        elif (location == 4):
            if (((board[0] == "W") and (board[2] == "W")) or ((board[8] == "W") and (board[12] == "W"))):
                flag1 = True
        elif (location == 5):
            if ((board[9] == "W") and (board[14] == "W")):
                flag1 = True
        elif (location == 6):
            if (((board[0] == "W") and (board[18] == "W")) or ((board[7] == "W") and (board[8] == "W"))):
                flag1 = True
        elif (location == 7):
            if (((board[6] == "W") and (board[8] == "W")) or ((board[2] == "W") and (board[15] == "W"))):
                flag1 = True
        elif (location == 8):
            if (((board[6] == "W") and (board[7] == "W")) or ((board[4] == "W") and (board[12] == "W"))):
                flag1 = True
        elif (location == 9):
            if (((board[5] == "W") and (board[14] == "W")) or ((board[10] == "W") and (board[11] == "W"))):
                flag1 = True
        elif (location == 10):
            if (((board[9] == "W") and (board[11] == "W")) or ((board[3] == "W") and (board[17] == "W"))):
                flag1 = True
        elif (location == 11):
            if (((board[1] == "W") and (board[20] == "W")) or ((board[9] == "W") and (board[10] == "W"))):
                flag1 = True
        elif (location == 12):
            if (((board[4] == "W") and (board[8] == "W")) or ((board[13] == "W") and (board[14] == "W"))):
                flag1 = True
        elif (location == 13):
            if (((board[12] == "W") and (board[14] == "W")) or ((board[16] == "W") and (board[19] == "W"))):
                flag1 = True
        elif (location == 14):
            if (((board[5] == "W") and (board[9] == "W")) or ((board[12] == "W") and (board[13] == "W"))):
                flag1 = True
        elif (location == 15):
            if (((board[2] == "W") and (board[7] == "W")) or ((board[16] == "W") and (board[17] == "W"))):
                flag1 = True
        elif (location == 16):
            if (((board[15] == "W") and (board[17] == "W")) or ((board[13] == "W") and (board[19] == "W"))):
                flag1 = True
        elif (location == 17):
            if (((board[15] == "W") and (board[16] == "W")) or ((board[3] == "W") and (board[10] == "W"))):
                flag1 = True
        elif (location == 18):
            if (((board[0] == "W") and (board[6] == "W")) or ((board[19] == "W") and (board[20] == "W"))):
                flag1 = True
        elif (location == 19):
            if (((board[18] == "W") and (board[20] == "W")) or ((board[13] == "W") and (board[16] == "W"))):
                flag1 = True
        elif (location == 20):
            if (((board[18] == "W") and (board[19] == "W")) or ((board[1] == "W") and (board[11] == "W"))):
                flag1 = True

    if (board[location] == "B"):
        if (location == 0):
            if (((board[6] == "B") and (board[18] == "B")) or ((board[2] == "B") and (board[4] == "B"))):
                flag1 = True
        elif (location == 1):
            if ((board[11] == "B") and (board[20] == "B")):
                flag1 = True
        elif (location == 2):
            if (((board[0] == "B") and (board[4] == "B")) or ((board[7] == "B") and (board[15] == "B"))):
                flag1 = True
        elif (location == 3):
            if ((board[10] == "B") and (board[17] == "B")):
                flag1 = True
        elif (location == 4):
            if (((board[0] == "B") and (board[2] == "B")) or ((board[8] == "B") and (board[12] == "B"))):
                flag1 = True
        elif (location == 5):
            if ((board[9] == "B") and (board[14] == "B")):
                flag1 = True
        elif (location == 6):
            if (((board[0] == "B") and (board[18] == "B")) or ((board[7] == "B") and (board[8] == "B"))):
                flag1 = True
        elif (location == 7):
            if (((board[6] == "B") and (board[8] == "B")) or ((board[2] == "B") and (board[15] == "B"))):
                flag1 = True
        elif (location == 8):
            if (((board[6] == "B") and (board[7] == "B")) or ((board[4] == "B") and (board[12] == "B"))):
                flag1 = True
        elif (location == 9):
            if (((board[5] == "B") and (board[14] == "B")) or ((board[10] == "B") and (board[11] == "B"))):
                flag1 = True
        elif (location == 10):
            if (((board[9] == "B") and (board[11] == "B")) or ((board[3] == "B") and (board[17] == "B"))):
                flag1 = True
        elif (location == 11):
            if (((board[1] == "B") and (board[20] == "B")) or ((board[9] == "B") and (board[10] == "B"))):
                flag1 = True
        elif (location == 12):
            if (((board[4] == "B") and (board[8] == "B")) or ((board[13] == "B") and (board[14] == "B"))):
                flag1 = True
        elif (location == 13):
            if (((board[12] == "B") and (board[14] == "B")) or ((board[16] == "B") and (board[19] == "B"))):
                flag1 = True
        elif (location == 14):
            if (((board[5] == "B") and (board[9] == "B")) or ((board[12] == "B") and (board[13] == "B"))):
                flag1 = True
        elif (location == 15):
            if (((board[2] == "B") and (board[7] == "B")) or ((board[16] == "B") and (board[17] == "B"))):
                flag1 = True
        elif (location == 16):
            if (((board[15] == "B") and (board[17] == "B")) or ((board[13] == "B") and (board[19] == "B"))):
                flag1 = True
        elif (location == 17):
            if (((board[15] == "B") and (board[16] == "B")) or ((board[3] == "B") and (board[10] == "B"))):
                flag1 = True
        elif (location == 18):
            if (((board[0] == "B") and (board[6] == "B")) or ((board[19] == "B") and (board[20] == "B"))):
                flag1 = True
        elif (location == 19):
            if (((board[18] == "B") and (board[20] == "B")) or ((board[13] == "B") and (board[16] == "B"))):
                flag1 = True
        elif (location == 20):
            if (((board[18] == "B") and (board[19] == "B")) or ((board[1] == "B") and (board[11] == "B"))):
                flag1 = True

    return flag1

def StaticEstimationGame(board):
    numWhitePieces = WhiteCount(board)
    numBlackPieces = BlackCount(board)
    L = GenerateMoveBlack(board)
    numBlackMoves = len(L)

    if (numBlackPieces <= 2):
        return 10000
    elif (numWhitePieces <= 2):
        return -10000
    elif (numBlackMoves == 0):
        return 10000
    else:
        return (1000 * (numWhitePieces - numBlackPieces) - numBlackMoves)

def WhiteCount(board):
    sum = 0
    for i in range(21):
        if (board[i] == "W"):
            sum += 1

    return sum


def BlackCount(board):
    sum = 0
    for i in range(21):
        if (board[i] == "B"):
            sum += 1

    return sum

def MaxMin(board, ply):
    if (WhiteCount(board) == 3):
        L = GenerateHoppingWhite(board)
    else:
        L = GenerateMoveWhite(board)

    count = 0
    path = ""

    if (ply == 1):
        index_value = -math.inf
        for l in L:
            if (StaticEstimationGame(l) >= index_value):
                index_value = StaticEstimationGame(l)
                index_board = l
                index_l = l

            count += 1
        path = path + index_l + " "

        return path, count, index_board, index_value
    else:
        index_value = -math.inf

        for l in L:
            child_path, child_count, child_board, child_value = MinMax(l, ply - 1)
            if (child_value >= index_value):
                index_value = child_value
                index_board = child_board
                index_path = child_path
                index_l = l

            count += child_count
        path = path + index_path + " " + index_l + " "

        return path, count, index_board, index_value




def MinMax(board, ply):
    if (BlackCount(board) == 3):
        L = GenerateHoppingBlack(board)
    else:
        L = GenerateMoveBlack(board)
    count = 0
    path = ""

    if (ply == 1):
        index_value = math.inf
        for l in L:
            if (StaticEstimationGame(l) <= index_value):
                index_value = StaticEstimationGame(l)
                index_board = l
                index_l = l
            count += 1
        path = path + index_l + " "

        return path, count, index_board, index_value
    else:
        index_value = math.inf

        for l in L:
            child_path, child_count, child_board, child_value = MaxMin(l, ply - 1)
            if (child_value <= index_value):
                index_value = child_value
                index_board = child_board
                index_path = child_path
                index_l = l
            count += child_count
        path = path + index_path + " " + index_l + " "

        return path, count, index_board, index_value

output1 = open(output_name, "w")

if (d == 0):
    print("Input position: " + board1 + " Output position: " + board1)
    print("Positions evaluated by static estimation: 1.")
    print("MINIMAX estimate: " + str(StaticEstimationGame(board1)) + ".")

    output1.write(board1)
else:
    black_board = SwitchWhiteBlack(board1)
    my_path, my_count, my_board, my_index = MaxMin(black_board, d)
    my_paths = my_path.split(" ")

    my_choice = my_paths[2 * d - 2]
    reverse_board = SwitchWhiteBlack(my_board)
    reverse_index = StaticEstimationGame(reverse_board)
    reverse_choice = SwitchWhiteBlack(my_choice)

    print("Input position: " + board1 + " Output position: " + reverse_choice)
    print("Positions evaluated by static estimation: " + str(my_count) + ".")
    print("MINIMAX estimate: " + str(reverse_index) + ".")
    #print(reverse_board)

    output1.write(reverse_choice)

output1.close()
