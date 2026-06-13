
USE ecommerce_db;
select * from cleaned_ecommerce;

-- Orders with Shipped status
SELECT * FROM cleaned_ecommerce
WHERE OrderStatus = 'Shipped';

-- Orders where Quantity > 3
SELECT * FROM cleaned_ecommerce
WHERE Quantity > 3;

-- Most expensive orders first
SELECT OrderID, Product, UnitPrice
FROM cleaned_ecommerce
ORDER BY UnitPrice DESC;

-- Total orders per Product
SELECT Product, COUNT(*) AS TotalOrders
FROM cleaned_ecommerce
GROUP BY Product;

-- Average UnitPrice per Product
SELECT Product, AVG(UnitPrice) AS AvgPrice
FROM cleaned_ecommerce
GROUP BY Product;

-- Total Revenue per Product (SUM)
SELECT Product, SUM(Quantity * UnitPrice) AS TotalRevenue
FROM cleaned_ecommerce
GROUP BY Product
ORDER BY TotalRevenue DESC;

-- Orders count by OrderStatus
SELECT OrderStatus, COUNT(*) AS Count
FROM cleaned_ecommerce
GROUP BY OrderStatus;


