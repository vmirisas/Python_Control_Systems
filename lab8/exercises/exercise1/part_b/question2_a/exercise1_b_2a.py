import control as co
import matplotlib.pyplot as plt

""" Συνάρτηση κατασκευής lead compensator
    input(θέσεις ενός πραγματικού μηδενικού και ενός πραγματικού πόλου)
    με αυτά κατασκευάζει τα πολυώνυμα μετά την προσθήκη των ο,x 
    returns (C(s) με αυτά κατασκευάζει) 
"""


def pid_comp(szero1, szero2):
    cz1 = 1 + (s / (-szero1))
    cz2 = 1 + (s / (-szero2))
    return cz1 * cz2 * (1 / s)


def plot_ts(TS):
    plt.axvline(-4 / TS, color='r', linestyle='--')


s = co.tf('s')

g = (s + 1) / ((s - 1) * (s - 4))
h1 = 1
h2 = 1 / (s - 1)

# a)
k = 2.5
gf = co.feedback(k * pid_comp(-0.5, -0.5) * g, h2, -1)  # υπολογίζω τους πόλου και τα μηδενικά του κλειστού συστήματος με Κ = 120 και feedback=h2
poles = co.pole(gf)
zeros = co.zero(gf)
print(poles, zeros)

plt.figure(1)
co.root_locus(pid_comp(-0.5, -0.5) * g * h2, grid=False)  # σχεδιάζω την γραφική παράστασή μου με lead_compensator
plt.xlim(-10, 3)
plt.ylim(-6, 6)
plt.plot(poles.real, poles.imag, 'rx')
# plt.plot(zeros.real, zeros.imag, 'ro')


plt.show()
