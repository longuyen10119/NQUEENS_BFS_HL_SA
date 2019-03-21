import numpy as np

# PROBLEM 11
# P = [100, 80, 60, 70, 60, 75, 85]
# S = [1]
# for i in range(1, len(P)):
#     for j in range(i - 1, -1, -1):
#         current = P[i]
#         back = P[j]
#         if P[i] < P[j]:
#             S.append(i - j)
#             break


# print(S)


# PROBLEM

# pos1 = np.random.randint(low=0, high=10)
# pos2 = np.random.randint(low=0, high=10)

# print(pos1)
# print(pos2)


import math

e1 = 1 / (3 + 1)
e2 = 1 / (4 + 1)
print(e1, e2)
T = 100

result = math.exp(-(e1 - e2) / T*1500)
print(result)
# print(result)
# count = 0
# for i in range(100):
#     gen = np.random.rand(1, 1)
#     pick = gen[0]
#     if pick < result:
#         count += 1
# print(count)
