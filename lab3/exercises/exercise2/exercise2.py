import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(u, t, k):
    y, z = u
    dudt = [z, (-2*z - k*y)/10]
    return dudt

#u0 = [1, 2]
u0 = [0, 1]



t = np.linspace(0,50,10000)

k = 5
sol1 = odeint(pend, u0, t, args=(k,))
k = 15
sol2 = odeint(pend, u0, t, args=(k,))


fig, (axs1, axs2) = plt.subplots(2, 1)
axs1.plot(t, sol1[:, 0], 'b', label='y(t)')
axs2.plot(t, sol2[:, 0], 'b', label='y(t)')


#plt.plot(t, sola[:, 0], 'b', label='y(t)')
plt.xlabel('t')

axs1.set_ylabel("y1")
axs2.set_ylabel("y2")


axs1.grid()
axs2.grid()


plt.show()