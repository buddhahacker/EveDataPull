use eve;
ALTER TABLE ActiveOrders ADD counter int(11) DEFAULT '0' NOT NULL;
SELECT @n:=0;
UPDATE ActiveOrders SET counter = @n := @n + 1;