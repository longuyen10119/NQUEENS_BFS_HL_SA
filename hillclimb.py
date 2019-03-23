import random
import time
import numpy as np
from inspect import signature
from copy import deepcopy

# Object Board with a board array
# value attribute


class Board:
    def __init__(self, *argw):
        if isinstance(argw[0], list):
            self.board = deepcopy(argw[0])
        elif isinstance(argw[0], int):
            self.board = list(np.random.randint(
                low=0, high=argw[0], size=argw[0]))
        self.value = -1
        self.calValue()

    def calValue(self):
        # Cost function
        # For cost function we count directly and indirectly attacking queens
        self.value = 0
        for i in range(len(self.board) - 1):
            for j in range(i + 1, len(self.board)):
                # check same column
                if self.board[i] == self.board[j]:
                    self.value += 1
                # check diagonal down left
                if self.board[i] == self.board[j] - (i - j):
                    self.value += 1
                # check diagonal down right
                if self.board[i] == self.board[j] + (i - j):
                    self.value += 1
        return self.value

    def getNeighbors(self):
        # How to generate N**2-N states
        listOfNeighbors = []
        for i in range(len(self.board)):
            l = deepcopy(self.board)
            for j in range(len(self.board)):
                if j != self.board[i]:
                    l[i] = j
                    b = Board(list(l))
                    listOfNeighbors.append(b)
        return listOfNeighbors

# Print board function


def printboard(b):
    board = b.board
    num = len(board)
    for i in range(num):
        for j in range(num):
            if board[i] == j:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()

# Returns the best neighbor from a list of neighbors


def getHighestNeighbor(listOfNeighbor):
    min = 9999999999
    pos = -1
    for i in range(len(listOfNeighbor)):
        if min >= listOfNeighbor[i].value:
            min = listOfNeighbor[i].value
            pos = i
    return listOfNeighbor[pos]

# Hill climbing function


def hillCLimbing(problem):
    current = problem
    while True:
        neighbors = current.getNeighbors()
        neighbor = getHighestNeighbor(neighbors)
        if neighbor.value >= current.value:
            return current
        current = neighbor


def main():
    print("HILL CLIMB FOR N QUEENS PROBLEM")
    N = int(input("Enter N: "))
    initialBoard = Board(N)

    result = []
    start = time.time()

    while True:
        result = hillCLimbing(initialBoard)
        if result.value == 0:
            break
        else:  # restart
            initialBoard = Board(N)

    end = time.time() - start
    print("Time taken: {:.4}".format(end))
    printboard(result)
    print("Value " + str(result.value))


main()
