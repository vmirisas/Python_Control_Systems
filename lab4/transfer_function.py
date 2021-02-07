import control as co

g1 = co.tf([3, 2], [5, 3, 7])
print(f"g1 = {g1}")

s = co.tf('s')
g2 = (3 * s + 2) / (5 * s ** 2 + 3 * s + 7)
print(f"g2 = {g2}")
