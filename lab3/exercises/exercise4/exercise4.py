import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def pend(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t) * np.exp(-2 * t)) / 10]
    return dudt


# u0 = [1, 2]
u0 = [0, 0]

t = np.linspace(0, 40, 1000)

sol = odeint(pend, u0, t)
plt.figure(1)
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.plot(t, sol[:, 1], 'r', label='y(t)')

plt.xlabel('t')

plt.xticks(np.arange(0, 101, 20))
plt.xlim(0, 60)
plt.grid()

plt.figure(2)
plt.plot(sol[:, 0], sol[:, 1], 'r', label='y(t)')
plt.grid()
plt.show()
