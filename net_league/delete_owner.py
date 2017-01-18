#!/usr/bin/env python3

import sqlite3
import sys

def delete_owners(conn, owners):
    conn.executemany('''DELETE FROM owners WHERE owner_name = ?;''', owners)

def run(argv):
    owners = []
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        owners.append(argv[i])
    conn = sqlite3.connect(db)
    delete_owners(conn, owners)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
