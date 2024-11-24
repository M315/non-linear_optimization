import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, diff

# Define the functions and variables
x = symbols('x')
f1 = x**2 + 4
f2 = 2 * x**2

# Find the points of intersection
intersection_points = solve(Eq(f1, f2), x)
intersection_points = [[float(p) for p in intersection_points][0]]

# Compute derivatives (slopes) of the functions
f1_derivative = diff(f1, x)
f2_derivative = diff(f2, x)

# Generate x values for plotting
x_vals = np.linspace(-4, 0, 500)
f1_vals = x_vals**2 + 4
f2_vals = 2 * x_vals**2
f = [x**2 + 4 if x**2 + 4 > 2 * x**2 else 2 * x**2 for x in x_vals]

# Plot the functions and additional features
plt.figure(figsize=(10, 8))
plt.plot(x_vals, f1_vals, label=r"$f_1 = x^2 + 4$", color="blue")
plt.plot(x_vals, f2_vals, label=r"$f_2 = 2x^2$", color="green")
plt.plot(x_vals, f, ":", label=r"$f = \max\{f_1, f_2\}$", color="orange")

for point in intersection_points:
    y1 = point**2 + 4
    y2 = 2 * point**2
    
    slope1 = float(f1_derivative.subs(x, point))
    slope2 = float(f2_derivative.subs(x, point))
    
    # Tangent lines
    y_tangent1 = slope1 * (x_vals - point) + y1
    plt.plot(x_vals, y_tangent1, '--', color="blue", alpha=0.7)
    
    y_tangent2 = slope2 * (x_vals - point) + y2
    plt.plot(x_vals, y_tangent2, '--', color="green", alpha=0.7)
    
    # Mark intersection points
    plt.scatter([point], [y1], color="red", label=r"$x_0$: " + f"({point:.2f}, {y1:.2f})")
    
    # Fill the area between the tangent lines
    plt.fill_between(x_vals, y_tangent1, y_tangent2, color="gray", alpha=0.2)

# Draw lines passing through intersection points
for point in intersection_points:
    y1 = point**2 + 4
    plt.plot(x_vals, (2 * x_vals - 2 * point) + y1, ':', color="purple", label=r"$l_1$")

    y2 = point**2 + 4
    plt.plot(x_vals, 10 * (point - x_vals) + y2, ':', color="black", label=r"$l_2$")

# Customize the plot
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(alpha=0.3)
plt.show()
