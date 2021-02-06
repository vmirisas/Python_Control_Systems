import control as co

s = co.tf('s')
g1 = 1 / ((s + 1) * (s - 1))
g2 = 1 / (s + 2)
g3 = (0.5 * s) / (3 * s ** 2 + 5 * s + 1)

g12 = co.parallel(g1, g2)
g123 = co.feedback(g12, g3, 1)
gtot = co.series(g123, g3)
print(gtot)
