import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers between 1 and 100
data = np.random.randint(1, 100, 50)

# Create a figure and subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 12))

# Line Chart
ax1.plot(data, color='blue', linestyle='-', marker='o', markersize=5)
ax1.set_title('Line Chart')
ax1.set_xlabel('Data Point')
ax1.set_ylabel('Value')

# Scatter Plot
ax2.scatter(range(1, 51), data, color='green', marker='o')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('Data Point')
ax2.set_ylabel('Value')

# Histogram
ax3.hist(data, bins=10, color='red', alpha=0.7)
ax3.set_title('Histogram')
ax3.set_xlabel('Value')
ax3.set_ylabel('Frequency')

# Box Plot
ax4.boxplot(data, vert=False, patch_artist=True)
ax4.set_title('Box Plot')
ax4.set_yticklabels(['Data'])
ax4.set_xlabel('Value')

# Adjust spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()
