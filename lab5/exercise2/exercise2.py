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
acbaef = co.feedback(acbas, e, 1)

print(acbaef)
t = np.linspace(0, 25, 100)


t1, stp = co.step_response(acbaef, t)
t2, imp = co.impulse_response(acbaef, t)
g1_map = co.pzmap(acbaef, plot=True)

plt.figure(2)
plt.plot(t, stp)
plt.title("Step Response")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()