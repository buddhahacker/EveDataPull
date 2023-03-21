
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


directoryvar = '/Users/freethebuddha/cloudstation/development/eve'   #establish directory
                                                        
chdir(directoryvar)    #change to that directory

todaydate = datetime.today().strftime('%Y-%m-%d')
filename = "Forge_Sales_Volume"+todaydate+".csv"

#create connection
con = mysql.connector.connect(host='localhost', database='eve1', user='root', password='knight12')


#create cursor
cur = con.cursor()


column_names = ["TheForge"]
df = pd.read_csv("FocusedTypeIDForge.csv", names=column_names)
#print(df)

typeid = df.TheForge.to_list()    ####  Using the TypeIDs in the The Forge file






lim = 100
new_list = []

for i in range(0,len(typeid)):
    sql1 ="""SELECT price, location_id FROM femAnalysis where type_id = %s limit %s"""
    
    typeidinner = typeid[i]
    data1 = (typeidinner,lim)
    
    cur.execute(sql1, data1)
    print(typeidinner)
    
    j=0
    for row in cur:            #when commented out the program fails
        oput=(typeid[i],row)
        (typid, tup)=oput   #pulling out the TYPE_ID
        o1=tup[0]           #1st element of SELECT statement
        o2=tup[1]           #2nd element of SELECT statment
        #print('typeid',typid, 'price', o1, 'location',o2)
        rlist= typid,o1,o2
        new_list.append(rlist)
        j+=1
        #print(row)

with open(filename, "w", newline="") as csv_file:
    cols = ["Type_ID","price","location"] 
    #cols = [] 
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()
    writer = csv.writer(csv_file)
    try:
        
        writer.writerows(new_list)
    except:
        print('error on id:', i)





directoryvar = '/Users/freethebuddha/cloudstation/development/eve/ANALYSIS'   #establish directory 
                                                        
chdir(directoryvar)    #change to that directory
#filename = "averageType_id=",type_id,".csv"
#writer = csv.writer(open('QueryANALYSIS'+filename, 'w'))
#writer.writerows(myresult)


con.close()
print('Select successfully executed')
