import matplotlib.pyplot as plt
import control as co

s = co.tf('s')

g = (s+1)/((s-1)*(s-4))
h1 = 1



plt.figure(1)
co.sisotool(g) # βλέπω απο την rlocus οτι για gain>5 οι πόλοι έρχονται στο μιγαδικό αρνητικό μέρος

plt.show()