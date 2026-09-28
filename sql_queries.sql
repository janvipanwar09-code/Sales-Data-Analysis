-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales_data;


-- Product-wise Sales
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;


-- Category-wise Sales
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Category
ORDER BY Total_Sales DESC;


-- Region-wise Sales
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region
ORDER BY Total_Sales DESC;


-- Highest Selling Product
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 1;


-- Monthly Sales
SELECT
    DATE_FORMAT(Date, '%Y-%m') AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Month
ORDER BY Month;
