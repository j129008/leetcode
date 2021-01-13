/*
https://leetcode.com/problems/employees-earning-more-than-their-managers

查出薪水比主管高的人
*/

select e.Name as Employee from Employee e
join Employee m on m.id = e.ManagerId
and e.Salary > m.Salary  # 這裏用 where 會慢很多, 在 join 的時候一起完成
