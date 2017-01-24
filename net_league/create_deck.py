#!/usr/bin/env python
# Use this script to add a new deck to the database.
#  Decks are expected to have the jenteki.net format for storing the
#  list of cards in the deck
import sqlite3
import sys

def check_card_list_syntax(card_list):
    for line in card_list.split('\n'):
        if len(line) == 0:
            continue
        num, *title = line.split(' ')
        title = ' '.join(title)
        print(num, title)
        try:
            num = int(num)
        except ValueError:
            return False
    return True

def run(argv):
    deck_filename = None
    owner = None
    deck_name = None
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-o':
            owner = argv[i+1]
        elif argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-f':
            deck_filename = argv[i+1]
        elif i == len(argv) - 1 and deck_filename is None:
            deck_filename = argv[i]

    if owner is None:
        print('No owner specified, Exiting')
        sys.exit(1)
    if deck_name is None:
        print('No deck name specified, Exiting')
        sys.exit(1)

    f = open(deck_filename, 'r')
    card_list = f.read()
    f.close()
    if check_card_list_syntax(card_list) == False:
        print('card list syntax error: expecting jinteki.net syntax, Exiting')
        sys.exit(1)

    conn = sqlite3.connect(db)
    if len(conn.execute('''
            SELECT deck_id FROM decks WHERE deck_name = ? AND owner = ?;
        ''', [deck_name, owner]).fetchall()) < 1:
        conn.execute('''
            INSERT INTO decks(deck_name, owner, card_list)
            VALUES(?, ?, ?);
            ''', [deck_name, owner, card_list])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
