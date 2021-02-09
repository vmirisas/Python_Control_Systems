import control as co
import matplotlib.pyplot as plt
import numpy as np

s = co.tf('s')
g = (s**2+5*s+4)/(s**2-5*s-24)
"""a) οχι ευσταθές"""
print(co.pole(g))
co.root_locus(g, ylim=(-0.25, 0.25))

"""b) απο root_locus μια καλή 
τιμή για ευστάθεια είναι k=8"""
g_gained = co.feedback(8 * g, sign=-1)
plt.figure(2)
#co.root_locus(g_gained, ylim=(-0.025, 0.025))

"""c)  """
print(g_gained)
co.pzmap(g_gained)
plt.show()