#!/usr/bin/env python
# Use this script to add new owners to the database
import sqlite3
import sys

def run(argv):
    owners = []
    db = 'card.db'
    for i in range(len(argv)):
        if '-n' == argv[i]:
            db = argv[i+1]
            i += 2
        if __file__ != argv[i]:
            owners.append( (argv[i],) )
        
    conn = sqlite3.connect(db)
    conn.executemany("INSERT OR REPLACE INTO owners(owner_name) VALUES (lower(trim(?)))", owners)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
