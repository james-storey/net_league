#!/usr/bin/env python3

import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ?;
    ''', [deck_owner, deck_name]).fetchone()


def delete_deck(conn, deck_id):
    conn.execute('''DELETE FROM decks WHERE deck_id = ?;''', [deck_id])

def run(argv):
    deck_name = None
    deck_owner = None
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
    conn = sqlite3.connect(db)
    deck_id, card_list = get_deck(conn, deck_owner, deck_name)
    delete_deck(conn, deck_id)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
