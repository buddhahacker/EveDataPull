use Eve;
CREATE TABLE ActiveOrders AS 
  SELECT distinct Order_id
  FROM evebuysales0922
  WHERE volume_remain < volume_total ;
  
ALTER TABLE ActiveOrders ADD counter int(11) DEFAULT '0' NOT NULL;
SELECT @n:=0;
UPDATE ActiveOrders SET counter = @n := @n + 1;
