#!/usr/bin/env python3
# Use after building a deck that could not be completed with the owners own cards
# This script allows the user to add cards directly from other owner's tableau
# Use build_deck to add cards to a deck from ones own tableau 
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()

def add_to_deck(conn, deck_id, card_id):
    conn.execute('''UPDATE cards SET used_in_deck = ?
        WHERE card_id = ?;
    ''', [deck_id, card_id])

def run(argv):
    deck_name = None
    deck_owner = None
    card_id = None
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
        elif argv[i] == '-c':
            card_id = argv[i+1]
    conn = sqlite3.connect(db)
    deck_id, card_list = get_deck(conn, deck_owner, deck_name)
    add_to_deck(conn, deck_id, card_id)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    run(sys.argv)
