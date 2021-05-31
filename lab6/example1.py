import control as co
import matplotlib.pyplot as plt

s = co.tf('s')
g1 = (s + 4) / ((s + 2) * (s + 1))
g2 = (s ** 2 + 3 * s + 4) / ((s + 2) * (s ** 2 + 1))
g3 = (2 * s + 1) / (s ** 2 + 4 * s + 8)

plt.figure(1)
g1_rlocus = co.rlocus(g1)
plt.xlim([-8, 0])

plt.figure(2)
g2_rlocus = co.rlocus(g2)
plt.xlim([-2, 1])

plt.figure(3)
g3_rlocus = co.rlocus(g3)
plt.xlim([-4, 0])

plt.show()