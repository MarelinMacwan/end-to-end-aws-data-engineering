CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.dim_customers (
    customer_id VARCHAR(50),
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS analytics.dim_products (
    product_id VARCHAR(50),
    product_category VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS analytics.fact_orders (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    order_date TIMESTAMP,
    quantity INT,
    revenue DECIMAL(10,2)
);
