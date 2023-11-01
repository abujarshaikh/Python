import pandas as pd
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own dataset)
data = {
    'Name': ['Abujar', 'Aditya', 'Sahil', 'Tejas', 'Tosib'],
    'Salary': [50000, 60000, 75000, 55000, 70000]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(df['Name'], df['Salary'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary vs. Name')
plt.show()
