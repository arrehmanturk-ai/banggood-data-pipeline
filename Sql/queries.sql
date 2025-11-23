USE BanggoodDB;
Go
SELECT * from [dbo].[Products];

--drop table Products;

-- Query 1: Average Price per Category
SELECT 
    Category,
    AVG(Price_Clean) AS AveragePrice,
    MIN(Price_Clean) AS MinPrice,
    MAX(Price_Clean) AS MaxPrice,
    COUNT(*) AS ProductCount
FROM Products
GROUP BY Category
ORDER BY AveragePrice DESC;

-- Query 2: Average Rating per Category
SELECT 
    Category,
    AVG(Rating_Clean) AS AverageRating,
    COUNT(*) AS TotalProducts,
    SUM(CASE WHEN Rating_Clean >= 4.0 THEN 1 ELSE 0 END) AS HighRatedProducts
FROM Products
WHERE Rating_Clean > 0
GROUP BY Category
ORDER BY AverageRating DESC;

-- Query 3: Product Count per Category
SELECT 
    Category,
    COUNT(Name) AS ProductCount,
    CAST(COUNT(Name) * 100.0 / (SELECT COUNT(*) FROM Products) AS DECIMAL(5,2)) AS PercentageOfTotal
FROM Products
GROUP BY Category
ORDER BY ProductCount DESC;

-- Query 4: Top 5 Most Reviewed Items per Category
WITH RankedProducts AS (
    SELECT 
        Category,
        Name,
        Reviews_Clean,
        Rating_Clean,
        Price_Clean,
        ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Reviews_Clean DESC) AS RowNum
    FROM Products
)
SELECT 
    Category,
    Name,
    Reviews_Clean AS TotalReviews,
    Rating_Clean,
    Price_Clean
FROM RankedProducts
WHERE RowNum <= 5
ORDER BY Category, RowNum;

-- Query 5: Price Level Distribution Analysis
SELECT 
    Price_Level,
    COUNT(*) AS ProductCount,
    AVG(Price_Clean) AS AvgPrice,
    AVG(Rating_Clean) AS AvgRating,
    AVG(Reviews_Clean) AS AvgReviews,
    CAST(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Products) AS DECIMAL(5,2)) AS Percentage
FROM Products
GROUP BY Price_Level
ORDER BY 
    CASE Price_Level
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
        ELSE 4
    END;