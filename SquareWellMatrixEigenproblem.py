import numpy as np
from numpy import linalg as LA
N = 10
b = np.ones(N - 1)
e = np.full(N, 2.)

#print(b)

a = np.diagflat(-b, 1)
c = np.diagflat(-b, -1)
d = np.diagflat(e)

print(a + c + d)
ħ = 1
m = 1
Δx = (a - 0)/(N - 1)
λ =  ħ**2/(2*m*(Δx)**2)


print(λ*(a + c + d))
