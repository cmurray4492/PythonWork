----------------------------------------------
-- SQL Windows Function
----------------------------------------------

-- Windows Function 

select 
	*,
	sum(sales_cost) over (partition by transaction_id) as transaction_total_sales,
	sales_cost / sum(sales_cost) over (partition by transaction_id) as transaction_sales_percent
from
	grocery_db.transactions;



-- Row Number and Rank 

select 
	*,
	row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number

from
	grocery_db.transactions;


-- Reference 
 


/* 
 * ROW NUMBER 
 * Will give a unique number to each row to each row of data in the set *even* if there are ties in the ortder by logic 
 */

