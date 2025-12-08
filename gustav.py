import functions as f
import numpy as np
import matplotlib.pyplot as plt

### Constants ###
FACTOR = np.random.uniform(0.03, 0.06)
A = -0.015
dt = 1
NUM_TREES = 400
a = 0.01
k = 40
m = 1.2
c = 1
T = 80
COST_FOR_GROWTH = 1

### Initialisation ###
forest_age = f.grow_initial_forest(NUM_TREES, 40)
forest_size = f.calculate_tree_growth(forest_age, k, a, A, m, c)
time = 0
carbon = f.calculate_max_carbon(forest_size, FACTOR)
plot_data = [[] for _ in range(NUM_TREES)] # Create lists to plot the tree growth
plot_average = []

### Main ###
while time < T:
    next_size = f.calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
    growth_increment = next_size - forest_size # Calculates how much the tree grows for each timestep.
    
    for i in range(NUM_TREES):
        if growth_increment[i] > 1:
            growth_increment[i] = 1

        plot_data[i].append(forest_size[i]) # Adds the current size of the trees into a list

        if growth_increment[i] < 0:
            growth_increment[i] = 0

        elif growth_increment[i] > 0:
            carbon[i] -= growth_increment[i] * COST_FOR_GROWTH

        if carbon[i] < 0: 
            carbon[i] = 0

    forest_size += growth_increment # Adds the growth to the current size of the tree
    average_size = forest_size.mean()
    plot_average.append(average_size)
    time += dt  
    forest_age += dt
    for i in range(NUM_TREES):
        carbon[i] += f.calculate_max_carbon(forest_size[i], FACTOR)

for i in range(NUM_TREES):
    plt.plot(plot_data[i], linewidth = 0.05, color = 'green') # Visualisation of how the tree grows over time.
plt.plot(plot_average, label = 'Average over all trees', linestyle = 'dotted', color = 'black')
plt.xlim([0, T])
plt.xlabel('Timesteps (100 years)')
plt.ylabel('Size of trees')
plt.title(f'Forest of {NUM_TREES} trees and its growth after 100 years with randomly\n refilled carbon reservior based on the size of trees')
plt.legend()
plt.show()