#!/usr/bin/python
import sys
import sqlite3

if len(sys.argv)!=2:
  print 'usage: ./create_db.py hw1'
  exit(0)
prefix=sys.argv[1]

conn=sqlite3.connect(prefix+'.db')

c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS board
             (ID   INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME TEXT NOT NULL,
              TIME INTEGER NOT NULL,
              ACCURACY INTERGER NOT NULL,
              RUNTIME INTEGER NOT NULL,
              SCORE INTEGER NOT NULL,
              LAST_SUBMIT DATETIME NOT NULL,
              SEMAPHORE INTEGER NOT NULL,
              UNIQUE(NAME));''')

import os
account=os.listdir('/home')
for name in account:
  c.execute("INSERT OR IGNORE INTO board (NAME,TIME,ACCURACY,RUNTIME,SCORE,LAST_SUBMIT,SEMAPHORE) VALUES ('" \
            +name+"','0','0','0','-1',datetime(CURRENT_TIMESTAMP,'localtime'),'0');")

conn.commit()
conn.close()
