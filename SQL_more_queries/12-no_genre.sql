-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title AS genre,tv_show_genres.genre_id AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY number_of_shows DESC;