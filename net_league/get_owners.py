#!/usr/bin/env python3
# get a list of owners in the database

import sqlite3
import sys

def run (argv):
    db = 'netrunner.db'
    conn = sqlite3.connect(db)
    owners = conn.execute('''SELECT * FROM owners;''').fetchall()
    print(owners)
    conn.close()

if __name__ == '__main__':
    run(sys.argv)
