#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
#Amazon aws time zone is EDT (NewYork) 
due = datetime.datetime(2014, 10, 10, 12, 0, 0, 0)
allow_upload = due > datetime.datetime.now()
prefix='hw1'
headerName='fileHandler.h'
sourceName='fileHandler.cpp'

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

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
print "user:"+user_name+"<br>"
import os
account=os.listdir('/home')
if not user_name in account:
  print "Wrong user"
else:
  hpp_fileitem=form['hpp']
  cpp_fileitem=form['cpp']
  if hpp_fileitem.filename and cpp_fileitem.filename:
    print 'tmp file upload success<br>'
    hpp_fn = os.path.basename(hpp_fileitem.filename)
    cpp_fn = os.path.basename(cpp_fileitem.filename)
    if hpp_fn!=headerName or cpp_fn!=sourceName:
      print "Please check file name. Don't modify the name.<br>"
      print "</body></html>"
      exit(0)
    open('tmp/'+user_name+'/'+hpp_fn,'wb').write(hpp_fileitem.file.read())
    open('tmp/'+user_name+'/'+cpp_fn,'wb').write(cpp_fileitem.file.read())
    if os.path.isfile('tmp/'+user_name+'/'+user_name):
      print "Detected previous exec file. <br>"
      os.remove('tmp/'+user_name+'/'+user_name)
    bashCommand=['g++',
                 'tmp/'+user_name+'/main.cpp',
                 'tmp/'+user_name+'/fileHandler.cpp',
                 '-I','tmp/'+user_name,'-O0',
                 '-o','tmp/'+user_name+'/'+user_name]
    subprocess.call(bashCommand)
    if os.path.isfile('tmp/'+user_name+'/'+user_name):
      print("file compile success<br>")
      print("<a href='run.cgi?id="+user_name+"'>jump to exec phase</a>")
    else:
      print("file compile fail<br>")
  else:
    print 'file upload fail<br>'
    print 'check your both of your files<br>'
print("</body>")
print("</html>")
