create database walmart;
USE walmart;
SHOW TABLES;
describe train_full;
describe test_full;

SELECT * FROM train_full LIMIT 10;
SELECT COUNT(*) FROM test_full;

 -- Total weekly sales by store
 
SELECT Store, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY Store
ORDER BY store asc;

-- Top 5 weekly sales by store

SELECT Store, SUM(Weekly_Sales) AS Top5_Total_Sales
FROM train_full
GROUP BY Store
ORDER BY Top5_Total_Sales desc limit 5;

--  Holiday vs non holiday sales

SELECT IsHoliday_x, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY IsHoliday_x;

--  Average sales per store during holidays

SELECT Store, AVG(Weekly_Sales) AS Avg_Holiday_Sales
FROM train_full
WHERE IsHoliday_x = TRUE
GROUP BY Store
ORDER BY Avg_Holiday_Sales DESC;

-- Sales by store type

SELECT Type, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY Type;

-- Fuel price correlation check

SELECT Fuel_Price, AVG(Weekly_Sales) AS Avg_Sales
FROM train_full
GROUP BY Fuel_Price
ORDER BY Fuel_Price;

-- Temperature impact

SELECT Temperature, AVG(Weekly_Sales) AS Avg_Sales
FROM train_full
GROUP BY Temperature
ORDER BY Temperature;

-- Effect of markdown

SELECT SUM(MarkDown1 + MarkDown2 + MarkDown3 + MarkDown4 + MarkDown5) AS Total_Markdowns,
       SUM(Weekly_Sales) AS Total_Sales
FROM train_full;

-- Sales by individual markdown

SELECT AVG(MarkDown1) AS Avg_MD1, AVG(MarkDown2) AS Avg_MD2,
       AVG(MarkDown3) AS Avg_MD3, AVG(MarkDown4) AS Avg_MD4,
       AVG(MarkDown5) AS Avg_MD5, AVG(Weekly_Sales) AS Avg_Sales
FROM train_full;

-- Trend analysis
-- Monthly sales trend

SELECT MONTH(Date) AS Month, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY MONTH(Date)
ORDER BY Month;

-- Yearly sales trend

SELECT YEAR(Date) AS Year, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY YEAR(Date)
ORDER BY Year;

-- Department Performance
-- Top 5 departrment store

SELECT Store, Dept, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY Store, Dept
ORDER BY Store, Total_Sales DESC limit 5;

-- Economic factors
-- Impact of unemployment

SELECT Unemployment, AVG(Weekly_Sales) AS Avg_Sales
FROM train_full
GROUP BY Unemployment
ORDER BY Unemployment;

-- - Impact of CPI

SELECT CPI, AVG(Weekly_Sales) AS Avg_Sales
FROM train_full
GROUP BY CPI
ORDER BY CPI;

-- Holiday Deep Dive
-- Sales by holiday flag across year

SELECT YEAR(Date) AS Year, IsHoliday_x, SUM(Weekly_Sales) AS Total_Sales
FROM train_full
GROUP BY YEAR(Date), IsHoliday_x
ORDER BY Year, IsHoliday_x;

-- Forecast Preparation

SELECT AVG(Temperature) AS Avg_Temp, AVG(Fuel_Price) AS Avg_Fuel, 
       AVG(MarkDown1 + MarkDown2 + MarkDown3 + MarkDown4 + MarkDown5) AS Avg_Markdowns
FROM test_full;