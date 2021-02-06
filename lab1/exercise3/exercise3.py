import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,4,0.1)
y = np.cos(2*x) + np.power(np.sin(x), 2) + 5

plt.plot(x,y)
plt.suptitle('Συνάρτηση')
plt.ylabel('y')
plt.xlabel('x')
plt.show()