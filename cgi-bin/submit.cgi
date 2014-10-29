#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
#Amazon aws time zone is EDT (NewYork) 
#due = datetime.datetime(2014, 10, 10, 12, 0, 0, 0)
from config import due
allow_upload = due > datetime.datetime.now()

from config import prefix
from config import headerName
from config import sourceName

print("Content-type: text/html")
print
#import cgitb
#cgitb.enable()

print("<html>")
print("<title>upload result</title>")
print("<body>")

if not allow_upload:
  print("<h1>It's not allowed uploading code now.</h1>")
  print("</body>")
  print("</html>")
  exit(0)

import cgi
import os
import subprocess
form=cgi.FieldStorage()

user_name=form.getvalue('user')
print "<h2>user:"+user_name+"</h2>"
token_key=form.getvalue('token')

import sqlite3
conn=sqlite3.connect(prefix+'.db')
c=conn.cursor()
c.execute("SELECT LAST_SUBMIT FROM board WHERE NAME= '"+user_name+"';")
previous=c.fetchall()[0][0]
import time
previous=time.strptime(previous,'%Y-%m-%d %H:%M:%S')
last_time=datetime.datetime(previous.tm_year,previous.tm_mon,previous.tm_mday,previous.tm_hour,previous.tm_min,previous.tm_sec)
elapse=datetime.datetime.now()-last_time
from datetime import timedelta

tokenCheck=sqlite3.connect('user.db')
checker=tokenCheck.cursor()
checker.execute("SELECT TOKEN FROM user WHERE NAME= '"+user_name+"';")
token=checker.fetchall()[0][0]

from checker import Checker

account=os.listdir('/home')
ta_account=['noahleft']

if not user_name in account:
  print "Wrong user"
elif token_key!=token:
  print "Wrong token key"
elif elapse<timedelta(seconds=600) and not user_name in ta_account:
  print '<h1>since last time you upload, it is less than 10 mins.</h1>'
else:
  hpp_fileitem=form['hpp']
  cpp_fileitem=form['cpp']
  if hpp_fileitem.filename and cpp_fileitem.filename:
    print '<h3>(1)tmp file upload success</h3>'
    hpp_fn = os.path.basename(hpp_fileitem.filename)
    cpp_fn = os.path.basename(cpp_fileitem.filename)
    if hpp_fn!=headerName or cpp_fn!=sourceName:
      print "Please check file name. Don't modify the name.<br>"
      print "</body></html>"
      exit(0)
    open(prefix+'/'+user_name+'/'+hpp_fn,'wb').write(hpp_fileitem.file.read())
    open(prefix+'/'+user_name+'/'+cpp_fn,'wb').write(cpp_fileitem.file.read())
    if Checker(prefix+'/'+user_name+'/'+hpp_fn) and Checker(prefix+'/'+user_name+'/'+cpp_fn):
      pass
    else:
      print "</body></html>"
      exit(0)
    if os.path.isfile(prefix+'/'+user_name+'/'+user_name):
      print "<h3>(2-1)detect previous exec file.</h3>"
      os.remove(prefix+'/'+user_name+'/'+user_name)
    bashCommand=['g++',
                 prefix+'/'+user_name+'/main.cpp',
                 prefix+'/'+user_name+'/'+sourceName,
                 '-I',prefix+'/'+user_name,'-O0',
                 '-o',prefix+'/'+user_name+'/'+user_name]
    subprocess.call(bashCommand)
    if os.path.isfile(prefix+'/'+user_name+'/'+user_name):
      print("<h3>(2)file compile success</h3>")
      print("<h3>(3)file is running</h3>")
      print("<a href='http://54.68.45.250/~ec2-user/leaderboard.cgi?idx="+prefix[2]+"'>jump back to leaderboard</a>")
      import subprocess
      subprocess.Popen(['python','run.py',user_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    else:
      print("file compile fail<br>")
  else:
    print 'file upload fail<br>'
    print 'check your both of your files<br>'
print("</body>")
print("</html>")
