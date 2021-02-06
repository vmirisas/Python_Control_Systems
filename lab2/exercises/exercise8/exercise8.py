import matplotlib.pyplot as plt
import numpy as np

t1 = np.linspace(0, 3, 300)
t2 = np.linspace(3, 4, 100)

y1 = np.zeros(len(t1))
y2 = 2 *(t2-3)

t = np.append(t1, t2)
y = np.append(y1, y2)

plt.plot(t, y)
plt.ylabel('y(t)')
plt.xlabel('t')
plt.grid(True, linestyle='--', color='lightgrey')
plt.xlim(0, 4)
plt.show()
