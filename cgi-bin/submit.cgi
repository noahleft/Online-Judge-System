#!/usr/bin/python
# -*- coding: UTF-8 -*-

prefix='hw1'

print("Content-type: text/html")
print
import cgitb
cgitb.enable()

print("<html>")
print("<title>upload result</title>")
print("<body>")
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
    print 'file upload success<br>'
    hpp_fn = os.path.basename(hpp_fileitem.filename)
    cpp_fn = os.path.basename(cpp_fileitem.filename)
    open('tmp/'+user_name+'/'+hpp_fn,'wb').write(hpp_fileitem.file.read())
    open('tmp/'+user_name+'/'+cpp_fn,'wb').write(cpp_fileitem.file.read())
    bashCommand=['g++',
                 'tmp/'+user_name+'/main.cpp',
                 'tmp/'+user_name+'/fileHandler.cpp',
                 '-I','tmp/'+user_name,'-O0',
                 '-o','tmp/'+user_name+'/'+user_name]
    subprocess.call(bashCommand)
    print("file compile success<br>")
    print("<a href='run.cgi?id="+user_name+"'>jump to exec phase</a>")
  else:
    print 'file upload fail<br>'
    print 'check your both of your files<br>'
print("</body>")
print("</html>")
