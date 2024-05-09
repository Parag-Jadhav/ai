N=int(input("Enter the board row/column total nos: "))

board = [[0]*N for i in range(N)]

def isSafe(i,j):
    #check row,column and diagonals
    for p in range(0,N):
        if board[i][p]==1 or board[p][j]==1:
            return False
    for n in range(N):#for checking diagonal
        for m in range(N):
            if i+j==n+m or i-j == n-m:
                if board[n][m]==1:
                    return False
    return True

def nqueen(noq):
    if noq == 0:
        return True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] !=1 and isSafe(i,j):
                board[i][j] = 1
                if nqueen(noq-1) == True:
                    return True
                else:
                    board[i][j]=0
    return False

def printBoard(board):
    for i in board:
        print(i)

if nqueen(N):
    printBoard(board)
else:
    print("Cant place")
