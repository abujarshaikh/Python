import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
data = np.random.randint(1, 100, 50)

# Create a figure with subplots for each type of plot
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line Chart
axes[0, 0].plot(data, color='blue', marker='o', linestyle='-')
axes[0, 0].set_title('Line Chart')
axes[0, 0].set_xlabel('Index')
axes[0, 0].set_ylabel('Value')

# Scatter Plot
axes[0, 1].scatter(range(50), data, color='green', marker='x')
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('Index')
axes[0, 1].set_ylabel('Value')

# Histogram
axes[1, 0].hist(data, bins=10, color='orange', edgecolor='black')
axes[1, 0].set_title('Histogram')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

# Box Plot
axes[1, 1].boxplot(data, vert=False)
axes[1, 1].set_title('Box Plot')
axes[1, 1].set_yticklabels([''])

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
