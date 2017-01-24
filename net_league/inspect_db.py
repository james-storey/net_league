#!/usr/bin/env python3

import sqlite3
import sys

def run(argv):
    db = 'netrunner.db'
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

if __name__ == "__main__":
    run(sys.argv)
