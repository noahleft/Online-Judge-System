#!/usr/bin/python
from config import prefix

import sqlite3

conn=sqlite3.connect('/home/ec2-user/public_html/cgi-bin/'+prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT ID,NAME from board WHERE SCORE!=-1 ORDER BY SCORE;")

orderList=cursor.fetchall()[::-1]
orderList=list(map(lambda x:x[0],orderList))

for order in range(len(orderList)):
  ident=orderList[order]
  last_order=order+1
  cursor.execute("UPDATE BOARD SET LAST_ORDER="+str(last_order)+" WHERE ID="+str(ident)+";")

conn.commit()
conn.close()

