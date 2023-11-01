import pandas as pd

# Define the file path
file_path = "Data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Get the shape of the data (number of rows and columns)
num_rows, num_columns = df.shape

# Get the data types of each column
data_types = df.dtypes

# Get the feature (column) names
feature_names = df.columns

# Get the description of the data
data_description = df.describe()

# Print the results
print("Shape of the data (number of rows, columns):", (num_rows, num_columns))
print("\nData Types:")
print(data_types)
print("\nFeature Names:")
print(feature_names)
print("\nData Description:")
print(data_description)
