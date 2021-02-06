import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.ones(len(x))
ramp_function = np.multiply(x, y)
plt.plot(x, ramp_function)
#plt.plot(x, x) #2nd way
plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Ramp Function')
plt.grid(True, linestyle='--', color='lightgrey')
plt.xticks(np.arange(0, 11, 1))
plt.show()
