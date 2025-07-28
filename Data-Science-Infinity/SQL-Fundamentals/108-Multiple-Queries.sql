---------------------------------------------
-- Multiple Querires
---------------------------------------------

select * from grocery_db.transactions where customer_id = 1;

create temp table cust_transaction as (
select
	customer_id,
	transaction_id,
	sum(sales_cost) as total_sales
from
	grocery_db.transactions
group by
	customer_id,
	transaction_id
);

select * from cust_transaction;


select 
	customer_id,
	avg(total_sales) as avg_transaction_sales
from 
	cust_transaction
group by 
	customer_id;


-- Common table expression

with cust_transaction_cte as (
select
	customer_id,
	transaction_id,
	sum(sales_cost) as total_sales
from
	grocery_db.transactions
group by
	customer_id,
	transaction_id
)


select 
	customer_id,
	avg(total_sales) as avg_transaction_sales
from 
	cust_transaction_cte
group by 
	customer_id;

