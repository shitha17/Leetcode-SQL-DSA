# Write your MySQL query statement below
SELECT user_name as results FROM
(
    SELECT b.name as user_name,COUNT(*) as counts FROM MovieRating as a
    JOIN Users as b
    ON a.user_id=b.user_id
    GROUP BY a.user_id
    ORDER BY counts DESC,user_name ASC LIMIT 1
) first_query
UNION ALL
SELECT movie_name as results FROM
(
    SELECT d.title as movie_name,AVG(c.rating) as grade FROM MovieRating as c
    JOIN Movies as d
    ON c.movie_id=d.movie_id
    WHERE SUBSTR(c.created_at,1,7)="2020-02"
    GROUP BY c.movie_id
    ORDER BY grade DESC,movie_name ASC LIMIT 1
) second_query;