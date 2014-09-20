#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

print("<html>")
print("<title>name change</title>")
print("<body>")

import cgi
import os
import subprocess
form=cgi.FieldStorage()

user_name=form.getvalue('original')
new_name=form.getvalue('new_name')
print "<h2>user:"+user_name+" try to change the display name</h2>"

prefix='user'
import sqlite3

account=os.listdir('/home')
if not user_name in account:
  print "Wrong user"
else:
  conn=sqlite3.connect(prefix+'.db')
  c=conn.cursor()
  c.execute("SELECT ALLOW_MODIFY FROM user WHERE NAME= '"+user_name+"';")
  previous=c.fetchall()[0][0]
  if int(previous)==1:
    c.execute("UPDATE user SET DISPLAY='"+new_name+"',ALLOW_MODIFY=0 "+ \
              "WHERE NAME='"+user_name+"';")
    conn.commit()
    print 'allow change'
  else:
    print 'you are not allowed to change your name twice'
  print 'change '+user_name+' into '+new_name

print '</body></html>'
