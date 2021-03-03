import control.matlab
import control as co

s = co.matlab.tf('s')
g1 = 1/((s+1)*(s-1))
g2 = 1/(s+2)
g3 = (0.5*s)/(3*s**2+5*s+1)


g12 = co.matlab.parallel(g1,g2)
g123 = co.matlab.feedback(g12,g3,-1)
g = co.matlab.series(g123,g3)
gtot = co.matlab.series(co.matlab.feedback(co.matlab.parallel(g1,g2),g3,-1),g3)
print(g, gtot)