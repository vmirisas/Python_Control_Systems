import control as co
import matplotlib.pyplot as plt
import numpy as np
from control.timeresp import step_info


def max_amplitude(signal, time):
    index_max = list(signal).index(max(signal))
    peak_max = [time[index_max], signal[index_max]]
    return peak_max


def min_amplitude(signal, time):
    index_min = list(signal).index(min(signal))
    peak_min = [time[index_min], signal[index_min]]
    return peak_min


def signal_info(signal, time):
    print(f"time= {max_amplitude(signal, time)[0]}, amplitude max= {max_amplitude(signal, time)[1]}")
    print(f"time= {min_amplitude(signal, time)[0]}, amplitude min= {min_amplitude(signal, time)[1]}")


k = 5
b = 2
m1 = 10
m2 = 80
t = np.linspace(0, 1000, 10001)


s = co.tf('s')
g1 = 1 / (m1 * s ** 2 + b * s + k)
g2 = 1 / (m2 * s ** 2 + b * s + k)

print(g1, g2)

t1, imp1 = co.impulse_response(g1, t)
t2, stp1 = co.step_response(g1, t)
t3, imp2 = co.impulse_response(g2, t)
t4, stp2 = co.step_response(g2, t)


#S = co.step_info(stp1, t, SettlingTimeThreshold=0.01, RiseTimeLimits=(0.1, 0.9))

print("g1 impulse info")
signal_info(imp1, t1)
print("g1 step info")
signal_info(stp1, t2)
print("g2 impulse info")
signal_info(imp2, t3)
print("g2 step info")
signal_info(stp2, t4)

fig, axs = plt.subplots(2, 2, figsize=(7, 7))
plt.subplots_adjust(hspace=0.5, wspace=0.5)

axs[0, 0].plot(t1, imp1)
axs[0, 0].plot(max_amplitude(imp1, t1)[0], max_amplitude(imp1, t1)[1], "o")

axs[0, 1].plot(t3, imp2)
axs[0, 1].plot(max_amplitude(imp2, t3)[0], max_amplitude(imp2, t3)[1], "o")

axs[1, 0].plot(t2, stp1)
axs[1, 0].plot(max_amplitude(stp1, t2)[0], max_amplitude(stp1, t2)[1], "o")

axs[1, 1].plot(t4, stp2)
axs[1, 1].plot(max_amplitude(stp2, t4)[0], max_amplitude(stp2, t4)[1], "o")

axs[0, 0].set_title("Impulse Response")
axs[0, 1].set_title("Impulse Response")
axs[1, 0].set_title("Step Response")
axs[1, 1].set_title("Step Response")

axs[0, 0].set_xlabel("Time")
axs[0, 1].set_xlabel("Time")
axs[1, 0].set_xlabel("Time")
axs[1, 1].set_xlabel("Time")

axs[0, 0].set_ylabel("Amplitude")
axs[0, 1].set_ylabel("Amplitude")
axs[1, 0].set_ylabel("Amplitude")
axs[1, 1].set_ylabel("Amplitude")

axs[0, 0].set_xlim([0, 100])
axs[1, 0].set_xlim([0, 100])
axs[0, 1].set_xlim([0, 500])
axs[1, 1].set_xlim([0, 500])

axs[0, 0].grid()
axs[0, 1].grid()
axs[1, 0].grid()
axs[1, 1].grid()

plt.show()
