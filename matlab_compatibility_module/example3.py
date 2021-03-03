import control as co
import matplotlib.pyplot as plt
import numpy as np
from control import matlab

s = co.tf('s')
g1 = ((4 * s ** 2 - 3) * (6 * s + 8)) / ((6 * s ** 3 - 2 * s ** 2 + 9) * (s ** 2 + 8))
print(g1)
t = np.linspace(0, 200, 1000)

imp, t1  = co.matlab.impulse(g1, t)
stp, t2  = co.matlab.step(g1, t)
plt.grid()
plt.figure(1)
plt.plot(t1,imp)

plt.figure(2)
plt.grid()
plt.plot(t2, stp)
plt.show()