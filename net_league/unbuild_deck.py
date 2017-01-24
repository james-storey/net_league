#!/usr/bin/env python3
# Dismantle a built deck.
# This also prints a list of cards that need to be returned to their rightful
# owners now that their cards are no longer in use
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()

def remove_owned_cards(conn, id, card_owner):
    conn.execute('''UPDATE cards SET used_in_deck = NULL
        WHERE used_in_deck = ? and owner = ?;
    ''', [id, card_owner])

def remove_unowned_cards(conn, id):
    c = conn.execute('''SELECT card_id, card_name, owner
        FROM cards WHERE used_in_deck = ?''', [id]).fetchall()
    conn.execute('''UPDATE cards SET used_in_deck = NULL
        WHERE used_in_deck = ?;''', [id])
    return c
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
    remove_owned_cards(conn, deck_id, deck_owner)
    return_list = remove_unowned_cards(conn, deck_id)
    print(return_list)
    conn.execute('''UPDATE decks SET active = 0
        WHERE deck_id = ?;''', [deck_id])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
