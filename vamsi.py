import random
import time

names = ["RAM", "AKSHAY", "ANAND", "PRAJAKTA", "SHYAM"]
boardSize = 20
vert, hor, diag = "Vertical", "Horizontal", "Diagonal"
directions = [vert, hor, diag]


def initBoard():
    board = []
    for i in range(0, boardSize):
        row = []
        for j in range(0, boardSize):
            cur = random.choice(range(0, 26))
            row.append(chr(ord('A')+cur)) 
        board.append(row)
    return board

def initAssigned():
    assigned = []
    for i in range(0, boardSize):
        row = []
        for j in range(0, boardSize):
            row.append(0)
        assigned.append(row)
    return assigned


def isPossibleVertical(row, col, name, assigned):
    n = len(name)
    if row+n >= boardSize:
        return False
    for i in range(row, boardSize):
        if(assigned[i][col] == 1):
            return False
    return True

def isPossibleHorizontal(row, col, name, assigned):
    n = len(name)
    if col+n >= boardSize:
        return False
    for i in range(col, boardSize):
        if(assigned[row][i] == 1):
            return False
    return True

def isPossibleDiagonal(row, col, name, assigned):
    n = len(name)
    for i in range(n):
        if(row+i >= boardSize or col+i >= boardSize or assigned[row+i][col+i] == 1):
            return False
    return True
    
def assignNameVertical(row, col, name, board, assigned):
    nameLen = len(name)
    for i in range(row, row+nameLen):
        board[i][col] = name[i-row]
        assigned[i][col] = 1

def assignNameHorizontal(row, col, name, board, assigned):
    nameLen = len(name)
    for i in range(col, col+nameLen):
        board[row][i] = name[i-col]
        assigned[row][i] = 1

def assignNameDiagonal(row, col, name, board, assigned):
    nameLen = len(name)
    for i in range(0, nameLen):
        board[row+i][col+i] = name[i]
        assigned[row+i][col+i] = 1

    
def assignNames(board, assigned):
    for i in range(len(names)):
        curName, curRow, curCol, curDir, found = names[i], 0, 0, 0, 0
        while(1):
            curRow = random.choice(range(0, boardSize))
            curCol = random.choice(range(0, boardSize))
            curDir = random.choice(range(0, len(directions)))

            if(curDir == 0):
                if(isPossibleVertical(curRow, curCol, curName, assigned)):
                    found = 1
                    assignNameVertical(curRow, curCol, curName, board, assigned)
            elif(curDir == 1):
                if(isPossibleHorizontal(curRow, curCol, curName, assigned)):
                    found = 1
                    assignNameHorizontal(curRow, curCol, curName, board, assigned)
            elif(curDir == 2):
                if(isPossibleDiagonal(curRow, curCol, curName, assigned)):
                    found = 1
                    assignNameDiagonal(curRow, curCol, curName, board, assigned)

            if found == 1:
                break
        
            

def printBoard(board):
    for i in board:
        print(*i)

def printSoln(board, assigned):
    for i in range(0, boardSize):
        for j in range(boardSize):
            if(assigned[i][j] == 1):
                print(board[i][j], end = " ")
            else :
                print('*' , end = " ")
        print()

    

board = initBoard()
assigned = initAssigned()
assignNames(board, assigned)

printBoard(board)
time.sleep(10)
print("")
printSoln(board, assigned)
