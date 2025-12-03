import functions as f
import numpy as np
import matplotlib.pyplot as plt

# x, y = f.get_tree_positions(100, 10)
time = 0
rate_parameter = -0.015

forest = f.grow_initial_forest(10, 0)
forest_new = np.zeros_like(forest)  
forest_new_plot = []  
print('Initial:', forest)
while time < 10:
    for i in range(len(forest)):
        size = f.calculate_tree_growth(forest[i], 0.01, 10, rate_parameter, 1.2)
        forest_new[i] = size

    forest_new_plot.append(forest_new[2])   

    time += 0.1
    forest += time
print('Simulation completed')
# print('After growth', forest_new)
# print(forest_new_plot)

plt.plot(forest_new_plot)
plt.xlim([0,100])
plt.show()