import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 5, 10])
y = np.array([0, 0, 2])
plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Step Function')
plt.grid(True, linestyle='--', color='lightgrey')
step = plt.step(x, y)
plt.xticks(np.arange(0, 11, 1))
plt.xlim(0, 10)
plt.show()
