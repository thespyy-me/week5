import matplotlib.pyplot as plt

# Step 1: Read the data file
filename = input("Enter the filename (e.g., data.txt): ")

x = []
y = []

with open(filename, 'r') as f:
    for line in f:
        if line.strip() == "":
            continue  # skip empty lines
        parts = line.strip().split()
        if len(parts) >= 2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))

# Step 2: Plot the data
plt.plot(x, y, marker='d', linestyle='dashdot', color='purple', label='Data from file')
plt.title("Data Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
