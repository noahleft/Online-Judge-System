#!/usr/bin/python                                                                            
# -*- coding: UTF-8 -*-

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

import cgi
import os
import subprocess
form=cgi.FieldStorage()

user_name=form.getvalue('original')
new_name=form.getvalue('new_name')

print '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>2014 Fall NCTUEE Data Structure</title>
  <link href="Site.css" rel="stylesheet">
</head>'''

def is_ascii(s):
  return all(ord(c) < 128 for c in s)

if user_name and new_name and is_ascii(user_name) and is_ascii(new_name):
  print '''
  <body>
  <nav id="nav01"></nav>'''
  print '<div id="main">'
  print '<h1>Change display name</h1>'
  prefix='user'
  import sqlite3
  account=os.listdir('/home')
  if not user_name in account:
    print "<h3>user:"+user_name+" is not in list</h3>"
  else:
    conn=sqlite3.connect(prefix+'.db')
    c=conn.cursor()
    c.execute("SELECT ALLOW_MODIFY FROM user WHERE NAME= '"+user_name+"';")
    previous=c.fetchall()[0][0]
    if int(previous)==1:
      c.execute("UPDATE user SET DISPLAY='"+new_name+"',ALLOW_MODIFY=0 "+ \
                "WHERE NAME='"+user_name+"';")
      conn.commit()
      print '<h3>set display name of '+user_name+' as '+new_name+'</h3>'
    else:
      print '<h3>user:'+user_name+' are not allowed to change your name twice</h3>'
  print '<footer id="foot01"></footer>'
  print '</div>'
elif user_name and new_name:
  print '''
  <body>
    <nav id="nav01"></nav>
    <div id="main">
      <h1>Change the name in leaderboard</h1>
      <h2>Note: You have only one chance to change your display name.</h2>
      <h3>!!!  ascii only  !!!</h3>
      <form action='change.cgi'>
        Original name:
        <input type='text' name='original'><br>
        New name:
        <input type='text' name='new_name'><br>
        <input type='submit'>
      </form>
      <footer id="foot01"></footer>
    </div>'''
else:
  print '''
  <body>
  <nav id="nav01"></nav>
  <div id="main">
    <h1>Change the name in leaderboard</h1>
    <h2>Note: You have only one chance to change your display name.</h2><br>
    <form action='change.cgi'>
      Original name:
      <input type='text' name='original'><br>
      New name:
      <input type='text' name='new_name'><br>
      <input type='submit'>
    </form>
    <footer id="foot01"></footer>
  </div>'''

print '''
<script src="Script.js"></script>
</body>
</html>'''
