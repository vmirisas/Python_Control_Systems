import control as co
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import lsim
from scipy import signal as sg

from functions.my_functions import step_info


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def plot_ts(TS):
    plt.axvline(-4 / TS, color='r', linestyle='--')


s = co.tf('s')
j = 0.01
c = 0.004
k = 10
km = 0.05
t = np.linspace(1, 30, 5000)

# 1)
g = km / (j * s ** 2 + c * s + k)
print(g)

# 2)
t1, gstp = co.step_response(g, t)
step_info(t1, gstp)
plt.figure(1)
plt.title('Step Response')
plt.plot(t1, gstp)
plt.grid()

# 3)
t2, gstp2 = co.step_response(3 * g, t)
step_info(t2, gstp2)
plt.figure(2)
plt.title('Step Response')
plt.plot(t2, gstp2)
plt.grid()
"""
charact2 = step_info_return(t1, gstp2)
ts2 = charact2[3]

data2 = np.column_stack(([t2, gstp2]))
ts2nearest = find_nearest(t2,ts2)
y2setling_time = data2[t2 == ts2nearest, 1]
"""

"""plt.plot(ts2nearest, y2setling_time, 'ro')
plt.annotate('settling time',xy=(ts2,y2setling_time))
plt.axvline(ts2nearest,ymin=0, ymax=0.5, color='grey',linestyle='--')
plt.axhline(y2setling_time,xmin=0, xmax=0.5, color='grey',linestyle='--')"""

# 4)
t4, imp = co.impulse_response(3 * g, t)
# step_info(t4, imp)
plt.figure(3)
plt.title('Impulse Response')
plt.plot(t4, imp)
plt.grid()

# 5)
plt.figure(4)
print(co.pole(g))
co.pzmap(g)

# 6)
plt.figure(5)
# co.sisotool(g)
"""Δεν υπάρχει"""


# 7)
def add_zero(szero):
    if szero == 0:
        szero = 0.001

    cz = 1 - (s / szero)
    return cz


k = 1200

plt.figure(6)
plot_ts(0.07)
co.root_locus(add_zero(-40) * g, grid=False)

gf1 = co.feedback(k * add_zero(-40) * g, 1, -1)
pol_values = co.pole(gf1)
plt.plot(pol_values.real, pol_values.imag, 'rx')

tstep, ystp = co.step_response(gf1, t)
step_info(tstep, ystp)


# 8)

def os_cosines(x):
    log2 = (np.log(x)) ** 2
    pi2 = (np.pi) ** 2
    numrator = np.log(x)
    denominator = np.sqrt(log2 + pi2)
    return numrator / denominator


def plot_line(slope):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = slope * x_vals
    plt.plot(x_vals, y_vals, 'r--')


plt.figure(7)
plot_ts(0.07)
co.root_locus(add_zero(-40) * g, grid=False)

k2 = 1200
gf2 = co.feedback(k2 * add_zero(-40) * g, 1, -1)
pol_values2 = co.pole(gf2)
plt.plot(pol_values2.real, pol_values2.imag, 'rx')

print(os_cosines(0.05))
slope1 = np.tan(np.arccos(os_cosines(0.05)))
plot_line(slope1)
plot_line(-slope1)

tstep2, ystp2 = co.step_response(gf2, t)
step_info(tstep2, ystp2)
plt.xlim(-100, 1)

# 9)
period = 0.1
freq = 1 / period
amp = 1
time = np.linspace(0, 1, 1000)
signal_sqr = amp * sg.square(2 * np.pi * freq * time)
plt.figure(8)
plt.plot(time, signal_sqr)
closedsys, tclosed, xout = lsim(gf2, signal_sqr, time)

plt.figure(9)
plt.plot(tclosed, closedsys)

plt.show()
