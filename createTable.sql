CREATE DATABASE ecommerce_sales;

\c ecommerce_sales

CREATE TABLE sales_data (
    product_id INT,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price DECIMAL,
    review_score DECIMAL,
    review_count INT,
    sales_month_1 INT,
    sales_month_2 INT,
    sales_month_3 INT,
    sales_month_4 INT,
    sales_month_5 INT,
    sales_month_6 INT,
    sales_month_7 INT,
    sales_month_8 INT,
    sales_month_9 INT,
    sales_month_10 INT,
    sales_month_11 INT,
    sales_month_12 INT
);
