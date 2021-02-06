import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(u, t):
    y, z = u
    dudt = [z, (-2*z - 5*y)/10]
    return dudt

u0 = [1, 2]
t = np.linspace(0,50,10000)

sol = odeint(pend, u0, t)

plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')

plt.grid()
plt.show()