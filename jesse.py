import numpy as np
import math
import copy
import time
import collections


# ------------------------
# Breadth-first Search
# function
# ------------------------
def bfs(board, n):
    # -----------------------
    # Deque meant to act as
    # a queue - FIFO
    # -----------------------
    movesMade = collections.deque()
    updateBoard = []

    # TODO: Do Breadth-first Search: if n=1-6 print number of solutions &
    # and visual graph, Else if n=7-20 only print number of solutions

    # ------------------------------
    # for loop to place Queen in
    # every spot in i=0 and add
    # to deque/queue movesMade
    # ------------------------------

    i = 0
    for j in range(len(board[i])):
        if board[i][j] == '-':
            board[i][j] = 'Q'
            movesMade.append(copy.deepcopy(board))
            board[i][j] = '-'

    # --------------------------------------------
    # While loop to pop deque/queue and
    # update the board with new placement
    # of queen in the following i then
    # adding it back to deque/queue. Effectively
    # making a breadth first search tree
    # --------------------------------------------
    while i < n-1:
        k = 0
        i += 1
        while k < pow(n, i+1):
            updateBoard = movesMade.popleft()
            for j in range(len(updateBoard[i])):
                if updateBoard[i][j] == '-':
                    updateBoard[i][j] = 'Q'
                    movesMade.append(copy.deepcopy(updateBoard))
                    updateBoard[i][j] = '-'
                # else:
                #     break
                k += 1

    return movesMade


def bfsPrunning(board, n):
    # -----------------------
    # Deque meant to act as
    # a queue - FIFO
    # -----------------------
    movesMade = collections.deque()
    updateBoard = []
    i = 0

    # ------------------------------
    # for loop to place Queen in
    # every spot in i=0 and add
    # to deque/queue movesMade
    # ------------------------------
    for j in range(len(board[i])):
        if board[i][j] == '-':
            board[i][j] = 'Q'
            movesMade.append(copy.deepcopy(board))
            board[i][j] = '-'

    # --------------------------------------------
    # While loop to pop deque/queue and
    # update the board with new placeme4nt
    # of queen in the following i then
    # adding it back to deque/queue. Effectively
    # making a breadth first search tree
    # --------------------------------------------
    while i < n-1:
        k = 0
        i += 1
        temp = len(movesMade)
        check = n*temp
        count = 0
        while k < check:
            updateBoard = movesMade.popleft()
            for j in range(len(updateBoard[i])):
                if updateBoard[i][j] == '-':
                    updateBoard[i][j] = 'Q'
                    if isMoveValid(updateBoard, n) is True:
                        count += 1
                        movesMade.append(copy.deepcopy(updateBoard))
                    updateBoard[i][j] = '-'
                k += 1

    return movesMade


# -----------------------
# Hill-climbing Search
# function
# -----------------------
def hcs(grid):
    # TODO: Do Hill-climbing Search: If n<=8 print visual Else print
    # Number of solutions
    return something

# ----------------------
# Simulated-anneling
# Search
# ----------------------


def sa(grid):
    # TODO: Simulated-anneling Search: If n<=8 print visual Else print
    # Number of solutions
    return something

# -----------------------------------
# Function to determine the distance
# to solution
# -----------------------------------


def cost():

    # TODO: Cost function determining the distance to solutions

    return distance


def isMoveValid(boardToCheck, n):
    for y in range(len(boardToCheck)):
        for x in range(len(boardToCheck[y])):
            if boardToCheck[y][x] == 'Q':  # Found a queen

                # ----------------------
                # Check for column up
                # ----------------------
                for j in range(y+1, n):
                    if boardToCheck[j][x] == 'Q':
                        return False

                # --------------------------
                # Check Diagonal Left up
                # --------------------------
                for a, b in zip(range(x-1, -1, -1), range(y+1, n, 1)):
                    if boardToCheck[b][a] == 'Q':
                        return False

                # -----------------------------
                # Check Diagonal Right up
                # -----------------------------
                for a, b in zip(range(x+1, n), range(y+1, n, 1)):
                    if boardToCheck[b][a] == 'Q':
                        return False

    return True


def vetForSolution(checkBoard, n):

    if n == 1:
        return True

    else:
        for y in range(len(checkBoard)):
            for x in range(len(checkBoard[y])):
                if checkBoard[y][x] == 'Q':  # Found a queen

                    # ----------------------
                    # Check for column down
                    # ----------------------
                    for j in range(y+1, n):
                        if checkBoard[j][x] == 'Q':
                            return False

                    # --------------------------
                    # Check Diagonal Left Down
                    # --------------------------
                    for a, b in zip(range(x-1, -1, -1), range(y+1, n, 1)):
                        if checkBoard[b][a] == 'Q':
                            return False

                    # -----------------------------
                    # Check Diagonal Right Down
                    # -----------------------------
                    for a, b in zip(range(x+1, n), range(y+1, n, 1)):
                        if checkBoard[b][a] == 'Q':
                            return False

        return True

# ------------------------
# Main Function asking
# for the initial input
# ------------------------


def main():

    board = []
    solutions = []
    i = 0

    # -----------------------
    # Made to test different
    # inputs from user
    # -----------------------
    print("Please enter number for grid")
    n = int(input())

    # -----------------------
    # Builds the board needed
    # based on n
    # -----------------------
    board = np.full((n, n), '-')


# -------------------------------------------
# TODO: Make a switch case for selecting
#      which search we will use and print
#      solution
# -------------------------------------------

    print("""
    (1)For Breadth First Search\n
    (2)For Breadth First Search with pruning\n
    (3)For Hill Climbing\n
    (4)For Simulated Annealing\n""")

    # -----------------------
    # Start time to solution
    # -----------------------
    start = time.time()
    time.process_time()

    x = int(input())
    while x < 5 and x > 0:
        # -------------------------
        # Part A: Do breadth first
        # search add it to tree
        # -------------------------
        if x == 1:
            movesMade = bfs(board, n)

            # for y in range(len(movesMade)):
            #     possibleSolution = movesMade.popleft()

            #     if vetForSolution(possibleSolution, n) is True:
            #         solutions.append(copy.deepcopy(possibleSolution))

            for m in movesMade:
                if vetForSolution(m, len(m)):
                    solutions.append(m)

        # ----------------------------
        # Part A(b): Do breadth first
        # search with Prunning
        # ----------------------------
        elif x == 2:
            solutionPrunning = bfsPrunning(board, n)
            for y in range(len(solutionPrunning)):
                solutions.append(copy.deepcopy(solutionPrunning))

        # ----------------------------
        # Part B: Do Hill Climbing
        # search
        # ----------------------------
        elif x == 3:
            # ----------------------------
            # TODO: Make Case for Part B
            #       Hill climbing Search
            # ----------------------------
            # All possiblities from current state:
            # Pick one of the best states and then update state
            # and repeat

            '''
            Pseudocode For Hill climbing
            X = Intial configuration
            Iterate
            1. E = Eval(x)
            2. N = Neighbors(x)
            3. For each Xi in N
            Ei = Eval(Xi)
            4. if all Ei's are lower than E
            return x
            else
            i* = argmax(Ei)
            X= Xi
            E = Ei
            '''
            return
        # ----------------------
        # Part B: Do Simulated
        # Annealing
        # ----------------------
        elif x == 4:
            # ----------------------------
            # TODO: Make Case for Part B
            #       Simulated Annealing
            #       Search
            # ----------------------------
            return
        else:
            print("Invalid selection. Closing program")
        break

    # ----------------------------
    # Print every branch of tree
    # ----------------------------
    if len(solutions) > 0:
        for i in range(len(solutions)):
            for j in range(len(solutions[i])):
                print("This j: ", j, solutions[i][j], end=" ")
                print()
            print()
        print("Number for Solutions: ", i+1)

    else:
        print("There are NO solutions")

    # -----------------------------
    # Time that taken to solution
    # -----------------------------
    elapsed = time.time() - start
    math.ceil(elapsed)
    print("Time from start to solution: ", round(elapsed, 1))


if __name__ == "__main__":
    main()
