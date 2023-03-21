


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
import numpy as np


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



s = '2021/04/01'
date = datetime.strptime(s, "%Y/%m/%d")






#modified_date = date + timedelta(days=1)

#read order numbers and pu in list





new_list = []
activelist = []
transaction = []
ordertrans = []


##############      LOAD DAILY PULL    ##########################

column_names = ["Duration", "BuyOrder", "IssueDate", "location", "minimumvolume", "order_id", "price", "locationname", "systemid", "typeid", "volume_remain", "volume_total",  "date_pulled"]
df = pd.read_csv("ConsolidatedDailyPull.csv", names=column_names)

 #TODO VERIFY DF CAN BE ITERATED


##############      LOOP THROUGH DF    ##########################

##### outer loop needed to iterate through the orders

##############      IF REMAIN VOL<TOTAL   #######################





##############      GRAB ORDER_ID    ##########################


##############      PULL ALL RECORDS FROM DB RELATED TO ORDER_ID    ##########################
print('going to next con')
#create connection
#con = mysql.connector.connect(host='10.0.0.7', database='Eve', user='buddhahacker', password='knight12')
con = mysql.connector.connect(host='localhost', database='Eve', user='root', password='knight12')
#con = mysql.connector.connect(host='DONT_RUN', database='Eve', user='root', password='knight12')


#create cursor
cur = con.cursor()
sale = []
transaction = []
OrderIDVal = 0
ordertrans = []




typeid = df.TheID.to_list()    ####  Using the TypeIDs in the The Forge file
print('len of new_list=', len(new_list))


#for x in range(0,len(activelist),2):   #############this increments the index x by 2 and limit reduced by 1 so I don't get out of bounds condition

                          ######problem is that in increment through the new_list doesn't need to occur if only pulling 1 fixed order_id
                           #### why do i need a tuple??  Why not just import the list of ints?  FIXED
                                                                                    #### Code for sales evaluation working correctly 5787862344 only has 5 days of trans over 32 days
    

new_list = l


problemcounter=0

for i in range(0,len(new_list)):                            #### 7-7 error review Change
#for i in range(0,2):   
    OrderIDVal = 0
    OrderIDVal = new_list[i]                   #### 4-26 Change
                
    TESTPULL = []
 

    
    sql1 ="""SELECT price, volume_remain, volume_total, location_id, order_id, date_pulled, type_id FROM EveSales0721 where order_id = %s limit %s"""
    #sql1 ="""SELECT price, volume_remain, volume_total, location_id, order_id, date_pulled FROM EveSales0721 where order_id = %s"""


    lim = 90   # This is the maximum number of days a character contract can be active in eve
    data1 = (OrderIDVal,lim)  #7-7 change to check error items
    #data1 = (OrderIDVal)
    #data1 = (6027617026,lim)
    cur.execute(sql1,data1)
    
    TESTPULL = cur.fetchall()
    

    if i == 100: 
        print('100',i)   
    if i == 500: 
        print('500',i)    
    if i == 1000: 
        print(i)  
        now = datetime.now()
        print("now =", now)
    if i == 5000: 
        print(i)               
        now = datetime.now()
        print("now =", now)      
    if i == 10000: 
        print(i) 
    if i == 15000: 
        print(i) 
    if i == 25000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 35000: 
        print(i) 
    if i == 45000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 55000: 
        print(i) 
    if i == 60000: 
        print(i) 
    if i == 70000: 
        print(i) 
    if i == 80000: 
        print(i) 
        now = datetime.now()
        print("now =", now)
    if i == 90000: 
        print(i) 
    if i == 100000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 110000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 120000: 
        print(i) 
    if i == 130000: 
        print(i) 
    if i == 140000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 150000: 
        print(i)         
        now = datetime.now()
        print("now =", now)
    if i == 160000: 
        print(i) 


##############      FIND TOTAL LEN AND THEN ONLY USE LAST ITEM FROM PULL    ##########################

#THIS IS NEVER EXECUTING
    for row in TESTPULL:            #when commented out the program fails
        oput=(typeid[1],row)           #put in 1 rather than i due to out of range condition                                                   
        (typid, tup)=oput   #pulling out the TYPE_ID
        o1=tup[0]           #1st element of SELECT statement    PRICE
        o2=tup[1]           #2nd element of SELECT statment     Volume_Remaining
        o3=tup[2]           #3rd element of SELECT statement    Volume_Total
        o4=tup[3]           #4th element of SELECT statment     location_id
        o5=tup[4]           #5th element of SELECT statment     Order_id
        o6=tup[5]           #6th element of SELECT statment     Date_Pulled
        o7=tup[6]           #7th element of Select Statment     TypeID                         
        
        rlist= o7,o1,o2,o3,(o3-o2),o4,o5,o6
        ordertrans.append(rlist)
       
    #print('i', i)


    ############ ORDERTRANS IS CUMULATIVE 
    ############ Data is being pulled correctly
    ############ Access data using ordertrans[row][entry]



##############      DUE CALC IF CURRENT REM IS < LAST REM    ##########################

sale = int    

for x in range(0,len(ordertrans)-1):   #calcuations is today's date data - tommorrow's date data
    s=0     #initialize so as to not pull in prior records data
    if ordertrans[x][6] == ordertrans[x+1][6]:
        print('test for order_trans', ordertrans[x][6], ordertrans[x+1][6])


        sale = ordertrans[x][2]-ordertrans[x+1][2]   # second item in x list of sales contains the number sold
        print('sale',sale)

        if sale > 0:
            b=[]
            for y in range(0,len(ordertrans[0])):           ##### why length of entry 0?  Does it matter? NO
                #b.append(ordertrans[x+1][y])             ##### place 2nd entry into database since it is the day the sale occurred
                b.append(ordertrans[x+1][y])               #puts the data in each entry location for the record
            b.append(sale)                                  #Adds the sales amount to the end of the record
            transaction.append(b)                           #Adds the full record the list of transaction records
            print('sale transaction',sale, '  b',b)


##############      LOOP BACK THROUGH DAILY SALES INCREMENTING ONE    ##########################

filenamesales = "Sales"+todaydate+".csv"

with open(filenamesales,"a", newline="") as csv_file:
    
    cols = ["Type_ID", "Price", "Volume_remain", "Volume_Total", "Sales to Date", "Location_id", "Order_ID","Date_Pulled", "SOLD THAT DAY"]
    
    writer = csv.DictWriter(csv_file, fieldnames=cols)
  
    writer.writeheader()
    writer = csv.writer(csv_file)
    try:
        
        writer.writerows(transaction)
    except:
        print('error on id:', i)
            


con.close()


















