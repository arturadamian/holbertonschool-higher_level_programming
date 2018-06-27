-- lists all the cities of California that can be found in the database
SELECT name FROM hbtn_0d_usa.cities WHERE state_id =
(select id from hbtn_0d_usa.states WHERE name = 'California');
