use Eve;
CREATE TABLE ActiveOrders AS 
  SELECT distinct Order_id
  FROM EveSales
  WHERE volume_remain < volume_total ;
