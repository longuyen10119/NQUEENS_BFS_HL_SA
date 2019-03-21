import matplotlib.pyplot as plt
import random
import time
import numpy as np
from copy import deepcopy
import math

iterations = []
values = []
K = 1000
T = 100
alpha = 0.9


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
                prob = math.exp(-(current.value - newNeighbor.value) / T*1500)
                gen = np.random.rand(1, 1)
                pick = gen[0]
                if pick < prob:
                    current = newNeighbor
        T = alpha * T
