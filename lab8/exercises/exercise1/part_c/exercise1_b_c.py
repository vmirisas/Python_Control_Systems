import control as co
import matplotlib.pyplot as plt
import numpy as np
from control import matlab


def lead_comp(spole, szero):
    cz = 1 + (s / (-szero))
    cp = 1 / (1 + (s / (-spole)))
    return cz * cp


def pid_comp(szero1, szero2):
    cz1 = 1 + (s / (-szero1))
    cz2 = 1 + (s / (-szero2))
    return cz1 * cz2 * (1 / s)


def pd_comp(szero):
    cz1 = 1 + (s / (-szero))
    return cz1


s = co.tf('s')
t = np.linspace(0, 10, 1000)
g = (s + 1) / ((s - 1) * (s - 4))
h2 = 1 / (s - 1)
ut = np.sin(t)

k_lead = 150
g_lead = co.feedback(k_lead * lead_comp(-60, -10) * g, h2, -1)
ylead, T1, u1out = matlab.lsim(g_lead, ut, t)

k_pid = 4
g_pid = co.feedback(k_pid * pid_comp(-0.5, -0.5) * g, h2, -1)
ypid, T2, u2out = matlab.lsim(g_pid, ut, t)

k_pd = 60
g_pd = co.feedback(k_pd * pd_comp(-4.4) * g, h2, -1)
ypd, T3, u3out = matlab.lsim(g_pd, ut, t)

fig, axs = plt.subplots(3, 1)
fig.suptitle('Responses for u(t)=sin(t)')
axs[0].plot(T1, ylead)
axs[1].plot(T2, ypid)
axs[2].plot(T3, ypd)

axs[0].set_ylabel('g_lead')
axs[1].set_ylabel('g_pid')
axs[2].set_ylabel('g_pd')
axs[2].set_xlabel('Time')
axs[0].grid()
axs[1].grid()
axs[2].grid()

for axs in fig.get_axes():
    axs.label_outer()
plt.show()
