import functions as f
import matplotlib.pyplot as plt

### CONSTANTS ###
NUM_TREES = 300
T = 80
LATTICE_SIZE = 20

### INITIALISATION ###
initial_forest_age = f.grow_initial_forest(NUM_TREES, 40)
initial_forest_age_no = initial_forest_age.copy()
initial_forest_age_myc = initial_forest_age.copy()

### NO MYCORRHIZA ###
plot_data_no, plot_average_no = f.no_mycorrhiza(NUM_TREES, T, initial_forest_age_no)

### Plot ###
for i in range(NUM_TREES):
    plt.plot(plot_data_no[i], linewidth = 0.05, color = 'green') # Visualisation of how the tree grows over time.
plt.plot(plot_average_no, label = 'Average over all trees', linestyle = 'dotted', color = 'black')
plt.xlim([0, T])
plt.xlabel('Timesteps (100 years)')
plt.ylabel('Size of trees')
plt.title(f'Forest of {NUM_TREES} trees and its growth after {T} years with randomly\n refilled carbon reservior dependent on the size of tree')
plt.legend()
plt.show()

### MYCORRHIZA ###
plot_data_myc, plot_average_myc = f.mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_age_myc)

### Plot ###
f.plot_network(NUM_TREES, LATTICE_SIZE) # Example of a network. Shows the connections for one tree

for i in range(NUM_TREES):
    plt.plot(plot_data_myc[i], linewidth = 0.05, color = 'green') # Visualisation of how the tree grows over time.
plt.plot(plot_average_myc, label = 'Average over all trees', linestyle = 'dotted', color = 'black')
plt.xlim([0, T])
plt.xlabel('Timesteps (100 years)')
plt.ylabel('Size of trees')
plt.title(f'Forest of {NUM_TREES} trees and its growth after {T} years with randomly\n refilled carbon reservior dependent on the size of tree')
plt.legend()
plt.show()

plt.plot(plot_average_no)
plt.plot(plot_average_myc)
plt.show()