import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

l1 = len(np.linspace(0, 4, 40, endpoint=False))
l2 = len(np.linspace(4, 8, 40, endpoint=False))
l3 = len(np.linspace(8, 10, 20))
y1 = np.zeros(l1)
y2 = np.ones(l2)
y3 = np.zeros(l3)
y12 = np.append(y1, y2)
y = np.append(y12, y3)
plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Square Pulse')
plt.grid(True, linestyle='--', color='lightgrey')
square = plt.step(x, y)
plt.xticks(np.arange(0, 11, 1))
plt.show()
