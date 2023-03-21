


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
##  ACTUAL SALES TRANSACTIONS BY PRODUCTS BY STATIONS
##
##
##
##
########################################################################################################################

directoryvar = '/Users/freethebuddha/cloudstation/development/eve'   #establish directory
                                                        
chdir(directoryvar)    #change to that directory

todaydate = datetime.today().strftime('%Y-%m-%d')

filename = "OrderIDs"+todaydate+".csv"



#TTTTTTTTEEEEEESSSSSTTTTTT

s = '2021/03/01'
date = datetime.strptime(s, "%Y/%m/%d")



#mydata = pd.read_csv("EveSalesTransactions2021-03-10.csv",skiprows=1)
#mydata = pd.read_csv("EveSalesTransactions2021-03-10.csv")


#modified_date = date + timedelta(days=1)

#read order numbers and pu in list


#create connection
con = mysql.connector.connect(host='10.0.0.32', database='Eve', user='buddhahacker', password='knight12')


#create cursor
cur = con.cursor()


new_list = []
transaction = []
ordertrans = []


#sql1 ="""SELECT order_id, FROM OrderIDs """
    
#typeidinner = typeid[i]
#data1 = (O_ID,lim)
    
cur.execute("SELECT order_id FROM OrderIDs")


new_list = cur.fetchall()


with open(filename, "w", newline="") as csv_file:
    cols = ["Order_ID"] 
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

##### outer loop needed to iterate through the orders

#create connection
con = mysql.connector.connect(host='10.0.0.32', database='Eve', user='buddhahacker', password='knight12')


#create cursor
cur = con.cursor()
sale = []
transaction = []

#for i in range(0,len(new_list)-1):
for i in range(0,1):
    cur.execute("select order_id, volume_remain, date_pulled from evesalesorders where order_id = '5737877671'") # order by date_pulled")
    ordertrans = cur.fetchall()
    #FRED = ordertrans =   cur.execute("select order_id, volume_remain from evesalesorders where order_id = '911222840'")
    #print('ordertrans',ordertrans)
    for x in range(0,len(ordertrans)-1):
        sale = ordertrans[x][1]-ordertrans[x+1][1]   # third item in x list of sales
        #print('sale=', sale)
        print('index, sale', x,sale)
        if sale > 0:
            b=[]
            for y in range(0,len(ordertrans[0])):
                b.append(ordertrans[x+1][y])
                print('b',b)
            b.append(sale)
            transaction.append(b)
            print(transaction)

        
#with open("test.csv", "w", newline="") as csv_file:
with open("test.csv","a", newline="") as csv_file:
    #cols = ["Type_ID","price","NumberSold","Volume_Remaining","Volume_Total","location","Order_ID","Date_Pulled"] 
    cols = ["Order_ID","Volume_remain", "Date_Pulled", "AmountSold"]
    #cols = [] 
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    #writer = csv.DictWriter(csv_file)
    writer.writeheader()
    writer = csv.writer(csv_file)
    try:
        
        writer.writerows(transaction)
    except:
        print('error on id:', i)
            


con.close()

#for i in range(0,len(mydata)):
#    ordernumber(i)= mydata(i,Order_ID)

#ordernumberswithdups = mydata["Order_ID"].tolist()

#ordernumbers = [] 
#for i in ordernumberswithdups: 
#    if i not in ordernumbers: 
#        ordernumbers.append(i) 
















