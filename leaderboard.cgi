#!/usr/bin/python

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

import cgi
form=cgi.FieldStorage()
idxList=[str(x) for x in range(1,7)]
if not form.getvalue('idx') in idxList:
  exit(-1)
prefix='hw'+form.getvalue('idx')

import sqlite3
conn=sqlite3.connect(prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT NAME,ACCURACY,RUNTIME,SEMAPHORE from board WHERE SCORE!=-1 ORDER BY SCORE;")

print '''
<!DOCTYPE html>
<html>
<head>
<title>2014 Fall NCTUEE Data Structure</title>
<meta charset="UTF-8">
<link href="Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">'''
print '<h1>Data Structure '+prefix+' leaderboard</h1>'
print '<table>'
print '<tr><th>NAME</th><th>ACCURACY</th><th>RUN TIME</th><th>Running</th></tr>'
for record in cursor.fetchall():
  print '<tr>'
  for element in record:
    print '<td>'+str(element)+'</td>'
  print '</tr>'
print '</table>'


print '''
  <footer id="foot01"></footer>
</div>

<script src="Script.js"></script>

</body>
</html>'''
