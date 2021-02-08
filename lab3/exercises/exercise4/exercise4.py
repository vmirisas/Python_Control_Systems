import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def pend(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t) * np.exp(-2 * t)) / 10]
    return dudt


u0 = [0, 0]

t = np.linspace(0, 100, 1000)

sol = odeint(pend, u0, t)
plt.figure(1)

plt.plot(t, sol[:, 0], 'b')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.xticks(np.arange(0, 101, 20))


plt.xlim(0, 60)
plt.grid()

plt.figure(2)
plt.plot(sol[:, 0], sol[:, 1])
plt.grid()
plt.show()
