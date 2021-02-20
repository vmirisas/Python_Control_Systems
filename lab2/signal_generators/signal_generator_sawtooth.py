import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

period = 5
frequency = 1 / period
amplitude = 3
time = np.linspace(0, 15, 150)
signal_saw = amplitude * sg.sawtooth(2 * np.pi * frequency * time)
plt.plot(time, signal_saw)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.suptitle('Sawtooth Wave')
plt.grid(True, linestyle='--', color='lightgrey')
plt.xticks(np.linspace(0, 15, 4))
plt.show()
