USE oscarbooks;

-- return average revenue per day, total per day, and how far below/above the day's
-- revenue compares to the average
SELECT stxndate,
ROUND(AVG(stxnamount) OVER(), 2) AS avg_sale_by_date,
SUM(stxnamount) OVER(PARTITION BY stxndate) AS total_sales_per_date,
SUM(stxnamount) OVER(PARTITION BY stxndate) - ROUND(AVG(stxnamount) OVER(), 2)
	AS deviation_from_avg
FROM salestransactions;