#!/usr/bin/python

prefix='hw1'

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

import sqlite3
conn=sqlite3.connect(prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT NAME,ACCURACY,SCORE from board WHERE SCORE!=-1 ORDER BY SCORE;")



print '''
<html>
<head>
<title>2014 Fall NCTUEE Data Structure</title>
<link href="Site.css" rel="stylesheet">
</head>
<body>

<nav id="nav01"></nav>

<div id="main">
'''
print '<h1>Data Structure '+prefix+' leaderboard</h1>'
print '<table>'
print '<tr><th>NAME</th><th>EXAMPLE PASS</th><th>ACCURACY</th><th>SCORE</th></tr>'
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
