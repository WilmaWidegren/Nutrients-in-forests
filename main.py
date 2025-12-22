import functions as f
import matplotlib.pyplot as plt
import numpy as np

### CONSTANTS ###
NUM_TREES = 300
T = 80
LATTICE_SIZE = 20

### INITIALISATION ###
initial_forest_size = f.grow_initial_forest(NUM_TREES, 30)
initial_forest_size_no = initial_forest_size.copy()
initial_forest_size_myc = initial_forest_size.copy()

### NO MYCORRHIZA ###
plot_data_no, plot_average_no = f.no_mycorrhiza(NUM_TREES, T, initial_forest_size_no)

### MYCORRHIZA ###
plot_data_myc, plot_average_myc = f.mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_size_myc)

### Plot ###
f.plot_graph(NUM_TREES, T, plot_data_no, plot_average_no) # Plot of no mycorrhiza
plt.show()

# f.plot_network(NUM_TREES, LATTICE_SIZE) # Example of a network. Shows the connections for one tree
# plt.show()

f.plot_graph(NUM_TREES, T, plot_data_myc, plot_average_myc) # Plot of mycorrhiza
plt.show()

plt.plot(plot_average_no, label = "no network")
plt.plot(plot_average_myc)
plt.legend()
plt.show()

### 100 runs simulations ###
N_RUNS = 100
all_avg_data_myc = []
all_avg_data_no = []

for _ in range(N_RUNS):
    initial_forest_size = f.grow_initial_forest(NUM_TREES, 30)
    initial_forest_size_no = initial_forest_size.copy()
    initial_forest_size_myc = initial_forest_size.copy()
    _, avg_myc = f.mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_size_myc)
    _, avg_no = f.no_mycorrhiza(NUM_TREES, T, initial_forest_size_no)
    all_avg_data_myc.append(avg_myc)
    all_avg_data_no.append(avg_no)

# Convert to array: shape = (N_RUNS, T)
all_avg_data_myc = np.array(all_avg_data_myc)
all_avg_data_no = np.array(all_avg_data_no) 

# Compute mean and standard deviation across runs
mean_avg_myc = np.mean(all_avg_data_myc, axis=0)
std_avg_myc = np.std(all_avg_data_myc, axis=0)
mean_avg_no = np.mean(all_avg_data_no, axis=0)
std_avg_no = np.std(all_avg_data_no, axis=0)

# Time axis
timesteps = np.arange(len(mean_avg_myc))

plt.plot(timesteps, mean_avg_myc, label="Mycorrhiza")
plt.plot(timesteps, mean_avg_no, label="No mycorrhiza")

# ±1 standard deviation shading
plt.fill_between(timesteps,
                 mean_avg_myc - std_avg_myc,
                 mean_avg_myc + std_avg_myc,
                 alpha=0.3,
                 label="± Std Dev")

plt.fill_between(timesteps,
                 mean_avg_no - std_avg_no,
                 mean_avg_no + std_avg_no,
                 alpha=0.3,
                 color = 'orange',
                 label="± Std Dev")

plt.xlabel("Time step")
plt.ylabel("Average tree size")
plt.legend(loc = 'lower right')
plt.title('Forest Growth Mean ± Std Dev \n(for 100 simulations with identical initialisation)')
plt.tight_layout()
plt.show()