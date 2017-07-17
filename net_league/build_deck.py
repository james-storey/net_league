#!/usr/bin/env python3
# Use this script to build a deck already added to the database
#  This will check all of the indicated owners cards and add any available
#  to the deck.
#  If the card is not owned, or in use in another deck, the script will
#  indicate in a print out what is missing.
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()

def build_deck_and_get_missing(conn, deck, deck_owner, deck_name):
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

def build_deck(deck_owner, deck_name, db):
    conn = sqlite3.connect(db)
    deck = get_deck(conn, deck_owner, deck_name)
    unfinished = build_deck_and_get_missing(conn, deck, deck_owner, deck_name)
    conn.execute('''UPDATE decks SET active = 1
        WHERE deck_id = ?;''', [deck[0]])
    conn.commit()
    conn.close()
    return unfinished

def run(argv):
    deck_name = None
    deck_owner = None
    db = 'card.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if '-d' == argv[i]:
            deck_name = argv[i+1]
        elif '-o' == argv[i]:
            deck_owner = argv[i+1]
        elif '-n' == argv[i]:
            db = argv[i+1]
    missing = build_deck(deck_owner, deck_name, db)
    print(missing)
    
if __name__ == "__main__":
    run(sys.argv)
