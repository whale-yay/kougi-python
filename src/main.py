import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(tight_layout=True)

ax = fig.add_subplot(1, 2, 1)
ax.plot([-np.pi/4, -np.pi/4, np.pi/4, np.pi/4], [0, 1, 1, 0])
ax.set_xlabel("Frequency $\omega$ [rad]")
ax.set_ylabel("$|X(e^{j\omega})|$")
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(0, 1.5)
ax.grid()

n = np.arange(-20, 20, 1)
wc = np.pi/4
x = (wc/np.pi)*np.sinc(n*wc/np.pi)
ax = fig.add_subplot(1, 2, 2)
ax.stem(n, x)
ax.set_xlim(-20, 20)
ax.set_ylim(-0.1, 0.3)
ax.set_xlabel("TIME $n$")
ax.set_ylabel("$x[n]$")
ax.grid()

fig.savefig("yeah.png")
