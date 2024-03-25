# Write your MySQL query statement below
select name, balance from 
(
select u.name, sum(t.amount) as balance
from users u 
inner join transactions t
on u.account = t.account
group by u.name) as table_balance
where balance > 10000

