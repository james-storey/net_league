#!/usr/bin/env python3
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ?;
    ''', [deck_owner, deck_name]).fetchone()

def build_deck(conn, deck, deck_owner, deck_name):
    unfinished = []
    deck_id, card_list = deck
    for line in card_list.split('\n'):
        if len(line) == 0:
            continue
        num, *title = line.split(' ')
        num = int(num)
        title = ' '.join(title)
        # Use cards by owner
        # if card not available by deck owner,
        #  flag and add to print out for followup
        print(num, title)
        followup = []
        cards = conn.execute('''SELECT card_id, used_in_deck FROM cards
            WHERE card_name = ? AND owner = ?;
        ''', [title, deck_owner]).fetchall()
        for i in range(num):
            if i >= len(cards):
                missing = num - i
                for j in range(missing):
                    followup.append((title, "not owned"))
                break
            if cards[i][1] is None:
                conn.execute('''UPDATE cards SET used_in_deck = ?
                    WHERE card_id = ?;
                ''', [deck_id, cards[i][0]])
            else:
                followup.append((title, "in use in deck " + str(cards[i][1])))
        unfinished.extend(followup)
    return unfinished

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
    deck = get_deck(conn, deck_owner, deck_name)
    unfinished = build_deck(conn, deck, deck_owner, deck_name)
    print(unfinished)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
