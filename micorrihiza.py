import functions as f
import numpy as np
import matplotlib.pyplot as plt

### Constants ###
FACTOR = np.random.uniform(0.01, 0.05)
A = -0.015
dt = 1
NUM_TREES = 400
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
plot_data = [[] for _ in range(NUM_TREES)] # Create lists to plot the tree growth
plot_average = []

x, y = f.get_tree_positions(NUM_TREES, 10)
#carbon_list=f.initial_carbon_matrix(forest_age)
conection_matrix = f.get_conections(x, y)


### Main ###
while time < T:
    new_carbon = f.uppdate_carbon_matrix(forest_size, conection_matrix, carbon)
    carbon=new_carbon

    next_size = f.calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
    growth_increment = next_size - forest_size # Calculates how much the tree grows for each timestep.
    
    for i in range(NUM_TREES):
        plot_data[i].append(forest_size[i]) # Adds the current size of the trees into a list
        if growth_increment[i] < 0:
            growth_increment[i] = 0

        elif growth_increment[i] > 0:
            carbon[i] -= 0.6

        if carbon[i] < 0: 
            carbon[i] = 0.3

    forest_size += growth_increment # Adds the growth to the current size of the tree
    average_size = forest_size.mean()
    plot_average.append(average_size)
    time += dt  
    forest_age += dt
    carbon += f.calculate_max_carbon(forest_age, FACTOR)

### Plot ###
for i in range(NUM_TREES):
    plt.plot(plot_data[i], linewidth = 0.05, color = 'green') # Visualisation of how the tree grows over time.
plt.plot(plot_average, label = 'Average over all trees', linestyle = 'dotted', color = 'black')
plt.xlim([0, T])
plt.xlabel('Timesteps (100 years)')
plt.ylabel('Size of trees')
plt.title(f'Forest of {NUM_TREES} trees and its growth after 100 years with randomly\n refilled carbon reservior based on the size of trees')
plt.legend()
plt.show()

# # Definiera vilka träd du vill visa kopplingar från
# target_trees = [np.random.randint(0, NUM_TREES)]

# plt.scatter(x, y, c='g', zorder=2)

# # Iterera ENDAST över de utvalda träden
# for i in target_trees:
#     # Fortsätt iterera över ALLA andra träd (j)
#     for j in range(NUM_TREES):
#         # Förhindra att rita en linje från trädet till sig självt
#         if i == j:
#             continue            
#         # Kontrollera kopplingen i matrisen (behöver bara kolla en riktning 
#         # eftersom matrisen är symmetrisk för detta nätverk)
#         if conection_matrix[i, j] == 1:
#             # Rita linjen
#             plt.plot([x[i], x[j]], [y[i], y[j]], 'r-', alpha=0.7, linewidth=0.2, zorder=1)

# plt.title(f"Entire mycorrhiza network")
# plt.show()