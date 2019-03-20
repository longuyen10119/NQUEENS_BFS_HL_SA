# E -> E1, E2, E3, E4
# if E' is better E
#   current = E
# but if worse:
#   accept P = e to the power of -(E-E')/T
import matplotlib.pyplot as plt
import random
import time
import numpy as np
from copy import deepcopy
import math

iterations = []
values = []
K = 10000
T = 10000
alpha = 0.9


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
        # Invert theses values so Higher would mean better
        # 1/(h+1)
        self.value = 1 / (self.value + 1)
        return self.value

    def pickNextRandomNeighbor(self):
        pickRow = np.random.randint(low=0, high=len(self.board))
        current = self.board[pickRow]
        pickCol = np.random.randint(low=0, high=len(self.board))

        while pickCol == current:
            pickCol = np.random.randint(low=0, high=len(self.board))
        # Maybe no need to deep copy self.board
        aboard = deepcopy(self.board)
        aboard[pickRow] = pickCol
        newNeighbor = Board(aboard)
        return newNeighbor


def SA(board):
    global T
    while True:
        current = board
        for i in range(0, K):
            values.append(current.value)
            if current.value == 1:
                return current
            newNeighbor = current.pickNextRandomNeighbor()
            if current.value <= newNeighbor.value:
                current = newNeighbor
            else:
                prob = math.exp(-(current.value - newNeighbor.value) / T*10000)
                gen = np.random.rand(1, 1)
                pick = gen[0]
                if pick < prob:
                    current = newNeighbor
        T = alpha * T


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


def main():
    print("SIMULATED ANNEALING FOR N QUEENS PROBLEM")
    # N = int(input("Enter N: "))
    N = 4
    initialBoard = Board(N)
    print(initialBoard.board)

    SA(initialBoard)

    iterations = np.arange(len(values))
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.plot(iterations, values, linewidth=0.5)
    plt.show()


main()
