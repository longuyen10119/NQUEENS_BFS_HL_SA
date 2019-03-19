

# Find ALL solutions to the N-queen
# problem using the Breadth-First-Search (BFS) algorithm, for N=1 up to 20. (20 mark)
# o For N=1 to 6, you need to list all the solutions.
# o For N=7 to 20, returns only the number of solutions.
#  Record the time taken to find all solutions for N=1 to 20. (10 mark)
#  Based on the results you obtained for N=1 to 20, predict the number of solutions and the
# time needed to obtain the solutions for N = 30. Show how you do that clearly. (10 mark)
#  Suggest a way to prune the search tree of the BFS to speed up the computation. (10 mark)


global N
N = 4

# Board printing solution


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

# --------- Utility function to check in a queen is safe to be put in place


def isSafe(board, row, col):

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True


# --------- Solve using backtracking
def solveNQueenUtil(board, col):
    # if all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i,  col):
            board[i][col] = 1

        # recur to place the rest of the queens
        if solveNQueenUtil(board, col+1):
            return True

        # if placing queen in board[i][col] is not good
        # then set to 0
        board[i][col] = 0

    # if the queen cannot be placed in any row in this column
    # returns false
    return False


def solveNQ():

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solveNQueenUtil(board, 0) == False:
        print("solution doesn't exit")
        return False

    printSolution(board)
    return True


# Driver
solveNQ()
