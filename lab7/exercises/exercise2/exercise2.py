import control as co
import numpy as np
import matplotlib.pyplot as plt


s = co.tf('s')
g = (s + 1) / (s ** 3 + 6 * s - 5)
plt.figure(1)
co.pzmap(g)
# siso = co.sisotool(g)
k = 11
z = -1
cs = k * (s - z)
"""Δοκιμάζοντας τιμές για μηδενικά, προσθέτω μόνο ένα πραγματικό μηδενικό, άρα το cs θα έχει 
πολυώνυμο στο αριθμητή και 1 στον παρονομαστή"""

g_feedback = co.feedback(co.series(g, cs), 1, sign=-1)
plt.figure(2)
co.pzmap(g_feedback)
plt.show()


