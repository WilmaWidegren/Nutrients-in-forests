import functions as f
import numpy as np
import matplotlib.pyplot as plt

# x, y = f.get_tree_positions(100, 10)
# x = np.random.randint(1, 40)
x = 1
time = 0
lista = []
rate_parameter = -0.015
while time < 10:
    size = f.calculate_tree_growth(x, 100, 0.01, rate_parameter, 1.2)
    lista.append(size)
    x += time
    time += 0.1

forest = f.grow_initial_forest(100, 30)
while time < 10:
    for i in range(len(forest)):
        size = f.calculate_tree_growth(forest[i])
