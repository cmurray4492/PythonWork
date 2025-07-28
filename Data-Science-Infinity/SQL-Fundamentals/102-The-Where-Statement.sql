select
	*
from
	grocery_db.customer_details
where
	distance_from_store < 2 and
	gender = 'M';
	

select
	*
from
	grocery_db.customer_details
where
	distance_from_store < 2 or
	gender = 'M';


select
	*
from 
	grocery_db.campaign_data;


select
	*
from 
	grocery_db.campaign_data
where 
	mailer_type in ('Mailer1', 'Mailer2');


select
	*
from 
	grocery_db.campaign_data
where 
	mailer_type like '%Mailer%';




