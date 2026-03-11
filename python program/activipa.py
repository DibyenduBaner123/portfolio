import pandas as pd

# 1. Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}
df = pd.DataFrame(data)

# 2. Display the DataFrame
print("DataFrame:")
print(df)

# 3. Select a specific column
print("\nSelect 'Name' column:")
print(df['Name'])

# 4. Filter rows based on a condition
print("\nFilter rows where Age is greater than 30:")
print(df[df['Age'] > 30])

# 5. Group by a column and perform aggregation (mean salary by city)
print("\nGroup by 'City' and calculate mean salary:")
print(df.groupby('City')['Salary'].mean())

# 6. Sorting the DataFrame by a column (e.g., by Age)
print("\nSort DataFrame by 'Age':")
print(df.sort_values(by='Age'))

# 7. Add a new column (e.g., Tax which is 10% of Salary)
df['Tax'] = df['Salary'] * 0.10
print("\nDataFrame after adding 'Tax' column:")
print(df)

# 8. Drop a column (e.g., Tax)
df = df.drop('Tax', axis=1)
print("\nDataFrame after dropping 'Tax' column:")
print(df)

# 9. Check for missing values (if any)
print("\nCheck for missing values:")
print(df.isnull().sum())

# 10. Descriptive statistics of the DataFrame
print("\nDescriptive statistics:")
print(df.describe())

# 11. Save DataFrame to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'.")
