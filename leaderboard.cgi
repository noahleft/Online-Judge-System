#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Content-type: text/html")
print("")
#import cgitb
#cgitb.enable()

import cgi
form=cgi.FieldStorage()
idxList=[str(x) for x in range(0,7)]
if not form.getvalue('idx') in idxList:
  exit(-1)
prefix='hw'+form.getvalue('idx')
import sqlite3
conn=sqlite3.connect(prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT NAME,ACCURACY,RUNTIME,SEMAPHORE from board WHERE SCORE!=-1 OR SEMAPHORE=1 ORDER BY SCORE;")

user_db=sqlite3.connect('user.db')
user_cursor=user_db.cursor()
user_cursor.execute("SELECT NAME,DISPLAY from user;")

user_pair=user_cursor.fetchall()
user_map={}
for element in user_pair:
  user_map[element[0]]=element[1]

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
print('<h1>Data Structure '+prefix+' leaderboard</h1>')
print('<table>')
print('<tr><th>NAME</th><th>ACCURACY</th><th>RUN TIME</th><th>Running</th></tr>')
recordList=cursor.fetchall()

for record in recordList[::-1]:
  print('<tr>')
  #record[0]=user_map[record[0]]
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
