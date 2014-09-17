#!/usr/bin/python
# -*- coding: UTF-8 -*-
prefix='hw1'
headerFile='fileHandler.h'
sourceFile='fileHandler.cpp'

print("Content-type: text/html\n\n")
print
import cgitb
cgitb.enable()
print("<html><body>")
import cgi
form=cgi.FieldStorage()
user=form.getvalue('id')
print 'user:'+user+'<br>'

import subprocess, threading

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            #print 'Thread started<br>'
            with open('tmp/'+user+'/log','w') as outfile:
              self.process = subprocess.Popen(self.cmd, shell=True, stdout=outfile)
            self.process.communicate()
            #print 'Thread finished<br>'

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            #print 'Terminating process<br>'
            self.process.terminate()
            thread.join()
            #print 'time out<br>'
            #print self.process.returncode
            return False
        #print self.process.returncode
        return True

command = Command('tmp/'+user+'/'+user)
success=command.run(timeout=15)


import re
import sqlite3
if success:
  with open('tmp/'+user+'/log','r') as infile:
    strlines=infile.readlines()
    runtime=int(re.match('Total use ([0-9]+)',strlines[len(strlines)-1]).group(1))
    print 'Ur run time score is '+str(runtime)+'<br>'
    conn=sqlite3.connect(prefix+'.db')
    c=conn.cursor()
    c.execute("SELECT SCORE FROM board WHERE NAME= '"+user+"';")
    previous=c.fetchall()[0][0]
    print 'current result '+str(previous)+'<br>'
    if previous==-1 or previous>runtime:
      isImproved=True
      pass
    else:
      runtime=previous
      isImproved=False
    print 'best result is '+str(runtime)+'<br>'
    accuracy=0
    score=accuracy*100-runtime
    sqlmessage ="UPDATE board SET RUNTIME = '"+str(runtime)+"',"
    sqlmessage+="TIME=TIME+1,"
    sqlmessage+="ACCURACY = '"+str(accuracy)+"',"
    sqlmessage+="SCORE = '"+str(score)+"'"
    sqlmessage+=" WHERE NAME = '"+user+"';"
    c.execute(sqlmessage)
    conn.commit()
    conn.close()
else:
  print 'time out'

import shutil
if isImproved:
  shutil.copy2('tmp/'+user+'/'+headerFile,'tmp/'+user+'/golden/'+headerFile)
  shutil.copy2('tmp/'+user+'/'+sourceFile,'tmp/'+user+'/golden/'+sourceFile)
print("</body></html>")
