import functions as f
import matplotlib.pyplot as plt

### CONSTANTS ###
NUM_TREES = 300
T = 100
LATTICE_SIZE = 20

### INITIALISATION ###
initial_forest_size = f.grow_initial_forest(NUM_TREES, 30)
initial_forest_size_no = initial_forest_size.copy()
initial_forest_size_myc = initial_forest_size.copy()
for i in range(10):
    initial_forest_size_no = initial_forest_size.copy()
    initial_forest_size_myc = initial_forest_size.copy()
    ### NO MYCORRHIZA ###
    plot_data_no, plot_average_no = f.no_mycorrhiza(NUM_TREES, T, initial_forest_size_no)

    ### MYCORRHIZA ###
    plot_data_myc, plot_average_myc = f.mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_size_myc)

    ### Plot ###
    f.plot_graph(NUM_TREES, T, plot_data_no, plot_average_no) # Plot of no mycorrhiza

    f.plot_network(NUM_TREES, LATTICE_SIZE) # Example of a network. Shows the connections for one tree

    f.plot_graph(NUM_TREES, T, plot_data_myc, plot_average_myc) # Plot of mycorrhiza

    plt.plot(plot_average_no, label = "no")
    plt.plot(plot_average_myc)
    plt.legend()
    plt.show()