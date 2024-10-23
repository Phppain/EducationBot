--task 1
SELECT c.Country, 
		COUNT(*) CNT
FROM [test].[dbo].[Customers] c
WHERE c.Country = 'USA' or c.Country = 'Germany'
GROUP BY c.Country


--task 2
SELECT o.ShipCountry,
		COUNT(*) CNT
FROM [test].[dbo].[Orders] o
WHERE o.ShipCountry = 'Brazil' or o.ShipCountry = 'Switzerland' or o.ShipCountry = 'Sweden'
GROUP BY o.ShipCountry


--task 3
SELECT e.LastName, e.FirstName,
		COUNT(*) CNT
FROM [test].[dbo].[Employees] e
WHERE e.LastName = 'Suyama' and e.FirstName = 'Michael'
GROUP BY e.LastName, e.FirstName


--task 4
SELECT e.LastName, o.EmployeeID,
		COUNT(*) CNT
FROM [test].[dbo].[Employees] e 
JOIN [test].[dbo].[Orders] o ON e.EmployeeID = o.EmployeeID
GROUP BY e.LastName, o.EmployeeID


--task5
SELECT COUNT(*) Summary
FROM [test].[dbo].[Orders] o
WHERE o.OrderDate > CONVERT(date, '1997-12-31')




