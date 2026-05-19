CREATE DATABASE retail_analytics;

USE retail_analytics;

CREATE TABLE superstore (
    Row_ID INT,
    Order_ID VARCHAR(50),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(50),
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    Postal_Code VARCHAR(20),
    Region VARCHAR(50),
    Product_ID VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT
);

 SELECT * FROM superstore;

SELECT SUM(Sales) AS Total_Sales
FROM superstore;

SELECT SUM(Profit) AS Total_Profit
FROM superstore;

SELECT COUNT(`Order ID`) AS Total_Orders
FROM superstore;

SELECT 
    Region,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(*) AS Total_Orders
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT 
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT 
    Segment,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(*) AS Total_Orders
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;

SELECT 
    (`Customer Name`),
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY (`Customer Name`)
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT 
    YEAR(STR_TO_DATE((`Order Date`), '%m/%d/%Y')) AS Year,
    MONTH(STR_TO_DATE((`Order Date`), '%m/%d/%Y')) AS Month,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY 
    YEAR(STR_TO_DATE((`Order Date`), '%m/%d/%Y')), 
    MONTH(STR_TO_DATE((`Order Date`), '%m/%d/%Y'))
ORDER BY Year, Month;

SELECT 
    `Sub-Category`,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Sub-Category`
ORDER BY Total_Profit DESC;

SELECT 
    Discount,
    ROUND(AVG(Profit), 2) AS Avg_Profit
FROM superstore
GROUP BY Discount
ORDER BY Discount ASC;

SELECT 
    `Product Name`,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT 
    Region,
    Category,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region, Category
ORDER BY Region, Total_Sales DESC;

SELECT 
    `Product Name`,
    Profit,
    CASE 
        WHEN Profit > 0 THEN 'Profitable'
        WHEN Profit < 0 THEN 'Loss'
        ELSE 'Break Even'
    END AS Profit_Status
FROM superstore
LIMIT 20;

SELECT 
    `Customer Name`,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
HAVING SUM(Sales) > (
    SELECT AVG(Sales) 
    FROM superstore
)
ORDER BY Total_Sales DESC;