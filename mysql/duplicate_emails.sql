/*
https://leetcode.com/problems/duplicate-emails/

查出重複的欄位
group by, count 的應用
*/

select t.Email from
    (select Email, count(Email) as num from Person p
        group by p.Email) t
where t.num > 1
