#!/usr/bin/python
import sqlite3

conn=sqlite3.connect('hw1.db')

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
