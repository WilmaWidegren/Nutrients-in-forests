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

### MYCORRHIZA ###
plot_data_myc, plot_average_myc = f.mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_age_myc)

### Plot ###
f.plot_graph(NUM_TREES, T, plot_data_no, plot_average_no) # Plot of no mycorrhiza

f.plot_network(NUM_TREES, LATTICE_SIZE) # Example of a network. Shows the connections for one tree

f.plot_graph(NUM_TREES, T, plot_data_myc, plot_average_myc) # Plot of mycorrhiza

plt.plot(plot_average_no)
plt.plot(plot_average_myc)
plt.show()