/*
https://leetcode.com/problems/second-highest-salary/submissions/

limit, offset, order by, ifnull 應用
 */

select
    ifnull(
        (select distinct Salary from Employee e
        order by e.Salary desc
        limit 1 offset 1),
        null
    ) as SecondHighestSalary
