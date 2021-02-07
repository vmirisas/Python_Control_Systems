import control as co
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 100, 100)
s = co.tf('s')
g1 = 1 / (2 * s ** 7 + 1 * s + 9)
g2 = (3 * s + 2) / (5 * s ** 2 + 3 * s + 7)
g3 = (2 * s) / (6 * s ** 2 + 7)
g4 = (s) / (6 * s + 7)

t1, imp1 = co.impulse_response(g1, t)
t2, imp2 = co.impulse_response(g2, t)
t3, imp3 = co.impulse_response(g3, t)
t4, imp4 = co.impulse_response(g4, t)

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
axs[0, 0].plot(t1, imp1)
axs[0, 1].plot(t2, imp2)
axs[1, 0].plot(t3, imp3)
axs[1, 1].plot(t4, imp4)
plt.show()