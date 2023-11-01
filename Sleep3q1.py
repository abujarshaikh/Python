import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the dataset
data = pd.read_csv('iris.csv')

# Create box plots for each feature by species
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.boxplot(x="species", y="sepal_length", data=data)
plt.title("Sepal Length Distribution by Species")

plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.boxplot(x="species", y="sepal_width", data=data)
plt.title("Sepal Width Distribution by Species")

plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.boxplot(x="species", y="petal_length", data=data)
plt.title("Petal Length Distribution by Species")

plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
sns.boxplot(x="species", y="petal_width", data=data)
plt.title("Petal Width Distribution by Species")

plt.show()
