#!/usr/bin/python
# -*- coding: UTF-8 -*-
prefix='hw0'
headerFile='calculator.h'
sourceFile='calculator.cpp'
import os
os.chdir(prefix)

import sys
user=sys.argv[1]
print 'user:'+user

import subprocess, threading
import sqlite3
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            #print 'Thread started<br>'
            with open(user+'/log','w') as outfile:
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
conn=sqlite3.connect(prefix+'.db')
c=conn.cursor()
c.execute("UPDATE board SET SEMAPHORE = 1 WHERE NAME ='"+user+"';")
conn.commit()
conn.close()
command = Command(user+'/'+user)
success=command.run(timeout=120)


import re
import shutil
conn=sqlite3.connect(prefix+'.db')
c=conn.cursor()
if success:
  with open(user+'/log','r') as infile:
    strlines=infile.readlines()
    examplePass=int(re.match('Example case ([0-9\.]+)',strlines[len(strlines)-3]).group(1))
    runtime=float(re.match('Total use  ([0-9\.]+)',strlines[len(strlines)-2]).group(1))
    accuracy=int(re.match('Total pass ([0-9]+)',strlines[len(strlines)-1]).group(1))
    print 'Ur run time score is '+str(runtime)+'<br>'
    c.execute("SELECT SCORE FROM board WHERE NAME= '"+user+"';")
    previous=c.fetchall()[0][0]
    score=accuracy*100-runtime
    print 'current result '+str(previous)+'<br>'
    if score>previous:
      isImproved=True
      sqlmessage ="UPDATE board SET RUNTIME = '"+str(runtime)+"',"
      sqlmessage+="TIME=TIME+1,"
      sqlmessage+="ACCURACY = '"+str(accuracy)+"',"
      sqlmessage+="SCORE = '"+str(score)+"',"
      sqlmessage+="LAST_SUBMIT = datetime(CURRENT_TIMESTAMP,'localtime'),"
      sqlmessage+="SEMAPHORE = 0 "
      sqlmessage+=" WHERE NAME = '"+user+"';"
    else:
      isImproved=False
      sqlmessage="UPDATE board SET TIME=TIME+1,LAST_SUBMIT = datetime(CURRENT_TIMESTAMP,'localtime'),SEMAPHORE = 0 " \
                 +"WHERE NAME = '"+user+"';"
    print 'best result is '+str(score)+'<br>'
    c.execute(sqlmessage)
    if success and isImproved:
      shutil.copy2(user+'/'+headerFile,user+'/golden/'+headerFile)
      shutil.copy2(user+'/'+sourceFile,user+'/golden/'+sourceFile)
else:
  sqlmessage="UPDATE board SET TIME=TIME+1,LAST_SUBMIT = datetime(CURRENT_TIMESTAMP,'localtime'),SEMAPHORE = 0 " \
             +"WHERE NAME = '"+user+"';"
  c.execute(sqlmessage)
  print 'time out'

conn.commit()
conn.close()
