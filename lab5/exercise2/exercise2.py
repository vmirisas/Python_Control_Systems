import control as co
import matplotlib.pyplot as plt
import numpy as np

s = co.tf('s')

a = 1 / (s - 3)
b = (s + 2) / (s - 2)
c = (s + 3) / (s + 4)
e = 1 / (s * ((s ** 2) + 1))

acp = co.parallel(c, a)
bap = co.parallel(b, a)
acbas = co.series(acp, bap)
acbaef = co.feedback(acbas, e, +1)

print(acbaef)

g_poles = co.pole(acbaef)
print("G poles")
for elem in g_poles:
    print(f'{elem: .2f}')

g_zeros = co.zero(acbaef)
print("G zeros")
for elem in g_zeros:
    print(f'{elem: .2f}')

g1_map = co.pzmap(acbaef, plot=True)

t = np.linspace(0, 25, 100)
t1, stp = co.step_response(acbaef, t)
t2, imp = co.impulse_response(acbaef, t) # Warning for infinite impulse at t=0

plt.figure(2)
plt.plot(t1, stp)
plt.title("Step Response")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.grid()

plt.figure(3)
plt.plot(t2, imp)
plt.title("Impulse Response")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.grid()
plt.show()
