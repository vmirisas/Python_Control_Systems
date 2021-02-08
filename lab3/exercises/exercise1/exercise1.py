import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pend(u, t):
    y, z = u
    dudt = [z, (-2*z - 5*y)/10]
    return dudt

u0a = [0, 0]
u0b = [0, 1]
u0c = [0, -1]

t = np.linspace(0,50,1000)

sola = odeint(pend, u0a, t)
solb = odeint(pend, u0b, t)
solc = odeint(pend, u0c, t)


print(f"max distance sola = {max(sola[:,0])}")
print(f"max distance solb = {max(solb[:,0])}")
print(f"max distance solc = {min(solc[:,0])}")

fig, (axs1, axs2, axs3) = plt.subplots(3, 1)
axs1.plot(t, sola[:, 0], 'b', label='y(t)')
axs2.plot(t, solb[:, 0], 'b', label='y(t)')
axs3.plot(t, solc[:, 0], 'b', label='y(t)')

plt.xlabel('t')

axs1.set_ylabel("y1")
axs2.set_ylabel("y2")
axs3.set_ylabel("y3")

axs1.grid()
axs2.grid()
axs3.grid()

plt.show()