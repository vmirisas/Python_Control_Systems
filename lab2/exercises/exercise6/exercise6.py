import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(0, 2, 200)
t2 = np.linspace(2, 4, 200)
t3 = np.linspace(4, 6, 200)
y1 = t1
y2 = np.ones(len(t2)) * 2
y3 = 6-t3
y12 = np.append(y1, y2)
y = np.append(y12, y3)
t12 = np.append(t1, t2)
t = np.append(t12, t3)

plt.ylabel('f(t)')
plt.xlabel('t')
plt.grid(True, linestyle='--', color='lightgrey')
step = plt.step(t, y)
plt.xlim(0, 6)
plt.ylim(-0.1, 2.5)
plt.show()
