

from os import chdir
import sys
import mysql.connector


directoryvar = '/Users/freethebuddha/cloudstation/development/eve'   #establish directory
                                                        
chdir(directoryvar)    #change to that directory



#create connection
con = mysql.connector.connect(host='localhost', database='Eve', user='root', password='knight12')


#create cursor
cur = con.cursor()

sql = """CREATE TABLE EveSalesOrders (
        duration INT,
        is_buy_order text,
        issued datetime,
        location_id INT,
        min_volume INT,
        order_id BIGINT,
        price double,
        LocationName text,
        system_id INT,
        type_id INT,
        volume_remain INT,
        volume_total INT,
        date_pulled datetime)"""

cur.execute(sql)
con.close()
print('table successfully created')
