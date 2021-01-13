/*
https://leetcode.com/problems/employees-earning-more-than-their-managers

查出薪水比主管高的人
*/

select e.Name as Employee from Employee e
join Employee m on m.id = e.ManagerId
where e.Salary > m.Salary
