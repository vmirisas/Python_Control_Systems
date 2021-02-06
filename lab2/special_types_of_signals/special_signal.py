import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 15, 0.1)
r = np.arange(5, 10, 0.1)
u1 = np.zeros(50)
u2 = np.sin(3 * r)
u3 = np.zeros(50)

u12 = np.append(u1, u2)
u = np.append(u12, u3)

plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Special Case')
plt.grid(True, linestyle='--', color='lightgrey')
plt.axis([0, 15, -1, 1])
plt.xticks(np.arange(0, 16, 1))
plt.plot(t, u)
plt.show()
