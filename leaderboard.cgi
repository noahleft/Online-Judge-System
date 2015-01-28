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

cursor.execute("SELECT NAME,ACCURACY,RUNTIME,LAST_ORDER from board WHERE SCORE!=-1 ORDER BY ACCURACY DESC,RUNTIME ASC;")

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
print("<tr><th class='noBorder'></th>")
#print("<th>Rank</th>")
print("<th>NAME</th><th>ACCURACY</th><th>RUN TIME</th><th>ORDER CHANGE</th></tr>")
recordList=cursor.fetchall()[::]

number=["<img src='graph/number1.svg' width='100%' />",
        "<img src='graph/number2.svg' width='100%' />",
        "<img src='graph/number3.svg' width='100%' />",
        "<img src='graph/number4.svg' width='100%' />",
        "<img src='graph/number5.svg' width='100%' />"]
img_up="<img src='graph/up.svg' width='20' />"
img_down="<img src='graph/down.svg' width='20' />"
img_blood="<img src='graph/new_blood.svg' width='20' />"

def calRank(acc,com,ref):
  if acc==100:
    if com-ref<=15:
      return '<font>'+str(int((com-ref)/2.5)+1)+'</font>'
    else:
      return 'none'
  return ''

for record in recordList:
  print('<tr>')
  if recordList.index(record)<=4:
    print('<td class="noBorder">'+number[recordList.index(record)]+'</td>')
  else:
    print('<td class="noBorder">'+str(recordList.index(record)+1)+'</td>')
  #print('<td>'+str(calRank(record[1],record[2],recordList[0][2]))+'</td>')
  flag='<font>'
  print('<td>'+flag+user_map[record[0]]+'</font>'+'</td>')
  for element in record[1:len(record)-1]:
    print('<td>'+flag+str(element)+'</font>'+'</td>')
  last_index=record[len(record)-1]
  index=recordList.index(record)+1
  if last_index==-1:
    print('<td>'+img_blood+' new blood'+'</td>')
  elif last_index-index==0:
    print('<td>'+'-'+'</td>')
  elif last_index-index>0:
    print('<td>'+img_up+'<font> jump up '+str(last_index-index)+' pos. Good job!</font></td>')
  else:
    print('<td>'+img_down+'<font> fall down '+str(index-last_index)+' pos.</font></td>')
  print('</tr>')
print('</table>')

print('''
  <footer id="foot01"></footer>
</div>

<script src="Script.js"></script>

</body>
</html>''')
