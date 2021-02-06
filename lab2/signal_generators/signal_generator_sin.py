import matplotlib.pyplot as plt
import numpy as np

period = 2
frequency = 1 / period
amplitude = 1
time = np.arange(0, 15, 0.1)
signal_sin = amplitude * np.sin(2 * np.pi * frequency * time)
plt.plot(time, signal_sin)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.suptitle('Sin Wave')
plt.grid(True, linestyle='--', color='lightgrey')
plt.show()
