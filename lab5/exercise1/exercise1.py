import control as co
import matplotlib.pyplot as plt

s = co.tf('s')
g1 = (s + 2) / (5 * s ** 3 + 7 * s - 3)
g2 = 1 / ((s ** 2 - 3 * s + 4) * (s + 8))

g12s = co.series(g1, g2)
g12p = co.parallel(g1, g2)
g12f = co.feedback(g1, g2, -1)

print(g12s, g12p, g12f)

g1_poles = co.pole(g1)
print("g1 poles")
for elem in g1_poles:
    print(f'{elem: .2f}')

g1_zeros = co.zero(g1)
print("g1 zero")
for elem in g1_zeros:
    print(f'{elem: .2f}')

g2_poles = co.pole(g2)
print("g2 poles")
for elem in g2_poles:
    print(f'{elem: .2f}')

g2_zeros = co.zero(g2)
print("g2 zero")
for elem in g2_zeros:
    print(f'{elem: .2f}')

g12s_poles = co.pole(g12s)
print("g12s poles")
for elem in g12s_poles:
    print(f'{elem: .2f}')

g12p_poles = co.pole(g12p)
print("g12p poles")
for elem in g12p_poles:
    print(f'{elem: .2f}')

g12f_poles = co.pole(g12f)
print("g12f poles")
for elem in g12f_poles:
    print(f'{elem: .2f}')

g12s_zeros = co.zero(g12s)
print("g12s zeros")
for elem in g12s_zeros:
    print(f'{elem: .2f}')

g12p_zeros = co.zero(g12p)
print("g12p zeros")
for elem in g12p_zeros:
    print(f'{elem: .2f}')

g12f_zeros = co.zero(g12f)
print("g12f zeros")
for elem in g12f_zeros:
    print(f'{elem: .2f}')

plt.figure(1)
g1_map = co.pzmap(g1, plot=True)

plt.figure(2)
g2_map = co.pzmap(g2, plot=True)

plt.figure(3)
g12s_map = co.pzmap(g12s, plot=True)

plt.figure(4)
g12p_map = co.pzmap(g12p, plot=True)

plt.figure(5)
g12f_map = co.pzmap(g12f, plot=True)

plt.show()
