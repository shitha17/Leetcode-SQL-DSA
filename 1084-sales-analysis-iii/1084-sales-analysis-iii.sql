SELECT p.product_id,p.product_name
FROM Product p
LEFT JOIN Sales s
ON p.product_id=s.product_id
GROUP BY s.product_id
HAVING MIN(s.sale_date)>'2018-12-31' AND MAX(s.sale_date)<'2019-04-01'