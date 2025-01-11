import numpy as np
import matplotlib.pyplot as plt

def f(x, y, invalid_coord=np.inf):
    if x**2 + y**2 >= 4:
        return invalid_coord
    return 2*x + y

coords = np.linspace(-2.5, 2.5, 1000)
z = np.array([np.array([f(x, y) for x in coords]) for y in coords])

# Plot the contour with labels
plt.figure(figsize=(8, 6))
contour = plt.contourf(coords, coords, z, levels=20, cmap="gist_heat_r") 
cbar = plt.colorbar(contour) 
cbar.set_label('f(x, y)')

y_line = 0.5 * coords
plt.plot(coords, y_line, color="green", linestyle="--", linewidth=1)

plt.plot(-4.0 / np.sqrt(5.0), -2.0 / np.sqrt(5.0), 'bo') 

plt.title("Contour Plot of $f(x_1, x_2) = 2 x_1 + x_2$")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")

plt.show()
