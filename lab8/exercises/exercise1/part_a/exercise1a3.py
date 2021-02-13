import matplotlib.pyplot as plt
import control as co




s = co.tf('s')

g = (s+1)/((s-1)*(s-4))
h1 = 1
h2 = 1/(s-1)
gf = co.feedback(g,h2,-1)


plt.figure(1)
co.root_locus(g*h2, grid=False) # βλέπω απο την rlocus οτι οι πόλοι είναι πραγματικοί και θετικοί αριθμοί, οπότε έχω πάντα αστάθεια.

plt.show()