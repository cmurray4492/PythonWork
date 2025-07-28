------------------------------------------------
-- JOINIUNG tables 
------------------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.loyalty_scores;

-- INNER JOIN
select 
	a.*,
	b.customer_loyalty_score

from
	grocery_db.customer_details a
	inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;

-- LEFT JOIN 
select 
	a.*,
	b.customer_loyalty_score

from
	grocery_db.customer_details a
	left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;


-- ADDING OTHER LOGIC 
select 
	a.*,
	b.customer_loyalty_score
from
	grocery_db.customer_details a
	left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
where 
	customer_loyalty_score > 0.5;


-- JOINGING MULTIPULE TABLES 
select 
	a.*,
	b.customer_loyalty_score,
	c.product_area_name
from
	grocery_db.transactions a
	left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
	inner join grocery_db.product_areas c on a.product_area_id = c.product_area_id;


-- OTHER JOIN TYPES











