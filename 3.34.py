import numpy as np
import matplotlib.pyplot as plt

a = 1
hbar = 1
pi = np.pi
mass = 1


def probability_density(p, n):
    prefactor = (a * hbar)/pi
    prefactor *= np.power(n * pi * hbar, 2)
    phi_squared = prefactor / np.power(np.power(a * p, 2) - np.power(n * pi * hbar, 2), 2)
    phi_squared *= (2 + np.power(-1, n-1) * np.cos(a * p / hbar))
    return phi_squared


n_values = [1, 2, 5, 10]
# n_values = [1, 2]
p_minimum = 0.0
p_maximum = (max(n_values) + 1) * pi * hbar / a
momentum_values = np.linspace(p_minimum, p_maximum, num=1000)


def energy(n):
    """Total energy of a particle in infinite square well"""
    energy_n = np.power(n * pi * hbar / a, 2) / (2 * mass)
    return energy_n


def momentum(energy_n):
    """Momentum of particle in infinity square well is
    square root of twice the total energy over the mass of the particle since the potential is zero in the well"""
    momentum_n = np.sqrt(2 * energy_n / mass)
    return momentum_n


for n in n_values:
    plt.plot(momentum_values, probability_density(momentum_values, n),
             label='n = {}  p_{} = {:.2f}'.format(n, n, momentum(energy(n))))

plt.legend()

plt.show()