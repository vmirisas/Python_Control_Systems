import control as co
import matplotlib.pyplot as plt
import numpy as np

def step_info(t, yout):
    print(f"Max Amp: {max(yout)}")
    print("OS: %f%s" % ((yout.max() / yout[-1] - 1) * 100, '%'))
    print("Tr: %fs" % (t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1] * .90)] - t[0]))
    print("Ts: %fs" % (t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1]) > 1.02)] - t[0]))

s = co.tf('s')
g = (s + 1) / (s ** 2 - 5 * s + 6)
t = np.linspace(0, 10, 1000)

"""A) δεν είναι ευσταθές, θετικούς πόλους"""
g_poles = co.pole(g)

"""B)"""
print(g)
grtl = co.root_locus(g, xlim=(-5, 5))

g_gained = co.feedback(10 * g, sign=-1)
print(g_gained)
plt.figure(2)
gg_rlc = co.root_locus(g_gained, xlim=(-5, 0.5))

t1, gstp = co.step_response(g, t)  # step response of open system
t2, gimp = co.impulse_response(g, t)  # impulse response of open system
t3, ggstp = co.step_response(g_gained, t)  # step response of closed system k=10
t4, ggimp = co.impulse_response(g_gained, t)  # impulse response of closed system k=10



step_info(t3, ggstp)
fig3, axs = plt.subplots(2, 2)
axs[0, 0].plot(t1, gstp)
axs[0, 1].plot(t2, gimp)
axs[1, 0].plot(t3, ggstp)
axs[1, 1].plot(t4, ggimp)

axs[0, 0].title.set_text('Step Response of Open')
axs[0, 1].title.set_text('Impulse Response of Open')
axs[1, 0].title.set_text('Step Response of Closed (k=10)')
axs[1, 1].title.set_text('Impulse Response of Closed (k=10)')

axs[0, 0].set_ylabel('Amplitude')
axs[1, 0].set_ylabel('Amplitude')
axs[1, 0].set_xlabel('Time')
axs[1, 1].set_xlabel('Time')
plt.show()
