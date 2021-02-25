import control as co
import matplotlib.pyplot as plt
import numpy as np
s = co.tf('s')
"""Για οποιοδήποτε κ το σύστημα είναι ευσταθές"""
#g = ((s + 1) * (s + 4)) / (s ** 2 + 5 * s + 6)

"""Για περίπου κ=0.5 ο πραγματικός πόλος με του μιγαδικούς
 αλλάζουν μεριά, οπότε το σύστημα δεν είναι σταθεροποιήσιμο"""
g= (s-2)/(s**3+2*s+1)
#fg = co.feedback(0.5*g,sign=-1)
#gpz = co.pzmap(fg)


#g = (s-2)*((s**2)+2)/((s-3)*(s+1)) #????

print(g)
#gpz = co.pzmap(g)
locus = co.root_locus(g)



"""print(g_rlocus)
print(klist)"""
plt.show()
