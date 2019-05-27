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

    for location in range(21):
        if (board[location] == "W"):
            numWhitePieces += 1
        elif (board[location] == "B"):
            numBlackPieces += 1

    return numWhitePieces - numBlackPieces

nodes_visited = []
nodes_level = []
nodes_estimates = []
def MaxMin(board, ply, a, b):

    if (ply == 0):
        index_value = StaticEstimationOpening(board)
        return index_value
    else:
        index_value = -math.inf
        L = GenerateAddWhite(board)
        for l in L:
            child_value = MinMax(l, ply - 1, a, b)
            nodes_visited.append(l)
            nodes_level.append(ply - 1)
            nodes_estimates.append(child_value)

            if (child_value >= index_value):
                index_value = child_value

            if (index_value >= b):
                return index_value
            else:
                a = max(index_value, a)

        return index_value


def MinMax(board, ply, a, b):

    if (ply == 0):
        index_value = StaticEstimationOpening(board)
        return index_value
    else:
        index_value = math.inf
        L = GenerateAddBlack(board)
        for l in L:
            child_value = MaxMin(l, ply - 1, a, b)
            nodes_visited.append(l)
            nodes_level.append(ply-1)
            nodes_estimates.append(child_value)

            if (child_value <= index_value):
                index_value = child_value

            if (index_value <= a):
                return index_value
            else:
                b = min(index_value, b)

        return index_value

my_index = MaxMin(board1, d, -10000000, 10000000)


#print(nodes_visited)
#print(nodes_level)
#print(nodes_estimates)

action = ""
flag1 = True
for i in range(len(nodes_estimates)):

    if ((nodes_level[i] == (d - 1)) and (nodes_estimates[i] == my_index) and (flag1 == True)):
        #print(i)
        action = nodes_visited[i]
        flag1 = False

count_nodes = 0
for i in range(len(nodes_level)):
    if (nodes_level[i] == 0):
        count_nodes += 1

print("Input position: " + board1 + " Output position: " + action)
print("Positions evaluated by static estimation: " + str(count_nodes) + ".")
print("Alpha-Beta Pruning estimate: " + str(my_index) + ".")


output1 = open(output_name, "w")
output1.write(action)
output1.close()

print("--- %s seconds ---" % (time.time() - start_time))