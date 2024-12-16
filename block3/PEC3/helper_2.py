import numpy as np
import matplotlib.pyplot as plt

N_POINTS = 500

def Id_S(x: float, y: float, invalid_coord=np.inf):
    if y >= (x - 3.0)**2 + 3.0 and y <= 8.0 - x:
        return 0.0
    return invalid_coord

x_coords = np.linspace(0.5, 4.5, N_POINTS)
y_coords = np.linspace(2.0, 10.0, N_POINTS)
z = np.array([np.array([Id_S(x, y) for x in x_coords]) for y in y_coords])

# Plot the contour with labels
plt.figure(figsize=(8, 6))
contour = plt.contourf(x_coords, y_coords, z, levels=20, cmap="Greys") 
# cbar = plt.colorbar(contour) 
# cbar.set_label('S')

y_line = 8.0 - x_coords
plt.plot(x_coords, y_line, color="green", linestyle="-", linewidth=2)

coords = x_coords
y_curve = (coords - 3.0)**2 + 3.0
plt.plot(coords, y_curve, color="green", linestyle="-", linewidth=2)

plt.scatter(4.0, 4.0, color="red", s=20, zorder=2)

y_line = 2.0 * (x_coords - 3.0) + 2.0
plt.plot(x_coords, y_line, color="orange", linestyle="-", linewidth=2)

y_line = 8.0 - x_coords
plt.plot(x_coords, y_line, color="orange", linestyle="--", linewidth=2)

plt.title("Set S")
plt.xlabel("$x$")
plt.ylabel("$y$")

plt.show()
