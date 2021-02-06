import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(0, 1, 100)
t2 = np.linspace(1, 2, 100)
t3 = np.linspace(2, 5, 300)
t4 = np.linspace(5, 6, 100)

y1 = np.zeros(len(t1))
y2 = -2+2*t2
y3 = 4 - t3
y4 = np.ones(len(t4))* -1

t = np.append(np.append(t1, t2), np.append(t3, t4))
y = np.append(np.append(y1, y2), np.append(y3, y4))

plt.ylabel('f(t)')
plt.xlabel('t')
plt.grid(True, linestyle='--', color='lightgrey')
step = plt.step(t, y)
plt.xlim(0, 6)
plt.ylim(-2, 2.5)
plt.show()
