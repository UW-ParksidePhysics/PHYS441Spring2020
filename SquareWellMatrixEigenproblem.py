import numpy as np
from numpy import linalg as LA
# for N=10
# we need to construct a 10x10 matrix

### Comments ###
# You will need to define λ: what makes sense for this?
# Play with NumPy's diagflat function:
#       notice how it can be used to define the off-diagonal terms
#       what would be the result of just first + second + third?
#       how can you use this to adjust N so you don't have to manually type out the matrix
#       try using diagflat to create a 3 3x3 matrices of the correct kind and adding them together
# How do the boundary conditions of the well enter this problem?
#       consider how the number of points relates to positions in the well and the width of the well
###

# first = np.array[[i == j, 2, λ, 0], (i, 10), (j, 10)]
# second = np.array[[i == j + 1, -λ, 0], (i, 10), (j, 10)]
# thrid = np.array[[i == j - 1, -λ, 0], (i, 10), (j, 10)]
# total = np.array[first[[i ,j]] + second[[i, j]] + third[[i, j]], (i, 10), (j, 10)]



# a = np.array([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            #  [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            #  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            #  [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 2])


# w, v = LA.eig(a)
# print(total)
matrix = []
            
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    matrix.append(row)
print(matrix)
    