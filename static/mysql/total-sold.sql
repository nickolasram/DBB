USE oscarbooks;

-- Return product names, how many have sold, revenue from each sold, and total revenue
SELECT DISTINCT prdname AS product,
SUM(stxnquantity) OVER(PARTITION BY productid) AS 'qty sold',
SUM(stxnunitprice * stxnquantity) OVER(PARTITION BY productid) AS product_total,
SUM(stxnunitprice * stxnquantity) OVER() AS total
FROM stxnitem
JOIN products
USING(productid);