import pandas as pd
import matplotlib.pyplot as plt

# Create a small dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'Salary': [50000, 60000, 52000, 70000, 58000],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by Department and calculate average salary
avg_salary = df.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(avg_salary)

# Plotting the average salary by department
plt.figure(figsize=(8, 5))
plt.bar(avg_salary['Department'], avg_salary['Salary'], color='skyblue')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()