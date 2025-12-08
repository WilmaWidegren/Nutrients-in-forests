import numpy as np
import matplotlib.pyplot as plt

# This function taker number ocf trees (int), size of forest (int), the size will be that squared in the first cuadrant
def get_tree_positions(Number_of_trees, size_of_forest):
    x_positions, y_positions = [], []

    for i in range(Number_of_trees):
        x_positions.append(np.random.uniform(0,size_of_forest))
        y_positions.append(np.random.uniform(0,size_of_forest))

    return x_positions, y_positions


def grow_initial_forest(Number_of_trees , max_age):
    tree_ages = []
    for i in range(Number_of_trees):
        tree_ages.append(np.random.uniform(1, max_age))
    return np.array(tree_ages)
    

def calculate_tree_growth(x :float, k: float, a: float, A: float, m: float, C: float) -> np.ndarray:
    """
    Calculates tree growth (Y) based on a modified sigmoidal growth function.

    The formula is: Y = k * (1 - e^((a + b * S) * A))^m

    This function is designed to model growth where juvenile trees grow faster 
    than mature ones, characterized by an S-shaped (sigmoidal) curve.

    Parameters:
    - x (np.ndarray): Age/Time of the tree. Randomly generated when initialising the forest.
    - k (float): Asymptotic scaling factor; controls the maximum potential size.
    - a (float): Initial coefficient influencing the growth rate. Coal?
    - A (float): Rate parameter; influences the speed at which the maximum size is approached.
    - m (float): Shape parameter; determines the point of inflection (when acceleration peaks).
    - C (float): Limiting factor; carbon reservior. Avaliable / Needed. If C = 1 -> Optimal growth.

    Returns:
    - np.ndarray: Calculated tree growth (Y) for each age (x).
    """
    
    # Ensure all inputs are float for calculation
    k, a, A, m = float(k), float(a), float(A), float(m)
    
    # Calculate the exponent term
    # Exponent = ((a + x) * A)
    exponent_term = (a + x) * A * C
    
    # Calculate the core sigmoid term
    # Sigmoid = (1 - e^(Exponent))^m
    sigmoid_term = (1 - np.exp(exponent_term))**m
    
    # Calculate the final growth value
    Y = k * sigmoid_term

    # Add Carbon term.
    
    return Y

def calculate_max_carbon(size: np.ndarray, factor: float) -> np.ndarray: 
    """
    Calculate the maximum amount of carbon avaliable based on the tree's current size. 
    Size = Current size of tree.
    factor = random number between 0.03 and 0.06
    """
    carbon_list = np.maximum(size*factor, 0.5) # Compare two arrays and returns a new array containing the element-wise maxima.
                                        # If the element is less than 0.3 return 0.3
    return carbon_list

def get_conections(x, y):
    number_of_trees = len(x)
    conections = np.zeros((number_of_trees, number_of_trees))

    s=0
    for i in range(len(conections)):
        
        for j in range(0,s):
            dx= x[i]-x[j]
            dy=y[i]-y[j]
            d = np.sqrt(dx**2+dy**2)
            if d<1:
                conections[i][j]=1
                conections[j][i]=1
            elif d>=50:
                conections[i][j]=0
                conections[j][i]=0
            elif 2/d > np.random.random():
                conections[i][j]=1
                conections[j][i]=1
        s+=1
    return conections


def uppdate_carbon_matrix(tree_size: np.ndarray, conection_matrix: np.ndarray, carbon_list) ->  np.ndarray:
    """
    Distributes carbon between connected trees if a significant size difference exists, 
    simulating a mycorrhizal network.
    """
    num_trees = len(conection_matrix)

    for i in range(num_trees):
        for j in range(i + 1, num_trees):
            if carbon_list[i] > 0.9 and conection_matrix[i][j] == 1:
                    size_difference = tree_size[i] - tree_size[j]
                    if size_difference > 15:
                        carbon_to_give = carbon_list[i] * 0.1
                        carbon_list[i] -= carbon_to_give
                        carbon_list[j] += carbon_to_give

                    elif size_difference < -15:
                        carbon_to_give = carbon_list[j] * 0.1
                        carbon_list[j] -= carbon_to_give
                        carbon_list[i] += carbon_to_give

    return carbon_list

def no_mycorrhiza(NUM_TREES, T, initial_forest_age):
    ### Constants ###
    FACTOR = np.random.uniform(0.03, 0.06)
    A = -0.015
    dt = 1
    a = 0.01
    k = 40
    m = 1.2
    c = 1
    COST_FOR_GROWTH = 1.3

    ### Initialisation ###
    forest_size = calculate_tree_growth(initial_forest_age, k, a, A, m, c)
    time = 0
    carbon = calculate_max_carbon(forest_size, FACTOR)
    plot_data = [[] for _ in range(NUM_TREES)] # Create lists to plot the tree growth
    plot_average = []
    forest_age = initial_forest_age
    ### Main ###
    while time < T:
        next_size = calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
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
            carbon[i] += calculate_max_carbon(forest_size[i], FACTOR)

    return plot_data, plot_average

def mycorrhiza(NUM_TREES, LATTICE_SIZE, T, initial_forest_age):
    ### Constants ###
    FACTOR = np.random.uniform(0.03, 0.06)
    COST_FOR_GROWTH = 1
    A = -0.015
    dt = 1
    a = 0.01
    k = 40
    m = 1.2
    c = 1

    ### Initialisation ###
    forest_size = calculate_tree_growth(initial_forest_age, k, a, A, m, c)
    time = 0
    carbon = calculate_max_carbon(forest_size, FACTOR)
    plot_data = [[] for _ in range(NUM_TREES)] # Create lists to plot the tree growth
    plot_average = []

    x, y = get_tree_positions(NUM_TREES, LATTICE_SIZE)
    conection_matrix = get_conections(x, y)
    forest_age = initial_forest_age

    ### Main ###
    while time < T:
        for _ in range(4):
            new_carbon = uppdate_carbon_matrix(forest_size, conection_matrix, carbon)
            carbon=new_carbon

        next_size = calculate_tree_growth(forest_age + dt, k, a, A, m, carbon)
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
            carbon[i] += calculate_max_carbon(forest_size[i], FACTOR)
    return plot_data, plot_average

def plot_network(NUM_TREES, LATTICE_SIZE):
    x, y = get_tree_positions(NUM_TREES, LATTICE_SIZE)
    #carbon_list=f.initial_carbon_matrix(forest_age)
    conection_matrix = get_conections(x, y)
    # Definiera vilka träd du vill visa kopplingar från
    target_trees = [np.random.randint(0, NUM_TREES)]

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
                plt.plot([x[i], x[j]], [y[i], y[j]], 'r-', alpha=0.7, linewidth=0.2, zorder=1)

    plt.title(f"Entire mycorrhiza network")
    plt.show()