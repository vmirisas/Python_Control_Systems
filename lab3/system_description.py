import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def system(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y) / 10]
    return dudt


u0 = [1, 2]
t = np.linspace(0, 50, 10000)

sol = odeint(system, u0, t)
plt.figure(1)
plt.plot(t, sol[:, 0], 'b', label='y(t)') # plot y(t)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()

plt.figure(2)
plt.plot(t, sol[:, 1], 'b', label="y'(t)") # plot z(t)=y'(t)
plt.xlabel('t')
plt.ylabel("y'(t)")
plt.grid()
plt.show()
