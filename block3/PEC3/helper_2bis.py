import numpy as np
import matplotlib.pyplot as plt

# Define the range for lambda and a
lambda_vals = np.linspace(0, 5, 100)  # scaling factor for directions
a_vals = np.linspace(-2, 1, 30)       # range for 'a' in the cone definition

# Compute the cone's vectors
vectors = []
for a in a_vals:
    for lam in lambda_vals:
        vectors.append(lam * np.array([-1, a]))

# Extract x and y coordinates of the vectors
x_coords = [vec[0] for vec in vectors]
y_coords = [vec[1] for vec in vectors]

# Plot tangent cone
plt.scatter(x_coords, y_coords, s=1, color="blue", alpha=0.6)

# (-1, y) Line
x_coords = np.array([-1 for _ in range(100)])
y_coords = np.linspace(-2.0, 1.0, 100)
plt.plot(x_coords, y_coords, color="red", linestyle="-", linewidth=2)

plt.title("Cono Contingente y su Base")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.show()
