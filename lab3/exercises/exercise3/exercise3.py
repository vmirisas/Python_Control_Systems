import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def pend(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t)) / 10]
    return dudt


# u0 = [1, 2]
u0 = [0, 0]

t = np.linspace(0, 100, 1000)

sol = odeint(pend, u0, t)

plt.plot(t, sol[:, 0], 'b', label='y(t)')
# axs1.plot(t, sol[:, 0], 'b', label='y(t)')
# axs2.plot(t, sol[:, 1], 'r', label="y'(t)")

# plt.plot(t, sola[:, 0], 'b', label='y(t)')
plt.xlabel('t')

# axs1.set_ylabel("y(t)")
# axs2.set_ylabel("y'(t)")

# axs1.grid()
# axs2.grid()
plt.xticks(np.arange(0, 101, 20))
plt.xlim(0, 100)
plt.grid()
plt.show()

# system balance
akr = sol[sol[:, 1] == 0, 0]
print(akr)
