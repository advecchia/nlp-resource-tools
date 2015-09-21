#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="mestrado", passwd="mestrado", db="mestrado")

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM table_test")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0], row[1]
