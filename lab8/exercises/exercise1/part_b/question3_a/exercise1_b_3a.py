import control as co
import matplotlib.pyplot as plt

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

g = (s + 1) / ((s - 1) * (s - 4))
h1 = 1
h2 = 1 / (s - 1)

# a)
k = 36
gf = co.feedback(k * pd_comp(-4.4) * g, h2, -1)  # υπολογίζω τους πόλου και τα μηδενικά του κλειστού συστήματος με Κ = 36 και feedback=h2
poles = co.pole(gf)
zeros = co.zero(gf)
print(f"poles: {poles}")
print(f"zeros: {zeros}")

plt.figure(1)
co.root_locus(pd_comp(-4.4) * g * h2, grid=False)  # σχεδιάζω την γραφική παράστασή μου με pd_compensator
plt.xlim(-15, 5)

plt.plot(poles.real, poles.imag, 'rx')

plt.show()
