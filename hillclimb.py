import random
import time
import numpy as np

N = 5

# Making only 57 states every move

# make initial state
initial = np.random.randint(low=1, high=N, size=N)


def hillCLimbing(problem):
    current = problem
    while True:
        print()
