import pandas as pd

# Import the dataset
data = pd.read_csv('winequality-red.csv')

# View basic statistical details
statistical_details = data.describe()

# Display the statistical details
print(statistical_details)
