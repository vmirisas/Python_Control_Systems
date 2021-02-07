import control as co
import matplotlib.pyplot as plt


def get_poles(system):
    poles = system[0]
    return poles

def get_zeros(system):
    zeros = system[1]
    return zeros


s = co.tf('s')
g1 = (s + 2) / (5 * s ** 3 + 7 * s - 3)
g2 = 1 / ((s ** 2 - 3 * s + 4) * (s + 8))

g12s = co.series(g1, g2)
g12p = co.parallel(g1, g2)
g12f = co.feedback(g1, g2, -1)

print(g12s, g12p, g12f)


plt.figure(1)
g1_map = co.pzmap(g1, plot=True)
print(f"poles\zeros g1= {g1_map}")

plt.figure(2)
g2_map = co.pzmap(g2, plot=True)
print(f"poles\zeros g2= {g2_map}")

plt.figure(3)
g12s_map = co.pzmap(g12s, plot=True)
print(f"poles\zeros g12s= {g12s_map}")

plt.figure(4)
g12p_map = co.pzmap(g12p, plot=True)
print(f"poles\zeros g12p= {g12p_map}")

plt.figure(5)
g12f_map = co.pzmap(g12f, plot=True)
print(f"poles\zeros g12f= {g12f_map}")

plt.show()
