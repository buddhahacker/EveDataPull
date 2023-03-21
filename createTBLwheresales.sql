use Eve;
CREATE TABLE evesales AS 
  SELECT *
  FROM EveSalesOrders
  WHERE volume_remain < volume_total;