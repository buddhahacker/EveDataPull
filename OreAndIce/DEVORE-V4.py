
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

##################   The Forge ORE Pull #########################

print('*********************  The Forge Focused Pull ***********************')
print('         No wareables, blueprints or items much under $500k')


directoryvar = '/Users/freethebuddha/cloudstation/development/eve'   #establish directory
                                                        
chdir(directoryvar)    #change to that directory

todaydate = datetime.today().strftime('%Y-%m-%d')

def get_sell_orders(region_id, type_id, page=1):
    try:
        url = "https://esi.evetech.net/latest/markets/{}/orders/?datasource=tranquility&order_type=sell&page={}&type_id={}".format(region_id, page, type_id)
        r = requests.get(url)
        sell_orders = r.json()
    except:
        print('error pulling json at type_id:', type_id)
    return sell_orders



###################Pull in all TypeID's for The Forge to iterate through  #################################################
column_names = ["Devoid"]
df = pd.read_csv("OreIceTypeIDs.csv", names=column_names)
print(df)

typeid = df.Devoid.to_list()    ####  Using the TypeIDs in the The Forge file
print(time)


################### Iterate through the TypeIDs pulling down the data from Evetech.  Then convert and write to csv file##################################

i=3  #initializes for something over 2
while i in range(2,len(typeid)):
    T_ID=typeid[i]
    print(T_ID)
    i+=1
    try:
        Sales = get_sell_orders(10000036,T_ID) # The Forge = 10000002 Everyshore 10000037, Metropolis 10000042
    except:
        print('url data pull error at id:', i)
    #print (Sales)
    print('index:',i)

    filename = "Devoid_ORE_"+todaydate+".csv"

    with open(filename, "a", newline="") as csv_file:
        cols = ["duration","is_buy_order","issued","location_id","min_volume","order_id","price","range","system_id","type_id","volume_remain","volume_total"] 
        writer = csv.DictWriter(csv_file, fieldnames=cols)
        writer.writeheader()
        try:
            writer.writerows(Sales)
        except:
            print('error on id:', i)




###################### Remove time from data column (2) and save off into ANALYSIS directory ################################
r = csv.reader(open(filename))       #Metropolis TheForge Everyshore
lines = list(r)

#TODO fix the no data issue


baddate = lines[0][2]
strip = 'T'
gooddate = baddate.split(strip, 1)[0]

for i in range(0,len(lines)):
    baddate = lines[i][2]
    strip = 'T'
    gooddate = baddate.split(strip, 1)[0]
    lines[i][2] = gooddate
    lines[i][7] = "Devoid" 
    lines[i].append(todaydate)
    #stripped = text.split(tim, 1)[0]
    #print('lines index',i,'  line',lines[i])
    i+=1

directoryvar = '/Users/freethebuddha/cloudstation/development/eve/ANALYSIS/DBload'   #establish directory 
                                                        
chdir(directoryvar)    #change to that directory

#writer = csv.writer(open('ANALYSIS'+filename, 'w'))

#writer.writerows(lines)
f = open('ANALYSIS'+filename, 'w')

with f:

    writer = csv.writer(f)
    writer.writerows(lines)


print("***************change column name in spreadsheat to Trange from range*******************")


# TODO I need to create a db and load it from the csv or this program
# TODO Iterate over region_id and then type_id 
# TODO need to load region_id and type_id into a files
# TODO need to prompt for what region you want pulled.  Option for all regions