import matplotlib.pyplot as plt


fig = plt.figure(figsize=(18, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
n = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
time = [0.000211, 0.0003841, 0.001206, 0.004196,
        0.01247, 0.03757, 0.1614, 1.564, 29.29, 1311]
numSolu = [2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712]

ax1.title('')
ax1.plot(n, time)
ax2.plot(n, numSolu)
plt.show()
