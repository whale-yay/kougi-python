import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(tight_layout=True)
a = np.array([-2, -1, -0.5, 0.5, 1, 2])
n = np.arange(-5, 10, 1)
u = np.ones(len(n))
u[n < 0] = 0

for i, a_i in enumerate(a):
    x = np.empty(len(n))
    for j, n_i in enumerate(n):
        x[j] = a_i ** n_i
    ax = fig.add_subplot(3, 2, i + 1)
    ax.stem(n, x, use_line_collection=True)
    ax.set_ylabel('x(n)')
    ax.set_xlabel('Time n a =' + str(a_i))
    ax.grid()

fig.savefig("img.png")
