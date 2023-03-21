


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
con = mysql.connector.connect(host='10.0.0.7', database='Eve', user='buddhahacker', password='knight12')


#create cursor
cur = con.cursor()


new_list = []
transaction = []
ordertrans = []
OrderIDList =[]

#sql1 ="""SELECT order_id, FROM OrderIDs """
    
#typeidinner = typeid[i]
#data1 = (O_ID,lim)
    
cur.execute("SELECT order_id FROM OrderIDs")


new_list = cur.fetchall()

fred = [] 
for i in range(0,len(new_list)): 
    fred.append(str(new_list[i][0])) 
OrderIDList = fred
print('I am with Fred')



with open(filename, "a", newline="") as csv_file:
    cols = ["Order_ID"] 
    #cols = [] 
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()
    writer = csv.writer(csv_file)
    try:
        writer.writerows(OrderIDList)
    except:
        print('error on id:', i)


con.close()
print('Select successfully executed')

##### outer loop needed to iterate through the orders
print('going to next con')
#create connection
con = mysql.connector.connect(host='10.0.0.7', database='Eve', user='buddhahacker', password='knight12')


#create cursor
cur = con.cursor()
sale = []
transaction = []
OrderIDVal = 0
ordertrans = []

column_names = ["TheID"]
df = pd.read_csv("ConsolidatedFocusedType_ID.csv", names=column_names)
#print(df)
typeid = df.TheID.to_list()    ####  Using the TypeIDs in the The Forge file



#for i in range(0,len(OrderIDList)-1):
for i in range(0,1):
    #OrderIDVal = OrderIDList[i]
    OrderIDVal = '5848328275'
   
    #print('OrderIDValue',OrderIDVal)
    #OrderIDValue = int(OrderIDVAL)
    #cur.execute("select order_id, volume_remain, date_pulled from evesalesorders where order_id = 'OrderIDValue'") # order by date_pulled")
    #ordertrans = cur.fetchall()

    
    sql1 ="""SELECT price, volume_remain, volume_total, location_id, order_id, date_pulled FROM EveSalesOrders where order_id = %s limit %s"""
    
    lim = 90   # This is the maximum number of days a character contract can be active in eve
    data1 = (OrderIDVal,lim)
    #data1 = (5737877671,lim)
    cur.execute(sql1, data1)
    #$$$ checking amount of rows pulled back
    TESTPULL = cur.fetchall()
    print('rows', TESTPULL)

#THIS IS NEVER EXECUTING
    for row in TESTPULL:            #when commented out the program fails
        oput=(typeid[i],row)                                                              
        (typid, tup)=oput   #pulling out the TYPE_ID
        o1=tup[0]           #1st element of SELECT statement    PRICE
        o2=tup[1]           #2nd element of SELECT statment     Volume_Remaining
        o3=tup[2]           #3rd element of SELECT statement    Volume_Total
        o4=tup[3]           #4th element of SELECT statment     location_id
        o5=tup[4]           #5th element of SELECT statment     Order_id
        o6=tup[5]           #6th element of SELECT statment     Date_Pulled                         
        #print('typeid',typid, 'price', o1, 'location',o2)
        rlist= typid,o1,o2,o3,(o3-o2),o4,o5,o6
        ordertrans.append(rlist)
        #print('row**********', row)
    print('i', i)


    ############ this works for individual orderIDs 4/24
    ############ Data is being pulled correctly
    ############ Access data using ordertrans[row][entry]




    #print('ordertrans', cur)
    
    #FRED = ordertrans =   cur.execute("select order_id, volume_remain from evesalesorders where order_id = '911222840'")
    #print('ordertrans',ordertrans)
    for x in range(0,len(ordertrans)-1):
 
        sale = ordertrans[x][2]-ordertrans[x+1][2]   # second item in x list of sales contains the number sold
        print('sale=', sale)
        #print('index, sale', x,sale)
        if sale > 0:
            b=[]
            for y in range(0,len(ordertrans[0])):
                b.append(ordertrans[x+1][y])
                #print('b',b)
            b.append(sale)
            transaction.append(b)
            #print(transaction)

        

with open("test.csv","a", newline="") as csv_file:
    
    cols = ["Type_ID", "Price", "Volume_remain", "Volume_Total", "Amount SOLD", "Location_id", "Order_ID","Date_Pulled"]
    
    writer = csv.DictWriter(csv_file, fieldnames=cols)
  
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
















