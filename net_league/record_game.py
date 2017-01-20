#!/usr/bin/env python3
import sqlite3
import sys

def set_result(conn, deck_id, win):
    if(win == True):
        return conn.execute('''UPDATE decks
            SET wins = wins + 1 WHERE deck_id = ?;
        ''', [deck_id])
    else
        return conn.execute('''UPDATE decks
            SET loses = loses + 1 WHERE deck_id = ?;
        ''', [deck_id])

def run(argv):
    deck_name = None
    deck_owner = None
    win = None
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
        elif argv[i] == '-w'
            win = True
        elif argv[i] == '-l'
            win = False
    if win is None:
        print("win / lose status not set, exiting")
        sys.exit(0)
    conn = sqlite3.connect(db)
    deck_id, card_list = get_deck(conn, deck_owner, deck_name)
    set_result(conn, deck_id, win)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    run(sys.argv)
