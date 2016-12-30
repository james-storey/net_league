#!/usr/bin/python
import sqlite3
import sys

owners = []
for i in range(len(sys.argv)):
    if __file__ != sys.argv[i]:
        owners.append( (sys.argv[i],) )

conn = sqlite3.connect('netrunner.db')
conn.executemany("INSERT OR REPLACE INTO owners(owner_name) VALUES (lower(trim(?)))", owners)
conn.commit()
conn.close()
