A. Write a query to print successful transactions for yesterday. The result must contain: transaction_no, customer_email, amount, payment_channel_name, payment_provider_name, paid_at.

SELECT transaction_no, c.customer_email, amount, pc.payment_channel_name, pp.payment_provider_name, paid_at
FROM transaction as t
INNER JOIN customer as c on c.Id = t.customer_id
INNER JOIN payment_channel as pc on pc.code = t.payment_channel_code
INNER JOIN payment_provider as pp on pp.code = t.payment_provider_code
WHERE status = "SUCCESS" && paid_at BETWEEN CURRENT_DATE - 1 + TIME '00:00' AND CURRENT_DATE - 1 + TIME '23:59'



B. Write a query to print a list of payment channels which do not have any transaction yesterday.

SELECT name
FROM payment_channel
WHERE code NOT IN (
SELECT payment_channel_code 
FROM transaction
WHERE status = "SUCCESS" && paid_at BETWEEN CURRENT_DATE - 1 + TIME '00:00' AND CURRENT_DATE - 1 + TIME '23:59')




C. Write a query to list top 10 customers this month based on total transaction amount. In case of the same transaction amount sort by customer email. The result must contain: customer_email, total transaction amount

SELECT TOP 10 c.email, c.customer_id, SUM(amount)
FROM transaction as t
INNER JOIN customer as c on c.Id = t.customer_id
WHERE t.status = "SUCCESS" and date_part('month', (SELECT t.paid_at)) = date_part('month', (SELECT current_timestamp));
GROUP BY customer_id
ORDER BY SUM(amount) DESC, c.email




d. Write a query to list the cheapest admin fee for each payment channel. In case of the same admin fee, separate the payment provider with comma. The result must contain:
payment_channel_code, cheapest admin_fee, cheapest payment_provider

SELECT pc.name as Channel, fee.admin_fee as Fee, string_agg( pp.name, ', ' ORDER BY pp.name) as Provider
FROM payment_channel_provider_fee fee
INNER JOIN payment_channel pc on pc.code = fee.payment_channel_code
INNER JOIN payment_provider pp on pp.code = fee.payment_provider_code
WHERE fee.admin_fee = (SELECT MIN(fee.admin_fee)
			FROM payment_channel_provider_fee fee
			WHERE pc.code = fee.payment_channel_code)



e. Create any indexes that you think are necessary for the transaction table and please explain why. Please also consider storage size and writing speed in determining the indexes. 
1. Make an user index for transaction table will reduce the time query needed
2. Payment channel index also useful for data reporting for channel



f. Write any concern you have regarding this database schema and please explain why (for example if you thought of any possibly unhandled cases, unnormalized or unoptimized tables).

1. For a good logging, its better if we have different table for success payment and failed payment
2. Item id should be made a separate table to reduce memory usage