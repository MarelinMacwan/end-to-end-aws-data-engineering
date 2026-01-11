-- Monthly Revenue
SELECT
    DATE_TRUNC('month', order_purchase_timestamp::timestamp) AS month,
    SUM(revenue::numeric) AS total_revenue
FROM analytics.fact_orders_stage1
GROUP BY 1
ORDER BY 1;

-- Top Categories
SELECT
    product_category_name,
    SUM(revenue::numeric) AS revenue
FROM analytics.fact_orders_stage1
GROUP BY product_category_name
ORDER BY revenue DESC
LIMIT 10;

-- Customer-Level Revenue
SELECT
    customer_id,
    SUM(revenue::numeric) AS total_revenue
FROM analytics.fact_orders_stage1
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 20;



