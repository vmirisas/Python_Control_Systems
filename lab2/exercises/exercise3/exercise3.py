import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 1000)
f = np.exp(-t) * np.sin(3 * t)

plt.ylabel('f(t)')
plt.xlabel('t')
plt.suptitle('Damped Oscillation')
plt.grid(True, linestyle='--', color='lightgrey')
step = plt.step(t, f)
plt.xticks(np.arange(0, 11, 1))
plt.xlim(0, 10)
plt.show()
