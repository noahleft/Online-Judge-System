#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Content-type: text/html")
print("")
#import cgitb
#cgitb.enable()

import cgi
form=cgi.FieldStorage()
idxList=[str(x) for x in range(1,7)]
if not form.getvalue('idx') in idxList:
  exit(-1)
prefix='hw'+form.getvalue('idx')
import sqlite3
conn=sqlite3.connect(prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT NAME,LAST_ACCURACY,LAST_RUNTIME,SEMAPHORE,LAST_SUBMIT from board WHERE SCORE!=-1 OR SEMAPHORE=1 OR TIME!=0 ORDER BY LAST_SUBMIT;")

user_db=sqlite3.connect('user.db')
user_cursor=user_db.cursor()
user_cursor.execute("SELECT NAME,DISPLAY from user;")

user_pair=user_cursor.fetchall()
user_map={}
for element in user_pair:
  user_map[element[0]]=element[1]

import time

print('''
<!DOCTYPE html>
<html>
<head>
<title>2014 Fall NCTUEE Data Structure</title>
<meta charset="UTF-8">
<link href="Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">''')
print('<h1>Data Structure '+prefix+' last upload result</h1>')
print('<h3>ACCURACY=0  RUNTIME=120 means Example case fail.</h3>')
print('<h3>ACCURACY=0  RUNTIME=999 means Program fail.</h3>')
print('<h4>Possible fail reason:<br>')
print('EXAMPLE CASE Fail, Segmentation fault, Memory Overflow, TIMEOUT or FLOAT POINT EXCEPTION!</h4>')
print('<h4>We set max run time as <font color="#FF0000">600sec</font>. Forever run means program is killed by system.(mostly, segmentation fault)</h4>')
print('<table>')
print("<th>NAME</th><th>LAST ACCURACY</th><th>LAST RUN TIME</th><th>Running</th><th>UPLOAD TIME</th></tr>")
recordList=cursor.fetchall()[::-1]

import time
import datetime

def shift_time(record):
  previous=record[len(record)-1]
  previous=time.strptime(previous,'%Y-%m-%d %H:%M:%S')
  last_time=datetime.datetime(previous.tm_year,previous.tm_mon,previous.tm_mday,previous.tm_hour,previous.tm_min,previous.tm_sec)
  record[len(record)-1]=str(last_time+datetime.timedelta(hours=12))
  return record

recordList=list(map(lambda x:list(x),recordList))
recordList=list(map(shift_time,recordList))

for record in recordList:
  print('<tr>')
  if record[3]==1:
    flag='<font color="#FF9900">'
  else:
    flag='<font>'
  print('<td>'+flag+user_map[record[0]]+'</font>'+'</td>')
  for element in record[1:]:
    print('<td>'+flag+str(element)+'</font>'+'</td>')
  print('</tr>')
print('</table>')

print('''
  <footer id="foot01"></footer>
</div>

<script src="Script.js"></script>

</body>
</html>''')
