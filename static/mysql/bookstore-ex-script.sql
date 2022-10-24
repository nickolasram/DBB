use oscarbooks;

WITH expenses AS (
	SELECT DISTINCT productid, 
	prdname,
	SUM(stxnquantity) OVER(PARTITION BY stxnitem.productid) AS qty_sold,
	SUM(stxnunitprice * stxnquantity) OVER(PARTITION BY stxnitem.productid) AS revenue_from_item,
	prddescription
	FROM stxnitem
	JOIN inventory
	USING(productid)
	JOIN products
	USING(productid)),
sales AS (
	SELECT DISTINCT productid, 
	prdname,
	SUM(ptxnquantity) OVER(PARTITION BY ptxnitem.productid) AS qty_bought,
	SUM(ptxnunitprice * ptxnquantity - ptxndiscount) OVER(PARTITION BY ptxnitem.productid) AS expense_on_item,
	prddescription
	FROM ptxnitem
	JOIN inventory
	USING(productid)
	JOIN products
	USING(productid))
SELECT sales.prdname,
expense_on_item,
revenue_from_item, 
revenue_from_item - expense_on_item AS profit_off_item,
ROUND(qty_sold / qty_bought, 2) * 100 AS percent_of_product_moved
FROM sales
JOIN expenses
USING(productid);

SELECT DISTINCT prdname AS product,
SUM(stxnquantity) OVER(PARTITION BY productid) AS 'qty sold',
SUM(stxnunitprice * stxnquantity) OVER(PARTITION BY productid) AS product_total,
SUM(stxnunitprice * stxnquantity) OVER() AS total
FROM stxnitem
JOIN products
USING(productid);

SELECT stxndate,
ROUND(AVG(stxnamount) OVER(), 2) AS avg_sale_by_date,
SUM(stxnamount) OVER(PARTITION BY stxndate) AS total_sales_per_date,
SUM(stxnamount) OVER(PARTITION BY stxndate) - ROUND(AVG(stxnamount) OVER(), 2)
	AS deviation_from_avg
FROM salestransactions;
