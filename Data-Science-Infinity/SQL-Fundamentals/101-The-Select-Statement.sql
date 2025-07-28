---------------------------------------
THE BASIC select statement
---------------------------------------

-- THE SELECT STATEMENT 

select 
	* 


from 
	grocery_db.customer_details


-- ORDER BY
order by
	distance_from_store,
	credit_score


-- DISTINCT 
	
select
	distinct
	* 

from 
	grocery_db.customer_details;


-- DISTINCT 
	
select
	distinct
	gender
	

from 
	grocery_db.customer_details;
	
	



-- GIVING COLUMNS AND ALIAS 

select
	distance_from_store as distance_to_store,
	customer_id as customer_number

from 
	grocery_db.customer_details;


	
-- CREATIG NEW COLUMNS 

select
	distance_from_store as distance_to_store,
	customer_id as customer_number,
	1 as new_col, 
	distance_from_store * 1.6 distance_from_store_km

from 
	grocery_db.customer_details;

