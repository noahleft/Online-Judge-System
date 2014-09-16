#!/usr/bin/python

prefix='hw1'

print("Content-type: text/plain")
print
import cgitb
cgitb.enable()

import sqlite3
conn=sqlite3.connect(prefix+'.db')
cursor=conn.cursor()

cursor.execute("SELECT NAME,SCORE from board WHERE SCORE!=-1 ORDER BY SCORE;")
print cursor.fetchall()

