import math
import sys
import time
start_time = time.time()

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


def GenerateAddWhite(board):
    L = []
    for location in range(21):
        if (board[location] == "x"):
            b = board[: location] + "W" + board[(location + 1) : ]
            if (closeMill(location, b)):
                L = GenerateRemoveBlack(b, L)
            else:
                L.append(b)
    return L

def GenerateAddBlack(board):
    L = []
    for location in range(21):
        if (board[location] == "x"):
            b = board[: location] + "B" + board[(location + 1) : ]
            if (closeMill(location, b)):
                L = GenerateRemoveWhite(b, L)
            else:
                L.append(b)
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

def NearMill(board):
    NearMillWhite = 0
    NearMillBlack = 0

    if (board[0] == "W"):
        if (((board[2] == "W") and (board[4] == "x")) or ((board[2] == "x") and (board[4] == "W")) or((board[6] == "W") and (board[18] == "x")) or ((board[6] == "x") and (board[18] == "W"))):
            NearMillWhite += 1
    if (board[1] == "W"):
        if ((board[11] == "W") and (board[20] == "x") or (board[11] == "x") and (board[20] == "W")):
            NearMillWhite += 1
    if (board[2] == "W"):
        if (((board[0] == "W") and (board[4] == "x")) or ((board[7] == "W") and (board[15] == "x")) or ((board[0] == "x") and (board[4] == "W")) or ((board[7] == "x") and (board[15] == "W"))):
            NearMillWhite += 1
    if (board[3] == "W"):
        if ((board[10] == "W") and (board[17] == "x") or (board[10] == "x") and (board[17] == "W")):
            NearMillWhite += 1
    if (board[4] == "W"):
        if (((board[0] == "W") and (board[2] == "x")) or ((board[8] == "W") and (board[12] == "x")) or ((board[0] == "x") and (board[2] == "W")) or ((board[8] == "x") and (board[12] == "W"))):
            NearMillWhite += 1
    if (board[5] == "W"):
        if ((board[9] == "W") and (board[14] == "x") or (board[9] == "x") and (board[14] == "W")):
            NearMillWhite += 1
    if (board[6] == "W"):
        if (((board[0] == "W") and (board[18] == "x")) or ((board[7] == "W") and (board[8] == "x")) or ((board[0] == "x") and (board[18] == "W")) or ((board[7] == "x") and (board[8] == "W"))):
            NearMillWhite += 1
    if (board[7] == "W"):
        if (((board[6] == "W") and (board[8] == "x")) or ((board[2] == "W") and (board[15] == "x")) or ((board[6] == "x") and (board[8] == "W")) or ((board[2] == "x") and (board[15] == "W"))):
            NearMillWhite += 1
    if (board[8] == "W"):
        if (((board[6] == "W") and (board[7] == "x")) or ((board[4] == "W") and (board[12] == "x")) or ((board[6] == "x") and (board[7] == "W")) or ((board[4] == "x") and (board[12] == "W"))):
            NearMillWhite += 1
    if (board[9] == "W"):
        if (((board[5] == "W") and (board[14] == "x")) or ((board[10] == "W") and (board[11] == "x")) or ((board[5] == "x") and (board[14] == "W")) or ((board[10] == "x") and (board[11] == "W"))):
            NearMillWhite += 1
    if (board[10] == "W"):
        if (((board[9] == "W") and (board[11] == "x")) or ((board[3] == "W") and (board[17] == "x")) or ((board[9] == "x") and (board[11] == "W")) or ((board[3] == "x") and (board[17] == "W"))):
            NearMillWhite += 1
    if (board[11] == "W"):
        if (((board[1] == "W") and (board[20] == "x")) or ((board[9] == "W") and (board[10] == "x")) or ((board[1] == "x") and (board[20] == "W")) or ((board[9] == "x") and (board[10] == "W"))):
            NearMillWhite += 1
    if (board[12] == "W"):
        if (((board[4] == "W") and (board[8] == "x")) or ((board[13] == "W") and (board[14] == "x")) or ((board[4] == "x") and (board[8] == "W")) or ((board[13] == "x") and (board[14] == "W"))):
            NearMillWhite += 1
    if (board[13] == "W"):
        if (((board[12] == "W") and (board[14] == "x")) or ((board[16] == "W") and (board[19] == "x")) or ((board[12] == "x") and (board[14] == "W")) or ((board[16] == "x") and (board[19] == "W"))):
            NearMillWhite += 1
    if (board[14] == "W"):
        if (((board[5] == "W") and (board[9] == "x")) or ((board[12] == "W") and (board[13] == "x")) or ((board[5] == "x") and (board[9] == "W")) or ((board[12] == "x") and (board[13] == "W"))):
            NearMillWhite += 1
    if (board[15] == "W"):
        if (((board[2] == "W") and (board[7] == "x")) or ((board[16] == "W") and (board[17] == "x")) or ((board[2] == "x") and (board[7] == "W")) or ((board[16] == "x") and (board[17] == "W"))):
            NearMillWhite += 1
    if (board[16] == "W"):
        if (((board[15] == "W") and (board[17] == "x")) or ((board[13] == "W") and (board[19] == "x")) or ((board[15] == "x") and (board[17] == "W")) or ((board[13] == "x") and (board[19] == "W"))):
            NearMillWhite += 1
    if (board[17] == "W"):
        if (((board[15] == "W") and (board[16] == "x")) or ((board[3] == "W") and (board[10] == "x")) or ((board[15] == "x") and (board[16] == "W")) or ((board[3] == "x") and (board[10] == "W"))):
            NearMillWhite += 1
    if (board[18] == "W"):
        if (((board[0] == "W") and (board[6] == "x")) or ((board[19] == "W") and (board[20] == "x")) or ((board[0] == "x") and (board[6] == "W")) or ((board[19] == "x") and (board[20] == "W"))):
            NearMillWhite += 1
    if (board[19] == "W"):
        if (((board[18] == "W") and (board[20] == "x")) or ((board[13] == "W") and (board[16] == "x")) or ((board[18] == "x") and (board[20] == "W")) or ((board[13] == "x") and (board[16] == "W"))):
            NearMillWhite += 1
    if (board[20] == "W"):
        if (((board[18] == "W") and (board[19] == "x")) or ((board[1] == "W") and (board[11] == "x")) or ((board[18] == "x") and (board[19] == "W")) or ((board[1] == "x") and (board[11] == "W"))):
            NearMillWhite += 1

    if (board[0] == "B"):
        if (((board[2] == "B") and (board[4] == "x")) or ((board[2] == "x") and (board[4] == "B")) or((board[6] == "B") and (board[18] == "x")) or ((board[6] == "x") and (board[18] == "B"))):
            NearMillBlack += 1
    if (board[1] == "B"):
        if ((board[11] == "B") and (board[20] == "x") or (board[11] == "x") and (board[20] == "B")):
            NearMillBlack += 1
    if (board[2] == "B"):
        if (((board[0] == "B") and (board[4] == "x")) or ((board[7] == "B") and (board[15] == "x")) or ((board[0] == "x") and (board[4] == "B")) or ((board[7] == "x") and (board[15] == "B"))):
            NearMillBlack += 1
    if (board[3] == "B"):
        if ((board[10] == "B") and (board[17] == "x") or (board[10] == "x") and (board[17] == "B")):
            NearMillBlack += 1
    if (board[4] == "B"):
        if (((board[0] == "B") and (board[2] == "x")) or ((board[8] == "B") and (board[12] == "x")) or ((board[0] == "x") and (board[2] == "B")) or ((board[8] == "x") and (board[12] == "B"))):
            NearMillBlack += 1
    if (board[5] == "B"):
        if ((board[9] == "B") and (board[14] == "x") or (board[9] == "x") and (board[14] == "B")):
            NearMillBlack += 1
    if (board[6] == "B"):
        if (((board[0] == "B") and (board[18] == "x")) or ((board[7] == "B") and (board[8] == "x")) or ((board[0] == "x") and (board[18] == "B")) or ((board[7] == "x") and (board[8] == "B"))):
            NearMillBlack += 1
    if (board[7] == "B"):
        if (((board[6] == "B") and (board[8] == "x")) or ((board[2] == "B") and (board[15] == "x")) or ((board[6] == "x") and (board[8] == "B")) or ((board[2] == "x") and (board[15] == "B"))):
            NearMillBlack += 1
    if (board[8] == "B"):
        if (((board[6] == "B") and (board[7] == "x")) or ((board[4] == "B") and (board[12] == "x")) or ((board[6] == "x") and (board[7] == "B")) or ((board[4] == "x") and (board[12] == "B"))):
            NearMillBlack += 1
    if (board[9] == "B"):
        if (((board[5] == "B") and (board[14] == "x")) or ((board[10] == "B") and (board[11] == "x")) or ((board[5] == "x") and (board[14] == "B")) or ((board[10] == "x") and (board[11] == "B"))):
            NearMillBlack += 1
    if (board[10] == "B"):
        if (((board[9] == "B") and (board[11] == "x")) or ((board[3] == "B") and (board[17] == "x")) or ((board[9] == "x") and (board[11] == "B")) or ((board[3] == "x") and (board[17] == "B"))):
            NearMillBlack += 1
    if (board[11] == "B"):
        if (((board[1] == "B") and (board[20] == "x")) or ((board[9] == "B") and (board[10] == "x")) or ((board[1] == "x") and (board[20] == "B")) or ((board[9] == "x") and (board[10] == "B"))):
            NearMillBlack += 1
    if (board[12] == "B"):
        if (((board[4] == "B") and (board[8] == "x")) or ((board[13] == "B") and (board[14] == "x")) or ((board[4] == "x") and (board[8] == "B")) or ((board[13] == "x") and (board[14] == "B"))):
            NearMillBlack += 1
    if (board[13] == "B"):
        if (((board[12] == "B") and (board[14] == "x")) or ((board[16] == "B") and (board[19] == "x")) or ((board[12] == "x") and (board[14] == "B")) or ((board[16] == "x") and (board[19] == "B"))):
            NearMillBlack += 1
    if (board[14] == "B"):
        if (((board[5] == "B") and (board[9] == "x")) or ((board[12] == "B") and (board[13] == "x")) or ((board[5] == "x") and (board[9] == "B")) or ((board[12] == "x") and (board[13] == "B"))):
            NearMillBlack += 1
    if (board[15] == "B"):
        if (((board[2] == "B") and (board[7] == "x")) or ((board[16] == "B") and (board[17] == "x")) or ((board[2] == "x") and (board[7] == "B")) or ((board[16] == "x") and (board[17] == "B"))):
            NearMillBlack += 1
    if (board[16] == "B"):
        if (((board[15] == "B") and (board[17] == "x")) or ((board[13] == "B") and (board[19] == "x")) or ((board[15] == "x") and (board[17] == "B")) or ((board[13] == "x") and (board[19] == "B"))):
            NearMillBlack += 1
    if (board[17] == "B"):
        if (((board[15] == "B") and (board[16] == "x")) or ((board[3] == "B") and (board[10] == "x")) or ((board[15] == "x") and (board[16] == "B")) or ((board[3] == "x") and (board[10] == "B"))):
            NearMillBlack += 1
    if (board[18] == "B"):
        if (((board[0] == "B") and (board[6] == "x")) or ((board[19] == "B") and (board[20] == "x")) or ((board[0] == "x") and (board[6] == "B")) or ((board[19] == "x") and (board[20] == "B"))):
            NearMillBlack += 1
    if (board[19] == "B"):
        if (((board[18] == "B") and (board[20] == "x")) or ((board[13] == "B") and (board[16] == "x")) or ((board[18] == "x") and (board[20] == "B")) or ((board[13] == "x") and (board[16] == "B"))):
            NearMillBlack += 1
    if (board[20] == "B"):
        if (((board[18] == "B") and (board[19] == "x")) or ((board[1] == "B") and (board[11] == "x")) or ((board[18] == "x") and (board[19] == "B")) or ((board[1] == "x") and (board[11] == "B"))):
            NearMillBlack += 1


    return 10 * (NearMillWhite - NearMillBlack)

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

def StaticEstimationOpening(board):
    numWhitePieces = 0
    numBlackPieces = 0
    nearmillvalue = NearMill(board)

    for location in range(21):
        if (board[location] == "W"):
            numWhitePieces += 1
        elif (board[location] == "B"):
            numBlackPieces += 1

    return numWhitePieces - numBlackPieces + nearmillvalue

def MaxMin(board, ply):
    L = GenerateAddWhite(board)
    count = 0
    path = ""

    if (ply == 1):
        index_value = -math.inf
        for l in L:
            if (StaticEstimationOpening(l) >= index_value):
                index_value = StaticEstimationOpening(l)
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
    L = GenerateAddBlack(board)
    count = 0
    path = ""

    if (ply == 1):
        index_value = math.inf
        for l in L:
            if (StaticEstimationOpening(l) <= index_value):
                index_value = StaticEstimationOpening(l)
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
    print("MINIMAX estimate: " + str(StaticEstimationOpening(board1)) + ".")

    output1.write(board1)
else:
    my_path, my_count, my_board, my_index = MaxMin(board1, d)
    my_paths = my_path.split(" ")

    print("Input position: " + board1 + " Output position: " + my_paths[2 * d - 2])
    print("Positions evaluated by static estimation: " + str(my_count) + ".")
    print("MINIMAX estimate: " + str(my_index) + ".")

    output1.write(my_paths[2 * d - 2])
    #print(my_board)

output1.close()

#print("--- %s seconds ---" % (time.time() - start_time))