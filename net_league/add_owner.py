#!/usr/bin/env python
import sqlite3
import sys

def run(argv):
    owners = []
    for i in range(len(argv)):
        if __file__ != argv[i]:
            owners.append( (argv[i],) )

    conn = sqlite3.connect('netrunner.db')
    conn.executemany("INSERT OR REPLACE INTO owners(owner_name) VALUES (lower(trim(?)))", owners)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
