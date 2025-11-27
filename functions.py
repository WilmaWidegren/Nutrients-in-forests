import numpy as np



def grow_forest():
    pass

# This function taker number ocf trees (int), size of forest (int), the size will be that squared in the first cuadrant
def get_tree_positions(Number_of_trees, size_of_forest):
    x_positions, y_positions = [], []

    for i in range(Number_of_trees):
        x_positions.append(np.random.uniform(0,size_of_forest))
        y_positions.append(np.random.uniform(0,size_of_forest))

    return x_positions, y_positions


def tree_growth_formula():
    pass

def initial_cole_matrix():
    pass

def uppdate_cole_matrix():
    pass