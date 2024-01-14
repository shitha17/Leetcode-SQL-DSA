WITH CTE AS (
    SELECT 
        id, 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS previous_num,
        LAG(num, 2) OVER (ORDER BY id) AS previous_num_2,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_num_2
    FROM 
        Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM CTE
WHERE (num = previous_num AND num = previous_num_2) 
   OR (num = next_num AND num = next_num_2);
