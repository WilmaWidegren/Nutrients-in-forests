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

x, y = f.get_tree_positions(NUM_TREES, 100)
#carbon_list=f.initial_carbon_matrix(forest_age)
conection_matrix = f.get_conections(x, y)


### Main ###
while time < T:
    for i in range(NUM_TREES):
        plot_data[i].append(forest_size[i]) # Adds the current size of the trees into a list
    
    next_size = f.calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
    growth_increment = next_size - forest_size # Calculates how much the tree grows for each timestep.

    forest_size += growth_increment # Adds the growth to the current size of the tree

    average_size = forest_size.mean()
    plot_average.append(average_size)
    time += dt  
    forest_age += dt
    #carbon += f.calculate_max_carbon(forest_age, FACTOR)
    
    new_carbon = f.uppdate_carbon_matrix(forest_size, conection_matrix, carbon)
    carbon=new_carbon
    for i in range(len(carbon)):
        carbon[i]+=0.05


### Plot ###
# for i in range(NUM_TREES):
#     plt.plot(plot_data[i], linewidth = 0.05, color = 'green') # Visualisation of how the tree grows over time.
# plt.plot(plot_average, label = 'Average over all trees', linestyle = 'dotted', color = 'black')
# plt.xlim([0, 100])
# plt.xlabel('Timesteps (100 years)')
# plt.ylabel('Size of trees')
# plt.title(f'Forest of {NUM_TREES} trees and its growth after 100 years with randomly\n refilled carbon reservior based on the size of trees')
# plt.legend()
#plt.show()





# plt.scatter(x,y, c='g', zorder=2)
# # Iterate over all possible pairs of trees
# for i in range(NUM_TREES):
#     for j in range(i + 1, NUM_TREES):
#         # Check if the trees are connected
#         if conection_matrix[i, j] == 1:
#             # Draw a line between the coordinates of tree i and tree j
#             # We use 'k--' for a dashed black line, or 'r-' for a solid red line
#             plt.plot([x[i], x[j]], [y[i], y[j]], 'k--', alpha=0.5, linewidth=0.5, zorder=1)
# plt.show()

# Definiera vilka träd du vill visa kopplingar från
target_trees = [0, 1] 

plt.scatter(x, y, c='g', zorder=2)

# Iterera ENDAST över de utvalda träden
for i in target_trees:
    # Fortsätt iterera över ALLA andra träd (j)
    for j in range(NUM_TREES):
        # Förhindra att rita en linje från trädet till sig självt
        if i == j:
            continue
            
        # Kontrollera kopplingen i matrisen (behöver bara kolla en riktning 
        # eftersom matrisen är symmetrisk för detta nätverk)
        if conection_matrix[i, j] == 1:
            # Rita linjen
            plt.plot([x[i], x[j]], [y[i], y[j]], 'r-', alpha=0.7, linewidth=1, zorder=1)

plt.title(f"Kopplingar från Träd {target_trees[0]}")
plt.show()