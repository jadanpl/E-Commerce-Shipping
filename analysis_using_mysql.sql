USE shipping_rating;
SELECT * FROM ecommerce_shipping_rating;
DESCRIBE ecommerce_shipping_rating;

-- (Q1) Average customer rating for orders (delivered with ship and have an avarage discount of at least 3%) based on the number of customer care calls made 
-- Method 1
SELECT Customer_care_calls, AVG(Customer_rating) AS avg_rating, AVG(Discount_offered) AS avg_discount
FROM (
    SELECT Customer_care_calls, Customer_rating, Discount_offered
    FROM ecommerce_shipping_rating
    WHERE Mode_of_Shipment="Ship"
) AS x
GROUP BY Customer_care_calls
HAVING avg_discount>3
ORDER BY avg_rating DESC;

-- Method 2
SELECT Customer_care_calls, AVG(Customer_rating) AS avg_rating, AVG(Discount_offered) AS avg_discount
FROM ecommerce_shipping_rating
WHERE Mode_of_Shipment="Ship"
GROUP BY Customer_care_calls
HAVING avg_discount>3
ORDER BY avg_rating DESC;

-- (Q2) Distribution of late & on time orders based on the mode of shipment
SELECT a.Mode_of_Shipment, (b.Total_Orders-a.Late_Orders) AS OnTime_Orders, 
	   (ROUND((b.Total_Orders-a.Late_Orders)/10999*100,2)) AS Pct_OnTime_Orders,
       a.Late_Orders, (ROUND(a.Late_Orders/10999*100,2)) AS Pct_Late_Orders, 
       b.Total_Orders
FROM (
	SELECT Mode_of_Shipment, COUNT(*) AS Late_Orders
	FROM ecommerce_shipping_rating
	WHERE Arrival=1
	GROUP BY Mode_of_Shipment) AS a
INNER JOIN(
	SELECT Mode_of_Shipment, COUNT(*) AS Total_Orders
	FROM ecommerce_shipping_rating
	GROUP BY Mode_of_Shipment) AS b
ON a.Mode_of_Shipment=b.Mode_of_Shipment;

-- (Q3) Any significant difference in the cost of products (max, min, avarage) for each customer rating level?
-- (Q3) If the rating is greater than 3, label the order as 'High Rated'. 
-- (Q3) If the rating is less than 3, label the order as 'Low Rated'. else label the order as 'Medium rated'.
SELECT 
    CASE
        WHEN Customer_rating > 3 THEN 'High Rated'
        WHEN Customer_rating < 3 THEN 'Low Rated'
        ELSE 'Medium Rated'
    END AS rating_level,
    Product_importance AS importance,
    COUNT(ID) AS num_of_orders,
    MAX(Cost_of_the_Product) AS max_product_cost,
    MIN(Cost_of_the_Product) AS min_product_cost,
    ROUND(AVG(Cost_of_the_Product), 2) AS avg_product_cost
FROM ecommerce_shipping_rating
GROUP BY Rating_Level , Product_importance
ORDER BY CASE
    WHEN Rating_Level = 'High Rated' THEN 1
    WHEN Rating_Level = 'Medium Rated' THEN 2
    WHEN Rating_Level = 'Low Rated' THEN 3
END DESC , CASE
    WHEN Product_importance = 'low' THEN 1
    WHEN Product_importance = 'medium' THEN 2
    WHEN Product_importance = 'high' THEN 3
END ASC;

-- Differences in customer rating for highly important products that were delivered via ship based on gender and prior purchases
SELECT Gender, Prior_purchases, AVG(Customer_rating) AS Avg_Rating
FROM ecommerce_shipping_rating
WHERE Mode_of_Shipment NOT IN ('Flight','Road') AND Product_importance="High"
GROUP BY Gender, Prior_Purchases
ORDER BY Prior_Purchases ASC;
