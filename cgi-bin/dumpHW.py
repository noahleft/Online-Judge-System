#!/usr/bin/python
from config import prefix
import sqlite3
conn=sqlite3.connect(prefix+'/'+prefix+'.db')
cursor=conn.cursor()
cursor.execute('select name,runtime,accuracy from board where accuracy>0 order by accuracy DESC,runtime ASC;')

data=cursor.fetchall()

import re
data=list(filter(lambda x:re.match('ds',x[0]),data))

with open(prefix+'.csv','w') as outfile:
  for record in data:
    outfile.write(str(record[0])+','+str(record[1])+','+str(record[2])+'\n')


