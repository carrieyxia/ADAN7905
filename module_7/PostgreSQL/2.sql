SELECT * FROM order_details
LIMIT 10;

-- 2.3 Write SQL query to identify top 10 selling products based on number of sales
SELECT
    products.product_id,
    products.product_name,
    SUM(order_details.quantity) AS num_sales
FROM
    products
JOIN
    order_details ON products.product_id = order_details.product_id
GROUP BY
    products.product_id, products.product_name
ORDER BY
    num_sales DESC
LIMIT 10;
-- 2.4 Write SQL query to identify top 10 selling products based on revenue (sale price after discount).
SELECT
    products.product_id,
    products.product_name,
    ROUND(SUM(order_details.quantity*order_details.unit_price - order_details.discount)::numeric, 2) AS revenue
FROM
    products
JOIN
    order_details ON products.product_id = order_details.product_id
GROUP BY
    products.product_id, products.product_name
ORDER BY
    revenue DESC
LIMIT 10;

-- 2.5 Write SQL query to identify the Supplier who has highest number of Products.
SELECT suppliers.supplier_id, suppliers.company_name, SUM(products.product_id) AS num_products
FROM suppliers
JOIN
    products ON suppliers.supplier_id = products.supplier_id
GROUP BY
    suppliers.supplier_id, suppliers.company_name
ORDER BY
    num_products DESC
LIMIT 1;

-- 2.6 Write SQL query to identify the postal_code with maximum number of Orders.
SELECT 
    ship_postal_code,ship_city, ship_region,
    COUNT(order_id) AS order_count
FROM 
    orders
GROUP BY 
    ship_postal_code, ship_city, ship_region
ORDER BY 
    order_count DESC
LIMIT 1;




