import functions as f
import numpy as np
import matplotlib.pyplot as plt
forest_new_plot1 = [] 
forest_new_plot2 = [] 
forest_new_plot3 = [] 
forest_new_plot4 = [] 
# x, y = f.get_tree_positions(100, 10)
# x = np.random.randint(1, 40)
# x = 23
# CONSTANTS
factor = np.random.uniform(0.01, 0.05)
rate_parameter = -0.015
dt = 1
num_trees = 10

# INITIALISATION
forest_age = f.grow_initial_forest(num_trees, 40)
forest_size = f.calculate_tree_growth(forest_age, 40, 0.01, rate_parameter, 1.2, 1)
time = 0
carbon = f.calculate_max_carbon(forest_age, factor)
print(forest_age)
plot_data = [[] for _ in range(num_trees)]

# MAIN LOOP
while time < 100:
    for i in range(num_trees):
        plot_data[i].append(forest_size[i])
    
    next_size = f.calculate_tree_growth(forest_age + dt, 40, 0.01, rate_parameter, 1.2, carbon)
    growth_increment = next_size - forest_size

    forest_size += growth_increment

    time += dt  
    forest_age += dt
    carbon = f.calculate_max_carbon(forest_age, factor)

print('After growth', forest_age)
# print(forest_new_plot)
for i in range(num_trees):
    plt.plot(plot_data[i], label=f'Tree {i+1}')
plt.xlim([0,100])
plt.legend()
plt.show()