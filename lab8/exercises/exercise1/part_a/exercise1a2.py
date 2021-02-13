import matplotlib.pyplot as plt
import control as co
import numpy as np


def slope_Os(x):
    log2 = (np.log(x)) ** 2
    pi2 = (np.pi) ** 2
    enumrator = log2 + np.sqrt((1 + 4 * pi2) * log2)
    denominator = 2 * pi2
    return enumrator / denominator

def plot_Os(x):
    slope = np.tan(np.arccos(slope_Os(x)))  # overshoot 30%
    axes = plt.gca()
    x1_vals = np.array(axes.get_xlim())
    x_vals = np.array((x1_vals[0], 0))
    y1_vals = slope*x_vals
    y2_vals = -slope * x_vals
    plt.plot(x_vals,y1_vals, 'r--', x)
    plt.plot(x_vals,y2_vals, 'r--')


s = co.tf('s')

g = (s+1)/((s-1)*(s-4))
h1 = 1
k = 10

gf = co.feedback(k*g,h1,-1)
co.root_locus(gf)
plot_Os(0.3)
plt.xlim([-8, 2])
plt.ylim([-3,3])
#co.sisotool(gf)
plt.show()