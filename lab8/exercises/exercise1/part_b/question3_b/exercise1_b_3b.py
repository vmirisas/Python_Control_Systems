import control as co
import matplotlib.pyplot as plt
import numpy as np

from functions.my_functions import step_info

""" Συνάρτηση κατασκευής lead compensator
    input(θέσεις ενός πραγματικού μηδενικού και ενός πραγματικού πόλου)
    με αυτά κατασκευάζει τα πολυώνυμα μετά την προσθήκη των ο,x 
    returns (C(s) με αυτά κατασκευάζει) 
"""
def pd_comp(szero):
    cz1 = 1 + (s / (-szero))

    return cz1

def plot_ts(TS):
    plt.axvline(-4 / TS, color='r', linestyle='--')

s = co.tf('s')

g = (s+1)/((s-1)*(s-4))
h1 = 1
h2 = 1/(s-1)


#b)
k = 60
gf = co.feedback(k*pd_comp(-4.4)*g, h2, -1) # υπολογίζω τους πόλου και τα μηδενικά του κλειστού συστήματος με Κ = 60 και feedback=h2
poles = co.pole(gf)
zeros = co.zero(gf)
print(f"poles: {poles}")
print(f"zeros: {zeros}")

plt.figure(1)
co.root_locus(pd_comp(-4.4)*g*h2, grid=False) # σχεδιάζω την γραφική παράστασή μου με pd_compensator
plot_ts(2)
plt.xlim(-15,5)

plt.plot(poles.real, poles.imag, 'rx')

t = np.linspace(0,3,1000)
t1, yout = co.step_response(gf, t)
step_info(t1, yout)

plt.show()
