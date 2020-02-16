import numpy as np
from numpy import linalg as LA
#for N=10 
#we need to construct a 10x10 matrix


#first = np.array[[i == j, 2, λ, 0], (i, 10), (j, 10)]
#second = np.array[[i == j + 1, -λ, 0], (i, 10), (j, 10)]
#thrid = np.array[[i == j - 1, -λ, 0], (i, 10), (j, 10)]
#total = np.array[first[[i ,j]] + second[[i, j]] + third[[i, j]], (i, 10), (j, 10)]

#a = np.array([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            #  [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            # [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            #  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
            #  [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 2])


#w, v = LA.eig(a)
#print(total)
matrix = []
            
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    matrix.append(row)
print(matrix)
    