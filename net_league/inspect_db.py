#!/usr/bin/env python3
# Use to get high level information about the database
# * Who is in it
# * What decks do they have
# * What packs do they own
import sqlite3
import sys

def run(argv):
    db = 'card.db'
    for i in range(len(argv)):
        if argv[i] == '-n':
            db = argv[i+1]
    conn = sqlite3.connect(db)

    owners = conn.execute('''
        SELECT * FROM owners;
    ''').fetchall()
    print(owners)

    decks = conn.execute('''
        SELECT deck_id, deck_name, owner, version FROM decks;
    ''').fetchall()
    print(decks)

    packs = dict()
    for o in owners:
        packs_per_owner = conn.execute('''
        SELECT DISTINCT pack FROM cards where owner = ?;
        ''', o).fetchall()
        packs[o] = packs_per_owner
    print(packs)

    conn.close()

if __name__ == "__main__":
    run(sys.argv)
