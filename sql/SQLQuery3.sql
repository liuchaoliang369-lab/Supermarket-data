
/*
insert into dbo.country (name,avg_unitprice,sum_unitprice,year)
select Country,avg(UnitPrice),sum(UnitPrice),YEAR(InvoiceDate) from saletable
group by Country,YEAR(InvoiceDate);
*/

/*
select * from dbo.country order by name  asc;
select sum(sum_unitprice) from dbo.country;
select sum(UnitPrice) from dbo.saletable;
*/

/*
create table counties_month
(
	country varchar(20),
	year_month datetime,
	sum_unitprice float
);
select * from counties_month;
*/

--alter table counties_month alter column year_month nvarchar(10);

/*
insert into counties_month(country,year_month,sum_unitprice)
select
	Country,format(InvoiceDate,'yyyy-MM'),sum(UnitPrice)
from saletable
group by Country,format(InvoiceDate,'yyyy-MM');
*/


/*
--去重复

WITH cte AS (
  SELECT 
    *,
    ROW_NUMBER() OVER (
      PARTITION BY country, year_month, sum_unitprice
      ORDER BY (SELECT 0)
    ) AS rn
  FROM dbo.counties_month
)
DELETE FROM cte WHERE rn > 1;

*/

/*
WITH cte AS (
  SELECT *,
         ROW_NUMBER() OVER (
           PARTITION BY country, year_month
           ORDER BY (SELECT 0)
         ) AS rn
  FROM dbo.counties_month
)
DELETE FROM cte WHERE rn > 1;
*/


select * from counties_month
order by year_month,sum_unitprice DESC;

