import functions as f
import numpy as np
import matplotlib.pyplot as plt

# x, y = f.get_tree_positions(100, 10)
# x = np.random.randint(1, 40)
# x = 23
factor = np.random.uniform(0.01, 0.05)
rate_parameter = -0.015
initialsize, initialage = f.grow_initial_forest(10, 40)
forest_new = np.zeros_like(forest)  
forest_new_plot1 = [] 
forest_new_plot2 = [] 
forest_new_plot3 = [] 
forest_new_plot4 = [] 
time = 0
    # print('Initial:', forest)
carbon = f.initial_carbon_matrix(forest)
print(carbon)
while time < 10:
    for i in range(len(forest)):
    
        size = f.calculate_tree_growth(forest[i], 40, 0.01, rate_parameter, 1.2, carbon[i])
        forest_new[i] = size
    
    forest += time
    time += 0.1
    carbon = f.calculate_max_carbon(forest, factor)
    forest_new_plot1.append(forest_new[0])
    forest_new_plot2.append(forest_new[1])
    forest_new_plot3.append(forest_new[2])
    forest_new_plot4.append(forest_new[3])
print('After growth', forest_new)
# print(forest_new_plot)

plt.plot(forest_new_plot1, label = 'färg')
plt.plot(forest_new_plot2, label = 'färg')
plt.plot(forest_new_plot3, label = 'färg')
plt.plot(forest_new_plot4, label = 'färg')
plt.xlim([0,100])
plt.legend()
plt.show()