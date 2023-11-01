import pandas as pd
import matplotlib.pyplot as plt

# Import the Iris dataset
data = pd.read_csv('iris.csv')

# Count the frequency of each species
species_counts = data['species'].value_counts()

# Create a pie plot
plt.figure(figsize=(6, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Frequency of Iris Species')

# Display the pie plot
plt.show()
