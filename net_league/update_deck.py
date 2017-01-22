#!/usr/bin/env python3
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    row = conn.execute('''SELECT deck_id, card_list, version, wins, loses
        FROM decks WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()
    return {
        'deck_id': row[0],
        'card_list': row[1],
        'version': row[2],
        'wins': row[3],
        'loses': row[4]
    }

def update_deck(conn, deck_name, deck_owner, card_list, version):
    return conn.execute('''INSERT INTO
        decks(deck_name, owner, card_list, version)
        VALUES(?, ?, ?, ?);
    ''', [deck_name, deck_owner, card_list, int(version) + 1])

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
    deck_name = None
    deck_owner = None
    deck_filename = None
    db = 'netrunner.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
        elif argv[i] == '-f':
            deck_filename = argv[i+1]
        elif i == len(argv) - 1 and deck_filename is None:
            deck_filename = argv[i]
    if deck_owner is None:
        print('No owner specified, exiting')
        sys.exit(1)
    if deck_name is None:
        print('No deck name specified, Exiting')
        sys.exit(1)

    f = open(deck_filename, 'r')
    deck_card_list = f.read()
    f.close()
    if check_card_list_syntax(deck_card_list) == False:
        print('card list syntax error: expecting jinteki.net syntax, exiting')
        sys.exit(1)

    conn = sqlite3.connect(db)
    deck = get_deck(conn, deck_owner, deck_name)
    update_deck(conn, deck_name, deck_owner,
        deck_card_list, deck['version']);
    conn.commit()
    conn.close()
if __name__ == '__main__':
    run(sys.argv)
