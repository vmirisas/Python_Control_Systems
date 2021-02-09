import control as co
import matplotlib.pyplot as plt
import numpy as np
from functions.my_functions import step_info

t = np.linspace(0, 10, 100)
s = co.tf('s')
g = (s ** 2 + 4 * s + 1) / (s ** 2 - 7 * s + 10)
siso = co.sisotool(g)

fg = co.feedback(3 * g, sign=-1)
t1, impg = co.impulse_response(fg, t)
t2, stpg = co.step_response(fg, t)

step_info(t2, stpg)

fig, ax = plt.subplots(2,1)
ax[0].plot(t1, impg)
ax[1].plot(t2, stpg)

ax[0].set_ylabel("Impulse Response")
ax[1].set_ylabel("Step Response")
ax[1].set_xlabel("Time")
ax[0].grid()
ax[1].grid()
plt.show()
