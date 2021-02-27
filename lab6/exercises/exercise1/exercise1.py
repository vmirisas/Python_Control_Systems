import control as co
import matplotlib.pyplot as plt
import numpy as np
s = co.tf('s')
"""Για οποιοδήποτε κ το σύστημα είναι ευσταθές"""
plt.figure(1)
g1 = ((s + 1) * (s + 4)) / (s ** 2 + 5 * s + 6)
co.root_locus(g1, grid=False)
"""Για περίπου κ=0.5 ο πραγματικός πόλος με του μιγαδικούς
 αλλάζουν μεριά, οπότε το σύστημα δεν είναι σταθεροποιήσιμο"""
plt.figure(2)
g2= (s-2)/(s**3+2*s+1)
co.root_locus(g2, grid=False)

plt.figure(3)
g3 = (s-2)*((s**2)+2)/((s-3)*(s+1))
rlist, klist = co.root_locus(g3,kvect=np.linspace(0.1,10,5001), grid=False)

plt.show()
