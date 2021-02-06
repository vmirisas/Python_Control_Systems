import control as co
import matplotlib.pyplot as plt
import numpy as np
from control import matlab


def max_amplitude(signal, time):
    index_max = list(signal).index(max(signal))
    peak_max = [time[index_max], signal[index_max]]
    return peak_max


def min_amplitude(signal, time):
    index_min = list(signal).index(min(signal))
    peak_min = [time[index_min], signal[index_min]]
    return peak_min


s = co.tf('s')
g1 = ((4 * s ** 2 - 3) * (6 * s + 8)) / ((6 * s ** 3 - 2 * s ** 2 + 9) * (s ** 2 + 8))
print(g1)
t = np.linspace(0, 200, 1000)

t1, imp = co.impulse_response(g1, t)
t2, stp = co.step_response(g1, t)

tsq = np.linspace(0, 10, 1000)
l1 = len(np.linspace(0, 4, 400, endpoint=False))
l2 = len(np.linspace(4, 8, 400, endpoint=False))
l3 = len(np.linspace(8, 10, 200))
sq = np.append(np.append(np.zeros(l1), np.ones(l2)), np.zeros(l3))
yout, T, xout = matlab.lsim(g1, sq, tsq)

print(f"g1 impulse : time= {max_amplitude(imp, t1)[0]}, amplitude max= {max_amplitude(imp, t1)[1]}")
print(f"g1 impulse : time= {min_amplitude(imp, t1)[0]}, amplitude min= {min_amplitude(imp, t1)[1]}")
print(f"g1 step : time= {max_amplitude(stp, t2)[0]}, amplitude max= {max_amplitude(stp, t2)[1]}")
print(f"g1 step : time= {min_amplitude(stp, t2)[0]}, amplitude min= {min_amplitude(stp, t2)[1]}")
print(f"g1 square : time= {max_amplitude(yout, T)[0]}, amplitude max= {max_amplitude(yout, T)[1]}")
print(f"g1 square : time= {min_amplitude(yout, T)[0]}, amplitude min= {min_amplitude(yout, T)[1]}")

fig, axs = plt.subplots(3, 1, figsize=(10, 7))
plt.subplots_adjust(hspace=0.7)
axs[0].plot(t1, imp)
axs[0].plot(max_amplitude(imp, t1)[0], max_amplitude(imp, t1)[1], "o")
axs[0].plot(min_amplitude(imp, t1)[0], min_amplitude(imp, t1)[1], "o")

axs[1].plot(t2, stp)
axs[1].plot(max_amplitude(stp, t2)[0], max_amplitude(stp, t2)[1], "o")
axs[1].plot(min_amplitude(stp, t2)[0], min_amplitude(stp, t2)[1], "o")

axs[2].plot(T, yout)
axs[2].plot(max_amplitude(yout, T)[0], max_amplitude(yout, T)[1], "o")
axs[2].plot(min_amplitude(yout, T)[0], min_amplitude(yout, T)[1], "o")

axs[0].set_title("Impulse Response")
axs[1].set_title("Step Response")
axs[2].set_title("Square Response")

axs[0].set_xlim([175, 200])
axs[1].set_xlim([175, 200])
axs[2].set_xlim([0, 10])
plt.show()
