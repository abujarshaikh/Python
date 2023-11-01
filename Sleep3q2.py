import pandas as pd

# Sample dataset (you can replace this with your own data or load from a file)
data = {
    "Heights": [165, 170, 175, 160, 180, 172, 168, 163, 158, 182],
    "Weights": [70, 75, 80, 65, 85, 77, 73, 68, 63, 88]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# View basic statistical details of the dataset
basic_stats = df.describe()

# Print the statistics
print(basic_stats)
