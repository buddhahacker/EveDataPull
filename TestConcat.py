import os
from os import chdir
from glob import glob
import pandas as pdlib
import shutil
from datetime import datetime, timedelta
from time import time




# Move to the path that holds our CSV files
csv_file_path = '/Users/freethebuddha/cloudstation/development/eve/Analysis/DBload'
chdir(csv_file_path)


todaydate = datetime.today().strftime('%Y-%m-%d')

csv_header = 'duration,is_buy_order,issued,location_id,min_volume,order_id,price,range,system_id,type_id,volume_remain,volume_total,date_pulled'
# List all CSV files in the working dir

list_of_files = os.listdir('.')
print(list_of_files)

file_out = "ConsolidateOutput"+todaydate+".csv"

csv_merge = open(file_out, 'a')
csv_merge.write(csv_header)
csv_merge.write('\n')

arr = os.listdir('.')
print('Processing ', len(arr), 'files.')
g=1
while g in range (0,len(arr)):
        fileentry = arr[g]
        print('filename: ', fileentry)
        



        
        csv_in = open(arr[g]).read()
        for line in csv_in:
            #if line.startswith(csv_header):
             #   continue
            csv_merge.write(line)
        g+=1
csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' )

