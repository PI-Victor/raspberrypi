#!/usr/bin/env python


import sqlite3


conn = sqlite3.connect('raspdb.db')
c = conn.cursor()
c.execute('insert into specs (cur_release) values (11111) ' )
conn.commit()
c.execute("select * from specs")
result = str(c.fetchall())
print  result.strip('/n')
