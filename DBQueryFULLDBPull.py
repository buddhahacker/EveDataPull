

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

#create connection
con = mysql.connector.connect(host='localhost', database='eve1', user='root', password='knight12')


#create cursor
cur = con.cursor()





cur.execute("SELECT * FROM klefmsanalysis ")

myresult = cur.fetchall()


#print(myresult)


directoryvar = '/Users/freethebuddha/cloudstation/development/eve/ANALYSIS'   #establish directory 
                                                        
chdir(directoryvar)    #change to that directory
filename = "FULLDBPull"+todaydate+".csv"
writer = csv.writer(open('QueryANALYSIS'+filename, 'w'))
writer.writerows(myresult)


con.close()
print('Select successfully executed')
