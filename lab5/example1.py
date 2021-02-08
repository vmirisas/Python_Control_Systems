import control as co
import matplotlib.pyplot as plt

s = co.tf('s')
g = (s + 4) / (7 * s ** 2 + 3 * s - 1)

g_poles = co.pole(g)
g_zeros = co.zero(g)

print('poles')
for elem in g_poles:  # print poles as a column vector for convenience
    print(f'{elem: .2f}')  # Two floating points per print

print('zeros')
for elem in g_zeros:
    print(f'{elem: .2f}')

g_map = co.pzmap(g, plot=True)
plt.show()
