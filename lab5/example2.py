import control as co

s = co.tf('s')
g1 = 1/((s+1)*(s-1))
g2 = 1/(s+2)
g3 = (0.5*s)/(3*s**2+5*s+1)
print(g)

g12 = co.parallel(g1,g2)
g123 = co.feedback(g12,g3,-1)
g = co.series(g123,g3)
gtot = co.series(co.feedback(co.parallel(g1,g2),g3,-1),g3)
print(g, gtot)
