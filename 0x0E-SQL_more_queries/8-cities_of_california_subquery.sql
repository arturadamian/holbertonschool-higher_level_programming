-- lists all the cities of California that can be found in the database
SELECT id, name FROM cities WHERE state_id=(
select id from states WHERE name='California') ORDER BY id ASC;
