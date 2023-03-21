
import os
from os import chdir
from glob import glob
import pandas as pd
import shutil
from datetime import datetime, timedelta
from time import time





# Move to the path that holds our CSV files
csv_file_path = '/Users/freethebuddha/cloudstation/development/eve/Analysis/DBload'
chdir(csv_file_path)


todaydate = datetime.today().strftime('%Y-%m-%d')


# List all CSV files in the working dir

list_of_files = os.listdir('.')
print(list_of_files)
file_out = "Consolidate_BP_Output"+todaydate+".csv"


dfs = list()
for filename in list_of_files:    
    df = pd.read_csv(filename)    
    #dfs.append(df)
    df.to_csv(file_out, mode='a', index = False, header = False)
df.head()

#Source Path
source = '/Users/freethebuddha/cloudstation/development/eve/Analysis/DBLoad'
  
# Destination path  
destination = '/Users/freethebuddha/cloudstation/development/eve/Analysis/ToBeLoaded'
  
# Move the content of  
# source to destination 
# using shutil.copytree() as parameter 


files = os.listdir(source)

for file in files:
	new_path = shutil.copy(f"{source}/{file}", destination)
	print(new_path)  

for file in files:
    os.remove(file)  
