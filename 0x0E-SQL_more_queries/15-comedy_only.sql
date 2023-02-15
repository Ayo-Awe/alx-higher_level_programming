--  lists all Comedy shows in the database
-- hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id = (SELECT id FROM tv_genres WHERE name="Comedy")
ORDER BY tv_shows.title ASC;
