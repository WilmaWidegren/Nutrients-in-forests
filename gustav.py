'''
Tree {
  id: int
  size: float  // calculated through allometric equations. 
  carbon: float
  x: float
  y: float
}
'''

'''
Connect two trees if the distance between them is less than a threshold.
if distance(tree_i, tree_j) < R and random() < p:
    connect(i, j)
'''

'''
If a tree is connected to another tree, it can transfer carbon to it.
Larger trees transfer carbon to smaller trees.
Larger trees do not need as much carbon as smaller trees.

If tree_i.size > tree_j.size:
    transfer_amount = f(tree_i.size, tree_j.size)
    tree_i.carbon -= transfer_amount
    tree_j.carbon += transfer_amount
'''

'''
Matrix with features for nodes and edges.
3D feature matrix for nodes: 
2D feature matrix for edges: carbon_transfer_cost?
'''

# Generating a smooth 3-phase growth function and plotting examples
import numpy as np
import matplotlib.pyplot as plt

def three_phase_size(t, s0=0.1, t1=5.0, t2=20.0, A=0.02, K=10.0, gamma=1.0):
    """
    Smooth three-phase growth:
      - Juvenile (0 <= t <= t1): accelerating growth ~ quadratic: s = s0 + A*t^2
      - Mature (t1 <= t <= t2): approximately linear (constant rate) with slope v = 2*A*t1
      - Senescent (t >= t2): decelerating, exponential approach to asymptote K
    
    Parameters
    ----------
    t : array-like or float
        Time values
    s0 : float
        Size at time 0 (initial size)
    t1 : float
        End time of juvenile phase (start of mature)
    t2 : float
        End time of mature phase (start of senescent)
    A : float
        Coefficient controlling juvenile acceleration (size ~ s0 + A t^2)
    K : float
        Asymptotic maximum size reached in senescent phase
    gamma : float
        Optional multiplier to scale times (keeps units flexible)
    """