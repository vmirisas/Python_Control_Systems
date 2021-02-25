import control as co
import matplotlib.pyplot as plt
import numpy as np

s = co.tf('s')
g = 1 / ((s + 1) * (s + 2))

print(co.pole(g))

# pole zero map
g_map = co.pzmap(g, plot=True)
plt.show()

# impulse response
ts = np.linspace(0, 20, 101)
t, y = co.impulse_response(g, ts)

# impulse response plot
plt.plot(t,y)
plt.title('Impulse Response')
plt.xlabel('time')
plt.ylabel('amplitute')
plt.show()