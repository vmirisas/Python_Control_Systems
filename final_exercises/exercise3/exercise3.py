import control as co
import numpy as np
import matplotlib.pyplot as plt
from functions.my_functions import step_info, step_info_return

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

s = co.tf('s')
j = 0.01
c = 0.004
k = 10
km = 0.05
t = np.linspace(1,30,5000)

#1)
g = km / (j * s ** 2 + c * s + k)
print(g)

#2)
t1, gstp = co.step_response(g, t)
step_info(t1, gstp)
plt.figure(1)
plt.title('Step Response')
plt.plot(t1, gstp)
plt.grid()

#3)
t2, gstp2 = co.step_response(3*g, t)
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

#4)
t4, imp = co.impulse_response(3*g, t)
#step_info(t4, imp)
plt.figure(3)
plt.title('Impulse Response')
plt.plot(t4, imp)
plt.grid()

#5)
plt.figure(4)
print(co.pole(g))
co.pzmap(g)

#6)
plt.figure(5)
co.sisotool(g)
"""Δεν υπάρχει"""

#7)
plt.figure(6)



plt.show()