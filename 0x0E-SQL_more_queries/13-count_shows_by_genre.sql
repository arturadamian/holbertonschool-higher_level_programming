-- script that lists all shows contained in hbtn_0d_tvshows
SELECT tv_genres.name AS genre, count(*) AS number_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id WHERE tv_show_genres.show_id IS NOT NULL GROUP BY genre ORDER BY number_shows DESC;
