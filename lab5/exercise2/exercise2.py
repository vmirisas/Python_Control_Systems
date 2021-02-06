import control as co
import matplotlib.pyplot as plt
import numpy as np

s = co.tf('s')

a = 1 / (s + 3)
b = (s + 2) / (s - 2)
c = (s + 3) / (s + 4)
e = 1 / (s * (s ** 2 + 1))

acp = co.parallel(a, c)
bap = co.parallel(b, a)
acbas = co.series(acp, bap)
acbaef = co.feedback(acbas, e, 1)

t = np.linspace(0, 25, 100)
t1, stp = co.step_response(acbaef, t)
#t2, imp = co.impulse_response(acbaef, t)
#UserWarning: System has direct feedthrough: ``D != 0``. The infinite impulse at ``t=0`` does not appear in the output. Results may be meaningless!
g1_map = co.pzmap(acbaef, plot=True)

plt.figure(2)
plt.plot(t1, stp)
plt.title("Step Response")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()