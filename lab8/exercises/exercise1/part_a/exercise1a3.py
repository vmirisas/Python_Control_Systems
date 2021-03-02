import control as co
import matplotlib.pyplot as plt

s = co.tf('s')

g = (s + 1) / ((s - 1) * (s - 4))
h2 = 1 / (s - 1)
gf = co.feedback(g, h2, -1)

plt.figure(1)
co.root_locus(g * h2, grid=False)  # βλέπω απο την rlocus οτι οι πόλοι είναι πραγματικοί και θετικοί αριθμοί, οπότε έχω πάντα αστάθεια.

plt.show()
