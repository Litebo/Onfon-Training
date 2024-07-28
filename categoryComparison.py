import pandas as pd

# Load the dataset
file_path = "./ecommerce_sales_analysis.csv"
data = pd.read_csv(file_path)

# Calculate total sales for each product
data['total_sales'] = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=1)

# Aggregate sales by category
category_sales = data.groupby('category').agg(
    total_sales=('total_sales', 'sum'),
    average_sales=('total_sales', 'mean')
).reset_index()

# Display total sales and average sales per category
print("Sales Performance by Category:")
print(category_sales)

# Compare the sales performance across different product categories
category_sales = category_sales.sort_values(by='total_sales', ascending=False)

# Plotting (optional for visualization)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(category_sales['category'], category_sales['total_sales'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.title('Total Sales by Category')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(category_sales['category'], category_sales['average_sales'], color='lightgreen')
plt.xlabel('Category')
plt.ylabel('Average Sales')
plt.title('Average Sales by Category')
plt.xticks(rotation=45)
plt.show()
