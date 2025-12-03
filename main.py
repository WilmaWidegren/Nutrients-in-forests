import functions as f
import numpy as np
import matplotlib.pyplot as plt

### Constants ###
FACTOR = np.random.uniform(0.01, 0.05)
A = -0.015
dt = 1
NUM_TREES = 10
a = 0.01
k = 40
m = 1.2
c = 1
T = 100

### Initialisation ###
forest_age = f.grow_initial_forest(NUM_TREES, 40)
forest_size = f.calculate_tree_growth(forest_age, k, a, A, m, c)
time = 0
carbon = f.calculate_max_carbon(forest_age, FACTOR)
print(forest_age)
plot_data = [[] for _ in range(NUM_TREES)] # Create lists to plot the tree growth

### Main ###
while time < T:
    for i in range(NUM_TREES):
        plot_data[i].append(forest_size[i]) # Adds the current size of the trees into a list
    
    next_size = f.calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
    growth_increment = next_size - forest_size # Calculates how much the tree grows for each timestep.

    forest_size += growth_increment # Adds the growth to the current size of the tree

    time += dt  
    forest_age += dt
    carbon = f.calculate_max_carbon(forest_age, FACTOR)

### Plot ###
for i in range(NUM_TREES):
    plt.plot(plot_data[i], label=f'Tree {i+1}') # Visualisation of how the tree grows over time.
plt.xlim([0,100])
plt.legend()
plt.show()