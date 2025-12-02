import functions as f
import numpy as np
import matplotlib.pyplot as plt

# x, y = f.get_tree_positions(100, 10)
# x = np.random.randint(1, 40)
# x = 23
time = 0
rate_parameter = -0.015
forest = f.grow_initial_forest(10, 60)
forest_new = np.zeros_like(forest)  
forest_new_plot = [] 
forest_new_plot_extra = [] 
print('Initial:', forest)
while time < 10:
    for i in range(len(forest)):
    
        size = f.calculate_tree_growth(forest[i], 100, 0.01, rate_parameter, 1.2)
        forest_new[i] = size
    forest_new_plot.append(forest_new[2])
    forest_new_plot_extra.append(forest_new[7])   
    forest += time
    time += 0.1
print('After growth', forest_new)
print(forest_new_plot)

plt.plot(forest_new_plot)
plt.plot(forest_new_plot_extra)
plt.xlim([0,100])
plt.show()