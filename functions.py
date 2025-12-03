import numpy as np

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
        tree_ages.append(np.random.uniform(0,max_age))
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

def calculate_max_carbon(age: np.ndarray, factor: float) -> np.ndarray: 
    """
    Calculate the maximum amount of carbon avaliable based on the tree's current size. 
    Size = Current age of tree.
    factor = constant.
    """
    carbon_list = np.maximum(age*factor, 0.5) # Compare two arrays and returns a new array containing the element-wise maxima.
                                        # If the element is less than 0.3 return 0.3
    return carbon_list

def initial_carbon_matrix(initial_age):
    carbon_list = calculate_max_carbon(initial_age, np.random.uniform(0,0.1))
    return carbon_list

def uppdate_carbon_matrix():
    pass