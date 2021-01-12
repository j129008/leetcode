/*
https://leetcode.com/problems/combine-two-tables/submissions/

left join 應用
*/
select FirstName, LastName, City, State from Person p
left join Address a on
p.PersonId = a.PersonId
