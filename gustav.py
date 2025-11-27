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