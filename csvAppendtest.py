

from os import chdir

from datetime import datetime, timedelta
from time import time
import pandas as pd
import re
import os
import csv

import sys


directoryvar = '/Users/freethebuddha/cloudstation/development/eve/test'    #establish directory
                                                        
chdir(directoryvar)    #change to that directory

import csv
#IRIS = "output.csv"#
#IRIS_data = "output1.csv"

#with open(IRIS, 'r', newline='') as f, open(IRIS_data, 'a', newline='') as data:
#    next(f)  # Skip over header in input file.
#    writer = csv.writer(data, quoting=csv.QUOTE_ALL)
#    writer.writerows(line.split() for line in f)


#df = pd.read_csv('output.csv')
#df.to_csv('outputCopy.csv','a',index=False, sep=',')

#cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
#cities.to_csv('cities.csv')

#dfs = [pd.read_csv(f, index_col=[0], parse_dates=[0])
#        for f in os.listdir(os.getcwd()) if f.endswith('csv')]

#finaldf = pd.concat(dfs, axis=1, join='inner').sort_index()
#print('done concate')
#finaldf.to_csv('test.csv', sep=',')



import glob

path = r'/Users/freethebuddha/cloudstation/development/eve/test' # use your path

all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:

    df = pd.read_csv(filename, index_col=None, header=0)

    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print('test')
frame.to_csv('test.csv', sep=',')



