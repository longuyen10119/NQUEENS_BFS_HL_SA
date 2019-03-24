# E -> E1, E2, E3, E4
# if E' is better E
#   current = E
# but if worse:
#   accept P = e to the power of -(E-E')/T


# Config 1
# K = 1000
# T = 100
# alpha = 0.9
# prob = * 1500


# Config 2
# K = 10000
# T = 0.1
# alpha = 0.9999
# prob = *1

import matplotlib.pyplot as plt
import random
import time
import numpy as np
from copy import deepcopy
import math

iterations = []
values = []
K = 5000
T = 100
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
        # pick a random number for row
        pickRow = np.random.randint(low=0, high=len(self.board))
        current = self.board[pickRow]
        pickCol = np.random.randint(low=0, high=len(self.board))
        # when picking a random for column
        # make sure to pick a different number
        # from current
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
            # values.append(current.value)
            if current.value == 1:
                return current
            newNeighbor = current.pickNextRandomNeighbor()
            if current.value <= newNeighbor.value:  # when neighbor is better
                current = newNeighbor
            else:
                # accept bad change with a possiblity p
                prob = math.exp(-(current.value - newNeighbor.value) / T*1500)
                gen = np.random.rand(1, 1)
                pick = gen[0]
                if pick < prob:
                    current = newNeighbor
        T = alpha * T

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


def main():
    print("SIMULATED ANNEALING FOR N QUEENS PROBLEM")
    N = int(input("Enter N: "))

    for i in range(4, N+1):
        initialBoard = Board(i)
        start = time.time()
        SA(initialBoard)
        end = time.time()-start
        print('WHEN N = '+str(i), end=' ')
        print('Time taken is {:.4f}'.format(end))

        # Graph Objective values and K iterations
        # iterations = np.arange(len(values))
        # fig = plt.figure(figsize=(18, 10))
        # ax = fig.add_subplot(111)
        # ax.plot(iterations, values, linewidth=0.5)
        # plt.show()


main()
