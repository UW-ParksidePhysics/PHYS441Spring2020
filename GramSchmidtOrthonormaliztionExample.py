import numpy as np

e1 = np.array([1. + 1.j, 1., 1.j])
e2 = np.array([1.j, 3., 1.])
e3 = np.array([0., 28., 8.])

print("|e1> = {}".format(e1))
print("|e2> = {}".format(e2))
print("|e3> = {}".format(e3))
print()

e1prime = e1/np.linalg.norm(e1)

e2prime = e2 - np.vdot(e1prime, e2) * e1prime
e2prime /= np.linalg.norm(e2prime)

e3prime = e3 - np.vdot(e1prime, e3) * e1prime \
             - np.vdot(e2prime, e3) * e2prime
e3prime /= np.linalg.norm(e3prime)

print("|e1'> = {}".format(e1prime))
print("|e2'> = {}".format(e2prime))
print("|e3'> = {}".format(e3prime))
print()

print("<e1'|e1'> = {}".format(np.vdot(e1prime, e1prime)))
print("<e1'|e2'> = {}".format(np.vdot(e1prime, e2prime)))
print("<e1'|e3'> = {}".format(np.vdot(e1prime, e3prime)))
print()

print("<e2'|e1'> = {}".format(np.vdot(e2prime, e1prime)))
print("<e2'|e2'> = {}".format(np.vdot(e2prime, e2prime)))
print("<e2'|e3'> = {}".format(np.vdot(e2prime, e3prime)))
print()

print("<e3'|e1'> = {}".format(np.vdot(e3prime, e1prime)))
print("<e3'|e2'> = {}".format(np.vdot(e3prime, e2prime)))
print("<e3'|e3'> = {}".format(np.vdot(e3prime, e3prime)))
print()
