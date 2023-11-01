import pandas as pd
import numpy as np

# Replace 'your_dataset.csv' with the actual file path of your dataset
file_path = 'your_dataset.csv'

# Load the dataset into a DataFrame
data = pd.read_csv(file_path)

# Print the first 10 rows
print("First 10 rows:")
print(data.head(10))

# Print the last 10 rows
print("\nLast 10 rows:")
print(data.tail(10))

# Print random 20 rows
random_20_rows = data.sample(20, random_state=42)  # You can change the random_state for different random rows
print("\nRandom 20 rows:")
print(random_20_rows)

# Display the shape of the dataset
print("\nShape of the dataset:", data.shape)
