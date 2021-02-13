import control as co
import matplotlib.pyplot as plt
import numpy as np


def os_cosines(x):
    log2 = (np.log(x)) ** 2
    pi2 = (np.pi) ** 2
    numrator = np.log(x)
    denominator = np.sqrt(log2+pi2)
    return numrator / denominator

def plot_line(slope):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = slope*x_vals
    plt.plot(x_vals,y_vals, 'r--')


s = co.tf('s')
g = (2*s+1)/(2*s**3+4*s**2-8*s+1)
#siso = co.sisotool(g)

k = 21.535

"""βάζω ένα πόλο z=-1(+-)i"""
cs = k*(1+s+(0.71*s)**2)
g_feedback = co.feedback(co.series(g,cs),1,sign=-1)

co.pzmap(g_feedback)

TS = 7
slope1 = np.tan(np.arccos(os_cosines(0.2)))
plt.axvline(-4/TS, color='r', linestyle='--')


plot_line(slope1)
plot_line(-slope1)

plt.xlim([-1.5, 0.5])
plt.ylim([-1.3,1.3])

plt.show()