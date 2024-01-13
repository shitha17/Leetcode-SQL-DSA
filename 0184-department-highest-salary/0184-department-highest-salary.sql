# Write your MySQL query statement below
with cte as (select d.name as Department,e.name as Employee,e.salary as salary,
dense_rank() over(partition by d.id order by salary desc) as rn from Employee e
join Department d on
e.departmentId=d.id)

select Department,Employee,Salary from cte where rn=1;
