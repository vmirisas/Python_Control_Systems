import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

period = 3
frequency = 1 / period
amplitude = 15
time = np.arange(0, 15, 0.1)
signal_square = amplitude * sg.square(2 * np.pi * frequency * time)
plt.plot(time, signal_square)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.suptitle('Square Wave')
plt.grid(True, linestyle='--', color='lightgrey')
plt.xticks(np.arange(0, 16, 5))
plt.show()
