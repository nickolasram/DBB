USE oscarbooks;

-- finding "prefered" customer(s) who have spent a certain amount of money
SELECT * FROM (
	-- subQ of customers and totals spent
	SELECT DISTINCT CONCAT(custfname," ",custlname) AS customer,
		SUM(stxnamount) OVER(PARTITION BY salestransactions.customerid) AS total_purchases
		FROM customers
		JOIN salestransactions
		USING(customerid)) totalspercustomer
WHERE total_purchases > 1000.00;