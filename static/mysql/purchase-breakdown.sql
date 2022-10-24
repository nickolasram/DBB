USE oscarbooks;
-- return a breakdown of purchase expenses including money per vendor, biggest purchases, average purchase
-- total purchases, and percentage of purchases for each vendor
SELECT DISTINCT venname AS vendor,
SUM(ptxntotal) OVER(PARTITION BY vendorid) AS paid_to_vendor,
MAX(ptxntotal) OVER(PARTITION BY vendorid) AS max_paid_to_vendor,
ROUND(AVG(ptxntotal) OVER(), 2) AS average_purchase,
SUM(ptxntotal) OVER() AS total_purchases,
ROUND(SUM(ptxntotal) OVER(PARTITION BY vendorid) / SUM(ptxntotal) OVER(), 2) AS percentage_of_purchases
FROM purchasetransactions
JOIN vendors
USING(vendorid)
ORDER BY percentage_of_purchases DESC;
