import control as co
import matplotlib.pyplot as plt
import numpy as np

s = co.tf('s')
g1 = (s + 1) / ((s ** 2) - (3 * s) + 2)

h1 = co.feedback(g1, 2, -1)
h2 = co.feedback(g1, 3, -1)
h3 = co.feedback(g1, 5, -1)

print("poles (k=2)")
for elem in co.pole(h1):
    print(f'{elem: .2f}')
print("poles (k=3)")
for elem in co.pole(h2):
    print(f'{elem: .2f}')
print("poles (k=5)")
for elem in co.pole(h3):
    print(f'{elem: .2f}')

plt.figure(1)
h1_map = co.pzmap(h1, plot=True, title='pzmap (k=2)')
plt.figure(2)
h2_map = co.pzmap(h2, plot=True, title='pzmap (k=3)')
plt.figure(3)
h3_map = co.pzmap(h3, plot=True, title='pzmap (k=5)')

t = np.linspace(0, 10, 1000)

t1, imp1 = co.impulse_response(h1, t)
t2, imp2 = co.impulse_response(h2, t)
t3, imp3 = co.impulse_response(h3, t)

t4, stp1 = co.step_response(h1, t)
t5, stp2 = co.step_response(h2, t)
t6, stp3 = co.step_response(h3, t)

fig1, axs = plt.subplots(3, 1)
fig1.suptitle("Impulse Response")
axs[0].plot(t1, imp1)
axs[1].plot(t2, imp2)
axs[2].plot(t3, imp3)

axs[0].set_ylabel("Amplitude")
axs[1].set_ylabel("Amplitude")
axs[2].set_ylabel("Amplitude")

axs[2].set_xlabel("Time")

fig2, axs = plt.subplots(3, 1)
fig2.suptitle("Step Response")
axs[0].plot(t4, stp1)
axs[1].plot(t5, stp2)
axs[2].plot(t6, stp3)

axs[0].set_ylabel("Amplitude")
axs[1].set_ylabel("Amplitude")
axs[2].set_ylabel("Amplitude")

axs[2].set_xlabel("Time")

plt.show()
