#!/usr/bin/env python3
# Use to delete an owner from the database
# This will delete the owner and all the cards that are linked with them

import sqlite3
import sys

def delete_owners(owners, db):
    conn = sqlite3.connect(db)
    conn.executemany('''DELETE FROM owners WHERE owner_name = ?;''', owners)
    conn.commit()
    conn.close()


def run(argv):
    owners = []
    db = 'card.db'
    for i in range(len(argv)):
        if argv[i] == '-n':
            db = argv[i+1]
        if __file__ == argv[i]:
            continue
        owners.append(argv[i])
    delete_owners(owners, db)

if __name__ == "__main__":
    run(sys.argv)
