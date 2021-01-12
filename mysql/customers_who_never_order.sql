/*
1. subquery 的應用
2. distinct 去除重複資料減少計算量
*/
select Name as Customers from Customers
where Customers.Id not in (
    select distinct CustomerId from Orders
)
