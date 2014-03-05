#!/usr/bin/env python


import sqlite3, time


conn = sqlite3.connect('raspdb.db')
c = conn.cursor()
while True:
    c.execute("select * from usage")
    result = str(c.fetchall())
    print result.strip(',')
    time.sleep(5)
