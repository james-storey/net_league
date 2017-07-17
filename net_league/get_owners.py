#!/usr/bin/env python3
# get a list of owners in the database

import sqlite3
import sys

def get_owners (db):
    conn = sqlite3.connect(db)
    owners = conn.execute('''SELECT * FROM owners;''').fetchall()
    conn.close()
    return owners


def run (argv):
    db = 'card.db'
    for i in range(len(argv)):
        if '-n' == argv[i]:
            db = argv[i+1]
    print(owners)

if __name__ == '__main__':
    run(sys.argv)
