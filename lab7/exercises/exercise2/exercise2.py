import control as co
import matplotlib.pyplot as plt

s = co.tf('s')
g = (s + 1) / (s ** 3 + 6 * s - 5)

plt.figure(1)
siso = co.sisotool(g)

plt.figure(2)
co.pzmap(g)

# control function
k = 11
z = -1
cs = k * (s - z)
"""Δοκιμάζοντας τιμές για μηδενικά, προσθέτω μόνο ένα πραγματικό μηδενικό, άρα το cs θα έχει 
πολυώνυμο στο αριθμητή και 1 στον παρονομαστή"""

# the controlled system
g_feedback = co.feedback(co.series(g, cs), 1, sign=-1)
print(g_feedback)

# pole zero plot of the closed controlled system
plt.figure(3)
co.pzmap(g_feedback)
plt.show()
