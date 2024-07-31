import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.formula.api import ols

file_path = "./ecommerce_sales_analysis.csv"
data = pd.read_csv(file_path)

data['total_sales_volume'] = data.loc[:, 'sales_month_1':'sales_month_12'].sum(axis=1)


data['price_pct_change'] = data['price'].pct_change().fillna(0)
data['sales_volume_pct_change'] = data['total_sales_volume'].pct_change().fillna(0)


data['PED'] = data['sales_volume_pct_change'] / data['price_pct_change']


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='price', y='total_sales_volume', hue='category')
plt.title('Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()


model = ols("total_sales_volume ~ price", data=data).fit()
print(model.summary())


plt.figure(figsize=(10, 6))
sns.regplot(x='price', y='total_sales_volume', data=data, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Regression Analysis: Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()

plt.figure(figsize=(12, 8))
sns.lmplot(x='price', y='total_sales_volume', data=data, hue='category', aspect=1.5, scatter_kws={'s':10})
plt.title('Regression Analysis by Category: Price vs. Total Sales Volume')
plt.xlabel('Price')
plt.ylabel('Total Sales Volume')
plt.show()
