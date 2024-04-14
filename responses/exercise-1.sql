-- write your SQL here
SELECT  oi.locationId AS location_id , EXTRACT(YEAR_MONTH FROM t.datetime) AS month_year, SUM(refund.amount) AS total_refund_amount
	FROM  transactions AS t, 
		JSON_TABLE(t.details, '$.items[*]' COLUMNS(id INT PATH '$.id', amount INT PATH '$.amount')) refund
	INNER JOIN orderItems oi ON oi.id=refund.id 
	group by oi.locationId, month_year
	order by MAX(t.datetime) DESC 
	
