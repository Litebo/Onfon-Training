import pandas as pd

file_path = "./ecommerce_sales_analysis.csv"
data = pd.read_csv(file_path)

data['total_sales'] = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=1)

data['average_review_score'] = data['review_score'] / data['review_count']

data['average_review_score'] = data['average_review_score'].fillna(0)

data = data.sort_values(by='total_sales', ascending=False)

top_5_products = data.head(5)

print("Top 5 Best-Selling Products:")
print(top_5_products[['product_id', 'product_name', 'total_sales']])

print("\nAverage Review Scores:")
print(data[['product_id', 'product_name', 'average_review_score']])

correlation = data['average_review_score'].corr(data['total_sales'])
print(f"\nCorrelation between average review scores and total sales: {correlation:.2f}")
