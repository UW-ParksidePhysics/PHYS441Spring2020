import numpy as np
from numpy import linalg as LA
# import matplotlib.pyplot as plt

N = 5
b = np.ones(N - 1)
e = np.full(N, 2.)

print(b)

a = np.diagflat(-b, 1)
print(a)
c = np.diagflat(-b, -1)
print(c)
d = np.diagflat(e)
print(d)
print(a + c + d)
hbar = 1
mass = 1
deltax = (1 - 0) / (N - 1)
print(deltax)
lamb = hbar ** 2 / (2 * mass * (deltax) ** 2)
print(lamb)
# numerator = ħ**2
# denom = 2*m*(Δx)**2
# λ = np.divide(numerator, denom, out=np.zeros_like(numerator), where=denom!=0)


# print(λ*(a + c + d))

eigenvalue, eigenvector = LA.eig(lamb * (a + c + d))
# print(eigenvalue)

print()

print(eigenvalue)
first_three = eigenvalue[eigenvalue.argsort()[:3]]
print(eigenvalue.argsort())
print(eigenvalue[eigenvalue.argsort()])
print(first_three)
# print(eigenvalue)
energy_one = np.power(np.pi, 2) / 2.0
print(energy_one)

out = []

for elm in first_three:
    out += [0.0, elm, 1.0]

out = np.array(out)

# plt.plot(out)
# plt.show()
