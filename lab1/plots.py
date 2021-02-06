import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6, 60)
y = np.sin(x)
plt.plot(x, y)
plt.suptitle('Διάγραμμα')  # centered title of the figure
plt.ylabel('y')  # laβel for y axis
plt.xlabel('x')  # label for x axis
plt.grid(True)  # define to show the grid in the plot
plt.axis([0, 6, -1.01, 1.01])  # define plot boundaries
plt.show()
