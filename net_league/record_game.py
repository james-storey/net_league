#!/usr/bin/env python3
# Use to record a game using at least one deck in the leauge
# This script sets the aggregate record on a specific deck
# To record a specific game with details, use the add_game script
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()

def set_result(conn, deck_id, win):
    if(win == True):
        return conn.execute('''UPDATE decks
            SET wins = wins + 1 WHERE deck_id = ?;
        ''', [deck_id])
    else
        return conn.execute('''UPDATE decks
            SET loses = loses + 1 WHERE deck_id = ?;
        ''', [deck_id])

def record_game(deck_name, deck_owner, win, db):
    conn = sqlite3.connect(db)
    deck_id, card_list = get_deck(conn, deck_owner, deck_name)
    set_result(conn, deck_id, win)
    conn.commit()
    conn.close()

def run(argv):
    deck_name = None
    deck_owner = None
    win = None
    db = 'card.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-d':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
        elif argv[i] == '-w':
            win = True
        elif argv[i] == '-l':
            win = False
        elif argb[i] == '-n':
            db = argv[i+1]
    if win is None:
        print("win / lose status not set, exiting")
        sys.exit(0)

if __name__ == '__main__':
    run(sys.argv)
