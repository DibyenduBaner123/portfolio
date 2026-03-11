import pandas as pd

# Create sample data and save it as a CSV file
data = {
    "Product": ["A", "B", "A", "C", "B", "A", "C", "C"],
    "Sales": [100, 200, 150, 300, 250, 180, 400, 350],
    "Region": ["North", "East", "West", "South", "North", "East", "West", "South"],
}

# Save sample data to a CSV
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

# Load the CSV file
sales_df = pd.read_csv("sales_data.csv")

# Display the first few rows of the dataset
print("Initial Dataset:")
print(sales_df)

# Group by Product and calculate the average sales
average_sales = sales_df.groupby("Product")["Sales"].mean()

print("\nAverage Sales per Product:")
print(average_sales)

# Filtering: Products with sales greater than 150
filtered_sales = sales_df[sales_df["Sales"] > 150]

print("\nProducts with Sales Greater Than 150:")
print(filtered_sales)
