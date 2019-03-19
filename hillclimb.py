import random
import time
import numpy as np
from inspect import signature
from copy import deepcopy


class Board:
    def __init__(self, *argw):
        if isinstance(argw[0], list):
            self.board = deepcopy(argw[0])
        elif isinstance(argw[0], int):
            self.board = np.random.randint(low=0, high=argw[0], size=argw[0])
        self.value = -1
        self.calValue()

    def calValue(self):
        # Cost function
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


def getHighestNeighbor(listOfNeighbor):
    min = -1
    pos = -1
    for i in range(len(listOfNeighbor)):
        if min > listOfNeighbor[i].value:
            min = listOfNeighbor[i].value
            pos = i
    return listOfNeighbor[pos]


def hillCLimbing(problem):
    current = problem
    while True:
        neighbors = current.getNeighbors()
        neighbor = getHighestNeighbor(neighbors)
        if neighbor.value >= current.value:
            return current
        current = neighbor


def main():
    N = 4
    initialBoard = Board(N)
    print("Start state")
    print(initialBoard.board)

    result = hillCLimbing(initialBoard)
    print("Finish")
    print(result.board)
    printboard(result)


main()

