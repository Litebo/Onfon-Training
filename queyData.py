# query_data.py
import pandas as pd
from sqlalchemy import create_engine

# Create an SQLAlchemy engine for PostgreSQL
engine = create_engine('postgresql://username:password@localhost/ecommerce_sales')

# Define the SQL query
query = """
SELECT 
    product_id, 
    product_name, 
    (sales_month_1 + sales_month_2 + sales_month_3 + sales_month_4 + sales_month_5 + 
     sales_month_6 + sales_month_7 + sales_month_8 + sales_month_9 + sales_month_10 + 
     sales_month_11 + sales_month_12) AS total_sales
FROM 
    sales_data
ORDER BY 
    total_sales DESC
LIMIT 5;
"""

# Execute the query and load the results into a DataFrame
top_5_products = pd.read_sql(query, engine)

# Display the results
print(top_5_products)
