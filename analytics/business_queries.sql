-- Monthly revenue
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(revenue) AS total_revenue
FROM analytics.fact_orders
GROUP BY 1
ORDER BY 1;

-- Top products
SELECT
    p.product_category,
    SUM(f.revenue) AS revenue
FROM analytics.fact_orders f
JOIN analytics.dim_products p
ON f.product_id = p.product_id
GROUP BY 1
ORDER BY revenue DESC
LIMIT 10;
