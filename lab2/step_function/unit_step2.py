import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(50)
y = np.ones(50)
step = np.append(x,y)
t = np.arange(0, 10, 0.1)
plt.ylabel('u(t)')
plt.xlabel('t')
plt.suptitle('Unit Step Function')
plt.grid(True, linestyle='--', color='lightgrey')
stepfig = plt.step(t,step)
plt.xticks(np.arange(0, 11, 1))
plt.show()