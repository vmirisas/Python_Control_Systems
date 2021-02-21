import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def system(u, t):
    y, z = u
    dudt = [z, (-2 * z - 5 * y + np.sin(t)) / 10]
    return dudt

u0 = [0, 0]

t = np.linspace(0, 100, 10000)

sol = odeint(system, u0, t)

plt.figure(1)
plt.plot(t, sol[:, 0], 'b')
plt.title('Displacement plot')
plt.xlabel('t')
plt.ylabel('y')
plt.xticks(np.arange(0, 101, 20))
plt.xlim(0, 100)
plt.grid()

plt.figure(2)
plt.plot(sol[t>50, 0], sol[t>50, 1])
plt.title('Phase plot for t>50')
plt.xlabel("y(t)")
plt.ylabel("y'(t)")
plt.grid()

plt.show()
