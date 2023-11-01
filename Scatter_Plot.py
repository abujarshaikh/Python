import matplotlib.pyplot as plt
import numpy as np

# Data
x_values = np.array([5,7,8,7,2,15,3,9,4,11,12,9,6])
y_values = np.array([99,86,80,88,111,75,103,90,98,78,77,85,84])

# Create the plot
plt.scatter(x_values, y_values)

# Add labels and title
plt.xlabel('Age of Car(Years)')
plt.ylabel('Maximum Speed')
plt.title('Correlation Between Car age and Speed')

# Display the plot
plt.show()
