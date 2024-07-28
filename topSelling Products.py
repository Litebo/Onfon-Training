import pandas as pd

file_path = "./ecommerce_sales_analysis.csv"
data =pd.read_csv(file_path)

data['total_sales'] = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=1)

data = data.sort_values(by='total_sales', ascending=False)

top_5_products = data.head(5)

print(top_5_products[['product_id', 'product_name', 'total_sales']])

