import control as co
import matplotlib.pyplot as plt
import numpy as np

from functions.my_functions import step_info

""" Συνάρτηση κατασκευής lead compensator
    input(θέσεις ενός πραγματικού μηδενικού και ενός πραγματικού πόλου)
    με αυτά κατασκευάζει τα πολυώνυμα μετά την προσθήκη των ο,x 
    returns (C(s) με αυτά κατασκευάζει) 
"""


def lead_comp(spole, szero):
    cz = 1 + (s / (-szero))
    cp = 1 / (1 + (s / (-spole)))
    return cz * cp


def plot_ts(TS):
    plt.axvline(-4 / TS, color='r', linestyle='--')


s = co.tf('s')

g = (s + 1) / ((s - 1) * (s - 4))
h1 = 1
h2 = 1 / (s - 1)

# b)
k = 150
gf = co.feedback(k * lead_comp(-60, -10) * g, h2, -1)  # υπολογίζω τους πόλου και τα μηδενικά του κλειστού συστήματος με Κ = 120 και feedback=h2
poles = co.pole(gf)
zeros = co.zero(gf)
print(poles, zeros)

plt.figure(1)
co.root_locus(lead_comp(-60, -10) * g * h2, grid=False)  # σχεδιάζω την γραφική παράστασή μου με lead_compensator
plot_ts(2)
plt.plot(poles.real, poles.imag, 'rx')
plt.plot(zeros.real, zeros.imag, 'ro')

plt.figure(2)
t = np.linspace(0, 3, 1000)
t1, yout = co.step_response(gf, t)

step_info(t1, yout)
plt.plot(t1, yout)

plt.show()
