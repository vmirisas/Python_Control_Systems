import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def pend(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t) * np.exp(-2 * t)) / 10]
    return dudt


# u0 = [1, 2]
u0 = [0, 0]

t = np.linspace(0, 100, 1000)

sol = odeint(pend, u0, t)

plt.plot(t, sol[:, 0], 'b', label='y(t)')
# fig, (axs1, axs2) = plt.subplots(2, 1)
# axs1.plot(t, sol[:, 0], 'b', label='y(t)')
# axs2.plot(t, sol[:, 1], 'r', label="y'(t)")

# plt.plot(t, sola[:, 0], 'b', label='y(t)')
plt.xlabel('t')

# axs1.set_ylabel("y(t)")
# axs2.set_ylabel("y'(t)")
# axs2.yaxis.set_major_formatter(FormatStrFormatter('%.2f')) # format the second y axis numbers
plt.xticks(np.arange(0, 101, 20))
plt.xlim(0, 100)
plt.grid()
plt.show()
