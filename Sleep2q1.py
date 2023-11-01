import pandas as pd

# Import the dataset
data = pd.read_csv('Data.csv')

# Calculate the mean of the salary and age columns
salary_mean = data['Salary'].mean()
age_mean = data['Age'].mean()

# Replace missing values with the respective means
data['Salary'].fillna(salary_mean, inplace=True)
data['Age'].fillna(age_mean, inplace=True)

# Display the modified dataset
print(data)
