import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def pend(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t)) / 10]
    return dudt

u0 = [0, 0]

t = np.linspace(0, 100, 1000)

sol = odeint(pend, u0, t)

plt.plot(t, sol[:, 0], 'b', label='y(t)')


plt.xlabel('t')

plt.xticks(np.arange(0, 101, 20))
plt.xlim(0, 100)
plt.grid()
plt.show()

# system balance
akr = sol[sol[:, 1] == 0, 0]

print(akr)
