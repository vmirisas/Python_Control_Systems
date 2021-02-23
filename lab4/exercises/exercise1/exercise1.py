import control as co
import matplotlib.pyplot as plt
import numpy as np


def peak_amplitude(signal, t):
    index_max = list(signal).index(max(signal))
    peak = [t[index_max], signal[index_max]]
    return peak

def step_info(t, yout):
    print(f"Max Amp: {max(yout)}")
    print("OS: %f%s" % ((yout.max() / yout[-1] - 1) * 100, '%'))
    print("Tr: %fs" % (t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1] * .90)] - t[0]))
    print("Ts: %fs" % (t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1]) > 1.02)] - t[0]))


s = co.tf('s')
g1 = 6 / (3 * s ** 2 + 2 * s + 6)
g2 = (2 * s - 3) / (6 * s ** 3 - 8 * s + 4)

t = np.linspace(0, 200, 10000)

t1, imp1 = co.impulse_response(g1, t)
t2, imp2 = co.impulse_response(g2, t)
t3, stp1 = co.step_response(g1, t)
t4, stp2 = co.step_response(g2, t)

print(f"g1 impulse : time= {peak_amplitude(imp1,t1)[0]}, amplitude max= {peak_amplitude(imp1,t1)[1]}")
print(f"g2 impulse : time= {peak_amplitude(imp2,t2)[0]}, amplitude max= {peak_amplitude(imp2,t2)[1]}")
print(f"g1 step : time= {peak_amplitude(stp1,t3)[0]}, amplitude max= {peak_amplitude(stp1,t3)[1]}")
print(f"g2 step : time= {peak_amplitude(stp2,t4)[0]}, amplitude max= {peak_amplitude(stp2,t4)[1]}")

print(step_info(t3, stp1))
print(step_info(t1, imp1))

# ορισμός πλέγματος γραφικών παραστάσεων
fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# γραφικές παραστάσεις αποκρίσεων και μεγίστων χρόνων
axs[0, 0].plot(t1, imp1)
axs[0, 0].plot(peak_amplitude(imp1,t1)[0], peak_amplitude(imp1,t1)[1], "o")
axs[0, 1].plot(t2, imp2)
axs[0, 1].plot(peak_amplitude(imp2,t2)[0], peak_amplitude(imp2,t2)[1], "o")
axs[1, 0].plot(t3, stp1)
axs[1, 0].plot(peak_amplitude(stp1,t3)[0], peak_amplitude(stp1,t3)[1], "o")
axs[1, 1].plot(t4, stp2)
axs[1, 1].plot(peak_amplitude(stp2,t4)[0], peak_amplitude(stp2,t4)[1], "o")

# Όρια άξονα x γραφικής παράστασης
axs[0, 0].set_xlim([0, 30])
axs[1, 0].set_xlim([0, 30])

# πλέγματα
axs[0, 0].grid()
axs[0, 1].grid()
axs[1, 0].grid()
axs[1, 1].grid()

# Τίτλοι
axs[0, 0].set_title("Impulse(g1)")
axs[0, 1].set_title("Impulse(g2)")
axs[1, 0].set_title("Step(g1)")
axs[1, 1].set_title("Step(g2)")

plt.setp(axs[-1, :], xlabel='Time(s)')
plt.setp(axs[:, 0], ylabel='Amplitude')

plt.show()
