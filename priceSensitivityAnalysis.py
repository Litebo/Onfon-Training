import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.formula.api import ols

# Load the dataset
file_path = "./ecommerce_sales_analysis.csv"
data = pd.read_csv(file_path)

# Assuming data contains 'product_id', 'price', and monthly sales columns 'sales_month_1' to 'sales_month_12'
# Calculate total sales volume for each product
data['total_sales_volume'] = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=1)

# Calculate percentage change in price and sales volume
data['price_pct_change'] = data['price'].pct_change().fillna(0)
data['sales_volume_pct_change'] = data['total_sales_volume'].pct_change().fillna(0)

# Calculate price elasticity of demand (PED)
data['PED'] = data['sales_volume_pct_change'] / data['price_pct_change']

# Visualize price sensitivity using scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='price', y='total_sales_volume', hue='category')
plt.title('Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()

# Perform regression analysis
model = ols("total_sales_volume ~ price", data=data).fit()
print(model.summary())

# Visualize regression analysis
plt.figure(figsize=(10, 6))
sns.regplot(x='price', y='total_sales_volume', data=data, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Regression Analysis: Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()

# Optional: Visualize the relationship by category
plt.figure(figsize=(12, 8))
sns.lmplot(x='price', y='total_sales_volume', data=data, hue='category', aspect=1.5, scatter_kws={'s':10})
plt.title('Regression Analysis by Category: Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()
