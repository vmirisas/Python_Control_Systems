import control as co
import control.matlab
import matplotlib.pyplot as plt

s = co.tf('s')
#g = (s+4)/((s+2)*(s+1))
#g = (s**2+3*s+4)/((s+2)*(s**2+1))
g = (2*s +1)/(s**2 +4*s+8)
g_rlocus = co.matlab.rlocus(g)



plt.show()