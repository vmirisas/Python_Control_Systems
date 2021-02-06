import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(0, 1, 100)
t2 = np.linspace(1, 2, 100)
t3 = np.linspace(2, 3, 100)
t4 = np.linspace(3, 4, 100)

y1 = t1
y2 = np.ones(len(t2))
y3 = 3 - t3
y4 = np.zeros(len(t4))

y = np.append(np.append(y1, y2), np.append(y3, y4))
t = np.append(np.append(t1, t2), np.append(t3, t4))

plt.ylabel('f(t)')
plt.xlabel('t')
plt.grid(True, linestyle='--', color='lightgrey')
step = plt.step(t, y)
plt.xlim(0, 4)
plt.ylim(-0.2, 1.2)
plt.show()
