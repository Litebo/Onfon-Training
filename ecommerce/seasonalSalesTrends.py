import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
file_path = "./ecommerce_sales_analysis.csv"
data = pd.read_csv(file_path)

# Calculate monthly sales for all products
monthly_sales = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=0)

# Calculate average monthly sales
average_monthly_sales = data.loc[:, 'sales_month_1':'sales_month_12'].mean(axis=0)

# Create a DataFrame for monthly sales
months = [f'sales_month_{i}' for i in range(1, 13)]
monthly_sales_df = pd.DataFrame({
    'month': months,
    'total_sales': monthly_sales,
    'average_sales': average_monthly_sales
})
 
monthly_sales_df['month'] = pd.to_datetime(monthly_sales_df['month'].str.replace('sales_month_', ''), format='%m').dt.strftime('%B')

 
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales_df, x='month', y='total_sales', marker='o')
plt.title('Total Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

 
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales_df, x='month', y='average_sales', marker='o', color='orange')
plt.title('Average Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Average Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

 
monthly_sales_series = pd.Series(monthly_sales.values, index=pd.date_range(start='2023-01', periods=12, freq='M'))
decomposition = seasonal_decompose(monthly_sales_series, model='additive')

 
decomposition.plot()
plt.show()
