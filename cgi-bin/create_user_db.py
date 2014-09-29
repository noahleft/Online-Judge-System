#!/usr/bin/python
import sys
import sqlite3

if len(sys.argv)!=2:
  print 'usage: ./create_user_db.py user'
  exit(0)
prefix=sys.argv[1]

conn=sqlite3.connect(prefix+'.db')

c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user
             (ID   INTEGER PRIMARY KEY AUTOINCREMENT,
              NAME TEXT NOT NULL,
              DISPLAY TEXT NOT NULL,
              ALLOW_MODIFY INTEGER NOT NULL,
              TOKEN TEXT NOT NULL,
              UNIQUE(NAME));''')

import os
import random
import string
N=5
account=os.listdir('/home')
for name in account:
  token=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
  c.execute("INSERT OR IGNORE INTO user (NAME,DISPLAY,ALLOW_MODIFY,TOKEN) VALUES ('" \
            +name+"','"+name+"','1','"+token+"');")

conn.commit()
conn.close()
