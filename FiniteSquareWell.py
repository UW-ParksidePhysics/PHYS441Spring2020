import numpy as np
import matplotlib.pyplot as plt

potential_a = 1.0  # a
well_depth = 0.5   # V_0

# Region I : x < -a
# Region II : -a < x < a
# Region III : x > a

# Number of points to evaluate in each region and altogether
number_of_points_region_one = 50
number_of_points_region_two = 2 * number_of_points_region_one
number_of_points_region_three = number_of_points_region_one
number_of_points = number_of_points_region_one + number_of_points_region_two + number_of_points_region_three

# x         (go from -2a to 2a)
x_values = np.linspace(-2*potential_a, 2*potential_a, num=number_of_points)

# V(x) = {0, x < -a ; -V_0, -a < x < a ; 0, x > a}
potential_region_one = np.full(number_of_points_region_one, 0.0)
potential_region_two = np.full(number_of_points_region_two, -well_depth)
potential_region_three = np.full(number_of_points_region_three, 0.0)
potential = np.concatenate((potential_region_one, potential_region_two, potential_region_three))

# Plot the potential
plt.plot(x_values, potential)
plt.show()

