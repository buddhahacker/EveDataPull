
import os
from os import chdir
from glob import glob
import pandas as pd
import shutil
from datetime import datetime, timedelta
from time import time



# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   result_obj = pd.concat([pdlib.read_csv(file) for file in list_of_files])
   # Convert the above object into a csv file and export
   result_obj.to_csv(file_out, index=False, encoding="utf-8")

# Move to the path that holds our CSV files
csv_file_path = '/Users/freethebuddha/cloudstation/development/eve/test'
chdir(csv_file_path)


todaydate = datetime.today().strftime('%Y-%m-%d')


# List all CSV files in the working dir

list_of_files = os.listdir('.')
print(list_of_files)
file_out = "ConsolidateOutput"+todaydate+".csv"








dfs = list()
for filename in filesnames:    
    df = pd.read_csv(filename)    
    dfs.append(df)
frame = pd.concat(dfs, axis=0, ignore_index=True)
df.head()