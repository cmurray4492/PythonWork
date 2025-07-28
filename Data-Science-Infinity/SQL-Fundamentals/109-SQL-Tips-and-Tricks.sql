-------------------------------------------------
-- Tips and Tricks
-------------------------------------------------


-- Lead and Lag

create temp table cust_trans as (
select 	
	distinct
	customer_id, 
	transaction_id,
	transaction_date
	
from
	grocery_db.transactions
	
where
	customer_id in (1,2)
);

-- select * from cust_trans;

select 
	*,
	lag(transaction_date, 1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag1,
	lag(transaction_date, 2) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag2,
	lead(transaction_date, 1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lead1
	
from
	cust_trans;


-- Rounding Data

select 
	*,
	round(sales_cost, 1) as round_sales_costs_1,
	round(sales_cost, 0) as round_sales_costs_0
from 
	grocery_db.transactions
where
	customer_id=1;



-- Random Sampling 

select 
	*
from 	
	grocery_db.customer_details
order by 
	random()
limit
	100;
	

-- Working with Dates

select 
	distinct 
	transaction_date,
	date_part('day', transaction_date) as day,
	date_part('month', transaction_date) as month,
	date_part('year', transaction_date) as year,
	date_part('dow', transaction_date) as dow
from 
	grocery_db.transactions
order by 
	transaction_date;


-- Working with Text

select 
	product_area_name,
	upper(product_area_name) as pan_upper,
	lower(product_area_name) as pan_lower,
	char_length(product_area_name) as pan_length,
	concat(product_area_name, ' - ', 'Department') as pan_concat
from
	grocery_db.product_areas;
	



