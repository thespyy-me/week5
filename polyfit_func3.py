import numpy as np
import matplotlib.pyplot as plt

# Read data from file
filename = input("Enter filename (e.g., data.txt): ")

x = []
y = []

with open(filename, 'r') as f:
    for line in f:
        if line.strip():
            xi, yi = map(float, line.strip().split())
            x.append(xi)
            y.append(yi)

# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

# Fit a polynomial of degree 1 (line), or change to 2, 3, etc. for curves
degree = int(input("Enter the degree of the polynomial to fit (e.g., 1 for line): "))
coeffs = np.polyfit(x, y, degree)

# Generate the fitted y-values
poly_func = np.poly1d(coeffs)
y_fit = poly_func(x)

# Plot original data and fitted curve
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_fit, color='red', label=f'Polynomial Fit (deg={degree})')
plt.title('Polynomial Fit Using polyfit()')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
