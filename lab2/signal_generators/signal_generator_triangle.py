import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

period = 5
frequency = 1 / period
amplitude = 3
time = np.linspace(0, 15, 150)
signal_triangle = amplitude * sg.sawtooth(2 * np.pi * frequency * time, width=0.5)
plt.plot(time, signal_triangle)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.suptitle('Triangle Wave')
plt.grid(True, linestyle='--', color='lightgrey')
plt.xticks(np.linspace(0, 15, 4))
plt.show()
