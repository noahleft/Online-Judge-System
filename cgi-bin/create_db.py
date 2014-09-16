#!/usr/bin/python
import sys
import sqlite3

if len(sys.argv)!=2:
  print 'usage: ./create_db.py hw1'
  exit(0)
prefix=sys.argv[1]

conn=sqlite3.connect(prefix)

c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS board
             (ID   INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME TEXT NOT NULL,
              TIME INTEGER NOT NULL,
              SCORE INTEGER NOT NULL,
              UNIQUE(NAME));''')

import os
account=os.listdir('/home')
for name in account:
  c.execute("INSERT OR IGNORE INTO board (NAME,TIME,SCORE) VALUES ('"+name+"','0','-1');")

conn.commit()
conn.close()
