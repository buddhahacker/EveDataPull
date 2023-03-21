
from os import chdir
import pandas as pd
from datetime import datetime, timedelta
from time import time
import PyPDF2
import re
import os
import csv
import requests
import sys
import mysql.connector


########################################################################################################################
##  SALES VELOCITY FOR PRODUCTS SOLD IN FLEMK
##
##
##
##
########################################################################################################################

directoryvar = '/Users/freethebuddha/cloudstation/development/eve'   #establish directory
                                                        
chdir(directoryvar)    #change to that directory

todaydate = datetime.today().strftime('%Y-%m-%d')

filename = "EveSalesOrders_VELOCITY"+todaydate+".csv"

#create connection
con = mysql.connector.connect(host='localhost', database='Eve', user='root', password='knight12')


#create cursor
cur = con.cursor()


column_names = ["TheID"]
df = pd.read_csv("ConsolidatedFocusedType_ID.csv", names=column_names)
#print(df)

typeid = df.TheID.to_list()    ####  Using the TypeIDs in the The Forge file






lim = 1000
new_list = []

for i in range(0,len(typeid)):
    sql1 ="""SELECT price, volume_remain, volume_total, location_id, order_id, date_pulled FROM EveSalesOrders where type_id = %s limit %s"""
    
    typeidinner = typeid[i]
    data1 = (typeidinner,lim)
    
    cur.execute(sql1, data1)
    print(typeidinner)
    
    j=0
    for row in cur:            #when commented out the program fails
        oput=(typeid[i],row)
        (typid, tup)=oput   #pulling out the TYPE_ID
        o1=tup[0]           #1st element of SELECT statement    PRICE
        o2=tup[1]           #2nd element of SELECT statment     Volume_Remaining
        o3=tup[2]           #3rd element of SELECT statement    Volume_Total
        o4=tup[3]           #4th element of SELECT statment     location_id
        o5=tup[4]           #5th element of SELECT statment     Order_id
        o6=tup[5]           #6th element of SELECT statment     Date_Pulled                         
        #print('typeid',typid, 'price', o1, 'location',o2)
        rlist= typid,o1,(o3-o2),o2,o3,o4,o5,o6
        new_list.append(rlist)
        j+=1
        #print(row)

with open(filename, "w", newline="") as csv_file:
    cols = ["Type_ID","price","NumberSold","Volume_Remaining","Volume_Total","location","Order_ID","Date_Pulled"] 
    #cols = [] 
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()
    writer = csv.writer(csv_file)
    try:
        
        writer.writerows(new_list)
    except:
        print('error on id:', i)


con.close()
print('Select successfully executed')
