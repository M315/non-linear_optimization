import numpy as np
import matplotlib.pyplot as plt

def f(x, y, invalid_coord=np.inf):
    if x < 0.0  or y < 0.0:
        return invalid_coord
    if x*y < 1.0:
        return invalid_coord
    if x + y < 4.0:
        return invalid_coord
    return x**2 + y**2

coords = np.linspace(-0.5, 4.5, 200)
z = np.array([np.array([f(x, y) for y in coords]) for x in coords])

# Plot the contour with labels
plt.figure(figsize=(8, 6))
contour = plt.contourf(coords, coords, z, levels=20, cmap="gist_heat_r") 
cbar = plt.colorbar(contour) 
cbar.set_label('f(x, y)')

y_line = 4 - coords
plt.plot(coords, y_line, color="green", linestyle="--", linewidth=2)

coords = np.linspace(0.25, 4.5, 200)
y_curve = 1 / coords
plt.plot(coords, y_curve, color="green", linestyle="-", linewidth=2)

# plt.scatter(2, 2, color="blue", s=20, zorder=2)

plt.title("Contour Plot of $f(x_1, x_2) = x_1^2 + x_2^2$")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")

plt.show()
