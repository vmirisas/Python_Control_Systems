import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 4, 8, 10])
y = np.array([0, 0, 2, 0])

plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Square Pulse')
plt.grid(True, linestyle='--', color='lightgrey')
square = plt.step(x, y)
plt.xticks(np.arange(0, 11, 1))
plt.xlim(0, 10)
plt.show()
