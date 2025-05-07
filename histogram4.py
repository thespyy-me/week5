import matplotlib.pyplot as plt

# Example data
data = [12, 15, 13, 19, 21, 25, 21, 22, 25, 19, 17, 18, 16, 15, 17, 25, 27, 28, 22, 23]

# Create histogram
plt.hist(data, bins=6, color='pink', edgecolor='indigo')
plt.title("Histogram of Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()
